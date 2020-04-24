from selenium import webdriver
from aip import AipOcr
import requests,time

""" 你的 APPID AK SK """
APP_ID = '17761420'
API_KEY = '67B7i0eYM0i3WfRo0zPXmUVT'
SECRET_KEY = 'aEWMxE0Upw83N3yDI4cbprxGXadoFe2W'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

browser = webdriver.Chrome()
browser.get('https://ma.scrmtech.com/user/index/login')
browser.find_element_by_xpath('//*[@id="login-email"]').send_keys('boyangliu@healthlink.cn')
browser.find_element_by_xpath('//*[@id="login-password"]').send_keys('4008185050Lby')
i = 0
while True:
    img_url = browser.find_element_by_xpath('//*[@id="code_img"]').get_attribute('src')  # 获取验证码图片链接
    img = requests.get(img_url)  # 打开验证码图片链接

    result = client.basicGeneral(img.content)
    print(result['words_result'])
    words_result = result['words_result']
    content = ''
    for word in words_result:
        content += word['words']
    browser.find_element_by_xpath('//*[@id="login-verify"]').send_keys(content)
    ele_login = browser.find_element_by_xpath('//*[@id="login-btn"]')
    ele_login.click()
    browser.implicitly_wait(3)
    if not browser.find_element_by_xpath('//*[@id="login-btn"]'):
        break
    else:
        browser.find_element_by_xpath('//*[@id="login-verify"]').clear()
        browser.find_element_by_xpath('//*[@id="code_img"]').click()  # 登录失败重新加载验证码
        time.sleep(5)
        print('登陆失败', i+1, '次')
        i += 1
        if i == 3:
            print('失败3次结束尝试')
            browser.quit()
            break
# ele_count = browser.find_element_by_xpath('/html/body/div[4]/div[1]/table/tbody/tr[2]/td[8]/a[2]')  # 会议统计
# ele_count.click()