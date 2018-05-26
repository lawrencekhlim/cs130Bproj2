import random
power = 5
size = 1
for i in range (power):
    size = size*10

for a in range (size):
    begin = random.randint(0,size-1)
    end = random.randint(begin+1,size)
    pay = random.randint(0,size)
    print (str(begin)+ " "+ str (end)+ " "+ str(pay))
