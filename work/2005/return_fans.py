"""
统计通过扫描二维码关注珊瑚但没有完成报名的客户明细
"""

import pandas as pd
import time,datetime

TIME = str(datetime.date.today())
PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\无锡 5月\源数据\\'

Staff = ['陈静' , '路宽']
FILE_SALE_INVITE = r'【邀请明细】国寿健康大联盟营销员海报' + TIME + '.csv'  # 一级客户邀请信息
FILE_MEMBER_INVITE = r'【邀请明细】国寿健康大联盟会员海报' + TIME + '.csv'  # 二级客户邀请信息

df_sale_invite = pd.read_csv(PATH + FILE_SALE_INVITE, engine='python')  # 一级
df_member_invite = pd.read_csv(PATH + FILE_MEMBER_INVITE, engine='python')  # 二级

# 筛选一级客户粉丝
df_sign = df_sale_invite[df_sale_invite["行为内容"] == '会议报名']
l_id = df_sign['被邀请人openid'].tolist()  # 挑选出报名用户的openid

df_first = df_sale_invite.drop(df_sale_invite.loc[df_sale_invite['被邀请人openid'].isin(l_id)].index)  # 删除openid与报名用户openid相同的人
df_first = df_first.drop(df_first.loc[df_first['邀请人姓名'].isin(Staff)].index)  # 删除测试信息
df_first = df_first.drop_duplicates(subset='被邀请人openid', keep='first')  # 去重
df_first = df_first[df_first['被邀请人姓名'] == '--']  # 去掉营销员扫自己海报的数据
df_first['行为内容'] = "未报名"  # 挑选扫描海报但未报名粉丝
df_first = df_first.rename(columns={'被邀请人昵称':'一级客户微信昵称',
                                    '被邀请人openid':'一级客户微信openid',
                                    '邀请人姓名':'营销员姓名',
                                    '邀请人手机号':'营销员手机号'})

# 筛选二级客户粉丝
df_sign = df_member_invite[df_member_invite["行为内容"] == '会议报名']
l_id = df_sign['被邀请人openid'].tolist()  # 挑选出报名用户的openid

df_second = df_member_invite.drop(df_member_invite.loc[df_member_invite['被邀请人openid'].isin(l_id)].index)  # 删除openid与报名用户openid相同的人
df_second = df_second.drop_duplicates(subset='被邀请人openid', keep='first')  # 去重
df_second = df_second[df_second['被邀请人姓名'] == '--']  # 去掉营销员扫自己海报的数据
df_second['行为内容'] = "未报名"
df_second = df_second.rename(columns={'被邀请人昵称':'二级客户微信昵称',
                                    '被邀请人openid':'二级客户微信openid',
                                    '邀请人姓名':'一级客户姓名',
                                    '邀请人手机号':'一级客户手机号'})

writer = pd.ExcelWriter(PATH + '..//未报名粉丝' + TIME + '.xlsx')
df_first.to_excel(writer, sheet_name='一级未报名客户',index=False)
df_second.to_excel(writer, sheet_name='二级未报名客户',index=False)
writer.save()
