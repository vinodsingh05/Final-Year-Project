import asyncio
import requests
from bs4 import BeautifulSoup
import time
from forex_python.converter import CurrencyRates
c = CurrencyRates()

url="https://www.idrive.com/pricing"

cval="h"
ccval=0
ctype="storage"
cdescription="(rate in per GB per month)IDrive Team 5TB Storage for one Year and Five Computers for 5 Users to access"
cprovider="Icedrive"

def fetch_data():
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    # print(soup)
    ele=soup.find_all(class_="pt-dollar")
    
    # print(ele.get_text())


    ctr=0
    for t in ele:
        if(ctr==2):
            s=t.get_text()
            s=s[1:]
            # print(s)
            global ccval
            ccval=float(s)
            ccval = c.convert("USD","INR", ccval)
            ccval=round(ccval,3)
            break;
        ctr+=1


# counter=0   

def upd():
    print("we are here")
    f = open("./subpro/obj20con.txt", "w")
   
    # ccval+=counter
    # f.write("Rs "+str(ccval))
    f.write(str(round(ccval/(12*5000),3)))
    f.write('\n')
    f.write(ctype)
    f.write('\n')
    f.write(cdescription)
    f.write('\n')
    f.write(cprovider)
    f.write('\n')
    f.write(url)
    f.write('\n')
    f.close()



async def main():
    while(1):
        fetch_data()
        upd()
        time.sleep(1)
    
   
asyncio.run(main())