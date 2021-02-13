from collections import defaultdict


class Node:
    def __init__(self, value):
        assert type(value) == int
        self.value = value
        self.next = None

    def setNext(self, node):
        self.next = node

    def hasNext(self):
        return not (self.next is None)

with open('./input.txt') as file:
    order = file.read()


head = Node(int(order[0]))
ptr = head
for i in range(1, len(order)):
    node = Node(int(order[i]))
    ptr.setNext(node)
    ptr = node

NUM_NODES = 1000000
NUM_REPEAT = 10000000

for i in range(10, NUM_NODES + 1):
    node = Node(i)
    ptr.setNext(node)
    ptr = node


ptr = head
nodeMap = defaultdict(Node)
while True:
    nodeMap[ptr.value] = ptr
    if ptr.hasNext():
        ptr = ptr.next
    else:
        ptr.next = head
        break

def printList(head):
    ref = head
    for _ in range(NUM_NODES):
        print(ref.value, end='-> ')
        ref = ref.next
    print()

ptr = head
for i in range(NUM_REPEAT):
    currentVal = ptr.value
    destinationVal = currentVal - 1
    nextNodes = []
    ptr2 = ptr
    for j in range(3):
        ptr2 = ptr2.next
        nextNodes.append(ptr2.value)
    # print(nextNodes)
    while True:
        if destinationVal <= 0:
            destinationVal = NUM_NODES
        if destinationVal not in nextNodes:
            break
        else:
            destinationVal -= 1

    node = nodeMap[destinationVal]
    nodeNext = node.next
    node.setNext(ptr.next)
    ptr2Next = ptr2.next
    ptr.setNext(ptr2Next)
    ptr2.setNext(nodeNext)

    # printList(head)
    ptr = ptr.next


nodeWithValOne = nodeMap[1]
result = (nodeWithValOne.next).value * ((nodeWithValOne.next).next).value
print(result)