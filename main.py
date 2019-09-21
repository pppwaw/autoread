# -*- coding: utf-8 -*-
import os
from com.dtmilano.android.viewclient import ViewClient
from automodules import *
serialnos=[]
for i in os.popen("adb devices"):
    if "\t" in i:
        serialnos.append(i.split("\t")[0])
print "找到设备"+",".join(serialnos)
devices=[]
for i in serialnos:
    # noinspection PyTypeChecker
    devices.append(ViewClient.connectToDeviceOrExit(serialno=i))
hour=3600
shuabao=ShuaBao(60,devices)
shuabao.run()
