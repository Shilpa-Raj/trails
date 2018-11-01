import random
import time

start_time=time.time()
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
print('linear time',end_time-start_time)

start=time.time()
x=sorted(x)
first=0
last=len(x)-1
mid=int((first+last)/2)
while (first<=last):
    if (find>x[mid]):
        first=mid+1
    elif (find==x[mid]):
          print('found at',mid)
          break
    else:
        last=mid-1
    mid = int((first + last) / 2)
if(first>last):
    print('not found')
end=time.time()

print('binary time',end-start)
