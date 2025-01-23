class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_end(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp  is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def print_item(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.item is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    break
                temp=temp.next

    

obj=SLL()

class Stack(SLL):
    def __init__(self, start=None):
        super().__init__(start)
        
    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        super().insert_at_start(data)
        print(f"This element is pushed: {data}")
    
    def pop(self):
        if not self.is_empty():
            print(f"Popped element: {self.start.item}")
            self.delete_at_first()
        else:
            print("Stack is empty!")
    
    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self.start.item}")
        else:
            print("Stack is empty!")

    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.peek()
s1.pop()
