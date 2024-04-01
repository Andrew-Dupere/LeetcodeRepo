"""
Rearrange the characters in an array so that no two adjacent characters are identical

input ['A','B','C','C']

output ['A','C','B','C']

"""

a = [1,2,3,4,4,56,7,8,5,4,4,6,7,7,7,10,11,12,14]

def func(arr):
    pass

    idx = 0
    check = True
    output = []    

    for i in range(len(arr)):

        try:

            if arr[i] == arr[i-1] or arr[i] == arr[i+1]:
                item = arr.pop(arr[i])

                for i in range(len(arr)):

                    if item != arr[i-1] and item != arr[i+1]:
                        arr.insert(i, item)
                        break          
                              
                                
        except IndexError:
            continue

print(a)

func(a)

print(a)




                







