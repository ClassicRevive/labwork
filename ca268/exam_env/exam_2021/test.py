from Queue import Queue

q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
x = q.dequeue()
y = q.dequeue()
z = q.dequeue()
q.enqueue(x)
q.enqueue(x)
x = q.dequeue()
str = ''
while not q.is_empty():
   str += q.dequeue()
print(str, end='')