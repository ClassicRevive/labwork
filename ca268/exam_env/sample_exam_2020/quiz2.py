from stack import Stack

s = Stack()
s.push('o')
s.push('i')
s.push('e')
x = s.pop()
y = s.pop()
z = s.pop()
s.push(z)
s.push(y)
s.push('i')
str = ''
while not s.is_empty():
   str += s.pop()
print(str, end='')
print()