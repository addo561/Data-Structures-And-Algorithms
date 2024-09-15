
class Queue:
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k 
        self.front = self.rear = -1

    def Enqueue(self,data):
        #for simple
        if(self.rear == self.k -1):
            print('full')  
        #for circular
        #if (self.rear + 1)%self.k==self.head:
            #print('circular is full')  

        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            #for circular
            #self.rear = (self.rear + 1)%self.k
            #for simple
            self.rear = self.rear + 1
            self.queue[self.rear] = data

    def dequeue(self):
        if(self.front == -1):
            print('Empty')
        elif(self.front==self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front] 
            #for simple
            self.front = self.front + 1
            #for circular
            #self.front = (self.front+ 1) % self.k
            return temp 
    def print_qu(self):
        if(self.front == -1):
            print('Empty')   
        else:
            for i in range(self.front,self.rear + 1):
                print(self.queue[i] , end=' ')  
            print()  

    '''
    for circular
    
    def printCQueue(self):
        if(self.front[] == -1):
            print("No element in the circular queue")

        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
    '''                   


obj = Queue(4)
obj.Enqueue(4)
obj.Enqueue(3)
obj.Enqueue(5)
obj.Enqueue(5)
obj.print_qu()
print(obj.dequeue())
obj.print_qu()