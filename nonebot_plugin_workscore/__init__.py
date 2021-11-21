# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 20:59
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from nonebot.adapters.cqhttp import Event,MessageEvent,MessageSegment,Bot
from nonebot import on_command
from nonebot.typing import T_State
import os
from os.path import dirname
from nonebot.rule import to_me
import requests

monthlist=["3","4","6","8","10","20","30","50","70","100","150"]

goworklist=['1','2','3','4','5']
moyulist=['1','2','3','4','5']
degreelist=['1','2','3','4','5','6','7']
workenvlist=['1','2','3','4']
moflist=['1','2','3']
colllist=['1','2','3']
rightlist=['1','2','3','4']
eightlist=["是","否"]
workarealist=['1','2','3','4']

monthdict={"3":"138","4":"184","6":"276","8":"368","10":"460","20":"920","30":"1379","50":"2299","70":"3218","100":"4598","150":"6897"}
degreedict={'1':'0.8','2':'1','3':'1.2','4':'1.4','5':'1.6','6':'1.8','7':'2'}
workenvdict={'1':'0.8','2':'0.9','3':'1','4':'1.1'}
mofdict={'1':'0.9','2':'1','3':'1.1'}
colldict={'1':'0.95','2':'1','3':'1.05'}
rightdict={'1':'1','2':'1.05','3':'1.1','4':'1.15'}
eightdict={'是':'0.95','否':'1'}
workareadict={'1':'1.5','2':'1.2','3':'1','4':'0.8'}



ces = on_command("workscore",aliases={"算性价比","性价比计算器","工作性价比"},rule=to_me())

@ces.args_parser
async def parse(bot: Bot, event: Event, state: T_State):
    resourcepath=dirname(__file__)+"/resource"
    if os.path.exists(resourcepath)==False:
        print("构建资源目录")
        os.mkdir(resourcepath)
        print("下载资源文件")
        open(dirname(__file__)+"/resource/"+"shuang.png",'wb').write(requests.get("https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/shuang.png").content)
        open(dirname(__file__) + "/resource/" + "shuangboom.png", 'wb').write(requests.get("https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/shuangboom.png").content)
        open(dirname(__file__) + "/resource/" + "yiban.png", 'wb').write(requests.get("https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/yiban.png").content)
        open(dirname(__file__) + "/resource/" + "cjrh.png", 'wb').write(requests.get("https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/cjrh.png").content)
        open(dirname(__file__) + "/resource/" + "hencan.jpg", 'wb').write(requests.get("https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/hencan.jpg").content)
    print(state)
    print(state["_current_key"], "********", str(event.get_message()))
    state[state["_current_key"]] = str(event.get_message())

    if str(event.get_message()) in ["取消", "算了"]:
        await ces.finish("已取消操作..", at_sender=True)


@ces.handle()
async def first_receive(bot: Bot, event: Event, state: T_State):
    # 获取用户原始命令，如：/test
    print(state)
    print(state["_prefix"]["raw_command"])
    # 处理用户输入参数，如：/test arg1 arg2
    raw_args = str(event.get_message()).strip()
    if raw_args:
        arg_list = raw_args.split()
        print("*******",arg_list)
        print(len(arg_list))


@ces.got("month",prompt="""
月薪（k）？
3
4
6
8
10
20
30
50
70
100
150
""")

async def get_1(bot:Bot,event:MessageEvent,state:T_State):
    if state["month"] not in monthlist:
        await ces.reject("月薪不正确！请重新输入")
        print(state)
        state["month"] = str(event.get_message())

@ces.got("musttime", prompt="""额定工作时长（小时\天）？
请回复0-15的数字
（回复数字）
    """)
async def get_3(bot:Bot,event:MessageEvent,state:T_State):
    if str(state['musttime']).isdigit()==False:
        await ces.reject("你输了个啥啊！？重输一遍工作时长！")
    if int(state['musttime'])>15 or int(state['musttime']) <0 :
            await ces.reject("工作时长不正确！请重新输入")


@ces.got("gowork",prompt="""总通勤时长(小时\天)？
回复通勤小时数
（回复数字）
""")
async def get_4(bot:Bot,event:MessageEvent,state:T_State):
    if str(state['gowork']).isdigit()==False:
        await ces.reject("通勤时长有误，请重新输入")
    if int(state['gowork']) < 0:
            await ces.reject("通勤时长有误，请重新输入")
    if int(state['gowork']) >4:
            await ces.finish("这通勤时长？你辞职吧,计算结束！")


@ces.got("moyu", prompt="""总摸鱼时长（不干活+吃饭+午休）？
请回复摸鱼小时数
（回复数字）
""")
async def get_5(bot:Bot,event:MessageEvent,state:T_State):
    if str(state['moyu']).isdigit()==False:
        await ces.reject("你输了个啥啊！？重输一遍！！！")
    if int(state['moyu']) > 4:
            await ces.finish("摸鱼这么久？你是老板吧，计算结束1")
    if int(state['gowork']) < 0:
            await ces.reject("摸鱼时长有误，请重新输入")

@ces.got("degree", prompt="""学历系数？
1、专科以下
2、普通本科
3、985/211本科
4、普通硕士
5、985/211硕士
6、普通博士
7、高级博士
（回复数字）
""")
async def get_6(bot:Bot,event:MessageEvent,state:T_State):
    if state['degree'] not in degreelist:
        await ces.reject("学历不正确！请重新输入")
@ces.got("workenv", prompt="""工作环境？
1、偏僻地区
2、工厂户外
3、普通
4、体制内
（回复数字）
""")
async def get_7(bot:Bot,event:MessageEvent,state:T_State):
    if state['workenv'] not in workenvlist:
        await ces.reject("工作环境不正确！请重新输入")
@ces.got("mof", prompt="""身边异性？
1、没有
2、不多不少
3、很多
（回复数字）
""")
async def get_8(bot:Bot,event:MessageEvent,state:T_State):
    if state['mof'] not in moflist:
        await ces.reject("身边异性状况不正确！请重新输入")
@ces.got("right", prompt="""是否也有职业资格要求？
1、没有
2、建造造价监理证书
3、建筑岩土结构证书
4、主任医师/教授职称
（回复数字）
""")
async def get_9(bot:Bot,event:MessageEvent,state:T_State):
    if state['right'] not in rightlist:
        await ces.reject("证书要求不正确！请重新输入")
@ces.got("coll", prompt="""身边同事？
1、SB多
2、普通多
3、优秀多
（回复数字）
""")
async def get_10(bot:Bot,event:MessageEvent,state:T_State):
    if state['coll'] not in colllist:
        await ces.reject("同事状况不正确！请重新输入")
@ces.got("eight", prompt="""是否8:30前上班？
是
否
""")
async def get_11(bot:Bot,event:MessageEvent,state:T_State):
    if state['eight'] not in eightlist:
        await ces.reject("不正确！请重新输入")
@ces.got("workarea", prompt="""综合工作环境？
1、一线城市
2、城市
3、小城市
4、镇村
（回复数字）
    """)
async def get_12(bot:Bot,event:MessageEvent,state:T_State):
    if state['workarea'] not in workarealist:
        await ces.reject("综合环境不正确！请重新输入")
    month=float(monthdict[state['month']])
    workenv=float(workenvdict[state['workenv']])
    mof=float(mofdict[state['mof']])
    coll=float(colldict[state['coll']])
    musttime=float(state['musttime'])
    gowork=float(state['gowork'])
    moyu=float(state['moyu'])
    eight=float(eightdict[state['eight']])
    degree=float(degreedict[state['degree']])
    right=float(rightdict[state['right']])
    data=[month,workenv,mof,coll,musttime,gowork,moyu,eight,degree,right]
    up=month*workenv*mof*coll*eight
    down=35*(musttime+gowork-0.5*moyu)*degree*right
    sum=round((up/down),2)
    print(sum)
    if 1.5<sum<2:
        score="很爽"
        img="shuang.png"
    if sum>2:
        score="爽到爆炸"
        img='shuangboom.png'
    if 0.8<sum<1.5:
        score="一般"
        img='yiban.png'
    if sum<0.4:
        score="惨绝人寰"
        img="cjrh.png"
    if 0.4<sum<0.8:
        score="很惨"
        img='hencan.jpg'
    path=dirname(__file__)+"/resource/"+img
    info="您的工作性价比评分为 [%s] \n性价比评价为 [%s] \n"%(sum,score)
    rely=[{
        'type':'text',
        'data':{
            'text':info
        }

    },
        {
            'type':'image',
            'data':{
                'file':f'file:///{path}'
            }
        }
    ]
    await bot.send(
            event=event,
            message=rely,
            at_sender=True
        )




# async def arg_handle(bot: Bot, event: Event, state: T_State):
#     # 在这里对参数进行验证
#     if state["month"] not in monthlist:
#         await ces.reject("月薪不正确！请重新输入")
#         print(state)
#     state[state["_current_key"]] = str(event.get_message())
#     if state['workday'] not in workdaylist:
#         await ces.reject("工作天数不正确！请重新输入")
#     state[state["_current_key"]] = str(event.get_message())
#
#     # 发送一些信息
#     await ces.finish("message")




__usage__ = """
发送
    算性价比

中途退出请发送
  算了/取消
"""
_help__plugin_name__ = "算性价比"

__permission__ = 2
__help__vesion__ = '0.1'


