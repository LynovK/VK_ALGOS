class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__ (self):
        return f"[{self.data}]->{self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def lenght(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
#############################################################################
#############################################################################
#############################################################################
#Задает линкед лист определенного размера
# if __name__ == '__main__':
#     linked_list = LinkedList()
#     temp = Node(1)
#     linked_list.head = temp
#     for i in range(2,5):
#         temp.next = Node(i)
#         temp = temp.next
#     print(linked_list)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_reversell(object):
    def reverseList(head):
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list

ll1 = ListNode(1)
rv1 = Solution_reversell()
print(rv1.reverseList())



# class Solution(object):
#     def reverseList(head):
#         """            :type head: ListNode
#         :rtype: ListNode
#         """
#         new_list = None
#         current = head
#
#         while current:
#             next_node = current.next
#             current.next = new_list
#             new_list = current
#             current = next_node
#         return new_list
