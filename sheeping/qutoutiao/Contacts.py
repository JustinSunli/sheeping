from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
driver.find_element_by_class_name("android.widget.EditText").send_keys("王彬")
driver.find_element_by_xpath("//*[contains(@text,'姓名拼音')]").send_keys("wangbin")
driver.find_element_by_xpath("//*[contains(@text,'昵称')]").send_keys("wb")
driver.find_element_by_id("com.android.contacts:id/change_button").click()

driver.find_element_by_id("android:id/text1").click()
# driver.find_element_by_id("com.android.documentsui:id/icon_mime").click()
driver.find_element_by_class_name("android.widget.ImageView").click()
driver.find_element_by_id("com.android.gallery:id/save").click()
driver.find_element_by_xpath("//*[contains(@text,'电话')]").send_keys("17835344021")
# driver.swipe(804,1536,136,397)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'电子邮件')]").send_keys("1874476942@qq.com")
time.sleep(1)


driver.swipe(804,1597,136,397)

time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'地址')]").send_keys("山西省运城市")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'公司')]").send_keys("北京忧思安")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'职务')]").send_keys("测试项目主任的学生")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'备注')]").send_keys("疯狂的菠萝")
driver.swipe(804,1597,136,397)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'聊天工具')]").send_keys("微信")
driver.swipe(804,1597,136,397)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'SIP')]").send_keys("111")
time.sleep(1)
driver.find_element_by_xpath("//*[contains(@text,'网站')]").send_keys("https://www.cnblogs.com/daiju123/")
driver.find_element_by_class_name("android.widget.ImageButton").click()