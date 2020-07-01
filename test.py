import matplotlib.pyplot as plt

fp=open('지역평균기온.txt','r',encoding="utf-8")
lst = dict()
for item in fp.readlines():
    lst[item.split(',')[0]] = item.split(',')[1].split('\n')[0]
fp.close()

area=[]
temp=list()
for item in lst.items():
    area.append(item[0])
    temp.append(item[1])
dt=dict(zip(area, temp))

plt.plot(temp,'go-.')
plt.xlabel("local")
plt.ylabel("temp")
plt.title("local average temp")

plt.subplot(2,2,1)
plt.plot(temp, 'go--')
plt.subplot(2,2,2)
plt.plot(temp, 'bx')
plt.subplot(2,2,3)
plt.plot(temp, 'r+-.')


plt.show()