"""Подсчет транспортного налога"""
mpg=raw_input("Tell me your car's power!")
mpg=int(mpg)

print "\nThanks,but how is about your region?"

region=raw_input("\nYour region is Moscow,Samara or Saint-Petersburg?\nTell me please:")

while region!="Moscow" and region!="Samara" and region!="Saint-Petersburg":
    region=raw_input("\nOoops,your region is Moscow,Samara or Saint-Petersburg?")

print "\nGreat!"

print "Let's think how much u have to pay:"

if mpg>=100 and mpg<=125 and region=="Moscow":
    nalog=24*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg<=100 and region=="Moscow":
    nalog=7*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=100 and mpg<=175 and region=="Moscow":
    nalog=49*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=200 and region=="Moscow":
    nalog=63*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=250 and mpg<=225 and region=="Moscow":
    nalog=70*mpg
    print "Pay "+str(nalog)+" in "+str(region)

elif mpg>=100 and mpg<=125 and region=="Samara":
    nalog=24*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg<=100 and region=="Samara":
    nalog=7*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=100 and mpg<=175 and region=="Samara":
    nalog=49*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=200 and region=="Samara":
    nalog=63*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=250 and mpg<=225 and region=="Samara":
    nalog=70*mpg
    print "Pay "+str(nalog)+" in "+str(region)  

elif mpg>=100 and mpg<=125 and region=="Saint-Petersburg":
    nalog=26*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg<=100 and region=="Saint-Petersburg":
    nalog=13*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=100 and mpg<=175 and region=="Saint-Petersburg":
    nalog=51*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=200 and region=="Saint-Petersburg":
    nalog=65*mpg
    print "Pay "+str(nalog)+" in "+str(region)
elif mpg>=250 and mpg<=225 and region=="Saint-Petersburg":
    nalog=72*mpg
    print "Pay "+str(nalog)+" in "+str(region)  
    

