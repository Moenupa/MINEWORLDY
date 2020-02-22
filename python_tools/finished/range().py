for i in range(0,5,1):
    print(i)
print(i)

x=0
for i in range(0,5,1):
    x=x+i
    print(x)
print(x)


print(list(range(5)))


print(list(range(0,-10,-1)))


squares = []
for i in range(1,11):
	square = i**2
	squares.append(square)
print(squares)
#this is how range() is used in practice

#Or used in an advanced way:

print(list(i**2 for i in range(1,11,2)))
