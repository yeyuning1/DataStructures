class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next=None):
        """Instantiates a Node with a default next of None"""
        self.data = data
        self.next = next


head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next
index = 1
probe = head
while index > 0:
    probe = probe.next
    index -= 1
print(probe.data)


def linkeoneway(arry):
    head = None
    for _ in arry:
        head = Node(_, head)

    while head != None:
        print(head.data)
        head = head.next
