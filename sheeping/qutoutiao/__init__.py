# coding: utf-8
#import os
#import sys
#rootpath=str("D://git//sheeping//sheeping")
#syspath=sys.path
#sys.path=[]
#sys.path.append(rootpath)
##将工程根目录加入到python搜索路径中
#sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])
#sys.path.extend(syspath)


# adb devices
# adb shell pm list package # adb shell pm list package -3 -f 
# adb logcat -c // clear logs
# adb logcat ActivityManager:I *:s

#aapt dump badging C:\Users\Administrator\Desktop\api\ff0602.apk


#adb connect连接设备很慢，需要用以下命令
#adb -s SAL0217A28001753 usb
#adb tcpip 5555
#adb connect 192.168.0.106:5555
#adb disconnect 192.168.0.106:5555

#start /b appium -a 127.0.0.1 -p 4723 -bp 4724 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4725 -bp 4726 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4727 -bp 4728 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4729 -bp 4730 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4731 -bp 4732 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4733 -bp 4734 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4735 -bp 4736 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4737 -bp 4738 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4739 -bp 4740 --session-override --relaxed-security
#start /b appium -a 127.0.0.1 -p 4741 -bp 4742 --session-override --relaxed-security

#npm config set registry https://registry.npm.taobao.org
#npm install appium -g
#npm update -g npm
#npm cache clean


#uiaotumatorviewer 

#C:\Users\Michael\AppData\Local\Android\Sdk\tools\monitor.bat Dump view UI hierarchy for Automator:

#pip install weditor==> python -m weditor


#netstat -ano|findstr "4735"
#tasklist |findstr "进程id号"
#taskkill /f /t /im "进程id或者进程名称"



#在微信任何聊天窗口输入debugx5.qq.com
#点击debugx5.qq.com，打开微信的x5内核调试页面，然后切到信息页签，勾选”是否打开TBS内核Inspector调试功能”
#微信公众号 or 小程序  androidProcess
#adb -s SAL0217A28001753 shell dumpsys activity top| findstr ACTIVITY
#adb -s SAL0217A28001753 shell ps 26387

#wechat webview
#debugmm.qq.com/?forcex5=true
#debugtbs.qq.com

#error: The instrumentation process cannot be initialized. Make sure the application under test does.
#adb -s SAL0217A28001753 uninstall io.appium.settings
##adb -s SAL0217A28001753 uninstall io.appium.uiautomator2.server.test



#定位元素的父（parent::）、兄弟（following-sibling::、preceding-sibling::）节点


#=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=


