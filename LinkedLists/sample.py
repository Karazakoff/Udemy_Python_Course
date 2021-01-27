class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
    def get(self, index):
        if index > self.length() - 1:
            prinr("Error, Index out of range!")
            return None
        cur = self.head
        counter = 0
        while cur.next != None:
            cur = cur.next
            if counter == index:
                print(cur.data)
                break
            else:
                counter += 1
        return None
    def erase(self, index):
        if index > self.length() - 1:
            print("Error, Erase index out of range!")
            return None
        cur = self.head
        cur_index = 0
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index:
                last_node.next = cur.next
                return None
            cur_index += 1




s = LinkedList()
s.display()
s.append(0)
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.append(7)
s.append(8)
s.append(9)
s.display()
print(s.length())
s.get(7)
s.get(0)
s.erase(0)
s.display()
