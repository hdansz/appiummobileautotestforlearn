from appium import webdriver
import os
import yaml

path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file=path+"/Config/desire_caps_wx.yaml"
#f=open(file,"r")
with open(file,'r') as f:
    CAPS=yaml.safe_load(f)

def mydriver():
    desired_caps = {}
    desired_caps['platformName'] = CAPS['platformName']
    desired_caps['platformVersion'] = CAPS['platformVersion']
    desired_caps['appPackage'] = CAPS['appPackage']
    desired_caps['appActivity'] = CAPS['appActivity']
    desired_caps['deviceName'] = CAPS['deviceName']
    desired_caps['noReset'] = CAPS['noReset']
    desired_caps['skipServerInstallation'] = CAPS['skipServerInstallation']
    desired_caps['skipDeviceInitialization'] = CAPS['skipDeviceInitialization']
    driver = webdriver.Remote(CAPS['port'], desired_caps)
    driver.implicitly_wait(10)
    return driver

