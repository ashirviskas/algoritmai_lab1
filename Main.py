import random
import time
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def length(self):
        node = self.first
        n = 0
        if node != None:
            n = 1
        while node.next != None:
            n += 1
            node = node.next
        return n


class Student:
    def __init__(self, name = None):
        self.name = name

    def __str__(self):
        return 'Name: ' + self.name


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for y in range(size)]

    def __str__(self):
        string = ""
        for student in self.table:
            string = string  + student.name + "; "
        return string


    def Retrieve(self, key):
        bytes = str.encode(key)
        number = int.from_bytes(bytes)
        hash = number % self.size
        j = 1
        while (self.table[hash] is not None and self.table[hash] != key):
            hash = (hash + j * j) % self.size
            j += 1
        if (self.table[hash] == None):
            print("no such data")
        else:
            return self.table[hash]

    def checkIfFull(self):
        full = True
        for student in self.table:
            if student is None:
                full = False
        return full
    def QuadraticHashInsert(self, student):

        if (self.checkIfFull()):
            print("Tabley is fulley")
            return
        key = student.name
        bytes = str.encode(key)
        number = int.from_bytes(bytes, byteorder='big')
        hash = number % self.size
        j = 1
        while self.table[hash] is not None and self.table[hash] != student:
            hash = (hash + j * j) % self.size
            j += 1
        if self.table[hash] == None:
            self.table[hash] = student

    def Remove(self, student):
        key = student.name
        bytes = str.encode(key)
        number = int.from_bytes(bytes)
        hash = number % self.size
        j = 1
        while self.table[hash] is not None and self.table[hash] != student:
            hash = (hash + j * j) % self.size
            j += 1
        if self.table[hash] is None:
            return False
        else:
            self.table[hash] = None
            return True

def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def counting_sort_linked(aList, k): #Counting Sort
    counter = [0] * ( k + 1 )
    node = aList.first
    if node != None:
        counter[node.value] += 1
        while node.next != None:
            node = node.next
            counter[node.value] += 1
    #for i in aList:
      #counter[i] += 1
    node = aList.first
    for i in range( len( counter ) ):
      for x in range (counter[i]):
        node.value = i
        node = node.next


def counting_sort_array(arrray, k):
    counter = [0] * (k + 1)
    for i in arrray:
        counter[i] += 1
    ndx = 0;
    for i in range(len(counter)):
        while 0 < counter[i]:
            arrray[ndx] = i
            ndx += 1
            counter[i] -= 1


def counting_sort_file(filename):
    file = open(filename)
    k = 0




def selection_sort_linked(aList):  # Selection Sort
    node0 = aList.first
    while (node0 != None):
        node_min = node0
        node1 = node0
        while (node1 != None):
            if (node_min.value > node1.value):
                node_min = node1
            node1 = node1.next
        temp = Node(node0.value)
        node0.value = node_min.value
        node_min.value = temp.value
        node0 = node0.next


def selection_sort_array(array):
    for fillslot in range(len(array) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if array[location] > array[positionOfMax]:
                positionOfMax = location
        temp = array[fillslot]
        array[fillslot] = array[positionOfMax]
        array[positionOfMax] = temp


def populate_list(aList, min, max, n):
        for i in range (n):
            aList.insert(random.randrange(min, max, 1))


def populate_array(array, min, max, n):
    for i in range(n):
        array.append(random.randrange(min, max, 1))


L = LinkedList()
minimum=int(input('Įveskite minimalų skaičių:'))
maximum=int(input('Įveskite maksimalų skaičių:'))
num=int(input('Įveskite elementų skaičių:'))

populate_list(L, minimum, maximum, num)
print("Sorting Linked List with counting sort")
start_time = time.time()
counting_sort_linked(L, maximum)
#print("Sorted Linked List:",L)

print("Time elapsed: ",time.time() - start_time)
Array = []
L.clear()
populate_array(Array, minimum, maximum, num)
#print(Array)
print("Sorting Array with counting sort")
start_time = time.time()
counting_sort_array(Array, maximum)
#print(Array)
print("Time elapsed: ",time.time() - start_time)


populate_list(L, minimum, maximum, num)
print("Sorting Linked List with selection sort")
start_time = time.time()
selection_sort_linked(L)
#print("Sorted Linked List:",L)

print("Time elapsed: ",time.time() - start_time)
Array = []
L.clear()
populate_array(Array, minimum, maximum, num)
#print(Array)
print("Sorting Array with selection sort")
start_time = time.time()
selection_sort_array(Array)
#print(Array)
print("Time elapsed: ",time.time() - start_time)
hashtable = HashTable(5)
hashtable.QuadraticHashInsert(Student("Matas Minelga"))
hashtable.QuadraticHashInsert(Student("Rokas"))
hashtable.QuadraticHashInsert(Student("Paulius"))
hashtable.QuadraticHashInsert(Student("Matas Minelga"))
hashtable.QuadraticHashInsert(Student("Simas"))
print(hashtable)

