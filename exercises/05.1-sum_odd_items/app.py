arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds (list):
    sum=0
    for x in list:
        if x % 2 != 0:
            sum += x
    return sum 

print(sum_odds(arr))
     