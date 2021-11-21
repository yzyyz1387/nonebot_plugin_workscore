<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/nonebot/nonebot2/master/docs/.vuepress/public/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# 工作性价比计算器📱

_✨ NoneBot2 工作性价比计算插件 ✨_

</div>


## 安装💿
`pip install nonebot-plugin-workscore`


## 导入📲
在**bot.py** 导入，语句：
`nonebot.load_plugin("nonebot_plugin_workscore")`

## 目录结构📂

初次使用时会创建`resource`并下载资源文件至`resource`下
```
├─resource
├   └─shuang.png.
├   └─shaungboom.png
├   └─yiban.png
├   └─cjrh.jpg
├   └─hencan.png
├─__init__.py

```


## 指令💻
`ces = on_command("workscore",aliases={"算性价比","性价比计算器","工作性价比"},rule=to_me())`

**示例**
`@Eternity. 算性价比`
`bot 算性价比`


每日只请求一次，当`news`目录中存在当天的新闻时，直接从本地文件发送，不请求api

**给个star吧~**

## 截图🖼

![](https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/nonebot_plugin_workscore.jpg)




