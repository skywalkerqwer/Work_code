from selenium import webdriver
import requests,time
import hashlib
import base64
from PIL import Image
from selenium.webdriver.common.keys import Keys

# API常参
TIME = time.strftime('%Y.%m.%d',time.localtime(time.time()))  # 当日日期
API_URL = 'http://pred.fateadm.com/api/capreg'  # 接口地址
PD_ID = '118244'  # 接口pd_id
PD_KEY = 'YosiO0Re11Ng1B7wv/xm1fxgdRXLL9Sj'  # 接口pd_key
APP_ID = '318244'
APP_KEY = '6cF06f9ylrJ3pYocL14PXRUAWmUJ2hZH'
TIMESTAMP = str(int(time.time()))  # 精确到秒的时间戳
# 加密签名
md5 = hashlib.md5()
md5.update((TIMESTAMP + PD_KEY).encode())
sign = md5.hexdigest()
md5 = hashlib.md5()
md5.update((PD_ID + TIMESTAMP + sign).encode())
sign = md5.hexdigest()

# 启动浏览器
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://ma.scrmtech.com/user/index/login')
browser.find_element_by_xpath('//*[@id="login-email"]').send_keys('boyangliu@healthlink.cn')  # 输入账户
browser.find_element_by_xpath('//*[@id="login-password"]').send_keys('4008185050Lby')  # 输入密码
browser.save_screenshot('../截图/%s.png'%TIME)  # 网页截图
# img_url = browser.find_element_by_xpath('//*[@id="code_img"]').get_attribute('src')  # 获取验证码图片链接  每次加载链接都会刷新
# print(img_url)
element = browser.find_element_by_xpath('//*[@id="code_img"]')  # 选取验证码图片元素
# 验证码图片顶点坐标
x_point = element.location['x']
y_point = element.location['y']
# 获取验证码图片的宽高
element_width = x_point + element.size['width']
element_height = y_point + element.size['height']
picture = Image.open('../截图/%s.png'%TIME)
img = picture.crop((x_point, y_point, element_width, element_height))  # 从网页截图中截取验证码截图
img.save('../截图/%s验证码.png'%TIME)
with open('../截图/%s验证码.png'%TIME, 'rb') as f:
    img = f.read()
img = base64.b64encode(img)  # 图片编码
img_str = img.decode('ascii')  # 转换字符串

files = {
        'img_data': ('img_data', img_str)
    }

params = {
    'user_id': PD_ID,
    'timestamp': TIMESTAMP,
    'sign': sign,
    'predict_type': '30400',
    'img_data': img_str
}
result = requests.post(API_URL, params)  # API返回结果

print(result.json())
result = result.json()
browser.find_element_by_xpath('//*[@id="login-verify"]').send_keys(eval(result['RspData'])['result'])  # 输入验证码

time.sleep(2)
browser.find_element_by_xpath('//*[@id="login-btn"]').click()  # 点击登录
time.sleep(1)
browser.find_element_by_xpath('//*[@id="login-btn"]').click()  # 点击登录
browser.implicitly_wait(10)
# 通过初始引导
browser.find_element_by_xpath('//*[@id="joyRidePopup0"]/a[1]').click()
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="joyRidePopup1"]/a[1]').click()
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="joyRidePopup2"]/a[1]').click()
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="joyRidePopup3"]/a[1]').click()
time.sleep(0.5)

browser.find_element_by_xpath('//*[@id="menu_980235"]').click()  # 点击会议管理
time.sleep(1)
browser.find_element_by_xpath('//*[@id="menu_980236"]').click()  # 点击会议列表
time.sleep(5)
# 切换到iframe子框架
main_frame = browser.find_element_by_id('mainFrame')
browser.switch_to.frame(main_frame)
browser.find_element_by_xpath('/html/body/div[4]/div[1]/table/tbody/tr[1]/td[8]/a[2]').click()  # 点击第一条会议的统计按钮
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/span').click()  # 点击导出CSV
time.sleep(10)

browser.get('https://app.ma.scrmtech.com/sap/meetingStat/StatDownloadListPage?source_id=11918')  # 跳转下载页面

browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]').send_keys(Keys.ENTER)  # 点击第一个下载按钮
