

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
# L   : push operation tracks in real time the min and is able to access at any time by peeking stack

def push(self, item, curr_min):
    if self.IsFull():
        raise Exception('Stack full')

    if self.IsEmpty():
        curr_min = item

    else:
        if item < curr_min:
            curr_min = item


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
# I   : implement a size limit on size of stack where if it is exceeded a new stack is then created
# D   : multiple stacks when push count exceeds limit
# E\A : design push so that if limit is met a new stack is used to store push contents, pop will begin
#       from the most recently created stack and when it is emptied it will then pop stack created
#       previous to that.
# L   : implementation follows scheme where if stack max is reached we start moving to second stack

def push(self, item):
    if len(self.stacks) and (len(self.stacks[-1]) < self.capacity):
        self.stacks[-1].append(item)
    else:
        self.stacks.append([item])

def pop(self):
    while len(self.stacks) and (len(self.stacks[-1]) == 0):
        self.stacks.pop()
    if len(self.stacks) == 0:
        return None
    item = self.stacks[-1].pop()
    if len(self.stacks[-1]) == 0:
        self.stacks.pop()

    return item


# 3.4 Queue via Stacks:
# Implement a MyQueue class which implements a queue using two stacks.
#
# I   : implement queue using stack
# D   : stack that maintains the order similar to queue
# E\A : have two stacks that shuffle values inside, first stack stores initial values until it
#       it needs to be popped, these values are then popped and moved to second stack, the order
#       it is now being filed under is proper queue where first in is at the head. New pushed items
#       are still put onto 1st stack and unless a pop removes all items ins 2nd is performed in the two stacks there
#       wont be any more shuffling
# L   : to pop item in queue stack takes the same amount of steps as it dude to push it in place but after a pop has
#       been made to a sizeable stack we can freely pop from stack in constant time

class QueueViaStacks():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def add(self, item):
        self.in_stack.push(item)

    def remove(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()


# 3.S Sort Stack:
# Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
#
# I   : sort stack using another stack
# D   : a stack that is sorted by its contents
# E\A : Pop an element from input stack call it temp while temporary stack is not empty and top of temporary stack is
#       greater than temp, pop from temporary stack and push it to the input stack push temp in temporary stack
# L   : More shuffling and monitoring where the sorted numbers a re held inside temp stack

def sort_stack(stack):
    temp = Stack()
    previous = current = stack.pop()

    # scan stacks for smaller values
    while current:
        if current < previous:
            temp.push(current)
        else:
            temp.push(previous)
        previous = current
        current = stack.pop()
    is_sorted = True
    current = temp.pop()

    while current:
        if current > previous:
            is_sorted = False
            stack.push(current)
        else:
            stack.push(previous)
        previous = current
        current = temp.pop()
        stack.push(previous)
        if is_sorted:
            return stack
        return sort_stack(stack)