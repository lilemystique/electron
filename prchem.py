from statistics import mean
import matplotlib.pyplot as plt

d = open('D:/Files/Python/new 28.txt', 'r', encoding = 'utf-8')
q = d.read().replace(',','.').replace(' ',' ').replace(',','.').replace('/n',' ').split()

p = [float(el) for el in q]

odd = (p[::2])
even = (p[1::2])
'''print('значення odd:', odd)
print('значення even:', even)'''
m = mean(even)
#print ('mean(even):', m)
data = []
for i in (even):
    if m>=i:
        data.append(i)  
#print("менше за мін", ltm)

w = data[0] #перший 
o = data[-1] #останній індекс

w1 = even.index(w) 
o1 = even.index(o)

y = even[int(w1): int(o1)]
x = odd[int(w1): int(o1)]

plt.figure(figsize=(6,6))
plt.plot(x,y,label ='.',color='black',marker='.',markersize=5)
plt.xlabel('x')
plt.ylabel('y')

#ax.hlines(m)

plt.title('графік - 28')
plt.savefig('quick.png',facecolor='white',edgecolor='white')