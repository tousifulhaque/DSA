## heap
from heapq import heapify


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
                parent_index = parent_index // 2 #1
            
            else:
                parent_index = (parent_index // 2) - 1 #0

            if self.heap[index] > self.heap[parent_index]: #13 #10
                tmp = self.heap[parent_index] #0
                self.heap[parent_index] = self.heap[index] #
                self.heap[index] = tmp
                index = parent_index # 1
        
    
    def insert_element(self, element):
        self.heap.append(element)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_down(self):
        index = 0
        
        while index < self.size:
            print(f'From while loop {index}')
            if index * 2 + 1 < self.size:
                # Getting the index of left child and right child
                left_child_index = index * 2 + 1
                right_child_index = index * 2 + 2
                # Indentifying if the left child is greater than the right child
                if right_child_index < self.size:
                    if self.heap[right_child_index] > self.heap[left_child_index]:
                        left_child_index = right_child_index
                # Comparing the parent with the left child
                if self.heap[index] < self.heap[left_child_index]:
                    tmp = self.heap[index]
                    self.heap[index] = self.heap[left_child_index]
                    self.heap[left_child_index] = tmp
                    index = left_child_index
                else:
                    break
            else:
                break

    def heap_from_array(self, arr):
        self.heap = arr
        self.size = len(arr)
        for i in range(((self.size -1) // 2), -1, -1):
            self.heapify(i) #3

    def heapify(self, i):
        #Check if heap
       
        parent_index = i #3
         # [32, 10 ,64, 13, 25, 65]
        while parent_index >= 0 :  #parent_index = 3
            # Check if the child element exists
            left_child_index = (parent_index * 2) + 1 #5
            right_child_index = (parent_index * 2) + 2 #6
            if (right_child_index < self.size) and (self.heap[right_child_index] > self.heap[parent_index]): #65 #64
                parent_index = right_child_index
                

            if (left_child_index < self.size) and (self.heap[left_child_index] > self.heap[parent_index]): 
                parent_index = left_child_index
                
            
            if parent_index != i:
                self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
                i = parent_index
                self.heapify(i)
            else:
                break


    def delete_heap_element(self):
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down()
if __name__ == "__main__":
    arr = [32, 10 ,64, 13, 25, 65, 30]
    heap = Heap()
    heap.heap_from_array(arr)
    print(heap)
