class LinkedList:
    def __init__(self):
        self.head = None

    # add to end of list
    def append(self, block):
        # if head is none head = new block
        if self.head is None:
            self.head = block

        else:
            current = self.head

            # iterate over current till next is none
            while current.next:
                current = current.next

            # next = new block
            current.next = block

    # add block to start of list
    def prepend(self, block):
        # if head is none block = head
        if self.head is None:
            self.head = block
        else:
            # next block is head
            # head is block
            block.next = self.head
            self.head = block

    # add at given index
    def add_index(self, index, block):
        if index == 0:
            self.prepend(block)
        else:
            current = self.head
            prev = None
            count = 0

            # iterate over list to index
            while current and count < index:
                prev = current
                current = current.next
                count += 1

            if count == index:
                # next block is current
                # previous is block
                block.next = current
                prev.next = block

    def print_list(self):
        current = self.head
        while current:
            print(current.text, end=" -> ")
            current = current.next
        print("None")
