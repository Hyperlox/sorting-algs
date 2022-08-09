import time

class SortingAlgs:
    def swap(data, index1, index2):
        temp = data[index1]
        data[index1] = data[index2]
        data[index2] = temp
    
    #bubble sort
    def bubbleSort(data):
        position = len(data) - 1
        while position >= 0:
            scan = 0
            while scan <= position -1:
                if data[scan] > data[scan+1]: #compare to
                    SortingAlgs.swap(data, scan, (scan + 1))
                scan+=1
            position-=1
    
    #quick sort
    def quickSort(data):
        SortingAlgs.quickSortMain(data, 0, len(data) - 1)

    def quickSortMain(data, min, max):
        if min < max:
            indexOfPartition = SortingAlgs.partition(data, min, max)
            SortingAlgs.quickSortMain(data, min, indexOfPartition-1)
            SortingAlgs.quickSortMain(data, indexOfPartition + 1, max)
    
    def partition(data, min, max):
        middle = (min+max)//2
        partitionElement = data[middle]
        SortingAlgs.swap(data, middle, min)
        left = min
        right = max
        while left < right:
            while left < right and data[left]<=(partitionElement): #compare to
                left+=1
            while data[right] > partitionElement:
                right -=1
            if left < right:
                SortingAlgs.swap(data, left, right)
        SortingAlgs.swap(data, min, right)
        return right
    
    #merge sort
    def mergeSort(data):
        SortingAlgs.mergeSortMain(data, 0, len(data)-1)

    def mergeSortMain(data, min, max):
        if min < max:
            mid = (min + max) // 2
            SortingAlgs.mergeSortMain(data, min, mid)
            SortingAlgs.mergeSortMain(data, mid + 1, max)
            SortingAlgs.merge(data, min, mid, max)

    def merge(data, first, mid, last):
        temp = [None]*len(data)
        first1 = first
        last1 = mid
        first2 = mid+1
        last2 = last
        index = first1
        while first1 <= last1 and first2 <= last2:
            if data[first1] < data[first2]:
                temp[index] = data[first1]
                first1 +=1
            else:
                temp[index] = data[first2]
                first2+=1
            index+=1
        while first1 <= last1:
            temp[index] = data[first1]
            first1+=1
            index+=1
        while first2 <= last2:
            temp[index] = data[first2]
            first2+=1
            index+=1
        index = first
        while index <= last:
            data[index] = temp[index]
            index+=1

#testing the algorithms out

start = time.time_ns()
array = [72, 27, 62, 32, 63, 100, 6, 27, 12, 51, 88, 48, 35, 31, 3, 98, 94, 10, 9, 31, 49, 44, 84, 93, 4, 78, 30, 92, 53, 17, 12, 31, 92, 68, 2, 66, 99, 3, 15, 5, 41, 17, 29, 73, 16, 23, 54, 51, 18, 16, 93, 54, 68, 97, 78, 51, 8, 46, 13, 39, 97, 100, 79, 2, 13, 62, 29, 85, 88, 46, 23, 14, 78, 82, 58, 74, 75, 77, 19, 100, 49, 40, 31, 87, 48, 24, 88, 27, 11, 2, 87, 84, 52, 51, 52, 3, 38, 24, 0, 0]
SortingAlgs.bubbleSort(array)
end = time.time_ns()
elapsedTime = (end - start) 
print("Bubble sort time: ",elapsedTime)
print(array)

start2 = time.time_ns()
array2 =[72, 27, 62, 32, 63, 100, 6, 27, 12, 51, 88, 48, 35, 31, 3, 98, 94, 10, 9, 31, 49, 44, 84, 93, 4, 78, 30, 92, 53, 17, 12, 31, 92, 68, 2, 66, 99, 3, 15, 5, 41, 17, 29, 73, 16, 23, 54, 51, 18, 16, 93, 54, 68, 97, 78, 51, 8, 46, 13, 39, 97, 100, 79, 2, 13, 62, 29, 85, 88, 46, 23, 14, 78, 82, 58, 74, 75, 77, 19, 100, 49, 40, 31, 87, 48, 24, 88, 27, 11, 2, 87, 84, 52, 51, 52, 3, 38, 24, 0, 0]
SortingAlgs.quickSort(array2)
end2 = time.time_ns()
elapsedTime2 = (end2-start2)
print("Quick sort time: ", elapsedTime2)
print(array2)

start3=time.time_ns()
array3 = [72, 27, 62, 32, 63, 100, 6, 27, 12, 51, 88, 48, 35, 31, 3, 98, 94, 10, 9, 31, 49, 44, 84, 93, 4, 78, 30, 92, 53, 17, 12, 31, 92, 68, 2, 66, 99, 3, 15, 5, 41, 17, 29, 73, 16, 23, 54, 51, 18, 16, 93, 54, 68, 97, 78, 51, 8, 46, 13, 39, 97, 100, 79, 2, 13, 62, 29, 85, 88, 46, 23, 14, 78, 82, 58, 74, 75, 77, 19, 100, 49, 40, 31, 87, 48, 24, 88, 27, 11, 2, 87, 84, 52, 51, 52, 3, 38, 24, 0, 0]
SortingAlgs.mergeSort(array3)
end3 = time.time_ns()
print("Merge sort time: " + str(end3-start3))
print(array3)