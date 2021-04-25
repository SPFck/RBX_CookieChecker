# Made by: Thomas Shelby#9918
# http://github.com/SPFck

import requests, json, time, os

def err(a1, a2):
	print(f"Error! {a1} | {a2}")
	exit()

def prc(x):
	if x == True:
		return "Yes"
	else:
		return "No"

def irt_chk():
	while True:
		curr_cookie = input("Cookie: ")
		os.system(config["clear_cmd"])
		try:
			req = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": curr_cookie})
			x = json.loads(req.text)
			print(f"Valid cookie!\nUserID: {x['UserID']}\nUsername: {x['UserName']}\nRobux: {x['RobuxBalance']}\nPremium: {prc(x['IsPremium'])}\n")
		except:
			print("Invalid cookie!\n")

def nirt_chk(x, y):
	save = open("working_cookies.txt", "w")
	with open(x) as cookies:
		for cookie in cookies:
			clean_c = cookie.replace("\n", "")
			try:
				req = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": clean_c})
				x = json.loads(req.text)
				print(f"Valid cookie! [UserID: {x['UserID']} | Username: {x['UserName']} | Robux: {x['RobuxBalance']} | Premium: {prc(x['IsPremium'])}]")
				save.write(f"{clean_c} -=- [UserID: {x['UserID']} | Username: {x['UserName']} | Robux: {x['RobuxBalance']} | Premium: {prc(x['IsPremium'])}]\n")
			except:
				print("Invalid cookie!")
			time.sleep(y)

config = json.loads(open("settings.json", "r").read())

if config["irt_chk"] == True:
	irt_chk()
elif config["irt_chk"] == False:
	try:
		open(config["list"], "r")
		time.sleep(1) # Prevent Errors
		nirt_chk(config["list"], config["delay"])
	except:
		err("Config Error", "list")
else:
	err("Config Error", "irt_chk")