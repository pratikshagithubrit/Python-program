

programming={"c":"ritchie","c++":"abc","python":"rossum"}

print("data of dictionry",programming)
print(")data traversal using loop")
for  x in programming:
    print(x)


print(")data traversal using loop")
for  x in programming:
    print(x,programming.get(x))


keyprogramming = programming.keys()
print(type(keyprogramming))

valueprogramming = programming.values()
print(type(keyprogramming))

for i in range(0,len(programming)):
    print("programming name is",keyprogramming[i],end=" ")
    print("name are",valueprogramming[i])