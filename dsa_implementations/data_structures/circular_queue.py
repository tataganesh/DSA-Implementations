class CircularQueue:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.array = [None for _ in range(capacity)]
        # rear points to the last inserted element.
        # front points to the first inserted element. Elements
        # are popped using front and they are insertted using rear.
        self.front = self.rear = -1

    def push(self, element):
        next_rear = (self.rear + 1) % self.capacity
        if next_rear == self.front:
            raise IndexError("Queue Full: Cannot insert element")
        self.front = max(self.front, 0)  # To handle empty queue insertion case
        self.rear = next_rear
        self.array[self.rear] = element

    def pop(self):
        if self.front == -1:
            raise IndexError("Queue Empty: Cannot pop")
        popped_element = self.array[self.front]
        # check if the popped element was the last element
        # in the array
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return popped_element

    def peek(self):
        if self.front == -1:
            raise IndexError("Queue Empty: Cannot peek")
        return self.array[self.front]

    def size(self):
        if self.front == -1:
            return 0
        # If rear is ahead of front, queue size
        # is just the dist between their indices
        if self.rear >= self.front:
            return self.rear - self.front + 1
        ## If front is ahead is ahead of rear,
        ## we first calc number of elements from front till end of array
        ## (capacity -front), then add it to number of elements from 0
        ## till rear (rear + 1)
        else:
            return self.capacity - self.front + self.rear + 1

    def print(self):
        print_list = []
        queue_size = self.size()
        if queue_size:
            current = self.front
            count = 0
            while count < queue_size:
                print_list.append(self.array[current])
                current = (current + 1) % self.capacity
                count += 1
        print(print_list)


if __name__ == "__main__":
    q = CircularQueue(capacity=3)
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(10)
    q.print()
    q.pop()
    q.print()
    q.pop()
    q.print()
    q.push(-25)
    q.print()
