import sys

def combSort(nums):
    shrinkFact = 1.3
    gaps = len(nums)
    swapped = True
    i = 0

    while(gaps > 1 or swapped):
        gaps = int(float(gaps) / shrinkFact)
        swapped = False
        i = 0
        while(gaps + i < len(nums)):
            if(nums[i] > nums[i + gaps]):
                nums[i],nums[i + gaps] = nums[i+gaps], nums[i]
                swapped = True
            i = i + 1

    return nums

num1 = input('Input comma separated numbers:\n').strip()
nums = [int(item) for item in num1.split(',')]
print(combSort(nums))


def cycleSort(vector):
    writes = 0
    for cycleStart,item in enumerate(vector):
        pos = cycleStart
        for item2 in vector[cycleStart+1:]:
            if(item2 < item):
                pos = pos + 1

        if(pos == cycleStart):
            continue

        while(item == vector[pos]):
            pos = pos + 1
        vector[pos],item = item,vector[pos]
        writes = writes + 1
        while(pos != cycleStart):
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if(item2 < item):
                    pos = pos + 1
            while(item == vector[pos]):
                pos = pos + 1
            vector[pos],item = item,vector[pos]
            writes = writes + 1

    return writes


x = [0, 1, 2, 2, 2, 2, 1, 9, 3.5, 5, 8, 4, 7, 0, 6]
xcopy = x[::]
writes = cycleSort(xcopy)
if(xcopy != sorted(x)):
    print("Wrong Order!")
else:
    print("{0}-{1}-{2}".format(x,xcopy,writes))































    