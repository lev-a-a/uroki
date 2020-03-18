#1048193761:AAGodFibb-gFkAcQPCbrk0eYVOuOPtsBMlw


import urllib.request

l=urllib.request.urlopen("https://api.privatbank.ua/p24api/pubinfo?cardExchange")
l=str(l.readlines()[0])



s=0
v=input ("usd, eur, rur ")
if v=="usd":
    s=l.find("USD")
if v=="eur":
    s=l.find("EUR")
if v=="rur":
    s=l.find("RUR")



i=l.find("buy=",s)+5
buy=(l[i:i+8])
i=l.find("sale=",s)+6
sale=(l[i:i+8])

l=urllib.request.urlopen("https://web.telegram.org/#/im?p=@Noviy_centr")
l=str(l.readlines()[0])
print (l)



print ("ПриватБанк "+v+":"+buy,sale)
