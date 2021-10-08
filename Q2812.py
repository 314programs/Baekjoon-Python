num = int(input())

#Turn it into a list for sorting
numlist = [int(v) for v in str(num)]
numlist.sort(reverse = True)
Result = ''

#Add the sorted items into the results
for item in numlist:
    Result += str(item)
print(Result)
