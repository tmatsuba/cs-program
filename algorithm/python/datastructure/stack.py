class Stack:
    u"""stackを表現するクラス
    """

    def __init__(self) -> None:
        self.lis = []

    def pop(self):
        if self.lis:
            return self.lis.pop()
        return None

    def push(self, elem) -> None:
        self.lis.append(elem)



if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
