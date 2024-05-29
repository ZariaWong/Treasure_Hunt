BigValueList=[]
BigMapList=[]
IniCoordinatesList=[]


k=1
m=0
values=input()
BigValueList.append(values)
while k != int(len(values)):
    k+=1
    values=input()
    BigValueList.append(values)
while m !=int(len(values)):
    values=input()
    V=len(values)
    BigMapList.append(values)
    m+=1

for a in range(len(values)):
    for b in range(len(values)):
        if BigMapList[a][b]=='0':
            IniCoordinatesList.append([b,a])


x=100
y=100
XYlist=[x,y]
for a in range(len(IniCoordinatesList)):
    if IniCoordinatesList[a][0]<=XYlist[0]:
        XYlist[0]=IniCoordinatesList[a][0]
    if IniCoordinatesList[a][1]<=XYlist[1]:
        XYlist[1]=IniCoordinatesList[a][1]
print(XYlist[0],XYlist[1])




