from selenium import webdriver
import time

mfile = open("massage.txt",encoding="utf8")
massage1 = ""
for x in mfile.readlines():
    massage1 += x
mfile.close()

browser = webdriver.Chrome()
f=open("number.txt", "r")
fread = f.read()
i = int(fread)
f.close()
url = "https://www.sarahaa.net/"
browser.get(url)
time.sleep(1)
while i > 0:
    js = "$.ajax({url: '/Messages/SendMessage',type: 'POST',cache: false,data: {userId: '"+ str(i) +"',text: `" + massage1 + "`}})"
    browser.execute_script(js)
    time.sleep(0.03)
    print(i)
    i = i - 1
    if(i % 1000 == 0):
        time.sleep(6)
    f=open("number.txt", "w")
    f.write(str(i))
    f.close()
