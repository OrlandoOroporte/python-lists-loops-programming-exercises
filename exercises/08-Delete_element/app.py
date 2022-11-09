people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:


def deletePerson(person_name):
    #Your code go here:
    newlis=[]
    for x in people:
        newlis.append(x)
    
    for x in newlis: 
        if x == person_name:
            newlis.remove(x)
    return newlis

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))