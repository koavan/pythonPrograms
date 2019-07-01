a=['Jan 1, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 5',
   'Jan 3, 2020: shop1 324$shop3 310$shop4 420$shop5 10',
   'Jan 6, 2020:',
   'Jan 8, 2020: shop1 316$shop1 820$shop3 330$shop4 420$shop5 17',
   'Jan 10, 2020: shop3 350']
myDict = {}

for e in a:
    dayVals = e[e.index(":")+1::].strip(" ")
    if len(dayVals)>=2:
        dayVals = dayVals.split("$")
        for i in dayVals:
            i = i.strip(" ")
            temp = i.split(" ")
            if temp[0] in myDict.keys():
                t = myDict.get(temp[0])
                t.append(int(temp[1]))
                myDict.update({temp[0]:t})
            else:
                myDict.update({temp[0]:[int(temp[1])]})

#print(myDict)
total = 0
for shop, cost in myDict.items():
    bill = sum(cost)
    if bill<=1000:
        bill = bill * 0.4
    elif bill>1000 and bill<=2000:
        bill = bill * 0.33
    elif bill>2000 and bill<=5000:
        bill = bill * 0.30
    elif bill<5000:
        bill = bill * 0.20
    print(shop + " bill: " + str(bill))
