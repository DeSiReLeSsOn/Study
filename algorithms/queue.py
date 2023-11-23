import collections

dq = collections.deque()

dq.append(5)
dq.append(6)
dq.append(7)
print(dq)
p_l = dq.popleft() # извлекает элемент с начала очереди за O(1)
a_l = dq.appendleft(4) # ставит элемент в начало очереди за O(1)