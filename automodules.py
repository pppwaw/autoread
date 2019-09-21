import time,random,threading,os
from com.dtmilano.android.viewclient import ViewClient
device, serialno = ViewClient.connectToDeviceOrExit()

# vc.findViewByIdOrRaise("com.jm.video:id/comment")
# vc.findViewByIdOrRaise("com.jm.video:id/editComment")
class BaseModules:
    def __init__(self, appTime, devices, ispraise):
        self.appTime = appTime
        self.devices = devices
    def run(self):
        self.threading=[]
        stoptime=int(time.time())+self.appTime
        for device,serialno in self.devices:
            info=device.getDisplayInfo()
            width,height = info["width"],info["height"]
            self.threading.append(threading.Thread(target=self._run,args=(device,serialno,stoptime,width,height)))
        [i.start() for i in self.threading]
        [i.join() for i in self.threading]
    def _run(self,device,serialno,stoptime,width=1080,height=1920):
        pass
class ShuaBao(BaseModules):
    def run(self,isPraise=True):
        self.threading=[]
        stoptime=int(time.time())+self.appTime
        for device,serialno in self.devices:
            info=device.getDisplayInfo()
            width,height = info["width"],info["height"]
            self.threading.append(threading.Thread(target=self._run,args=(device,serialno,stoptime,width,height,isPraise)))
        [i.start() for i in self.threading]
        [i.join() for i in self.threading]

    def _run(self,device=None,serialno=None,stoptime=7200,width=1080,height=1920,isPraise=True):
        if device==None:
            device, serialno = ViewClient.connectToDeviceOrExit()
        elif serialno==None:
            serialno=device.serialno
        device.startActivity("com.jm.video/.ui.main.SplashActivity")
        time.sleep(8)
        device.touch(width/2, height/2)
        vc = ViewClient(device, serialno)
        device.touch(width/2, height/2)
        while True:
            vc.swipe(width / 2, height / 4 * 3, width / 2, height / 4 * 1)
            t=random.randint(1,20)
            print t
            if t>stoptime-int(time.time()):
                t=stoptime-int(time.time())
            if t%2==0:
                time.sleep(t/2)
                vc.findViewByIdOrRaise("com.jm.video:id/praise").touch()
                time.sleep(t/2)
            else:
                time.sleep(t)
            if int(time.time()) >= stoptime:
                break
        device.shell("am force-stop com.jm.video")
class HuiShiPin(BaseModules):
    def _run(self,device=None,serialno=None,stoptime=7200,width=1080,height=1920,isPraise=True):
        if device==None:
            device, serialno = ViewClient.connectToDeviceOrExit()
        elif serialno==None:
            serialno=device.serialno

        device.startActivity("com.jm.video/.ui.main.SplashActivity")
        time.sleep(8)
        device.touch(width/2, height/2)
        vc = ViewClient(device, serialno)
        device.touch(width/2, height/2)
        while True:
            vc.swipe(width/2,height/4*1,width/2,height/4*3)
            t=random.randint(1,20)
            print t
            if t>stoptime-int(time.time()):
                t=stoptime=int(time.time())
            if t%2==0:
                time.sleep(t/2)
                vc.findViewByIdOrRaise("com.jm.video:id/praise").touch()
                time.sleep(t/2)
            else:
                time.sleep(t)
            if int(time.time()) >= stoptime:
                break
        device.shell("am force-stop com.jm.video")
