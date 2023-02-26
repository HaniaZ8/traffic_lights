

#testing ways to resolve the sleep issue
import time
b = True
a = True
#have to have boolean variables for each part (so the sleep seconds don't sum up)
while a == True:
    print("start")
    time.sleep(4)
    print('end')
    a = False

while b == True:
    print("start1")
    time.sleep(4)
    print('end1')
    b = False