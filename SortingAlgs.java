import java.util.*;
import java.lang.*;
import java.io.*;

public class SortingAlgs
{
    private static void swap(int[] data, int index1, int index2)
    {
        int temp = data[index1];
        data[index1] = data[index2];
        data[index2] = temp;
    }

    //bubble sort
    public static void bubbleSort(int[] data)
    {
        int position, scan;
        for (position = data.length - 1; position >= 0; position--)
        {
            for (scan = 0; scan <= position - 1; scan++)
            {
                if (data[scan] > data[scan+1])
                    swap(data, scan, scan + 1);
            }
        }
    }  

    //quick sort
    public static void quickSort(int[] data)
    {
        quickSort(data, 0, data.length - 1);
    }
    
    private static void quickSort(int[] data, int min, int max)
    {
        if (min < max)
        {
            int indexOfPartition = partition(data, min, max); //creates partitions 
            quickSort(data, min, indexOfPartition-1); //sort the left partition 
            quickSort(data, indexOfPartition + 1, max); //sort the right partition 
        }
    }
    
    private static int partition(int[] data, int min, int max)
    {
        int partitionElement;
        int left, right;
        int middle = (min + max)/2;
        partitionElement = data[middle]; //middle data value is partition
        swap(data, middle, min); //moves partition out of the way
        left = min;
        right = max;
        while (left < right)
        {
            //searches for an element that is greater than partition 
            while (left < right && data[left] <= partitionElement)
                left++;
            //searches for an element that is less than partition
            while (data[right] > partitionElement)
                right--;
            //swaps the elements
            if (left < right)
                swap(data, left, right);
        }
        swap(data, min, right); //moves the partition element back to place
        return right;
    }  

    //merge sort 
//     public static void mergeSort(int[] data)
//     {
//         mergeSort(data, 0, data.length-1);
//     }
    
//     private static void mergeSort(int[] data, int min, int max)
//     {
//         if (min < max) //stops the recursion when there is only one value in the array
//         {
//             int mid = (min + max) / 2;
//             //splits the array into two 
//             mergeSort(data, min, mid);
//             mergeSort(data, mid + 1, max);
//             merge(data, min, mid, max);
//         }
//     }

//     private static void merge(int[] data, int first, int mid, int last)
//     {
//         int[] temp = new int[data.length]; //creates a temporary array to put items in
//         int first1 = first, last1 = mid; //endpoints of first subarray
//         int first2 = mid+1, last2 = last; //endpoints of second subarray
//         int index = first1; //index while putting values in the temporary array
//         //Copies smaller item of the two arrays into the temporary array until one of the subarrays is used up
//         while (first1 <= last1 && first2 <= last2)
//         {
//             if (data[first1] < data[first2])
//             {
//                 temp[index] = data[first1];
//                 first1++;
//             }
//             else
//             {
//                 temp[index] = data[first2];
//                 first2++;
//             }
//             index++;
//         }
//         //copies remaining elements from first subarray, if any
//         while (first1 <= last1)
//         {
//             temp[index] = data[first1];
//             first1++;
//             index++;
//         }
//         while (first2 <= last2)
//         {
//             temp[index] = data[first2];
//             first2++;
//             index++;
//         }
//         //copies merged data into original array
//         for (index = first; index <= last; index++)
//             data[index] = temp[index];
//     }
    
    private static void merge(int a[], int beg, int mid, int end)    
    {    
        int i, j, k;  
        int n1 = mid - beg + 1;    
        int n2 = end - mid;    

       /* temporary Arrays */  
            int LeftArray[] = new int[n1];  
            int RightArray[] = new int[n2];  

        /* copy data to temp arrays */  
        for (i = 0; i < n1; i++)    
        LeftArray[i] = a[beg + i];    
        for (j = 0; j < n2; j++)    
        RightArray[j] = a[mid + 1 + j];    

        i = 0; /* initial index of first sub-array */  
        j = 0; /* initial index of second sub-array */   
        k = beg;  /* initial index of merged sub-array */  

        while (i < n1 && j < n2)    
        {    
            if(LeftArray[i] <= RightArray[j])    
            {    
                a[k] = LeftArray[i];    
                i++;    
            }    
            else    
            {    
                a[k] = RightArray[j];    
                j++;    
            }    
            k++;    
        }    
        while (i<n1)    
        {    
            a[k] = LeftArray[i];    
            i++;    
            k++;    
        }    

        while (j<n2)    
        {    
            a[k] = RightArray[j];    
            j++;    
            k++;    
        }    
    }    
    
    private static void mergeSort(int a[], int beg, int end)  
    {  
        if (beg < end)   
        {  
            int mid = (beg + end) / 2;  
            mergeSort(a, beg, mid);  
            mergeSort(a, mid + 1, end);  
            merge(a, beg, mid, end);  
        }  
    }
    
    public static void mergeSort(int a[])
    {
        mergeSort(a, 0, a.length - 1);
    }

    //for driver method
    public static int[] randArray(int length){
        Random rand = new Random();
        int[] arr = new int[length];
        for (int x = 0; x < length; x++){
            arr[x]=rand.nextInt(length+1);
        }
        return arr;
    }

    public static long mean(ArrayList<Long> arr){
        long sum = 0;
        for (int i=0; i < arr.size(); i++){
            sum += arr.get(i);
        }
        return (sum/arr.size());
    }

    //driver method
    public static void main(String args[])
    {
        ArrayList<Long> bubbleResult = new ArrayList<Long>();
        ArrayList<Long> quickResult = new ArrayList<Long>();
        ArrayList<Long> mergeResult = new ArrayList<Long>();
        int numTrials = 100;
        int arrayLength = 1000000;

        for (int trial = 0; trial < numTrials; trial++){
            int[] arr = randArray(arrayLength);
            long start = System.nanoTime();
            int[] newArraylist = arr.clone();
            SortingAlgs.bubbleSort(newArraylist);
            long end = System.nanoTime();
            bubbleResult.add(end-start);

            long start2 = System.nanoTime();
            int[] newArraylist2 = arr.clone();
            quickSort(newArraylist2);
            long end2 = System.nanoTime();
            quickResult.add(end2-start2);

            long start3 = System.nanoTime();
            int[] newArraylist3 = arr.clone();
            mergeSort(newArraylist3);
            long end3 = System.nanoTime();
            mergeResult.add(end3-start3);
            
        }

        long result = mean(bubbleResult);
        System.out.println("Elapsed time for bubble sort: " + result);
        long result1 = mean(quickResult);
        System.out.println("Elapsed time for quick sort: " + result1);
        long result2 = mean(mergeResult);
        System.out.println("Elapsed time for merge sort: " + result2);
    }
}
