import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://tieba.baidu.com/home/main?un=fobkbmdo&fr=index'
url_send = 'https://tieba.baidu.com/f/commit/post/add'
url_sign = 'https://tieba.baidu.com/f?kw=%E6%8E%A8%E7%90%86&fr=home'

cookie_str = 'BAIDUID=D8DE4E1003D11716D4923276198CE45C:FG=1; BIDUPSID=D8DE4E1003D11716D4923276198CE45C; PSTM=1508380007; BDUSS=NWbTIwanl1fkVIdlJVRXIySWtVcjlpTlVjelhTWUhlZWF4bXdmZzJSRVZFa1phQVFBQUFBJCQAAAAAAAAAAAEAAABebxQpZm9ia2JtZG8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWFHloVhR5aQ3; TIEBAUID=4a22c8fc6e17bf05280bc56e; TIEBA_USERTYPE=c1fb10681d804fdf682c2b57; bdshare_firstime=1517375715247; STOKEN=94ad9aa872d2081419db1a9d116f88fe82b62b6bbc0d3afdb9db02fd66a2a133; wise_device=0; BDSFRCVID=McDsJeC62iVfsbrA1PqQeJuo5ea2nbrTH6ao9ceOmwd3GC1eTpuGEG0Pqx8g0Kuba13OogKK0mOTH65P; H_BDCLCKID_SF=tJAHoKPatI_3fP36q6LKDTOB-p0X5-CsBC7RQhcH0KLKjfQIKP5KLj_rKJQ-BJQyJCTKoJrt-fb1MRjvetbqXPuWbabx35o-QTRtKh5TtUJaJKnTDMRh-4oLDPnyKMnitIj9-pPKJxt0HPonHj-KefK; H_PS_PSSID=1429_12897_21111_20929; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-179%3A131%3A; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1522656825,1523273058,1523876395,1524038966; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1524038966'
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
