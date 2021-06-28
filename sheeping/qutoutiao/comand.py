##############'grep' 不是内部或外部命令，也不是可运行的程序
#adb -s UEUDU17919005255 shell "pm list package | grep uiautomator"
#adb -s UEUDU17919005255 shell pm list instrumentation

#启动错误，卸掉重新装
#adb uninstall io.appium.uiautomator2.server
#adb uninstall io.appium.uiautomator2.server.test

#git log --oneline -n 10


#adb not found
#netstat -ano|findstr '5037'
#tasklist |findstr '15828'

# adb devices
# adb shell pm list package # adb shell pm list package -3 -f 
# adb logcat -c // clear logs
# adb logcat ActivityManager:I *:s

#adb shell pm list packages


#adb shell ps | findstr com.android
#adb -s UEUDU17919005255 shell am force-stop 'com.kuaishou.nebula'
#
#adb  uninstall io.appium.uiautomator2.server
#adb  uninstall io.appium.uiautomator2.server.test
