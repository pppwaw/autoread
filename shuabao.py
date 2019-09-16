import time,random
from com.dtmilano.android.viewclient import ViewClient
device, serialno = ViewClient.connectToDeviceOrExit()
device.touch(540,900)
vc = ViewClient(device, serialno)
device.touch(540,900)
# vc.findViewByIdOrRaise("com.jm.video:id/comment")
# vc.findViewByIdOrRaise("com.jm.video:id/editComment")
now_time = int(time.time())
zero_time = now_time + 86400 - now_time % 86400 + time.timezone - 3600
two_time = now_time + 7200
device.startActivity("com.jm.video/.ui.main.SplashActivity")
while True:

    vc.swipe(540,1100,540,700)
    t=random.randint(1,20)
    print t
    if t%2==0:
        print "yes"
        time.sleep(t/2)
        vc.findViewByIdOrRaise("com.jm.video:id/praise").touch()
        time.sleep(t/2)
    else:
        print "no"
        time.sleep(t)
    if int(time.time()) >= zero_time:
        break
    elif int(time.time()) >= two_time:
        break