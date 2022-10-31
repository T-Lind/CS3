from DoubleLinkedList import DoubleLinkedList
from time import time

my_list = DoubleLinkedList()

for i in range(1000000):
    my_list.push(i)


start_t = time()
my_list.get(0)
print(time()-start_t)

start_t = time()
my_list.get_front(0)
print(time()-start_t)

my_list.remove(10)

print(len(my_list))


