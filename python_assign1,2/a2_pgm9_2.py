import a2_pgm9 as q
q.enqueAtRear(30)
q.enqueAtRear(40)
q.enqueAtFront(20)
q.enqueAtFront(10)
print(q.s.data)
q.dequeAtFront()
q.dequeAtRear()
q.enqueAtRear(50)
q.enqueAtFront(0)
print(q.s.data)
print(q.length())
print(q.frontElement())
print(q.rearElement())