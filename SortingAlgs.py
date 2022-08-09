from statistics import mean
import time
from random import seed
from random import randint
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

seed(1)
def randArray(length):
    arr = []
    for _ in range(length):
        arr.append(randint(0, length))
    return arr
#
# testing the algorithms out
# 500: 8903010, 12557462
bubbleResult = []
quickResult = []
mergeResult = []
numTrials = 100
arrayLength = 1000
for trial in range(numTrials):
    arr = randArray(arrayLength)
    start = time.time_ns()
    SortingAlgs.bubbleSort(arr.copy())
    end = time.time_ns()
    bubbleResult.append(end-start)

    start2 = time.time_ns()
    SortingAlgs.quickSort(arr.copy())
    end2 = time.time_ns()
    quickResult.append(end2 - start2)

    start3=time.time_ns()
    SortingAlgs.mergeSort(arr.copy())
    end3 = time.time_ns()
    mergeResult.append(end3-start3)

print("Bubble sort time: ",mean(bubbleResult))
print("Quick sort time: ", mean(quickResult))
print("Merge sort time: ", mean(mergeResult))

# testArray = randArray(500)
# start = time.time_ns()
# # array = [48, 95, 70, 53, 58, 27, 61, 48, 93, 39, 26, 97, 86, 46, 87, 66, 48, 2, 57, 85, 16, 91, 74, 15, 59, 77, 92, 59, 23, 88, 97, 45, 34, 56, 42, 62, 41, 17, 93, 15, 27, 73, 40, 96, 19, 55, 73, 18, 83, 65, 35, 68, 19, 13, 97, 11, 59, 4, 86, 78, 35, 36, 76, 100, 70, 49, 6, 30, 71, 79, 30, 75, 73, 99, 35, 63, 6, 91, 51, 59, 44, 73, 95, 41, 77, 31, 94, 82, 81, 71, 72, 61, 71, 52, 43, 38, 37, 38, 3, 3, 94, 73, 27, 54, 84, 42, 85, 49, 87, 10, 14, 89, 27, 52, 27, 67, 12, 6, 90, 41, 59, 46, 41, 79, 4, 84, 54, 74, 22, 2, 66, 66, 11, 17, 32, 14, 69, 8, 42, 69, 51, 67, 28, 85, 83, 27, 7, 50, 50, 12, 51, 78, 92, 68, 85, 8, 20, 4, 25, 61, 80, 47, 88, 68, 2, 60, 93, 69, 16, 54, 25, 82, 40, 97, 45, 8, 83, 46, 74, 6, 41, 42, 86, 49, 90, 71, 32, 44, 48, 8, 29, 64, 24, 28, 5, 56, 46, 77, 42, 11, 62, 81, 98, 28, 55, 43, 29, 33, 41, 78, 4, 99, 30, 46, 92, 89, 33, 12, 85, 20, 94, 53, 81, 31, 14, 44, 27, 73, 72, 39, 88, 37, 47, 9, 78, 81, 72, 99, 11, 53, 2, 96, 71, 46, 51, 50, 53, 0, 58, 94, 6, 73, 25, 22, 35, 51, 65, 26, 74, 82, 90, 37, 13, 15, 77, 69, 35, 69, 44, 27, 28, 52, 45, 99, 56, 40, 80, 37, 1, 73, 14, 77, 18, 40, 94, 13, 94, 34, 5, 44, 53, 37, 89, 47, 1, 83, 48, 14, 41, 66, 84, 100, 17, 73, 44, 98, 97, 11, 39, 38, 50, 44, 94, 95, 58, 41, 60, 94, 34, 68, 72, 8, 70, 27, 18, 44, 99, 30, 97, 82, 86, 38, 21, 35, 86, 83, 77, 71, 59, 35, 5, 70, 11, 49, 5, 35, 52, 72, 100, 48, 67, 4, 34, 24, 22, 84, 100, 10, 89, 84, 29, 61, 71, 53, 59, 93, 7, 60, 65, 98, 29, 8, 77, 0, 29, 77, 98, 42, 55, 28, 36, 22, 55, 2, 38, 90, 39, 77, 36, 16, 99, 1, 70, 98, 58, 52, 42, 41, 7, 13, 2, 71, 59, 1, 57, 97, 39, 4, 78, 1, 81, 68, 19, 59, 86, 80, 36, 86, 77, 45, 42, 97, 91, 91, 1, 38, 90, 38, 64, 24, 26, 60, 80, 40, 92, 67, 83, 15, 80, 31, 83, 28, 1, 93, 80, 91, 63, 83, 33, 49, 2, 73, 40, 88, 95, 30, 66, 7, 40, 87, 38, 58, 44, 99, 100, 8, 52, 99, 31, 72, 17, 33, 85, 91, 88, 83, 64, 8, 74, 0, 46, 55, 56, 0, 64, 53, 66, 47, 42, 74, 5, 19, 61, 48, 91, 89, 73, 82, 38, 73]
# SortingAlgs.bubbleSort(testArray.copy())
# end = time.time_ns()
# elapsedTime = (end - start) 
# print("Bubble sort time: ",elapsedTime)

# start2 = time.time_ns()
# # array2 =[48, 95, 70, 53, 58, 27, 61, 48, 93, 39, 26, 97, 86, 46, 87, 66, 48, 2, 57, 85, 16, 91, 74, 15, 59, 77, 92, 59, 23, 88, 97, 45, 34, 56, 42, 62, 41, 17, 93, 15, 27, 73, 40, 96, 19, 55, 73, 18, 83, 65, 35, 68, 19, 13, 97, 11, 59, 4, 86, 78, 35, 36, 76, 100, 70, 49, 6, 30, 71, 79, 30, 75, 73, 99, 35, 63, 6, 91, 51, 59, 44, 73, 95, 41, 77, 31, 94, 82, 81, 71, 72, 61, 71, 52, 43, 38, 37, 38, 3, 3, 94, 73, 27, 54, 84, 42, 85, 49, 87, 10, 14, 89, 27, 52, 27, 67, 12, 6, 90, 41, 59, 46, 41, 79, 4, 84, 54, 74, 22, 2, 66, 66, 11, 17, 32, 14, 69, 8, 42, 69, 51, 67, 28, 85, 83, 27, 7, 50, 50, 12, 51, 78, 92, 68, 85, 8, 20, 4, 25, 61, 80, 47, 88, 68, 2, 60, 93, 69, 16, 54, 25, 82, 40, 97, 45, 8, 83, 46, 74, 6, 41, 42, 86, 49, 90, 71, 32, 44, 48, 8, 29, 64, 24, 28, 5, 56, 46, 77, 42, 11, 62, 81, 98, 28, 55, 43, 29, 33, 41, 78, 4, 99, 30, 46, 92, 89, 33, 12, 85, 20, 94, 53, 81, 31, 14, 44, 27, 73, 72, 39, 88, 37, 47, 9, 78, 81, 72, 99, 11, 53, 2, 96, 71, 46, 51, 50, 53, 0, 58, 94, 6, 73, 25, 22, 35, 51, 65, 26, 74, 82, 90, 37, 13, 15, 77, 69, 35, 69, 44, 27, 28, 52, 45, 99, 56, 40, 80, 37, 1, 73, 14, 77, 18, 40, 94, 13, 94, 34, 5, 44, 53, 37, 89, 47, 1, 83, 48, 14, 41, 66, 84, 100, 17, 73, 44, 98, 97, 11, 39, 38, 50, 44, 94, 95, 58, 41, 60, 94, 34, 68, 72, 8, 70, 27, 18, 44, 99, 30, 97, 82, 86, 38, 21, 35, 86, 83, 77, 71, 59, 35, 5, 70, 11, 49, 5, 35, 52, 72, 100, 48, 67, 4, 34, 24, 22, 84, 100, 10, 89, 84, 29, 61, 71, 53, 59, 93, 7, 60, 65, 98, 29, 8, 77, 0, 29, 77, 98, 42, 55, 28, 36, 22, 55, 2, 38, 90, 39, 77, 36, 16, 99, 1, 70, 98, 58, 52, 42, 41, 7, 13, 2, 71, 59, 1, 57, 97, 39, 4, 78, 1, 81, 68, 19, 59, 86, 80, 36, 86, 77, 45, 42, 97, 91, 91, 1, 38, 90, 38, 64, 24, 26, 60, 80, 40, 92, 67, 83, 15, 80, 31, 83, 28, 1, 93, 80, 91, 63, 83, 33, 49, 2, 73, 40, 88, 95, 30, 66, 7, 40, 87, 38, 58, 44, 99, 100, 8, 52, 99, 31, 72, 17, 33, 85, 91, 88, 83, 64, 8, 74, 0, 46, 55, 56, 0, 64, 53, 66, 47, 42, 74, 5, 19, 61, 48, 91, 89, 73, 82, 38, 73]
# SortingAlgs.quickSort(testArray.copy())
# end2 = time.time_ns()
# elapsedTime2 = (end2-start2)
# print("Quick sort time: ", elapsedTime2)

# start3=time.time_ns()
# # array3 = [48, 95, 70, 53, 58, 27, 61, 48, 93, 39, 26, 97, 86, 46, 87, 66, 48, 2, 57, 85, 16, 91, 74, 15, 59, 77, 92, 59, 23, 88, 97, 45, 34, 56, 42, 62, 41, 17, 93, 15, 27, 73, 40, 96, 19, 55, 73, 18, 83, 65, 35, 68, 19, 13, 97, 11, 59, 4, 86, 78, 35, 36, 76, 100, 70, 49, 6, 30, 71, 79, 30, 75, 73, 99, 35, 63, 6, 91, 51, 59, 44, 73, 95, 41, 77, 31, 94, 82, 81, 71, 72, 61, 71, 52, 43, 38, 37, 38, 3, 3, 94, 73, 27, 54, 84, 42, 85, 49, 87, 10, 14, 89, 27, 52, 27, 67, 12, 6, 90, 41, 59, 46, 41, 79, 4, 84, 54, 74, 22, 2, 66, 66, 11, 17, 32, 14, 69, 8, 42, 69, 51, 67, 28, 85, 83, 27, 7, 50, 50, 12, 51, 78, 92, 68, 85, 8, 20, 4, 25, 61, 80, 47, 88, 68, 2, 60, 93, 69, 16, 54, 25, 82, 40, 97, 45, 8, 83, 46, 74, 6, 41, 42, 86, 49, 90, 71, 32, 44, 48, 8, 29, 64, 24, 28, 5, 56, 46, 77, 42, 11, 62, 81, 98, 28, 55, 43, 29, 33, 41, 78, 4, 99, 30, 46, 92, 89, 33, 12, 85, 20, 94, 53, 81, 31, 14, 44, 27, 73, 72, 39, 88, 37, 47, 9, 78, 81, 72, 99, 11, 53, 2, 96, 71, 46, 51, 50, 53, 0, 58, 94, 6, 73, 25, 22, 35, 51, 65, 26, 74, 82, 90, 37, 13, 15, 77, 69, 35, 69, 44, 27, 28, 52, 45, 99, 56, 40, 80, 37, 1, 73, 14, 77, 18, 40, 94, 13, 94, 34, 5, 44, 53, 37, 89, 47, 1, 83, 48, 14, 41, 66, 84, 100, 17, 73, 44, 98, 97, 11, 39, 38, 50, 44, 94, 95, 58, 41, 60, 94, 34, 68, 72, 8, 70, 27, 18, 44, 99, 30, 97, 82, 86, 38, 21, 35, 86, 83, 77, 71, 59, 35, 5, 70, 11, 49, 5, 35, 52, 72, 100, 48, 67, 4, 34, 24, 22, 84, 100, 10, 89, 84, 29, 61, 71, 53, 59, 93, 7, 60, 65, 98, 29, 8, 77, 0, 29, 77, 98, 42, 55, 28, 36, 22, 55, 2, 38, 90, 39, 77, 36, 16, 99, 1, 70, 98, 58, 52, 42, 41, 7, 13, 2, 71, 59, 1, 57, 97, 39, 4, 78, 1, 81, 68, 19, 59, 86, 80, 36, 86, 77, 45, 42, 97, 91, 91, 1, 38, 90, 38, 64, 24, 26, 60, 80, 40, 92, 67, 83, 15, 80, 31, 83, 28, 1, 93, 80, 91, 63, 83, 33, 49, 2, 73, 40, 88, 95, 30, 66, 7, 40, 87, 38, 58, 44, 99, 100, 8, 52, 99, 31, 72, 17, 33, 85, 91, 88, 83, 64, 8, 74, 0, 46, 55, 56, 0, 64, 53, 66, 47, 42, 74, 5, 19, 61, 48, 91, 89, 73, 82, 38, 73]
# array3 = testArray.copy()
# SortingAlgs.mergeSort(array3)
# end3 = time.time_ns()
# # print(array3)
# print("Merge sort time: " + str(end3-start3))