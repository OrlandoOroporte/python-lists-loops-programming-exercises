my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

def prom (list):
    aux = 0 
    for i in range(len(list)):
        aux += list[i]
    return aux/len(list)

   
print(prom(my_list))
