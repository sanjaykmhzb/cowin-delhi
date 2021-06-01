###############################################################################
"""
Created on Thu May 31 13:22:46 2021
Author: Parul Gangwar
Program: To get the vaccine availability details on Telegram for Delhi location
Filters: 18+ and available_capacity_dose1 >1
"""
###############################################################################

import requests
import datetime
import time

theday = datetime.date.today()
start = theday - datetime.timedelta(days=0)
dates = [start + datetime.timedelta(days=d) for d in range(7)]

listOfAllCentresFor18=[]    
###############################################################################
#List of Delhi Pincodes
###############################################################################    
pinid =[110001,	110002,	110003,	110004,	110005,	110006,	110007,	110008,	110009,	110010,	110011,	110012,	110013,	110014,	110015,	110016,	110017,	110018,	110019,	110020,	110021,	110022,	110023,	110024,	110025,	110026,	110027,	110028,	110029,	110030,	110031,	110032,	110033,	110034,	110035,	110036,	110037,	110038,	110039,	110040,	110041,	110042,	110043,	110044,	110045,	110046,	110047,	110048,	110049,	110050,	110051,	110052,	110053,	110054,	110055,	110056,	110057,	110058,	110059,	110060,	110061,	110062,	110063,	110064,	110065,	110066,	110067,	110068,	110069,	110070,	110071,	110072,	110073,	110074,	110075,	110076,	110077,	110078,	110079,	110080,	110081,	110082,	110083,	110084,	110085,	110086,	110087,	110088,	110089,	110090,	110091,	110092,	110093,	110094,	110095,	110096,	110097,	110098,	110099,	110100,	110101,	110102,	110103,	110104,	110105,	110106,	110107,	110108,	110109,	110110]

###############################################################################
#COWIN API and Telegram API URL
###############################################################################
for p in pinid:
    for d in dates:
        d1=str(d.strftime("%d-%m-%Y"))
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}".format(p,d1)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers=headers)
        data = x.json()
        
        cnt2=1
        centre_detail_2 = ""        
        centre_detail_2 = centre_detail_2 + "Date: "+ d1 + "\n"
        
        for d in data["sessions"]:
         
            if d["min_age_limit"] == 18 and d["available_capacity_dose1"] > 1:
                #centre_detail_2 =centre_detail_2 + "\nPincode:" + str(d["pincode"]) +"\nCentre {0}: ".format(cnt2)+ ", "+"\nCentre Address:" + d['name'] + ", " + d["address"] + "\nVaccine: " + d['vaccine'] + "\nSlots for Dose 1: " + str(d["available_capacity_dose1"]) + '\n' 
                centre_detail_2 = centre_detail_2 + "\nDistrict:" + d['district_name'] + "\nPincode:" + str(d["pincode"]) + "\nCentre:" + d['name'] + "\n"+ d['address'] + "\nVaccine: " + d['vaccine'] + "\nFee:"+ str(d["fee"]) +"\nSlots for Dose1: " + str(d["available_capacity_dose1"]) + '\n' 
                listOfAllCentresFor18.append(centre_detail_2)
                centre_detail_2=''
                cnt2=cnt2+1
        
        
###############################################################################
#Sending data to Telegram bot
###############################################################################                
messageFor18 = ""
if len(listOfAllCentresFor18) >0:
    messageFor18 = messageFor18 + "[18 to 44][1st Dose]\n"
    for mess in  listOfAllCentresFor18:
        messageFor18 = messageFor18 + mess +"\n"
        messageFor18 = messageFor18 + "\n"     
    base_url = "https://api.telegram.org/bot1752190941:AAFDD_WZs_1XjsBgo_rhx5lZ4W6F0nrjOb8/sendMessage?chat_id=@COWIN_Delhi_Upd&text={0}".format(messageFor18)
    print("Response:",requests.get(base_url))
    print("Message Sent for 18+!")
else:
    messageFor18="No slot available for 18+"
    base_url = "https://api.telegram.org/bot1752190941:AAFDD_WZs_1XjsBgo_rhx5lZ4W6F0nrjOb8/sendMessage?chat_id=@COWIN_Delhi_Upd&text={0}".format(messageFor18)
    print("Response:",requests.get(base_url))
    print("No slot available for 18+")
        
while True:
    time.sleep(30)

