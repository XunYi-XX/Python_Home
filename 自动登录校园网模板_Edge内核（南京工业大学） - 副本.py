'''
driver路径:"C:/Windows/msedgedriver.exe"
edge路径："C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
URL：复制到的网址
登录按钮XPath：//*[@id="edit_body"]/div[2]/div[3]/form/input[1]
账号XPath：//*[@id="edit_body"]/div[2]/div[3]/form/input[2]
密码XPath：//*[@id="edit_body"]/div[2]/div[3]/form/input[3]
注销XPath：//*[@id="edit_body"]/div/div[2]/form/input
运营商选择框XPath：//*[@id="edit_body"]/div[2]/div[3]/select
'''

"""自动化测试"""
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

"""启动引擎"""
selenium_path ='C:/Windows/msedgedriver.exe'
# 通过service方法打开路径
service = Service(selenium_path)
# 再去调用
driver = webdriver.Edge(service=service)
# 访问校园网认证网址
driver.get("URL")

time.sleep(1)
# 目标 XPath 路径
zhuxiao_xpath = '//*[@id="edit_body"]/div/div[2]/form/input'

# 判断是否存在该 XPath
try:
    # 尝试查找元素
    element = driver.find_element(By.XPATH, zhuxiao_xpath)
    print("校园网已登录，即将退出程序！")
    driver.quit()
except NoSuchElementException:
    # 如果捕获到没有元素的异常
    print("校园网未登录，开始执行登录程序！")
    #寻找账号输入框
    Account = driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[3]/form/input[2]')
    print('程序已完成： 1   /  8  .')
 
    ActionChains(driver)\
                          .send_keys_to_element(Account, "账号")\
                          .perform()
    print('程序已完成： 2   /  8  .')

    #寻找密码输入框
    Account = driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[3]/form/input[3]')
    print('程序已完成： 3   /  8  .')
 
    ActionChains(driver)\
                          .send_keys_to_element(Account, "密码")\
                          .perform()
    print('程序已完成： 4   /  8  .')

    # 定位下拉框元素
    dropdown_element = driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[3]/select')
    print('程序已完成： 5   /  8  .')
    
    # 使用 Select 处理下拉框
    select = Select(dropdown_element)
    print('程序已完成： 6   /  8  .')
    
    # 选择某个选项（示例：通过可见文本选择）
    select.select_by_visible_text("中国移动")
    #中国移动卡此处不做修改，中国电信卡请把此处的"中国移动"改为"中国电信"
    print('程序已完成： 7   /  8  .')

    #点击登录按钮
    click_LOAD = driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[3]/form/input[1]')
    ActionChains(driver) \
                         .click(click_LOAD) \
                         .perform()
    print('程序已完成： 100%   .')
    driver.quit()
    print('校园网登录成功，程序即将退出.')

