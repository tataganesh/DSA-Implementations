import pytest
from dsa_implementations.data_structures.circular_queue import CircularQueue


@pytest.fixture
def queue():
    return CircularQueue(capacity=10)


def test_push(queue):
    queue.push(5)
    assert queue.peek() == 5
    queue.push(-1)
    assert queue.peek() == 5


def test_pop(queue):
    queue.push(5)
    queue.push(10)
    queue.push(25)
    assert queue.pop() == 5
    queue.push(-1)
    assert queue.pop() == 10


@pytest.mark.parametrize("capacity", [-1, 0, -1000])
def test_invalid_capacity(capacity):
    with pytest.raises(ValueError, match="Capacity must be greater than 0"):
        CircularQueue(capacity=capacity)


def test_peek(queue):
    queue.push(5)
    queue.push(-15)
    assert queue.peek() == 5
    queue.pop()
    assert queue.peek() == -15


def test_queue_full(queue):
    for i in range(queue.capacity):
        queue.push(i)
    with pytest.raises(IndexError, match="Queue Full: Cannot insert element"):
        queue.push(10)


def test_queue_empty_pop(queue):
    with pytest.raises(IndexError, match="Queue Empty: Cannot pop"):
        queue.pop()


def test_queue_empty_pop_after_operations(queue):
    num_elements = 2
    for i in range(num_elements):
        queue.push(i)
    for i in range(num_elements):
        queue.pop()
    with pytest.raises(IndexError, match="Queue Empty: Cannot pop"):
        queue.pop()


def test_size(queue):
    for i in range(5):
        queue.push(i)
    assert queue.size() == 5
    queue.peek()
    assert queue.size() == 5
    queue.pop()
    queue.pop()
    assert queue.size() == 3


def test_multiple_data_types(queue):
    queue.push(5)
    queue.push("hello")
    queue.push([1, 2, 3])
    assert queue.pop() == 5
    assert queue.pop() == "hello"
    assert queue.pop() == [1, 2, 3]


def test_circular_behaviour(queue):
    # First fill the queue
    for _ in range(queue.capacity):
        queue.push(10)
    # Pop some elements from the queue
    for _ in range(3):
        queue.pop()
    # Push into queue to leverage circularity
    queue.push(5)
    queue.push(15)
    # Check that queue size is 9
    # 10 pushes, 3 pops, 2 pushes
    assert queue.size() == 9
    assert queue.peek() == 10


def test_circular_behaviour_full_cycle(queue):
    # Fill the queue
    for i in range(queue.capacity):
        queue.push(i)

    # Empty the queue
    for i in range(queue.capacity):
        assert queue.pop() == i

    # Refill the queue
    for i in range(queue.capacity):
        queue.push(i + 10)

    assert queue.size() == queue.capacity
    assert queue.peek() == 10


def test_boundary_push_pop(queue):
    # Fill to capacity
    for i in range(queue.capacity):
        queue.push(i)

    assert queue.size() == queue.capacity

    # Remove one item and add one item
    queue.pop()
    queue.push(100)

    assert queue.size() == queue.capacity
    assert queue.peek() == 1
