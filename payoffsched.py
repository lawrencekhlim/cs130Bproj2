
import sys

def binary_search (twodarray, time):
    front, back = 0,len(twodarray)
    # k < i => a[k] < n
    # k >= j => a[k] >= n
    while front != back:
        mid = (back-front)/2 +front
        if twodarray[mid][0] < time:
            front = mid+1
        else:
            back = mid
    return front

input = []
for line in sys.stdin:
    l = line.strip().split(" ")
    l = map(int, l)
    input.append (l)

#print (input)

# Sort
sorted_arr = sorted(input, key=lambda interval: interval[0])
print (sorted_arr)

table = [0] * len (sorted_arr)
previous = [0] * len (sorted_arr)
table [len (sorted_arr)-1] = sorted_arr [len (sorted_arr)-1][2]
previous [len (sorted_arr)-1] = binary_search (sorted_arr, sorted_arr [len (sorted_arr)-1][1])

#print (previous[len (sorted_arr)-1])
for i in range (len (sorted_arr)-2, -1, -1):
    index = binary_search (sorted_arr, sorted_arr [i][1])
    table [i] = sorted_arr[i][2] + sorted_arr[index][2]
    previous [i] = index
    if table[i] < table [i+1]:
        table [i] = table [i+1]
        previous [i] = -1 * (i+1)
print ("Maximum Payoff: " + str(table[i]))

point = 0
while (point != len (sorted_arr)):
    newpoint = previous[point]
    if newpoint < 0:
        point = -1 * newpoint
    else:
        print (str(sorted_arr[point][0]) + " " + str(sorted_arr[point][1]) + " " + str(sorted_arr[point][2]))
        point = newpoint


