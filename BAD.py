import os
import time
import sys
print("\033[91mChecking dependencies...\033[0m ")
print("I am considering you had instaleed module request! \nPlease type \033[91mpip install requests \033[0m to install it. ")
time.sleep(3)
os.system("bash rq.sh")
import requests
time.sleep(1)
os.system("toilet -f mono12 -F gay Scammer ")
print("coded by\033[96m github.com/Dhirendra"
      "dirdir \033[0m")
print("use for fun not for revenge "
	  "instagram -_bad_dhirendra\033[0m")
phone_no = input("enter phone number(with country code) : ")
msg = input("message to send : ")

resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
})

print(resp.json())
if '"success" : true ' in resp.text :
	print("\033[92m Msg sent \033[0m")
if '"success" : false ' in resp.text :
	print("\033[91m Failed to send sms! ")
#include(scr/www.nemx,mlo ,cmd pi i  amdhirenddra kumar)