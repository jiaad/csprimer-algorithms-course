

class DLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = DLNode(val)
        if not self.head:
            self.head = new_node
            self.length += 1
            return self
        if not self.head.prev:
            head = self.head
            head.prev = new_node
            head.next = new_node
            new_node.prev = self.head
            self.length += 1
            return
        head = self.head
        prev = head.prev
        prev.next = new_node
        head.prev = new_node
        new_node.prev = prev
        self.length += 1
        return self 
    
    def popq(self):
        if not self.head: 
            print("Empty Q")
            return
        head = self.head
        if not head.prev:
            self.head = None
            self.length -= 1
            return
        nh = head.next

        if nh == head.prev:
            nh.prev = None
        else:
            nh.prev = head.prev
        self.head = nh

        # delete prev head
        head.next = None
        head.prev = None
        self.length -= 1
        return 



    def popStack(self):
        if not self.head: 
            print("Empty Q")
            return
        head = self.head
        if not head.prev:
            self.head = None
            self.length -= 1
            return
        prev = head.prev
        prev2 = prev.prev
        prev2.next = None
        prev.prev = None
        head.prev = prev2
        self.length -= 1
        return 
         
    # HELPER METHODS
    def print(self):
        print("peinr start")
        l = []
        p = self.head
        while p:
            l.append(p.val)
            p = p.next
        print(l)
        print("print end")

    def last(self):
        head = self.head
        while head.next:
            head = head.next
        return head.val

    def exists(self, val):
        p = self.head
        while p:
            if p.val == val: return True
            p = p.next
        return False

        
        

a = Queue()
a.push(90)
assert a.head.val == 90
a.push(93)
assert a.head.val == 90
assert a.head.prev.val == 93
a.push(94)
assert a.head.prev.val == 94
assert a.head.val == 90
a.push(95)
assert a.head.val == 90
assert a.head.prev.val == 95
a.push(96)
assert a.head.val == 90
assert a.head.prev.val == 96
assert a.head.next.val == 93
assert a.head.next.next.val == 94
assert a.head.next.next.next.val == 95
assert a.head.next.next.next.next.val == 96


# test relations
assert a.head.next.prev.val == 90
assert a.head.next.prev.next.val == 93
assert a.head.next.prev.next.prev.val == 90
assert a.head.next.next.next.prev.val == 94
assert a.head.next.next.next.prev.next.val == 95


# =========== POP =============
a.popStack()
assert a.last() == 95
a.popStack()
assert a.last() == 94
assert a.head.prev.val == 94
assert a.head.prev.next == None
assert a.head.prev.prev.val == 93


# add more
a.push(1)
assert a.head.prev.val == 1
assert a.last() == 1
a.push(2)
a.push(3)
a.push(4)

a.popq()

assert a.head.val == 93
assert a.head.next.val == 94
assert a.head.prev.val == 4



b = Queue()

b.push(1)
assert b.head.prev == None
assert b.head.next == None
assert b.head.val == 1

b.popq()
assert b.head == None

b.push(1)
assert b.head.prev == None
assert b.head.next == None
assert b.head.val == 1


b.push(2)
assert b.head.prev.val == 2
assert b.head.next.val == 2
assert b.head.val == 1

b.popq()
assert b.head.val  == 2
assert b.head.prev == None
assert b.head.next == None


b.push(3)
b.push(4)
b.push(5)
b.push(6)
b.push(7)

assert b.length == 6
assert b.last() == 7
assert b.head.val == 2
b.popq()
assert b.length == 5
assert b.last() == 7



b.popq()
assert b.length == 4
assert b.last() == 7

b.popq()
assert b.length == 3
assert b.last() == 7


b.popq()
assert b.length == 2
assert b.last() == 7



b.popq()
assert b.length == 1
assert b.last() == 7

assert b.head.prev == None
assert b.head.next == None
assert b.head.val == 7
print("ok")

# 
# print(a.head.next.prev.next.val)
# assert a.head.val == 96
# a.pop(100)
# assert a.head.val == 96
# a.pop(96)
# assert a.head.val == 95
# a.pop(95)
# assert a.head.val == 94
# a.print()
# 
# assert a.exist(95) == False
# assert a.exist(100) == False
# assert a.exist(96) == False
# assert a.exist(94) == True
# assert a.exist(93) == True
# assert a.exist(90) == True
# 
# 
