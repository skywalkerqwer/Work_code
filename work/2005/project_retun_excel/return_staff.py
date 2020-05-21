"""
    统计已登录但未领取海报的营销员清单
"""
import pandas as pd
import datetime,os


TIME = str(datetime.date.today())


def read_df(PATH, sale_file):
    # 1 读取
    # FILE_sales_invite = r'【邀请明细】国寿健康大联盟营销员海报' + TIME + '.csv'  # 一级客户邀请信息
    FILE_sales_info = r'员工列表.csv'

    df_info = pd.read_csv(PATH + FILE_sales_info, engine='python')  # 营销员备案
    df_sale_invite = pd.read_csv(PATH + sale_file, engine='python')  # 一级
    df_info = deal_staff(df_info)
    return df_info, df_sale_invite

def replace_c(x):  # 2 移除逗号comma
    x = str(x)
    x = x.replace(',', '')
    x = x.replace('，', '')
    return x

def deal_staff(df_info):
    # 2 处理员工列表
    df_info['客户经理工号'] = df_info['客户经理工号'].fillna(0)
    df_info['客户经理工号'] = df_info['客户经理工号'].apply(replace_c)
    df_info['客户经理工号'] = df_info['客户经理工号'].astype('int64')
    df_info = df_info[df_info['绑定状态'] == '已绑定']
    return df_info

def do_delete(PATH, sale_file):
    # 3 删除已领取海报的营销员
    df_info, df_sale_invite = read_df(PATH, sale_file)
    poster_phone_list = df_sale_invite['邀请人手机号'].tolist()
    df_info = df_info.drop(df_info[df_info['手机号'].isin(poster_phone_list)].index)
    df_out = do_out(df_info)
    return df_out

def do_out(df_info):
    # 4 构建输出表格
    df_output = pd.DataFrame(columns=['营销员姓名', '营销员手机号', '营销员工号', '所属职场'])
    df_output['营销员姓名'] = df_info['姓名']
    df_output['营销员手机号'] = df_info['手机号']
    df_output['营销员工号'] = df_info['客户经理工号']
    df_output['所属职场'] = df_info['二级名称']
    return df_output

def domain(PATH, sale_file):
    # 保存
    save_path = PATH + TIME
    is_exists = os.path.exists(save_path)
    if not is_exists:
        os.makedirs(save_path)
    writer = pd.ExcelWriter(save_path + '//未领取海报营销员' + TIME + '.xlsx')
    df_output = do_delete(PATH, sale_file)
    df_output.to_excel(writer, index=False)
    writer.save()

if __name__ == '__main__':
    PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\无锡 5月\源数据\\'
    domain(PATH)