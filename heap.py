## heap
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __str__(self, *args, **kwargs):
        return str(self.heap)

    def heapify_up(self, index):
        parent_index  = index #2
        while parent_index > 0 :
            if parent_index % 2  == 1:
                parent_index = parent_index // 2
            
            else:
                parent_index = (parent_index // 2) -1
                
            if self.heap[index] > self.heap[parent_index]:
                tmp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[index]
                self.heap[index] = tmp
                index = parent_index
        
    
    def insert_element(self, element):
        self.heap.append(element)
        print(self.heap)
        self.size += 1
        self.heapify_up(self.size - 1)


if __name__ == "__main__":
    arr = [32, 10 ,2, 13]
    heap = Heap()
    for i in arr:
        heap.insert_element(i)
    


