import requests
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
    'appid': NEI_MENG,
    # 'meeting_id': '',
}


def get_data(url, meeting_id):
    params['meeting_id'] = meeting_id
    result = requests.post(url, params=params, headers=headers).json()
    print(result)
    dict_result = result['data']
    df_meeting = pd.DataFrame(dict_result)
    return df_meeting

if __name__ == '__main__':

    sale_meeting_id = 12667
    # df = get_data(invite_info, sale_meeting_id)

# writer = pd.ExcelWriter('p.xlsx')
# df_meeting.to_excel(writer,index=False)
# writer.save()