import queues
q1 = queues.FlexiQueue()
q1.enque(10)
q1.enque(20)
q1.enque(30)
q1.enque(40)
q1.enque(50)
print(q1.data)
print(q1.first())
q1.deque()
q1.deque()
q1.deque()
q1.deque()
q1.deque()
print(q1.data)
print(q1.length())
print(q1.first())
print(q1.isempty())
print(q1.isfull())