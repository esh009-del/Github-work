

def createqueue(size):
    queue=[None] *5 
    front = -1
    rear = -1
    return queue , front , rear 
def enqueue(queue , front , rear , item , size):
    if rear== size - 1:
        print("queue is full cannot enqueue")
        return queue , front , rear 
    if front==-1:
        front=0
    rear +=1
    queue[rear]= item
    print("item has been added to queue")
    return queue , front , rear
def dequeue(queue , front , rear ):
    if front== -1:
        print("QUEUE is empty ")
        return queue , front , rear , None
    item = queue[front]
    front +=1 
    print("Removed from queue")
    return queue , front , rear , item 
    
size=5
queue , front , rear = createqueue(size)
queue , front, rear = enqueue(queue , front , rear , "Eshaan" , size)
print(queue , front , rear )+
queue , front , rear = enqueue(queue , front ,  rear , "Callum" , size)
print( queue , front , rear )
queue , front , rear , item = dequeue( queue , front , rear )
print( queue , front , rear , item )
print("shush")