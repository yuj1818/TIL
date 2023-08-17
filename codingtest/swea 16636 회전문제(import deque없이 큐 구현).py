def isEmpty():
    return front == rear

def isFull():
    return (rear + 1) % len(Q) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(Q)
        return Q[front]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Q = [0]
    Q.extend(list(map(int, input().split())))
    front = 0
    rear = N
    for _ in range(M):
        enQueue(deQueue())
    answer = deQueue()
    print(f'#{tc} {answer}')