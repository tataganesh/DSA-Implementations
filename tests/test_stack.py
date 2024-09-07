import pytest
from dsa_implementations.data_structures.stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_push(stack):
    stack.push(5)
    assert stack.top() == 5
    stack.push(-1)
    assert stack.top() == -1


def test_pop(stack):
    stack.push(5)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 5
    assert stack.isEmpty()


def test_top(stack):
    stack.push(5)
    stack.push(10)
    stack.push(15)
    assert stack.top() == 15
    stack.pop()
    assert stack.top() == 10


def test_isempty(stack):
    stack.push(5)
    stack.push(10)
    stack.pop()
    assert not stack.isEmpty()
    stack.pop()
    assert stack.isEmpty()


def test_pop_emptystack(stack):
    with pytest.raises(IndexError, match="Cannot pop from empty stack"):
        stack.pop()


def test_top_emptystack(stack):
    with pytest.raises(
        IndexError, match="Cannot retrieve top element from empty stack"
    ):
        stack.top()


def test_multiple_data_types(stack):
    stack.push(5)
    stack.push("hello")
    stack.push([1, 2, 3])
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 5


def test_stack_size(stack):
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.push(10)
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1
    stack.top()
    assert stack.size() == 1


@pytest.mark.parametrize(
    "items",
    [
        [1, 2, 3, 4, 5],
        ["abc", "def"],
        [True, False, True, True, True],
        [55, False, (2, 4, 6)],
    ],
)
def test_stack_order(stack, items):
    for item in items:
        stack.push(item)
    for item in reversed(items):
        assert stack.pop() == item
