import threading
import serial
import datetime
import sys
import traceback

import com_getparam
import com_func
import com_logging2
import com_appConst
import com_putHttp

mDevice = "/dev/ttyACM0"

mOK_CODE=1
mNG_CODE=0

ER_STAT_000="000"
ER_STAT_101="101"
ER_STAT_102="102"
ER_STAT_103="103"

sHEAD="res_dat="

def is_validTime(tmBef, tmNow, iMax):
	ret=False
	
	tmSpan     = tmNow - tmBef
	iSpan     = tmSpan.total_seconds()
	print "iSpan="+ str(iSpan)
	if iSpan > iMax:
		ret=True
	return ret

def init_proc():
    ser=serial.Serial(mDevice ,9600)
    clsConst  = com_appConst.appConstClass()
    clsParam = com_getparam.getparamClass()
    clsCom  = com_func.funcClass()
    clsLog = com_logging2.loggingClass()
    clsHttp= com_putHttp.putHttpClass()
    
    from datetime import datetime
    tmBefPush = datetime.now()

    while True:
        val=ser.readline()
        bFrom = clsParam.Is_fromMC(val)
        if bFrom==True:
        	dic= clsParam.getDict(val)
        	sTime = datetime.now().strftime("%Y%m%d%H%M%S")
        	
        	tmNow = datetime.now()
        	if is_validTime(tmBefPush, tmNow, clsConst.mTimePut ):
        		tmBefPush = datetime.now()
        		try:
        			sRes="";
	        		sMsg = clsHttp.send_push( dic, clsConst.mREST_KEY )
        			sRes =sHEAD + sMsg
        			ser.write(sRes)
	        	except:
					print "--------------------------------------------"
					print traceback.format_exc(sys.exc_info()[2])
					print "--------------------------------------------"
					clsLog.debug( traceback.format_exc(sys.exc_info()[2]) )
        		
        print("IN :"  + val)
	
if __name__ == "__main__":
	t = threading.Timer( 60.0, init_proc)
	t.start()

