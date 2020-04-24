import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase

file = r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙国寿\内蒙古汇总活动日报数据2019-12-27.xlsx'

username = 'boyangliu@healthlink.cn'
password = 'He@lthlink123'

# smtp = smtplib.SMTP()
# smtp.connect('smtp.exmail.qq.com', 465)
smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com')
smtp.login(username, password)

sender = 'boyangliu@healthlink.cn'
receivers = '984356166@qq.com'  # 收件人邮箱
# receivers = 'jingchen@healthlink.cn'  # 收件人邮箱
# cc = '15902162780@163.com,870024258@qq.com'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers
# message['Cc'] = cc
# 邮件主题
subject = '测试邮件'
message['Subject'] = Header(subject, 'utf-8')

# 正文
text_str = """测试邮件及测试附件，请检查附件能否打开
"""
message.attach(MIMEText(text_str, 'plain', 'utf-8'))


# 附件
path = r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙国寿\数据源\\'
TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 当日日期  2019-12-06
company = "呼和浩特分公司"

# att = MIMEBase('application', 'octet-stream')
# att.set_payload(open(r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙0107活动\活动数据表头模板.xlsx', 'rb').read())
# att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '活动数据表头模板.xlsx'))
# encoders.encode_base64(att)
# att = MIMEText(open(path + '..//内蒙古%s活动日报数据'%company + TIME + '.xlsx', 'rb').read(), 'base64', 'utf-8')  # 必须用rb格式读取
# att["Content-Type"] = 'application/octet-stream'
# 生成附件的名称
# att["Content-Disposition"] = 'attachment; filename="%s.xlsx"'%TIME

part = MIMEApplication(open(r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙0107\活动数据表头模板.xlsx', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '活动数据表头模板.xlsx'))
message.attach(part)  # 添加附件


try:
    smtp.sendmail(sender, receivers.split(','), message.as_string())
    print('发送成功')
except:
    print('发送失败')
