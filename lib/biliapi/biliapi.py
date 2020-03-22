# -- coding: utf-8 --

# VCOnline数据站 / BiliAPI
# 项目地址：https://github.com/elecmonkey/vconline-bilispider
# 说明：本类库可以通过哔哩哔哩弹幕网的视频编号、用户编号等获得一些相关数据。
# 开发：B站@小李Xiao_li，Github@elecmonkey

import json
import urllib.request
import urllib.parse
import math

def getHttpPage(url):
    Headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    return urllib.request.urlopen(urllib.request.Request(url=url, headers=Headers)).read().decode()

class Video:
    __aid = 0
    __caching = {'getVideoInfo': '', 'getVideoData': '', 'getVideoTag': ''} # 缓存

    def __init__(self, aid):
        self.__aid = aid
    def setAid(self, aid):
        self.__aid = aid
    def getAid(self, aid):
        return self.__aid

    def getVideoInfo(self, method = 0):
        # 获取视频信息
        if method == 0 and self.__caching['getVideoInfo'] != '':
            return self.__caching['getVideoInfo'];
        try:
            JsonData = getHttpPage("http://api.bilibili.com/x/web-interface/view?aid=" + str(self.__aid))
            DicData = json.loads(JsonData)
            ReData = {
                "error" : 0,
                "cid" : DicData['data']['cid'], # CID
                "title" : DicData['data']['title'], # 标题
                "pic" : DicData['data']['pic'], # 封面url
                "videos" : DicData['data']['videos'], # 分P数
                "tid" : DicData['data']['tid'], # 分区编号
                "tname" : DicData['data']['tname'], # 版名
                "copyright" : DicData['data']['copyright'], # 作品类型
                "pubdate" : DicData['data']['pubdate'], # 投稿时间
                "desc" : DicData['data']['desc'], # 简介
                "duration" : DicData['data']['duration'], # 时常
                "up" : { # UP主信息
                    "mid" : DicData['data']['owner']['mid'], # UID
                    "name" : DicData['data']['owner']['name'], # 用户名
                    "face" : DicData['data']['owner']['face'] # 头像url
                }
            }
            StaffInfoReturn = ""
            if 'staff' in DicData['data']:
                StaffInfo = DicData['data']['staff']
                for StaffInfo_Value in StaffInfo:
                    StaffInfoReturn += str(StaffInfo_Value['mid']) + ',' + StaffInfo_Value['name'] + ',' + StaffInfo_Value['title'] + '|'
            else:
                StaffInfoReturn = str(DicData['data']['owner']['mid']) + ',' + DicData['data']['owner']['name'] + ',UP主|'
            ReData['staff'] = StaffInfoReturn[0:-1]
            # 构建staff列表字符串
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getVideoInfo'] = ReData
        return ReData

    def getVideoData(self, method = 0):
        # 获取视频实时数据
        if method == 0 and self.__caching['getVideoData'] != '':
            return self.__caching['getVideoData']
        try:
            JsonData = getHttpPage("http://api.bilibili.com/archive_stat/stat?aid=" + str(self.__aid))
            DicData = json.loads(JsonData)
            ReData = {
                "error" : 0,
                "view" : DicData['data']['view'], # 播放量
                "danmaku" : DicData['data']['danmaku'], # 弹幕
                "reply" : DicData['data']['reply'], # 评论
                "favorite" : DicData['data']['favorite'], # 收藏
                "coin" : DicData['data']['coin'], # 硬币
                "share" : DicData['data']['share'], # 分享
                "like" : DicData['data']['like'] # 点赞
            }
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getVideoData'] = ReData
        return ReData

    def getVideoTag(self, method = 0):
        if method == 0 and self.__caching['getVideoTag'] != '':
            return self.__caching['getVideoTag']
        # 获取视频所有Tag
        try:
            JsonData = getHttpPage("http://api.bilibili.com/x/tag/archive/tags?aid=" + str(self.__aid))
            DicData = json.loads(JsonData)['data']
            ReData = {"error": 0}
            for DicData_Key in DicData:
                ReData[DicData_Key['tag_id']] = DicData_Key['tag_name']
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getVideoTag'] = ReData
        return ReData

class Folder:
    __fid = 0
    __caching = {'getFolder': ''}

    def __init__(self, fid):
        self.__fid = fid
    def setAid(self, fid):
        self.__fid = fid
    def getAid(self, fid):
        return self.__fid

    def getFolder(self, page = 1, method = 0):
        # 获取收藏夹下所有视频
        if method == 0 and self.__caching['getFolder'] != '':
            return self.__caching['getFolder']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/medialist/gateway/base/spaceDetail?media_id=" + str(self.__fid) + "&pn=" + str(page) + "&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp")
            DicData = json.loads(JsonData)
            FolderPage = math.ceil(int(DicData['data']['info']['media_count']) / 20)
            ReData = {"error": 0, 'page': FolderPage}
            VideoCount = 0
            for DicData_key in DicData['data']['medias']:
                VideoCount = VideoCount + 1
                ReData[VideoCount] = DicData_key['id']
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getFolder'] = ReData
        return ReData

class Upper:
    __uid = 0
    __caching = { }

    def getUpperVideo(self, method = 0):
        # 获取UP主所有视频
        if method == 0 and self.__caching['getUpperVideo'] != '':
            return self.__caching['getUpperVideo']
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/space/arc/search?mid=" + str(self.__uid) + "&pn=1&ps=1")
            DicData = json.loads(JsonData)
            UpperPage = math.ceil(int(DicData['data']['page']['count']) / 20)
            ReData = {"error": 0}
            VideoCount = 0
            for iFolderPage in range(1, UpperPage + 1):
                JsonData = self.__getHttpPage("https://api.bilibili.com/x/space/arc/search?mid=" + str(self.__uid) + "&pn=" + str(iFolderPage) + "&ps=20")
                DicData = json.loads(JsonData)
                for DicData_key in DicData['data']['list']['vlist']:
                    VideoCount = VideoCount + 1
                    ReData[VideoCount] = DicData_key['aid']
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
            self.__caching = ReData
        return ReData

    def getUpperNavnum(self):
        # 获取UP主作品数量
        if method == 0 and self.__caching['getUpperNavnum'] != '':
            return self.__caching['getUpperNavnum']
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/space/navnum?mid=" + str(self.__uid))
            DicData = json.loads(JsonData)
            self.__caching['getUpperNavnum'] = {"error": 0,
                    "video" : DicData['data']['video'],
                    "audio" : DicData['data']['audio']
            }
        except KeyError:
            self.__caching['getUpperNavnum'] = {"error": 1}
        except:
            self.__caching['getUpperNavnum'] = {"error": 2}
        return self.__caching['getUpperNavnum']

    def getUpperStat(self):
        # 获取UP主作品总数据
        if method == 0 and self.__caching['getUpperStat'] != '':
            return self.__caching['getUpperStat']
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/space/upstat?mid=" + str(self.Uid))
            DicData = json.loads(JsonData)
            self.__caching['getUpperStat'] = {"error": 0,
                    "archive" : DicData['data']['archive']['view'],
                    "article" : DicData['data']['article']['view'],
                    "likes" : DicData['data']['likes']
            }
        except KeyError:
            self.__caching['getUpperStat'] = {"error": 1}
        except:
            self.__caching['getUpperStat'] = {"error": 2}
        return self.__caching

    def getUpperRelationstat(self, method = 0):
        # 获取UP主关注人数、粉丝数
        if method == 0 and self.__caching['getUpperRelationstat'] != '':
            pass
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/relation/stat?vmid=" + str(self.Uid))
            DicData = json.loads(JsonData)
            return {"error": 0,
                    "following" : DicData['data']['following'], # 关注数
                    "follower" : DicData['data']['follower'] # 粉丝数
            }
        except KeyError:
            return {"error": 1}
        except:
            return {"error": 2}

    def getUpperSpaceTop(self):
        # 获取UP主首页推荐
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/space/top/arc?vmid=" + str(self.Uid))
            DicData = json.loads(JsonData)
            if DicData['message'] == '没有置顶视频':
                return {"error": 1}
            else:
                ReData = {
                    "error": 0,
                    "aid": DicData['data']['aid'],  # AID
                    "title": DicData['data']['title'],  # 标题
                    "pic": DicData['data']['pic'],  # 封面url
                    "videos": DicData['data']['videos'],  # 分P数
                    "tid": DicData['data']['tid'],  # 分区编号
                    "tname": DicData['data']['tname'],  # 版名
                    "copyright": DicData['data']['copyright'],  # 作品类型
                    "pubdate": DicData['data']['pubdate'],  # 投稿时间
                    "desc": DicData['data']['desc'],  # 简介
                    "duration": DicData['data']['duration'],  # 时常
                    "reason": DicData['data']['reason'] # 推荐理由
                }
                return ReData
        except KeyError:
            return {"error": 1}
        except:
            return {"error": 2}

class Search:
    def getUpperInfo(self):
        # 获取UP主信息
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/space/acc/info?mid=" + str(self.Uid))
            DicData = json.loads(JsonData)
            ReData = {
                "error": 0,
                "name" : DicData['data']['name'], # ID
                "sex" : DicData['data']['sex'], # 性别
                "face" : DicData['data']['face'], # 头像url
                "sign" : DicData['data']['sign'], # 个性签名
                "level" : DicData['data']['level'], # 等级
                "birthday" : DicData['data']['birthday'], # 生日
                "official_title" : DicData['data']['official']['title'], # 官方认证信息
                "top_photo" : DicData['data']['top_photo'] # 空间横幅url
            }
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        return ReData

    def getSearch(self, page):
        # 全站搜索接口
        # 每页20条，page为页数。
        try:
            JsonData = self.__getHttpPage("https://api.bilibili.com/x/web-interface/search/type?context=&page=" + str(page) + "&order=&keyword=" + urllib.parse.quote(self.Keyword) + "&duration=&tids_1=&tids_2=&__refresh__=true&search_type=video&highlight=1&single_column=0")
            DicData = json.loads(JsonData)
            PageData = {
                "numResults" : DicData['data']['numResults'],
                "numPages": DicData['data']['numPages']
            }
            ReData = { }
            if (page == PageData['numPages']):
                iPage = PageData['numResults'] - 20 * (page - 1)
            else :
                iPage = 20
            for iGetVideo in range(0, iPage):
                ReData[iGetVideo] = {
                    "aid" : DicData['data']['result'][iGetVideo]['aid'],
                    "author" : DicData['data']['result'][iGetVideo]['author'],
                    "uid" : DicData['data']['result'][iGetVideo]['mid'],
                    "typeid" : DicData['data']['result'][iGetVideo]['typeid'],
                    "typename" : DicData['data']['result'][iGetVideo]['typename'],
                    "title" : DicData['data']['result'][iGetVideo]['title'],
                    "description" : DicData['data']['result'][iGetVideo]['description'],
                    "pic" : DicData['data']['result'][iGetVideo]['pic'],
                    "tag" : DicData['data']['result'][iGetVideo]['tag']
                }
            return {"error": 0, "Page" : PageData, "Data" : ReData}
        except KeyError:
            return {"error": 1}
        except:
            return {"error": 2}