# Ques 4
print("Question 4")
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


n = int(input("enter the number of integers to be entered:\n"))
li = list(map(int, input("Enter the integers with spaces but without commas:\n").strip().split()))
quickSort(li, 0, n - 1)
print("Sorted array is: ", li)


# Ques 5
print("question 5")
n = int(input("enter the number of integers to be entered:\n"))
li = list(map(int, input("Enter the integers with space but without commas:\n").strip().split()))
# Part 1
li.sort()
print("Sorted array is:", li)

# Part 2
flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input("Enter the integer from list whose index and number of occurances you want to find:\n"))
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Value is at index:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("Error")

# Part 3
if(ind == -1):
    print("No element\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total number of occurances is:", count - 1)
