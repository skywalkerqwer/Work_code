import pandas as pd
import scrm_api

PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙国寿\数据源\\'

sale_meeting_id = 12667
member_meeting_id = 12668

df_sales = scrm_api.get_data(scrm_api.invite_info, sale_meeting_id)
df_member = scrm_api.get_data(scrm_api.invite_info, member_meeting_id)

writer = pd.ExcelWriter(PATH + '接口数据.xlsx')
df_sales.to_excel(writer, sheet_name='营销员会议', index=False)
df_member.to_excel(writer, sheet_name='会员会议', index=False)
writer.save()