"""
测试SCRM接口
"""
import requests
import json
import pandas as pd


# 鉴权参数
SOURCE = '166'
SECRET = 'b0021555a4de20992285827912ae422d'
LV_TONG = 'wx67da237aa0ad1d5c'
YING_XIAO = 'gh_92fe4b7d01e9'
NEI_MENG = 'wx61d18882e6fcc7a2'
headers = {'content-type': 'application/json'}

# API地址
meeting_list = 'https://api.ma.scrmtech.com/app-api/meetingSap/meetingList'
invite_info = 'https://api.ma.scrmtech.com/app-api/meetingSap/inviteInfo'
poster_list = 'https://api.ma.scrmtech.com/app-api/poster/getPosterList'
poster_invite_info = 'https://api.ma.scrmtech.com/app-api/poster/getPosterInviteInfo'

# post参数
params = {
    'source': SOURCE,
    'secret': SECRET,
    'appid': LV_TONG,
    'meeting_id': 11122,
}

result = requests.post(invite_info, params=params, headers=headers).json()
print('post:',result)
# dict_result = result['data']
# df_meeting = pd.DataFrame(dict_result)
# print(df_meeting)
# writer = pd.ExcelWriter('p.xlsx')
# df_meeting.to_excel(writer,index=False)
# writer.save()
