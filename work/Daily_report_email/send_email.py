import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 当日日期  2019-12-06

with open('D:\Code\work\Daily_report_email\email_address', 'r', encoding='UTF-8') as f:
    address = eval(f.read())

# 邮箱账号密码
username = 'boyangliu@healthlink.cn'
password = 'He@lthlink123'

# 登录邮箱
# smtp = smtplib.SMTP()
# smtp.connect('smtp.exmail.qq.com', 465)
smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com')
smtp.login(username, password)

# 发件人、收件人、抄送
sender = 'boyangliu@healthlink.cn'
cc = address['抄送全']


def send_mail(path, company, event_name):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = address[company]
    message['Cc'] = cc
    # 邮件主题
    subject = '%s活动日报数据%s'%(company, TIME)
    message['Subject'] = Header(subject, 'utf-8')

    # 正文
    text_str = """您好：
        附件为附件为”%s“活动数据，%s活动日报，统计截止至%s。
    """%(event_name, company, TIME)
    message.attach(MIMEText(text_str, 'plain', 'utf-8'))

    # 添加附件
    # att = MIMEText(open(path + '..//内蒙古%s活动日报数据'%company + TIME + '.xlsx', 'rb').read(), 'base64', 'utf-8')
    # att["Content-Type"] = 'application/octet-stream'
    # att["Content-Disposition"] = 'attachment; filename="%s.xlsx'%TIME

    # 解决附件中文乱码问题
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(open(path + '..//%s活动日报数据' % company + TIME + '.xlsx', 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '%s活动日报数据%s.xlsx' % (company, TIME)))
    encoders.encode_base64(att)

    part = MIMEApplication(open('foo.xlsx', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")

    message.attach(att)  # 添加附件
    try:
        smtp.sendmail(sender, address[company].split(',')+cc.split(','), message.as_string())
        print('发送成功')
    except:
        print('发送失败')


def summary_mail(path, event_name):
    # 发送汇总邮件
    acc = address['抄送部分']
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = address['汇总']
    message['Cc'] = acc
    # 邮件主题
    subject = '汇总活动日报数据%s' % TIME
    message['Subject'] = Header(subject, 'utf-8')

    # 正文
    text_str = """您好：
            附件为附件为”%s“活动数据，汇总活动日报，统计截止至%s。
        """ %(event_name, TIME)
    message.attach(MIMEText(text_str, 'plain', 'utf-8'))

    # 解决附件中文乱码问题
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(open(path + '..//汇总活动日报数据' + TIME + '.xlsx', 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '汇总活动日报数据%s.xlsx' % TIME))
    encoders.encode_base64(att)
    message.attach(att)  # 添加附件
    try:
        smtp.sendmail(sender, address['汇总'].split(',') + acc.split(','), message.as_string())
        print('发送成功')
    except:
        print('发送失败')
