# To find the frequency of the elements

def countFrequency(arr, size):

    for i in range(0, size):
        flag = False
        count = 0

        for j in range(i+1, size):
            if arr[i] == arr[j]:
                flag = True
                break

        if flag == True:
            continue

        for j in range(0, i+1):
            if arr[i] == arr[j]:
                count += 1

        print("{0}: {1}".format(arr[i], count))

arr = [5, 8, 5, 7, 8, 10]
n = len(arr)
countFrequency(arr, n)