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


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.get_queue()) == 0:
            return True
        return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
