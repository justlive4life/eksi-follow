import requests
ses = requests.Session()
baseheaders = {
    "Host": "eksisozluk.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
baseheaders2 = {
    "Host": "eksisozluk.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",

}

base = ses.get("https://eksisozluk.com", headers=baseheaders)
print(ses.cookies.get_dict())
giris = ses.get("https://eksisozluk.com/giris", headers=baseheaders)

reqv = ses.cookies["__RequestVerificationToken"]
cokus = []
for c in ses.cookies:
    template = c.name + "=" + c.value + ";"
    cokus.append(template)
urc = cokus[0] + " " + cokus[1] + " " + cokus[2] + " " + cokus[3]
baseheaders["cookie"] = urc

print(baseheaders)
myjson = {
    "__RequestVerificationToken": reqv,
    "UserName": "thearteus@proton.me",
    "Password": "Kisarok2009!",
    "RememberMe": "False",
    "ReturnUrl": "https://eksisozluk.com/"
}
print(myjson)
log = ses.post("https://eksisozluk.com/giris",
               headers=baseheaders, json=myjson)
print(log)
print(log.headers)
home = ses.get("https://eksisozluk.com/")
print(home.content)
