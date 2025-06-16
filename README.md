# vconline-bilispider

**历史项目，该项目现已归档。**

> 经测试，五年前 Bilibili 使用的 API 仍有部分可用。
> 
> **仍然可以正常工作的 API：**
> 
> - `getVideoInfo` (获取视频信息)
> - `getVideoTag` (获取视频所有 Tag)
> - `getUpperNavnum` (获取 UP 主作品数量)
> - `getUpperRelationstat` (获取 UP 主关注人数、粉丝数)
> - `getUpperSpaceTop` (获取 UP 主首页推荐)
> - `getFolder` (获取收藏夹下所有视频)

> **目前已失效或存在问题的 API：**
> 
> - `getVideoData` (获取视频实时数据): 报错 `{'error': 2}`
> - `getUpperVideo` (获取 UP 主所有视频): 报错 `{'error': 1}`
> - `getUpperStat` (获取 UP 主作品总数据): 报错 `{'error': 1}`
> - `getUpperInfo` (获取 UP 主信息): 报错 `{'error': 1}`
> - `getSearch` (全站搜索接口): 报错 `{'error': 2}`


基于 Python 3 的综合性 Bilibili 中文 VOCALOID 板块数据爬虫。

## 用到的第三方包
均可通过pip直接安装
 - flask（Web框架）
 - pymongo（MongoDB数据库）
 - gevent
