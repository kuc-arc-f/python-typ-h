# -*- coding: utf-8 -*- 
import requests
import json
import com_appConst

mHEAD="web-response1="

#com_putHttp
class putHttpClass:

	def __init__(self):
		print ""

	def send_push(self, dict, sKey):
		sRet=""
		clsConst  = com_appConst.appConstClass()
		sParam ="mc_id="+ str(int(dict["mc_id"]))
		sParam+="&rkey="+ clsConst.mREST_KEY
		sParam+="&snum_1="+str(int(dict["snum_1"]))
		sParam+="&snum_2="+str(int(dict["snum_2"]))
		sParam+="&snum_3="+str(int(dict["snum_3"]))
		sParam+="&snum_4="+str(int(dict["snum_4"]))
		sUrl= clsConst.mURL +"/php/mc_post2.php?" +sParam
		try:
			r = requests.get(sUrl ,  timeout=30)
			print r.status_code
			sText= r.text
			print sText
			if (mHEAD in sText):
				dic = sText.split(mHEAD)
				if (len(dic) > 1):
					print dic[1]
					sRet=dic[1]
		except:
			print "failue, send_parse"
			raise
		finally:
			print "End ,send_parse"
		return sRet
		
	def send_parse(self, dict, sTime):
		clsConst  = com_appConst.appConstClass()
		headers = {
		  "X-Parse-Application-Id": clsConst.mParse_APP_ID ,
		  "X-Parse-REST-API-Key": clsConst.mParse_REST_ID ,
		  "Content-Type": "application/json"
		}
		dtParam ={'mc_id': int(dict["mc_id"]) }
		dtParam["snum1"] = int(dict["snum_1"])
		dtParam["snum2"] = int(dict["snum_2"])
		dtParam["snum3"] = int(dict["snum_3"])
		dtParam["snum4"] = int(dict["snum_4"])
		dtParam["dtnum"] = int(sTime)
		
		try:
			r = requests.post('https://api.parse.com/1/classes/SenObject1', headers=headers , data=json.dumps(dtParam), timeout=30)
			print r.status_code
			print r.json()
		except:
			print "failue, send_parse"
			raise
		finally:
			print "End ,send_parse"
