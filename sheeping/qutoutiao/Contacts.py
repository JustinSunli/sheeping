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
driver.find_element_by_class_name("android.widget.EditText").send_keys("����")
driver.find_element_by_xpath("//*[contains(@text,'����ƴ��')]").send_keys("wangbin")
driver.find_element_by_xpath("//*[contains(@text,'�ǳ�')]").send_keys("wb")
driver.find_element_by_id("com.android.contacts:id/change_button").click()

driver.find_element_by_id("android:id/text1").click()
# driver.find_element_by_id("com.android.documentsui:id/icon_mime").click()
driver.find_element_by_class_name("android.widget.ImageView").click()
driver.find_element_by_id("com.android.gallery:id/save").click()
driver.find_element_by_xpath("//*[contains(@text,'�绰')]").send_keys("17835344021")
# driver.swipe(804,1536,136,397)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'�����ʼ�')]").send_keys("1874476942@qq.com")
time.sleep(1)


driver.swipe(804,1597,136,397)

time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'��ַ')]").send_keys("ɽ��ʡ�˳���")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'��˾')]").send_keys("������˼��")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'ְ��')]").send_keys("������Ŀ���ε�ѧ��")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'��ע')]").send_keys("���Ĳ���")
driver.swipe(804,1597,136,397)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'���칤��')]").send_keys("΢��")
driver.swipe(804,1597,136,397)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'SIP')]").send_keys("111")
time.sleep(1)
driver.find_element_by_xpath("//*[contains(@text,'��վ')]").send_keys("https://www.cnblogs.com/daiju123/")
driver.find_element_by_class_name("android.widget.ImageButton").click()