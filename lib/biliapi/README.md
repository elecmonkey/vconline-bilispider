# BiliAPI for Python
### 获取哔哩哔哩弹幕网的一些数据

---

### 类名：__BiliAPI__
##### 说明：哔哩哔哩弹幕网数据接口类。
示例：`newbili = BiliAPI()`
#### 属性：
##### 1. Aid 说明：视频AV号
##### 2. Uid 说明：UP主UID编号
##### 3. Fid 说明：收藏夹编号
##### 4. Keyword 说明：搜索关键字
#### 方法：
##### 1. __`getVideoInfo()`__
说明：获取视频信息。
示例：
```python
newbili.Aid = 2129461
print(newbili.getVideoInfo())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|cid|CID编号||
|title|标题||
|pic|封面链接||
|videos|分P数||
|tid|分区编号||
|tname|版面||
|copyright|版权属性||
|pubdate|投稿时间||
|desc|简介||
|duration|时长||
|up mid|UP主UID||
|up name|UP主名字||
|up face|UP主头像链接||
|staff|联合投稿人列表||

##### 2. __`getVideoData()`__
说明：获取视频实时数据。
示例：
```python
newbili.Aid = 2129461
print(newbili.getVideoData())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|view|播放量||
|danmaku|弹幕||
|reply|评论||
|favorite|收藏||
|coin|硬币||
|share|分享||
|like|点赞||

##### 3.__`getVideoTag()`__
说明：获取视频所有标签。
示例：
```python
newbili.Aid = 2129461
print(newbili.getVideoTag())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|[TagID]|Tag名字||
|…|…||

##### 4.__`getFolder()`__
说明：获取收藏夹下所有视频。
示例：
```python
newbili.Fid = 186053798
print(newbili.getFolder())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|[number]|视频AID||
|…|…||

##### 5.__`getUpperVideo()`__
说明：获取UP主所有视频。
示例：
```python
newbili.Uid = 181559021
print(newbili.getUpperVideo())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|[number]|视频AID||
|…|…||

##### 6.__`getUpperNavnum()`__
说明：获取UP主作品数量。
示例：
```python
newbili.Uid = 181559021
print(newbili.getUpperNavnum())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|video|视频数量||
|audio|音频数量||

##### 7.__`getUpperStat()`__
说明：获取UP主作品总数据。
示例：
```python
newbili.Uid = 181559021
print(newbili.getUpperStat())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|archive|视频播放量||
|article|文章浏览量||
|likes|获赞||
##### 8.__`getUpperRelationstat()`__
说明：获取UP主关注人数、粉丝数。
示例：
```python
newbili.Uid = 181559021
print(newbili.getUpperRelationstat())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|following|关注数||
|follower|粉丝数||

##### 9.__`getUpperSpaceTop()`__
说明：获取UP主首页推荐。
示例：
```python
newbili.Uid = 181559021
print(newbili.getUpperSpaceTop())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|aid|视频AID||
|title|标题||
|pic|封面链接||
|videos|分P数||
|tid|分区编号||
|tname|版面||
|copyright|版权属性||
|pubdate|投稿时间||
|desc|简介||
|duration|时长||
|reason|推荐理由||

##### 10.__`getUppeInfo()`__
说明：获取UP主所有视频。
示例：
```python
newbili.Uid = 181559021
print(newbili.getUpperInfo())
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|name|ID||
|sex|性别||
|face|头像url||
|sign|个性签名||
|level|等级||
|birthday|生日||
|official_title|官方认证信息||
|top_photo|空间横幅url||

##### 11.__`getSearch(page)`__
说明：全站搜索。
示例：
```python
newbili.KeyWord = "Vocaloid中文曲"
print(newbili.getSearch(1))
```
返回值：
|Key|Value说明|必要|
|:---:|:---:|:---:|
|error|0：正常<br />1：视频不存在<br />2：其它错误|√|
|Page|numResults：结果数<br />numPages：结果页数||
|Data|[number]<br />aid：视频AID<br />author：作者<br />uid：作者UID<br />typeid：分区编号<br />typename：版面名<br />title：标题<br />description：简介<br />pic：封面url<br />tag：逗号分隔的标签||
