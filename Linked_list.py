class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def setValue(self, new_value):
        self.value = new_value
    def getNext(self):
        return self.next
    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception("New Next must be Node")

    def clear(self):
        self.value = None
        self.next = None
    def __str__(self):
        next = self.next
        return "Node("+str(self.value)+") -->" + ("x" if next is None else str(next))
class LinkedList:
    def __init__(self, data = []):
        self.head, self.tail, self.len = None, None, 0
        for e in data:
            self.append(e)
    def __len__(self):
        return self.len
    def append(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            self.setTail(new_node)
        self.len = self.len  + 1
    def search(self, value):
        current = self.head
        while current is not None and current.getValue() != value:
            current = current.getNext()
        return current
    def getHead(self):
        return self.head

    def setHead(self, head):
        self.head = head
        self.prev = None
    def getTail(self):
        return self.tail
    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None
    def update(self, old_value, new_value):
        node_origin = self.search(old_value)
        node_origin.setValue(new_value)
    def slice(self, value, n=1):
        ld = LinkedList()
        node_origin = self.search(value)
        if node_origin is not None:
            current, index = node_origin, 0
            while current is not None and index < n:
                ld.append(current.getValue())
                current = current.getNext()
                index += 1
        return ld
    def isEmpty(self):
        return len(self) == 0
    def merge(self, list_b):
        if self.isEmpty():
            return list_b
        if list_b.isEmpty():
            return self
        self.tail.setNext(list_b.getHead())
        self.setTail(list_b.getTail())

    def delete(self, value):
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1: # Soy el ??nico               #Si es el ??nico valor
                self.head, self.tail = None, None
            else:
                if value_node == self.getHead():            #Si el valor es el mismo que el valor de la cabeza
                    self.head = value_node.getNext()
                else:
                    #Buscar el previo a value_node
                    prev = self.head
                    while prev.getNext() != value_node:
                        prev = prev.getNext()
                    if value_node == self.getTail():       #Si el valor es el mismo que el valor de la cola
                        self.setTail(prev)
                    else:
                        prev.setNext(value_node.getNext())  #Si el valor es cualquier otro valor
            value_node.clear()                              #borra el valor del nodo
            self.len -= 1                                   #cambia la longitud al eliminae el valor
        else:
            raise Exception("Element not found.")        # si el valor del nodo es none

class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self, e):
        self.data.append(e) #Punto de referencia c??mo el inicio
    def dequeue(self): #como punto de referencia el inicio
        element = self.data[0]
        self.data.pop(0)
        return element
    def __str__(self):
        return "Queue("+str(self.data[0])+")"
    def __len__(self):
        return len(self.data)
#Implementaci??n LIFO
class Stack:
    def __init__(self):
        self.data = []
    def push(self, e):
        #self.data.append(e) #Punto de referencia c??mo el final
        self.data.insert(0,e) #Punto de referencia c??mo el inicio
    def pop(self):
        element = self.data[0]
        self.data.pop(0)
        return element
        #self.data.pop(0) Punto de referencia es el inicio
    def __str__(self):
        return "Stack("+str(self.data[0])+")"
    def __len__(self):
        return len(self.data)

def main():
    list = LinkedList([ 1,2,3,4,5,6])
    list.reverse()
    print(list)
main()