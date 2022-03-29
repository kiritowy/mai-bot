import random
import re

from PIL import Image
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot
from src.libraries.image import *
from random import randint
import nonebot
from nonebot.adapters.cqhttp import ActionFailed


help = on_command('help')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''可用命令如下（任何人可用）：
今日舞萌：查看今天的舞萌运势
XXXmaimaiXXX什么：随机一首歌
随个[dx/标准][绿黄红紫白]<难度>：随机一首指定条件的乐曲
查歌<乐曲标题的一部分>：查询符合条件的乐曲
[绿黄红紫白]id<歌曲编号>：查询乐曲信息或谱面信息
<歌曲别名>是什么歌：查询乐曲别名对应的乐曲
定数查歌 <定数> ：查询定数对应的乐曲
定数查歌<定数下限> <定数上限>：可查询指定范围内定数的歌
分数线 <难度+歌曲id> <分数线> 详情请输入“分数线 帮助”查看

---------

四六级：可获得四六级查分网站（限定时间）
青年大学习：可获得最新一期青年大学习的答案
龙图：可获得随机龙图（图库待扩充）
maimai牌子：可获得牌子达成条件的歌曲列表
/sleep：获得随机时长精致睡眠
/缚心（/fuxin、/负心）：可迫害缚心（图库待扩充）
/泡泡（/paopao、/炮炮、/狍狍、/跑跑）：可迫害泡泡（图库待扩充）
俄罗斯|乌克兰：可发送俄罗斯乌克兰的梗图'''


    await help.send(Message([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        }
    }]))

help2 = on_command('管理help')


@help2.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help2_str = '''主人专用：
听他话 @某人：增加某人在这个群操作bot管理的权限
不听他话 @某人：去掉某人在这个群操作bot管理的权限

---------

主人&在本群中有操作权限的人：
点烟 @某人 时间（单位：秒）：禁言某人固定时长
点烟 @某人：禁言某人随机时长
灭烟 @某人：解除禁言
改马甲 @某人 新马甲：改某人马甲
改头衔 @某人 新头衔：改某人头衔
/飞机票 @某人：踢某人出群
/黑 @某人：把某人踢出群并拉黑
bot听谁话：可查看谁在本群有操作bot管理的权限'''

    await help2.send(Message([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(text_to_image(help2_str)), encoding='utf-8')}"
        }
    }]))


paopaohelp = on_command('/泡泡专用')


@paopaohelp.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help3_str = '''泡泡专用：
当发图片时：返回“tql”
当发送tql等语句时：返回“那还得是您比较强”
当发送教教我等语句时：返回“先教我先教我”
当发送卖若语句时：返回“卖若还是你比较在行”'''

    await paopaohelp.send(Message([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(text_to_image(help3_str)), encoding='utf-8')}"
        }
    }]))



async def _group_poke(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id) and event.user_id != 652099302)
    return value

async def _group_poke_paopao(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.user_id == 652099302)
    return value


async def sleepsb(gid: int, id: int, time: int):
    yield nonebot.get_bot().set_group_ban(
                group_id=gid,
                user_id=id,
                duration=time,
    )
poke = on_notice(rule=_group_poke, priority=10, block=True)


@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sb = int(event.get_user_id())
    gid = event.group_id
    time = random.randint(1, 43200)
    baning = sleepsb(gid=gid, id=sb, time=time)
    # if event.__getattribute__('group_id') is None:
    #     event.__delattr__('group_id')
    # await poke.send(Message([{
    #     "type": "poke",
    #     "data": {
    #         "qq": f"{event.sender_id}"
    #     }
    # }]))
    async for sleeped in baning:
        if sleeped:
            try:
                await sleeped
            except ActionFailed:
                await poke.finish("拍你妈")
            else:
                await poke.finish("拍你妈")
                # logger.info("禁言操作成功")

poke2 = on_notice(rule=_group_poke_paopao, priority=10, block=True)


@poke2.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sb = 652099302
    gid = event.group_id
    time = random.randint(1, 300)
    baning = sleepsb(gid=gid, id=sb, time=time)
    async for sleeped in baning:
        if sleeped:
            try:
                await sleeped
            except ActionFailed:
                await poke2.finish("喜欢拍是吧")
            else:
                await poke2.finish("喜欢拍是吧")
                # logger.info("禁言操作成功")

