
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

    def print_list(self):
        current = self.head
        while current:
            print(current.text, end=" -> ")
            current = current.next
        print("None")