

class Sorting:

    def bubbleSort(self, elements):
        length= len(elements)
        for sub in range(1,length):
            for i in range(length-sub):
                if elements[i]>elements[i+1]:
                    temp = elements[i]
                    elements[i]=elements[i + 1]
                    elements[i + 1]=temp
            
        return elements
    

    def modifiedBubbleSort(self, elements):
        length= len(elements)
        for sub in range(1,length):
            flag=0
            for i in range(length-sub):
                if elements[i]>elements[i+1]:
                    flag=1
                    temp = elements[i]
                    elements[i]=elements[i + 1]
                    elements[i + 1]=temp
            if not flag:
                break

        return elements
    

    def selctionSort(self, elements):
        length=len(elements)

        for i in range(length):
            min=i
            for j in range(i+1,length):
                if elements[j] < elements[min]:
                    min=j
            
            if min != i:
                elements[i],elements[min] = elements[min],elements[i]

        return elements
    


    def insertionSort(self, elements):
        length=len(elements)

        for i in range(1, length):
            key = elements[i]
            j = i - 1
            while j >= 0 and elements[j] > key:
                elements[j + 1] = elements[j]
                j = j - 1
            elements[j + 1] = key
        
        return elements




    def quickSort(self, elements):
        self.quick(elements, 0, len(elements)-1)

    def quick(self, elements, left, right):
        if left >= right:
            return
        
        # Find the correct position of loc 
        loc=left
        l=left
        r=right
        while left<right:
            while elements[loc] < elements[right]:
                right-=1
            else:
                elements[loc],elements[right]=elements[right], elements[loc]
                loc = right
            
            while elements[loc] > elements[left]:
                left+=1
            else:
                elements[loc], elements[left]= elements[left], elements[loc]
                loc = left

        # Again apply the method for left sub-list and right sub-list 
        self.quick(elements, l, loc-1)
        self.quick(elements, loc+1, r)

    
    # Presize Quicksort for python coding
    def presizeQuickSort(self, elements):
        if len(elements) <=1 :
            return elements
        else:
            pivot = elements[0]
            less = [i for i in elements[1:] if i <= pivot]
            greater = [i for i in elements[1:] if i > pivot]
            return self.presizeQuickSort(less) + [pivot] + self.presizeQuickSort(greater)
        

    def MergeSort(self, elements):
        if len(elements) <= 1:
            return elements
        else:
            left_sub_list=self.MergeSort(elements[:len(elements)//2])
            right_sub_list=self.MergeSort(elements[len(elements)//2:])
            sortedList=self.merge(left_sub_list, right_sub_list)
            return sortedList
            
    def merge(self, elements1, elements2):
        i=0
        j=0
        sorted_elements=[]
        while i<len(elements1) and j<len(elements2):
            if elements1[i] < elements2[j]:
                sorted_elements.append(elements1[i])
                i+=1
            else:
                sorted_elements.append(elements2[j])
                j+=1
            
        sorted_elements.extend(elements1[i:])
        sorted_elements.extend(elements2[j:])    
        return sorted_elements
    
    # Merge Sort. Some different
    def merge_sort(self, list1):
        if len(list1)>1:
            mid=len(list1)//2
            leftList=list1[:mid]
            rightList=list1[mid:]
            
            self.merge_sort(leftList)
            self.merge_sort(rightList)

            i=j=k=0
            while i<len(leftList) and j<len(rightList):
                if leftList[i]<rightList[j]:
                    list1[k]=leftList[i]
                    i+=1
                else:
                    list1[k]=rightList[j]
                    j+=1
                k+=1
                
            while i<len(leftList):
                list1[k]=leftList[i]
                i+=1
                k+=1
                
            while j<len(rightList):
                list1[k]=rightList[j]
                j+=1
                k+=1
                
        return list1
    
    
        
            
        
        

if __name__ == "__main__":
    obj= Sorting()
    elements=[24, 58, 11, 67, 92, 43]
    print("Bubble Sort: ",obj.bubbleSort(elements))

    elements=[24, 58, 11, 67, 92, 43]
    print("Modified Bubble Sort: ",obj.modifiedBubbleSort(elements))

    elements=[38, 90, 47, 69, 52, 88, 71, 18, 20]
    print('Selection Sort: ', obj.selctionSort(elements))

    elements=[50, 20, 37, 91, 64, 18, 43, 59, 72, 81]
    print('Insertion Sort: ', obj.insertionSort(elements))

    elements=[27, 15, 39, 21, 28, 70]
    obj.quickSort(elements)
    print("Quick Sort: ",elements)

    elements=[58, 62, 91, 43, 29, 37, 88, 72, 16, 30,34, 66] 
    print("Presize Quick Sort: ",obj.presizeQuickSort(elements))

    
    elements=[70, 29, 83, 42, 16, 90, 56, 34, 20, 71, 88]
    print("Merge Sort: ",obj.MergeSort(elements))

    elements=[70, 29, 83, 42, 16, 90, 56, 34, 20, 71, 88, 92, 7]
    print("Merge Sort (some different): ", obj.merge_sort(elements))