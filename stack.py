# Function to check validity of stack sequence 
def validateStackSequence(pushed, popped): 
    # maintain count of popped elements 
    j = 0

    # an empty stack 
    stack = [] 

    for x in pushed: 
        stack.append(x) 

        # check if appended value is next to be popped out 
        while stack and j < len(popped) and stack[-1] == popped[j]: 
            stack.pop() 
            j = j + 1

    return j == len(popped) 


# Driver code 
# pushed = [1, 2, 3, 4, 5] 
# popped = [4, 5, 3, 2, 1] 
# print(validateStackSequence(pushed, popped)) 


popped = list()
stacklength = 4
pushed = list(i for i in range(stacklength))
import itertools
validset = set()
for sub_popped in itertools.permutations(pushed, stacklength):
    print(sub_popped, end = "")
    if validateStackSequence(pushed, sub_popped):
        print(True, end = "")
        validset.add(sub_popped)
    print()

print(len(validset))