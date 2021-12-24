import random
import re


import requests
import time
from selenium import webdriver
import selenium.webdriver.common.keys  as keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keywords = ["阿水","jkl","冰皇","jackeylove","冰冰"]
url = "https://tieba.baidu.com/f?fr=home&kw=%E6%8A%97%E5%8E%8B%E8%83%8C%E9%94%85"
list = ["喻文波最帅，喻文波最强，喻文波是tes的主，是ad的王，他做的每一次决策都无比正确，他a人的每一刀都闪闪发光，\
        他的每一次火箭跳跃都是布施的圣火，他的每一个奥术迁跃都是希望的光芒。喻文波，你永远不会犯错，\
        因为ad的定义由你来谱写；冰冰！我的冰冰！我命运般的冰冰！我的生命之光！我的热血之火！我的热爱！我的灵魂！\
        又稳又c的冰冰就是带刺的玫瑰！有毒的罂粟！滔搏的胜利不能没有冰冰！","差不多得了 左手拿了这么多MVP还要被水\
        鬼黑,带你们家giegie打比赛可真累"]
def login(url,list):
    #实例化谷歌设置选项
    option = webdriver.ChromeOptions()
    #添加保持登录的数据路径：安装目录一般在C:\Users\xxx\AppData\Local\Google\Chrome\User Data
    option.add_argument(r"user-data-dir=C:\Users\hasee\AppData\Local\Google\Chrome\User Data")

    x = random.randint(0,len(list)-1)

    print(x)

    driver = webdriver.Chrome(options=option)
    driver.get(url)

    #添加等待时间，直到页面加载完毕再继续
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='ueditor_replace']"))
    )
    for i in range(4):
        driver.find_element_by_tag_name('body').send_keys(keys.Keys.END)
        time.sleep(1)

    elem = driver.find_element_by_xpath("//div[@id='ueditor_replace']/p")
    elem.click()
    time.sleep(1)
    elem.send_keys(list[x])
    time.sleep(1)
    driver.find_element_by_xpath("//em[text()='发 表']").click()

    time.sleep(2)
    print("自动评论成功！")
    driver.close()

def findHerf(keyword):
    url_search = "https://tieba.baidu.com/f/search/res?ie=utf-8&qw="

    res = requests.get(url_search+keyword)


    res_get = re.compile(r'<a data-tid=(.*?)target="_blank"')

    links_get = re.findall(res_get,res.text)

    hrefs = []

    for i in links_get:
        links_search = re.compile(r'href="(.*?)"')
        links = re.findall(links_search,i)
        hrefs.append(links[0])

    return hrefs

for keyword in keywords:
    hrefs = findHerf(keyword)

    for href in hrefs:
        url = "https://tieba.baidu.com"+href
        print(url)
        login(url,list)
        time.sleep(2)


