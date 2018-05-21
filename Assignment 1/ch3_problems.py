

#
#   My Solutions to Cracking the Coding interview v.6
#   Luis A. Mireles / Summer 2018
#


# 3.1 Three in One:
# Describe how you could use a single array to implement three stacks.
#
# I   : Create 3 stacks with one array
# D   : 3 stacks which contain elements from single array
# E\A : stacks will be created from contents of array where we first analyze the length of the array and build stack
#       from beginning to mid/2, from midpoint to (mid + mid/2), then lastly mid + mid/2 to length
# L   : By manipulating the cells of the array, dependent on the size we can push contents onto stack 1,2,3

def three_in_one(array):
    length = len(array)
    mid = length/2

    if length < 2:
        print("Not long enough array")
        return False

    else:

        s1 = Stack()
        s2 = Stack()
        s3 = stack()

        for i in array:
            if array(range(0, int(mid/2))):
                s1.push(i)
            elif array(range(int(mid), int(mid) + int(mid/2))):
                s2.push(i)
            elif array(range(int(mid+mid/2) + length)):
                s3.push(i)
            else:
                continue



# 3.2 Stack Min:
# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum
#
# I   : find min function in stack
# D   : stack that can return min
# E\A : in stack. at each push we analyze the current min value. So at new stack we initiate min to be current contents
#       of stack, then when a second item is pushed we compare the prev min and value stored in push item. The new item
#       will then hold the min of the stack at it's current state and so fourth
# L   :

def stack_min(stack):
    print("..")


# 3.3 Stack of Plates:
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
#
# I   :
# D   :
# E\A :
# L   :

def set_of_stacks(stack):
    print("..")


# 3.4 Queue via Stacks:
# Implement a MyQueue class which implements a queue using two stacks.
#
# I   :
# D   :
# E\A :
# L   :

def queue_via_stack(stack):
    print("..")


# 3.S Sort Stack:
# Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
#
# I   :
# D   :
# E\A :
# L   :

def sort_stack(stack):
    print("..")