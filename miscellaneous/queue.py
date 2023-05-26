class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def get_queue(self):
        return self.__queue

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        val = self.__queue[0]
        self.__queue.pop(0)
        return val


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
print(que.get_queue(), sep=' ', end='')
print()

try:
    for i in range(4):
        print(que.get())
except IndexError:
    print("Queue error")
