class LinkedList:

    def __init__(self, elements):
        self.head, self.tail = None, None
        for el in elements:
            self.reverse(el)

    def __str__(self):
        if self.isEmpty():
            return "[]"
        return "[" + str(self.head) + "]"

    def isEmpty(self):
        return self.head is None and self.tail is None

    def reverse(self, element):
        if element is None:
            pass                            #Si no tiene elementos, al arreglo ya esta invertido
        else:
            newNode = Node(element)         #Si tiene algún elemento
            if self.isEmpty():              #
                self.head = newNode         #El elemento pasa a ser la cabeza
                self.tail = newNode         #El elemento pasa a ser tambien la cola
            else:
                current = self.head         #En caso de que ya haya un elemento, el actual pasa a ser la cabeza
                current.setPrev(newNode)
                newNode.setNext(current)
                self.head = newNode


class Node:
    def __init__(self, value, next=None, prev=None):
        self.setValue(value)
        self.setNext(next)
        self.setPrev(prev)

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def __str__(self):
        return '(' + str(self.value) + ') -->' + str(self.next)

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception('Error en actualización del Nodo')

    def setPrev(self, new_prev):
        if isinstance(new_prev, Node) or new_prev is None:
            self.prev = new_prev
        else:
            raise Exception('Error en actualización del Nodo')

    def clear(self):
        self.setNext(None)
        self.setPrev(None)


def main():
    lst = LinkedList([1,2,3,4,5])
    print(lst)


main()