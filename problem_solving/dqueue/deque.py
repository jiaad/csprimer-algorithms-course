class DNode(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque(object):
    def __init__(self) -> None:
        self.head = None 
        self.tail = None
        self.length = 0

    def push_left(self, val):
        new_node = DNode(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        head = self.head
        head.prev = new_node
        new_node.next = head
        self.head = new_node
        self.length += 1
        return
    
    def push_right(self, val):
        new_node = DNode(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        tail = self.tail
        new_node.prev = tail
        tail.next = new_node
        self.tail = new_node
        self.length += 1
        return
    
    def pop_left(self):
        if not self.head:
            print("head not exist")
            raise ValueError
        head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return  head.val
        nh = head.next
        head.next = None
        nh.prev = None
        self.head = nh
        self.length -= 1
        return head.val
    
    def pop_right(self):
        if not self.head:
            print("head not exist")
            raise ValueError
        tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return tail.val
        nt = tail.prev
        tail.prev = None
        nt.next = None
        self.tail = nt
        self.length -= 1
        return tail.val


if __name__ == "__main__":
    a = Deque()

    assert a.head == None
    a.push_left(1)
    assert a.head.val == 1
    assert a.head == a.tail

    a.push_left(2)
    assert a.head.val == 2

    a.push_left(3)
    assert a.head.val == 3

    a.push_right(4)
    a.push_right(5)
    a.push_right(6)
    a.push_right(7)

    assert a.head.next.next.next.next.next.next.val == 7
    assert a.head.next.next.next.next.next.val == 6
    assert a.head.next.next.next.next.val == 5
    assert a.head.next.next.next.val == 4

    a.pop_left()
    a.pop_left()
    a.pop_left()
    a.pop_left()
    a.pop_left()
    print(a.tail.val)
    assert a.tail.val == 7
    a.push_right(500)
    assert a.tail.val == 500
    a.pop_right()
    assert a.tail.val == 7

    print("ok")


def push_left(self, val):
    n = DNode(val)
    if self.size == 0:
        self.head = n
    else:
        self.tail.prev = n
    n.next = self.tail
    self.size += 1
