# Stack, Queue, and Bidirectional Queue
from collections import deque

"""Data structures are fundamental components of programming 
because they organize and store data in computer programs. 
Among them, stacks, queues and two-way queues (deques) 
are particularly important because of their versatility 
and efficiency in solving various algorithmic problems.
"""


# stack

"""
A stack is one of the fundamental data structures in programming, 
which allows you to insert and remove data according to the principle 
"Last In, First Out" (LIFO).

In a structured linear list organized according to the LIFO principle, 
elements can be added and removed only from one end, called the "top of the list". 


There are basic stack operations:

Push - adding an element.
Pop - removing an element.
Peek - viewing the top element.
Is Empty - checking the stack for emptiness."""


# A simple implementation of these stack commands includes the following functions:


# Creating a stack
def create_stack():
    return []


# Check for emptiness
def is_empty(stack):
    return len(stack) == 0


# Adding an element
def push(stack, item):
    stack.append(item)


# Removing an element
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Stack is empty")


# View the top element
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty")

# First, let's create a stack and add a few elements:
stack = create_stack()
push(stack, "a")
push(stack, "b")
push(stack, "c")
print("~" * 30)

"""
The stack now contains the elements ['a', 'b', 'c'], 
where 'c' is at the top of the stack."""

# Let's look at the top element:
print(peek(stack))  # Print 'c'


# Let's remove the top element:
print(pop(stack))  # Print 'c'
print("~" * 30)


"""The stack now contains ['a', 'b']. If we try 
to view or delete the top element again, we get 'b'.

If we keep removing elements until the stack is empty, 
and then try to remove or view the top element again, 
both the pop() and peek() functions will return a "Stack Empty" message.

Stacks in programming are ideal for tasks where you need 
to keep track of elements in reverse order. For example, 
'stacks are used in the management of function calls 
and in various algorithms.
"""


# Queue ''deque''


"""
A queue in programming is an abstract data structure that operates 
on a first-in, first-out basis (FIFO: First In, First Out). 
Elements are added (enqueue) to one end of the structure 
and removed (dequeue) from the other end.

There are basic operations for a queue:

Enqueue - adding an element to the end of the queue.
Dequeue - removing an element from the beginning of the queue.
Front/Peek - view the first element of the queue without deleting it.
Is Empty - checking whether the queue is empty.
Size - definition of the number of elements in the queue.


Queues are widely used in programming to manage the flow 
of data and tasks, especially when the order of elements matters.



In Python, a queue can be implemented using the built-in list type, 
although this is not always the most efficient way due to the high 
cost of Dequeue operations. Lists in Python are implemented in such 
a way that selecting an element by index takes place in constant time 
(very quickly) and adding/removing an element from the end of the list 
is also very fast. But adding an element anywhere else in the list 
causes Python to recalculate the indices of all elements of the list 
to the end. For large lists, this can be very disadvantageous. A more 
efficient option is to use deque from the collections module as a queue.
"""


# Creating a queue
queue = deque()

# Enqueue: Adding elements
queue.append("a")
queue.append("b")
queue.append("c")

print(
    "Queue after adding elements:", list(queue)
)  # Queue after adding elements: ['a', 'b', 'c']


# Dequeue: Dequeue an element
print("Removed item:", queue.popleft())  # Deleted item: a

print(
    "Queue after removing element:", list(queue)
)  # Queue after removing element: ['b', 'c']

# Peek: View the first element
print("First element in queue:", queue[0])  # The first element in the queue: b

# IsEmpty: Check for emptiness
print("Is the queue empty:", len(queue) == 0)  # Whether the queue is empty: False

# Size: Queue size
print("Queue size:", len(queue))  # Queue size: 2
print("~" * 30)

"""In this example, we use deque to create a queue, which allows us 
to efficiently add elements to the end of the queue (Enqueue) 
and remove elements from the beginning (Dequeue). The popleft() 
operation is used for Dequeue because it removes the first element 
from the deque, conforming to the FIFO behavior of a queue."""


# Two-way deque queue


"""
A double-ended queue, or Deque (short for "double-ended queue"), 
is a type of data structure that allows elements to be inserted 
and deleted from both ends. This flexibility makes 
Deque particularly useful in many programming scenarios.

Unlike a normal queue, where elements can be added and removed 
from only one end, Deque allows operations to be performed on both ends. 
Therefore, the deque from the collections module is implemented in such 
a way that the operations of adding and removing elements a
re very efficient, even for large data sets.

Basic deque methods:

append(x) - adds element x to the end of the queue.
appendleft(x) - adds element x to the beginning of the queue.
pop() - removes and returns an element from the right end of the queue. 
If the queue is empty, throws an IndexError exception.
popleft() - removes and returns an element from the left end of the queue. 
If the queue is empty, throws an IndexError exception.
"""

# Create an empty two-way queue
d = deque()

# Add elements to the queue
d.append("middle")  # Add 'middle' to the end of the queue
d.append("last")  # Add 'last' to the end of the queue
d.appendleft("first")  # Add 'first' to the beginning of the queue

# Display the current state of the queue
print(
    "Queue after adding elements:", list(d)
)  # Queue after adding elements: ['first', 'middle', 'last']

# Delete and output the last element (from the right end)
print("Removed last element:", d.pop())  # Last element removed: last

# Delete and output the first element (from the left end)
print("First element removed:", d.popleft())  # First element removed: first

# Output the current state of the queue after removing elements
print(
    "Queue after removing elements:", list(d)
)  # Queue after removing elements: ['middle']
print("~" * 30)

"""Another feature of the deque is the ability to limit the size of the Deque:
"""

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)  # deque([5, 6, 7, 8, 9], maxlen=5)
print("~" * 30)

"""
As can be seen from the example, the new elements displace 
the older ones, but the size remains unchanged. 
Otherwise, a deque behaves exactly like a Python list.

Two-way queues combine the capabilities of stacks and queues, 
allowing elements to be added and removed from both ends. 
This makes them extremely flexible for different scenarios. 
Deques are often used where fast access to elements from both ends 
of a structure is required, such as in algorithms that require
 handling buffers or palindromes, and in tasks with different priorities.

Let's say we have a list of tasks for the day, where each task 
is described as a dictionary with two attributes: the task type 
(fast or slow) and its name. Our task is to distribute these tasks 
in such a way that the fast tasks are executed first. 
To do this, we will use a two-way queue, which allows us 
to add elements to both the beginning and the end of the queue.
"""


tasks = [
    {"type": "fast", "name": "Wash dishes"},
    {"type": "slow", "name": "Watch the series"},
    {"type": "fast", "name": "Walk the dog"},
    {"type": "slow", "name": "Read a book"},
]

"""
Tasks defined as "fast" must be executed first, 
so they have a higher priority. Instead, "slow" tasks 
can wait and we add them to the end of the queue, executing after all fast tasks.

The purpose of this problem is to demonstrate how a 
two-way queue can be used to control the priority of tasks.
"""
# Initialize the task queue
task_queue = deque()

# Allocation of tasks to the queue according to their priority
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Add to high priority
        print(f"Quick task added: {task['name']}")
    else:
        task_queue.append(task)  # Add to low priority
        print(f"Added slow task: {task['name']}")

# Execution of tasks
while task_queue:
    task = task_queue.popleft()
    print(f"Executing task: {task['name']}")
print("~" * 30)


"""Lets consider how this problem is solved. 
Therefore, an empty two-way queue is created for storing tasks.

Then we perform task distribution by priority.

We go through each task on the list.
If the task type is "fast", we add it to the beginning of the queue, giving it a high priority.
If the task type is "slow", we add it to the end of the queue, giving it a lower priority.

Quick tasks are prioritized because they are added to the front of 
the queue and run first. Slow tasks are added to the end of 
the queue and wait until all fast tasks are completed. 
What the withdrawal process demonstrates:
"""


# Added a quick task: Wash the dishes
# Added a slow task: Watch TV series
# Added a quick task: Walk the dog
# Added a slow task: Read a book
# The task is completed: Walk the dog
# The task is in progress: Wash the dishes
# The task is in progress: Watch the TV series
# The task is in progress: Read a book


"""Of course, all this could be done with the help of ordinary lists. 
Using a deque instead of a regular list to manage tasks provides greater efficiency, 
especially with frequent insertion and deletion operations at both ends of the structure. 
Unlike regular lists, where such operations can be slow, 
especially at the beginning of the list, a deque is optimized 
for fast insertions and deletions, making it ideal for tasks 
where you need to dynamically manage high- and low-priority elements."""

print("dir(deque)")
print(dir(deque))
print("~" * 30)
