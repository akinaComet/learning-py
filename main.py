class Queue:
    __front_pointer = 0
    __rear_pointer = 0
    q = []

    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
    
    def is_full(self):
        return self.__rear_pointer == self.__size
    
    def add(self, item):
        if(self.__rear_pointer == self.__size):
            print("cannot add any more items, queue is full!")
        else:
            self.q.append(item)
            self.__rear_pointer += 1

    def delete(self):
        if(self.__front_pointer == self.__rear_pointer):
            print("cannot delete any items as the queue is empty! :3")
        else:
            self.__front_pointer += 1
    
    def display_queue(self):
        print(self.q)
        pos_q = [' '] * (self.__size + 1)
        
        pos_q[self.__front_pointer] = '^'
        pos_q[self.__rear_pointer] = '^'
        print(pos_q)

        print("front pointer: " + str(self.__front_pointer))
        print("rear pointer: " + str(self.__rear_pointer))
        
q = Queue(2)
print(q.get_size())
q.display_queue()
q.add(5)
q.display_queue()
q.add(10)
q.display_queue()  
q.delete()
q.display_queue()
q.add(7)
    
