motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

#change element in a group.
motorcycles[0]='ducati'
print(motorcycles)

#add an element at the end of the group
motorcycles.append('honda')
print(motorcycles)

#active changable elements try:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#insert element (place definable
motorcycles.insert(0,'ducati')
print(motorcycles)

#delete elements
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
del motorcycles[1]
del motorcycles[0]
print(motorcycles)

#delete and store an element
#pop() acts on the last element
#pop(0) acts on the first one
motorcycles=['honda','yamaha','suzuki']
pop_motorcycles=motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

#use value to delete:remove
motorcycles.remove('honda')
print(motorcycles)

#reason for remove
motorcycles=['honda','yamaha','suzuki']
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive.')




