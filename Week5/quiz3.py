import random

queue = []

for x in range(0,10):
    queue += [(random.randint(0,100))]

print(f'Queue is {queue}')

while len(queue) != 0:
    curnum = queue.pop(0)
    print(f'Current number is {curnum} and the queue is {queue}')
print('the queue is now empty')