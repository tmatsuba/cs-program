class Queue:
    u"""stackを2つ使用して、queueを表現するクラス
    """

    def __init__(self) -> None:

        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element) -> None:
        self.stack1.append(element)

    def dequeue(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2.pop()

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
