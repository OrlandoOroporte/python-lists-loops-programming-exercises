par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

pars = par.lower()
counts = {}
#your code go here:

for e in pars:
    if e != ' ':
        if e not in counts:
            counts[e] = 1
        else: counts[e] += 1

print(counts)

