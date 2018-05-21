

#
#   My Solutions to Cracking the Coding interview v.6
#   Luis A. Mireles / Summer 2018
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def remove_node(self, value):

        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True

            prev = curr
            curr = curr.getNextNode()

        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current= current.next


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 2.1 Remove Dups:
# Write code to remove duplicates from an unsorted linked list.
#
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
#
# I   : Remove nodes that match nodes of previous values
# D   : LL that has no duplicates in end
# E\A : As you scan list, store values of each node and when a duplicate occurence occurs you redirect the previous
#       nodes .next pointer to the next non duplicate number. Therefor it is necessary while checking you consult
#       your list of values that you're not assigning the next node to a duplicate.
# L   : Assume list is unsorted, we have two pointers that point to the current node being analyzed and the sec(ond)
#       which will check future nodes in sequence to see if they match current. This occurs for all nodes, space
#       complexity is optimal but time is dependent on the size of n where complexity is equal to n^2-n

def remove_dup(link_list):
    current = sec = link_list.head

    # use current node to check all future nodes for
    # duplicate occurrences, this occurs for all nodes
    while current is not None:
        while sec.next.data is not None:

            # if duplicate exists redirect .next
            if sec.next.data == current.data:
                sec.next = sec.next.next
            else:
                sec = sec.next
        current = sec = current.next
    return link_list


# 2.2 Return Kth to Last:
# Implement an algorithm to find the kth to last element of a singly linked list.
#
# I   : Find kth to last element
# D   : We locate from (end-n) node
# E\A : We have two pointers that move together but one has a head start by k hops, when leading pointer reaches end
#       of list the second pointer will be located on kth node.
# L   :


def kth_from_last(k, link_list):
    end = kth = link_list.head

    # establish head start in end node
    for end in range(0, k):
        end = end.next

    # when head start is established we
    # begin moving pointers until end is reached
    while end.next is not None:
        end = end.next
        kth = kth.next
    return kth.data


# 2.3 Delete Middle Node:
# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
#
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
#
# I   : delete mid node in link list
# D   : link list where middle node is removed
# E\A : set two pointers, one whose job is to reach the end of the list and the other to reach the middle of the list
#       the mid pointer will move every 2nd hop the end pointer does, so when end is reached the mid node will be in
#       the correct position to delete
# L   :

def del_med(link_list):
    end = mid = link_list.head

    # establish fast and slow runner
    while end is not None:
        for i in link_list:
            if i % 2:
                end = end.next
            else:
                mid = mid.next
                end = end.next

    if mid is not link_list.head or mid is not end:
        mid = mid.prev
        mid.next = mid.next.next
    else:
        print("link list too small")


# 2.4 Partition:
# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
#
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints: #3, #24
#
# I   : Rearrange so that all values less than x are to it's left, and all greater to it's right.
# D   : an arranged list of numbers where x is the midpoint of list and as mentioned above
# E\A : move down list and analyze if value is less than or greater than x, then begin sort as you
#       move towards end of list
# L   :

def partition(self, val):
    prev = None
    x = self
    while x:
        if prev and x.data < val:
            prev.next = x.next
            x.next = self
            self = x
            x = prev.next
        else:
            prev = x
            x = x.next
    return self


# 2.5 Sum Lists:
# You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
#
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
# Output: 2 -) 1 -) 9. That is, 912.
#
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
#
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).That is,617 + 295.
# Output: 9 -) 1 -) 2. That is, 912.
#
# I   : use numbers stored in a linked list to create two seperate numbers (stored backwards) to add sep by +.
# D   : a new number returned that represents the addition of two numbers
# E\A : push numbers in stack until an operator is read, then append whats popped from stack into new number and
#       begin same process with second number except when end of link list is reached we add these two numbers
# L   :

def sum_lists(self):
    current = self.head
    stack = Stack()
    value = 0

    while current:
        if current.date == '+':
            while not stack:
                value.extend(stack.pop())
        else:
            push(current.data)
            current = current.next

