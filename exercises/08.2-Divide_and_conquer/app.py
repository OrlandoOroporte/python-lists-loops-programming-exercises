list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

odd = []
even=[]

def merge_two_list (list):
    for x in list: 
        if x % 2 == 0:
            even.append(x)
        elif x % 2 !=0:
            odd.append(x)
    return [odd] + [even]



print(merge_two_list(list_of_numbers))

