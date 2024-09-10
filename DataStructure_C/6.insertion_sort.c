// write a program to implement insertion sort

#include <stdio.h>

// Function to sort an array using insertion sort
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Function to print an array of size n
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int n;

    // Ask the user for the number of elements
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];

    // Ask the user to enter the elements
    printf("Enter the elements:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Perform insertion sort
    insertionSort(arr, n);

    // Print the sorted array
    printf("Sorted array: \n");
    printArray(arr, n);

    return 0;
}

// OUTPUT
// Enter the number of elements: 5
// Enter the elements:
// 12
// 11
// 13
// 5
// 6
// Sorted array: 
// 5 6 11 12 13 
