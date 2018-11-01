import random
import time
start_time =time.time()

x = random.sample(range(0, 100), 10)
print(x)
key=False
find = int(input('enter the search element'))
for i in range(len(x)):
    if x[i]==find:
        key=True
        print('found',find,i)
        break
if (key==False):
    print('not found')
end_time=time.time()
print(end_time-start_time)

start=time.time()
s=sorted(random.sample(range(0,99),10))
print(s)
key=int(input('enter the search element' ))
first=0
last=len(s)-1
mid=int((first+last)/2)
while (first<=last):
    if (key>s[mid]):
        first=mid+1
    elif (key==s[mid]):
          print('found at',mid)
          break
    else:
        last=mid-1
    mid = int((first + last) / 2)
end=time.time()
print('binary',end-start)

