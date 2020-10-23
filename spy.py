def spy_game(arr):
    k = 0
    check_arr = [0,0,7]
    for i in arr:
        if i == check_arr[k]:
            if check_arr[k] == 7:
                return True
            else:
                k = k + 1
    return False
print(spy_game([1,7,2,0,4,5,0]))
