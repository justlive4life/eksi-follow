import requests
from requests_html import AsyncHTMLSession, HTML, HTMLSession

ses = HTMLSession()

baseheadersa = {
    "User-Agent": "PostmanRuntime/7.26.10",
    "Content-Type": "application/x-www-form-urlencoded"
}


#
baseheaders = {
    "Host": "eksisozluk.com",
    "User-Agent": "PostmanRuntime/7.26.10",
    "Content-Length": "0"
}
giris = ses.get("https://eksisozluk.com/giris", headers=baseheaders)


rvt = giris.html.find(
    'input[name="__RequestVerificationToken"]', first=True).attrs['value']
myjson = {
    "__RequestVerificationToken": rvt,
    "UserName": "thearteus@proton.me",
    "Password": "Eksisozluk!3",
    "RememberMe": "true",
    "ReturnUrl": "https://eksisozluk.com/"
}
log = ses.post("https://eksisozluk.com/giris",
               data=myjson)

myheaders = {
    "x-requested-with": "XMLHttpRequest"
}
for i in range(11000, 3500000):
    i += 1
    res = ses.post(
        "https://eksisozluk.com/userrelation/addrelation/" + str(i) + "?r=b", headers=myheaders)
    if len(res.content) > 3:
            print('Takip Edildi: ' + str(i))
            print(res.content)
    elif len(res.content) > 10:
            print("Ratelimit")
        