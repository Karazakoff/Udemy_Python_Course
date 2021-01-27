import time


arr = [1,2,3,4,5,6,7,8,9,10,100,1000,10000,100000,100000]



start = time.time()

# for i in range(len(arr)):
#     arr[i] = arr[i] * 10000
# print(arr)
arr = list(map(lambda x: x * 10000, arr))
end = time.time()
print(end - start)
