#set a temp sequence to the list
cars=['bmw','audi','toyota','subaru']
print('Here is the original list.')
print(cars)

print('\nHere is the sorted list.')
print(sorted(cars))

print('\nHere is the original list again.')
print(cars)

#set a permenant sequence to the list
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#print the list backwards(permenant
cars=['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

#number of elements in the list(starts from 1
print(str(len(cars))+' car brand(s) in total')

