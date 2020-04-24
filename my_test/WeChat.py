"""
微信接口
"""
import itchat
import time
from itchat.content import *

"""
# 消息轰炸
itchat.auto_login(hotReload=True)

remark_name = input('输入接入聊天的微信名：')
cnt = int(input('输入发送次数：'))  # 计数器
try:
    name = itchat.search_friends(remark_name)[0]['UserName']
    for i in range(cnt):
        itchat.send_msg('Python自动发送', name)
except IndexError as ie:
    print('未搜索到', remark_name)
except Exception as e:
    print(e)
"""
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
# 关注任何发来的文字消息
@itchat.msg_register('Text')
# @itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    # 当消息不是由自己发出的时候
    # if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
    itchat.send_msg(u"[自动回复]：[%s]收到好友@%s 的信息：%s\n" %
                    (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                     msg['User']['NickName'],
                     msg['Text']),
                    toUserName=msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login()
    # 获取自己的UserName
    # myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
