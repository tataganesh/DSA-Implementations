import pytest
from dsa_implementations.data_structures.circular_queue import CircularQueue


@pytest.fixture
def queue():
    return CircularQueue(capacity=10)


def test_basic_push(queue):
    queue.push(5)
    assert queue.peek() == 5
    queue.push(-1)
    assert queue.peek() == 5


def test_basic_pop(queue):
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
