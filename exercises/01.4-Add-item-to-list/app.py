#Remember import random function here:
import random

my_list = [4,5,734,43,45]


def listaAleatorios(n):
      for i in range(n):
        i = random.randint(1, 101)
        my_list.append(i)
      return my_list

listaAleatorios(10)
print(my_list)
    





