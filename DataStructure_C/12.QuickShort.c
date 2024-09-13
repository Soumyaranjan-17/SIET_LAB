// WAP to implement quick short algorithm

#include <stdio.h>

// Function to swap elements at index a and b
void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// Function to find the partition position
int partition(int array[], int low, int high) {
    // Select the rightmost element as pivot
    int pivot = array[high];
    // Pointer for the greater element
    int i = (low - 1);

    // Traverse each element of the array
    // Compare them with the pivot
    for (int j = low; j < high; j++) {
        if (array[j] <= pivot) {
            // If an element smaller than the pivot is found
            // Swap it with the element pointed by i
            i++;
            swap(&array[i], &array[j]);
        }
    }

    // Swap the pivot element with the element at i + 1
    swap(&array[i + 1], &array[high]);

    // Return the partition point
    return (i + 1);
}

// Function to perform quicksort on the array
void quickSort(int array[], int low, int high) {
    if (low < high) {
        // Find the pivot element such that
        // elements smaller than pivot are on the left of pivot
        // elements greater than pivot are on the right of pivot
        int pi = partition(array, low, high);

        // Recursively call quicksort on the left and right subarrays
        quickSort(array, low, pi - 1);
        quickSort(array, pi + 1, high);
    }
}

// Function to print array elements
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// Main function to test the quicksort implementation
int main() {
    int data[] = {8, 7, 2, 1, 0, 9, 6};
    int n = sizeof(data) / sizeof(data[0]);

    printf("Unsorted Array:\n");
    printArray(data, n);

    // Perform quicksort on the data
    quickSort(data, 0, n - 1);

    printf("Sorted Array in Ascending Order:\n");
    printArray(data, n);

    return 0;
}


// OUTPUT

// Unsorted Array:
// 8 7 2 1 0 9 6 
// Sorted Array in Ascending Order:
// 0 1 2 6 7 8 9 
