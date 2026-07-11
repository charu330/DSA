


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy=ListNode()
        self.size=0

        

    def get(self, index: int) -> int:
        current=self.dummy.next
        if index<0 or index>=self.size:
            return -1
        for _ in range(index):
            current=current.next
        return current.val
        

    def addAtHead(self, val: int) -> None:
    
        newnode=self.addAtIndex(0, val)
# 707. Design Linked List
        

    def addAtTail(self, val: int) -> None:
        newnode=self.addAtIndex(self.size, val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index<0:
            index=0
        pd=self.dummy
        for _ in range(index):
            pd=pd.next
        newnode=ListNode(val, pd.next)
        pd.next=newnode
        self.size+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
      
        
        pd = self.dummy
        for _ in range(index):
            pd = pd.next
        node_to_delete = pd.next
        pd.next = node_to_delete.next
        node_to_delete.next = None  
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
