import requests
from bs4 import BeautifulSoup

msg_url = "http://msg.csdn.net/"
login_url = "http://passport.csdn.net/"

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

session = requests.session()
session.headers.update(headers)
r = session.get(login_url)
page  =BeautifulSoup(r.text,'lxml')
authentication = {
	"username":"baabo",
	"Password":"gaoxzcsdn@0124",
	"lt":page.select("[name=lt]")[0]["value"],
	"execution":page.select("[name=execution]")[0]["value"],
	"_eventId":"submit",

}
r = session.post(login_url,authentication)
r2 = session.get(msg_url)
print(r2.text)
