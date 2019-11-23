#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we will always have to loop through
        every item in the list in order to count them all."""
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because the length of the list doesn't matter"""
        # Create new node to hold given item
        new_node = Node(item)
        # Append node after tail, if it exists
        if self.tail is not None:
            self.tail.next = new_node
        # Otherwise, set head to node
        else:
            self.head = new_node
        # Reassign tail to new node
        self.tail = new_node
        self.count += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because the length of the list doesn't matter"""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.head is not None:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.count += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(n) If the first item is the one we're looking
        for, it will only have to loop through once.
        Worst case running time: O(n) If the item is the last item in the list,
        we will have to loop throuh every item before we reach the last one."""
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality() function
        if self.head is not None:
            current = self.head
            while current is not None:
                if quality(current.data) is True:
                    return current.data
                else:
                    current = current.next
        else:
            return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(n) This function uses the length of the list 
        to loop through each item to find if it's the correct one to delete. If it's
        the first item, it'll only run once. 
        Worst case running time: O(n) If the item we're looking for is the last item,
        it will take the longest amount of time."""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        previous = None
        current = self.head
        found = False
        if self.is_empty():
            raise ValueError(f'Item not found: {item}')
        
        # If only one node in the list
        elif self.head == self.tail: 
            if current.data == item:
                self.head = None
                self.tail = None
            else:
                raise ValueError(f'Item not found: {item}')
        
        else:
            while current is not None:
                if current.data == item:
                    found = True
                    # If first node is the correct one
                    if previous is None: 
                        self.head = current.next
                    #If last node is the correct one
                    elif current == self.tail: 
                        self.tail = previous
                        previous.next = None
                    else:
                        previous.next = current.next
                previous = current
                current = current.next
            if found is False:
                raise ValueError(f'Item not found: {item}')



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    # print('\nTesting prepend:')
    # for item in ['A', 'B', 'C']:
    #     print('prepend({!r})'.format(item))
    #     ll.prepend(item)
    #     print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        # for item in ['B', 'C', 'A']:
        #     print('delete({!r})'.format(item))
        #     ll.delete(item)
        #     print('list: {}'.format(ll))
        ll.delete('A')
        print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
