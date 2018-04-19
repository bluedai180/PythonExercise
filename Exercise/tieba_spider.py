import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://tieba.baidu.com/home/main?un=fobkbmdo&fr=index'
url_send = 'https://tieba.baidu.com/f/commit/post/add'
url_sign = 'https://tieba.baidu.com/f?kw=%E6%8E%A8%E7%90%86&fr=home'

cookie_str = ''
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


def sign():
    browser = webdriver.PhantomJS('D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    for key in cookies:
        c = {}
        c['name'] = key
        c['value'] = cookies[key]
        c['domain'] = '.baidu.com'
        c['path'] = '/'
        c['httponly'] = False
        c['secure'] = False
        browser.add_cookie(c)

    browser.get(url_sign)
    browser.implicitly_wait(3)

    sign_btn = browser.find_elements_by_xpath('//*[@id="signstar_wrapper"]/a')[0]
    sign_btn.click()
    sign_btn.click()

    print(browser.page_source.encode('utf-8').decode())

    browser.quit()


def send_posts():
    data = str2dic(
        'ie=utf-8&kw=%E5%8D%95%E6%9C%BA%E6%B8%B8%E6%88%8F&fid=407248&tid=5649760137&vcode_md5=&floor_num=23&rich_text=1&tbs=f0f598aecd004a1c1524122217&content=%5Bbr%5D%E9%AD%94%E5%85%BD%E4%BA%89%E9%9C%B8&basilisk=1&files=%5B%5D&mouse_pwd=99%2C99%2C97%2C121%2C98%2C103%2C96%2C98%2C92%2C100%2C121%2C101%2C121%2C100%2C121%2C101%2C121%2C100%2C121%2C101%2C121%2C100%2C121%2C101%2C121%2C100%2C121%2C101%2C92%2C103%2C102%2C99%2C109%2C98%2C92%2C100%2C108%2C103%2C101%2C121%2C100%2C101%2C109%2C101%2C15241222546850&mouse_pwd_t=1524122254685&mouse_pwd_isclick=0&__type__=reply&_BSK=JVwSUGcLBF83AFZzQztEElBFCwIWaVcbHD5WBH8Vd2BpAHxNUnpmR1VVPDsXSAZLKBx9Dl42WSstG01BMAAGEWc4XCUIIBpRRVJrZ3oNIl5QKQhRNhUIBHEGfl4IaRMyIgVpfkRsWhklTQhRHBtRM3FLUlRrAhILbT57CywAWhAGDi4yemIQVFUiTgYGXTQ%2FPFV%2FWQZndFNGAG9iShwSWGl7PlIfIlFoa01WTXYHBgdnFAF9W2xHAF5XaXU0FFcNHn9XF3IFc2FgHHIYAGt%2BXRNSMSQBAQgHegplFExgCXBuS1BSaRNUGmdPEXpWDlMCWBMnJH8XRxINDEIUd1N2NmQJaA5WKiBNRQc8ZgccH1t9GW0GTGEPYmxMRFQBEwgJIEQRZUF%2BRgFdV3BmawlXWQxvXQYxRzM1fRIxXhFzZExMAW17Rl0ZS3MIOVUSI11rfAlVQX8TVEQ2AX46Ej8XVw9LJzsvV1lRUS4SVWlWKj8iVXwJQSgpGAYfLjIISwYeIEY7Wwl8SCYsGw8XaV5UTisQQXMVIwYcBgIrMC5NWVRSIhRDIRkqPzJRJAZcJ2gZGlAoOgFDXkUmWjZTFz4UKT8TBE8tWFdfKgdKcw0jFVEeDio5OEQHG1MoCVMnVDR8IVUiHFwnJREXUi97F05YBiVEPVUMIxprfA5TQX8Tc0IrRgF9TW4CAUhdZzEvSxZDVyIJBjFaFSQjWT4IG2BkBlVoMzYQRFwMaUswUBsNGDp8UkMKdBMeCzEHRjpNbgUCSF1lZmMXRRscIFYEfxckMSJZPAZAIhscOUVtPQMPBks9Gn0OXmENdWpPU1F3BhwHZxkBfVtsAkIfAml1PhRXDRwDMmoJF2pyPQFyVREzLFA2fX97Rl8bS3MKOUEQM0wuMRBBESRfQEQoXRp%2FGmwtXgsTLCE%2FBRZYWig6BjgXanImAXJVEQcRMTkRcXUHHAhTaVwtQRst')
    data['kw'] = '单机游戏'
    data['floor_num'] = 23
    data['content'] = '星际'
    data['title'] = '单机游戏'
    print(data)
    resp = requests.post(url_send, headers=headers, cookies=cookies, data=data)
    print(resp.text)


def str2dic(text):
    idic = {}
    ilist = text.split('&')
    for item in ilist:
        name, value = item.split('=', 1)
        idic[name] = value
    return idic


def get_star():
    resp = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(str(resp.content.decode('utf-8')), "html.parser")
    for x in soup.find_all("a", class_="u-f-item unsign"):
        print(x.span.text)
