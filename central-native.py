values = [47,95,88,73,88,84]

print (len(values)) #count
print (sum(values)) #sum

#mean
mean = (sum(values)/len(values))
print (mean)

#median
n = len(values)
values.sort()

if n % 2 == 0:
    median1 = values[n//2]
    median2 = values[n//2-1]
    median = (median1 + median2)/2
else:
    median = values[n//2]
print (median)

#mode
mode = max(values, key = values.count)
print (mode)  


