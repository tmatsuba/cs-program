from datastructure.stack import Stack
from datastructure.queue import Queue
from datastructure.array_structure import toarray, tolist


def test_list():

    lis = tolist(1, 3, 2, 4, 7, 6, 8, 5)

    assert lis[0] == 1
    assert lis[1] == 3
    assert lis[2] == 2
    assert lis[3] == 4
    assert lis[4] == 7
    assert lis[5] == 6
    assert lis[6] == 8
    assert lis[7] == 5

def test_array():
    lis = [1, 3, 2, 4, 7, 6, 8, 5]
    arr = toarray(lis)

    assert arr[0] == 1
    assert arr[1] == 3
    assert arr[2] == 2
    assert arr[3] == 4
    assert arr[4] == 7
    assert arr[5] == 6
    assert arr[6] == 8
    assert arr[7] == 5

def test_stack():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() is None

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

def test_queue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1
    assert queue.dequeue() is None

    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1

    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
