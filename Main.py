import random
import time
import sys
import os
import fileinput
import struct
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


def file_size(filename):
    st = os.stat(filename)
    return st.st_size


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
    ndx = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            arrray[ndx] = i
            ndx += 1
            counter[i] -= 1


def counting_sort_file(filename):
    file = open(filename)
    k = 0


def populate_binary_file_array(filename, min, max, size):
    file = open(filename, 'wb', 0)
    for i in range(size):
        rndint = random.randint(min,max)
        my_bytes = rndint.to_bytes(4, sys.byteorder)
        my_bytearray = bytearray(my_bytes)
        file.write(my_bytes)
        print(rndint)
    file.close()


def populate_binary_file_list(filename, min, max, size):
    file = open(filename, 'wb', 0)
    for i in range(size):
        rndint = random.randint(min, max)
        my_bytes = rndint.to_bytes(4, sys.byteorder)
        file.write(my_bytes)
        if (i != size-1):
            next_node = (i+1).to_bytes(4, sys.byteorder)
            file.write(next_node)
            my_bytearray = bytearray(my_bytes + next_node) ### NEED REDOING! my_bytearray remove!
        else:
            next_node = (2147483647).to_bytes(4, sys.byteorder)
            file.write(next_node)
        #file.write(my_bytearray)
        print(rndint)
    file.close()


def swap_in_file_array(filename, a_ind, b_ind, linked_list=False):
    with open(filename, "r+b", 0) as file:
        data = file.read()
        tuples = [data[i:i+4] for i in range(0, len(data), 4)]
        a = []
        b = []
        step = 1
        if linked_list:
            step = 2
        for i in range(0, (len(tuples)), step):
            if i == a_ind:
                a = tuples[i]
                # print(struct.unpack("i", tupples[i])[0])
            if i == b_ind:
                b = tuples[i]
        tuples[b_ind] = a
        tuples[a_ind] = b
        data = b''.join(tuples)
        file.seek(0)
        file.write(data)
        file.close()
        return True



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

def selection_sort_linked_file(filename):  # Selection Sort
    node0 = 0
    while (node0 < 2147483647):
        node_min = node0
        node1 = node0
        while (node1 < 2147483647):
            file = open(filename, "rb", 0)
            data = file.read()
            file.close()
            tuples = [data[i:i + 4] for i in range(0, len(data), 4)]
            if struct.unpack("i", tuples[node_min*2])[0] > struct.unpack("i", tuples[node1*2])[0]:
                node_min = node1
            node1 = struct.unpack("i", tuples[node1*2+1])[0]
        swap_in_file_array(filename, node0*2, node_min*2)
        node0 = struct.unpack("i", tuples[node0 * 2 + 1])[0]


def selection_sort_array(array):
    for fillslot in range(len(array) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if array[location] > array[positionOfMax]:
                positionOfMax = location
        temp = array[fillslot]
        array[fillslot] = array[positionOfMax]
        array[positionOfMax] = temp

def selection_sort_array_file(filename):
    length = file_size(filename)/4
    length = int(length)
    for fillslot in range(length-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            file = open(filename, "rb", 0)
            data = file.read()
            file.close()
            tuples = [data[i:i + 4] for i in range(0, len(data), 4)]
            if struct.unpack("i", tuples[location])[0] > struct.unpack("i", tuples[positionOfMax])[0]:
                positionOfMax = location
        swap_in_file_array(filename,fillslot,positionOfMax)



def populate_list(aList, min, max, n):
        for i in range (n):
            aList.insert(random.randrange(min, max, 1))


def populate_array(array, min, max, n):
    for i in range(n):
        array.append(random.randrange(min, max, 1))


def do_in_memory(sizes):
    for size in sizes:
        L = LinkedList()
        populate_list(L, 0, 10000, size)
        print("Sorting Linked List with counting sort, size: ", '{:>10}'.format(size))
        start_time = time.time()
        counting_sort_linked(L, 10000)
        #print("Sorted Linked List:",L)
        print("Time elapsed: ",time.time() - start_time)
        L.clear()
    for size in sizes:
        Array = []
        populate_array(Array, 0, 10000, size)
        #print(Array)
        print("Sorting Array with counting sort, size: ", '{:>10}'.format(size))
        start_time = time.time()
        counting_sort_array(Array, 10000)
        #print(Array)
        print("Time elapsed: ",time.time() - start_time)

    for size in sizes:
        populate_list(L, 0, 10000, size)
        print("Sorting Linked List with selection sort, size: ", '{:>10}'.format(size))
        start_time = time.time()
        selection_sort_linked(L)
        #print("Sorted Linked List:",L)

        print("Time elapsed: ",time.time() - start_time)
        L.clear()

    for size in sizes:
        Array = []
        populate_array(Array, 0, 10000, size)
        print("Sorting Array with selection sort, size: ", '{:>10}'.format(size))
        start_time = time.time()
        selection_sort_array(Array)
        print("Time elapsed: ",time.time() - start_time)
    hashtable = HashTable(5)
    hashtable.QuadraticHashInsert(Student("Matas Minelga"))
    hashtable.QuadraticHashInsert(Student("Rokas"))
    hashtable.QuadraticHashInsert(Student("Paulius"))
    hashtable.QuadraticHashInsert(Student("Matas Minelga"))
    hashtable.QuadraticHashInsert(Student("Simas"))
    print(hashtable)

sizes = [10, 100, 200, 400, 800, 1600, 10000]
sizes = [5]
#do_in_memory(sizes)
#populate_binary_file_array("arr_data", 0, 1024, 5)
#swap_in_file_array("arr_data", 1, 2)
#selection_sort_array_file("arr_data")
populate_binary_file_list("list_data", 0, 1024, 5)
selection_sort_linked_file("list_data")

#populate_binary_file_list("list_data", 0, 1024, 5)
# do_in_memory(sizes)
"""L = LinkedList()
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
print(hashtable)"""
