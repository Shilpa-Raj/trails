import random
import time
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



