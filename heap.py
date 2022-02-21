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

    def heapify(self,array):
    
        #Check if heap
        def swap_elements(child, parent):#5, #2
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = tmp

        self.size = len(array) #7 
        self.heap = array
        parent_index = self.size - 1 #6
         # [32, 10 ,64, 13, 25, 65]
        while parent_index >= 0:  #parent_index = 2
            # Check if the child element exists
            left_child_index = (parent_index * 2) + 1 #5
            right_child_index = (parent_index * 2) + 2 #6

            if right_child_index < self.size:
                if self.heap[right_child_index] > self.heap[left_child_index]: #65 #30
                    left_child_index = right_child_index 
                if self.heap[left_child_index] > self.heap[parent_index]: #65 #64
                    swap_elements(left_child_index, parent_index)
                
            elif left_child_index < self.size:
                if self.heap[left_child_index] > self.heap[parent_index]: 
                    swap_elements(left_child_index, parent_index)

            else:
                pass

            parent_index -= 1 #1




    def delete_heap_element(self):
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down()
if __name__ == "__main__":
    arr = [32, 10 ,64, 13, 25, 65, 30]
    heap = Heap()
    heap.heapify(arr)
    print(heap)
    
