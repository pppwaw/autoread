import time,random,threading,os
from com.dtmilano.android.viewclient import ViewClient
device, serialno = ViewClient.connectToDeviceOrExit()

# vc.findViewByIdOrRaise("com.jm.video:id/comment")
# vc.findViewByIdOrRaise("com.jm.video:id/editComment")
class BaseModules:
    def __init__(self, appTime, devices):
        self.appTime = appTime
        self.devices = devices
    def run(self,ispraise=True):
        self.threading=[]
        stoptime=int(time.time())+self.appTime
        for device,serialno in self.devices:
            self.threading.append(threading.Thread(target=self._run,args=(device,serialno,stoptime,ispraise)))
        [i.start() for i in self.threading]
        [i.join() for i in self.threading]
    def _run(self,device,serialno,stoptime,isPraise):
        pass
class Shuabao(BaseModules):
    def _run(self,device=None,serialno=None,stoptime=7200,isPraise=True):
        if device==None:
            device, serialno = ViewClient.connectToDeviceOrExit()
        elif serialno==None:
            serialno=device.serialno
        device.startActivity("com.jm.video/.ui.main.SplashActivity")
        time.sleep(8)
        device.touch(540, 900)
        vc = ViewClient(device, serialno)
        device.touch(540, 900)
        while True:
            vc.swipe(540,1100,540,700)
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
