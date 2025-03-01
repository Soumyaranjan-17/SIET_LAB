#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) // Fixed the loop to increment j
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr, i, j); // Correctly increment i before swapping
        }
    }
    swap(arr, i + 1, high); // Place the pivot in the correct position
    return (i + 1);
}

// Quick Sort function
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pivot
        quickSort(arr, pi + 1, high); // After pivot
    }
}

int main()
{
    int n;
    srand(time(NULL));

    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    
    // Initialize array with random numbers
    for (int i = 0; i < n; i++)
    {
        arr[i] = rand() % 100000; // Random numbers between 0 and 99999
    }

    clock_t start_time = clock();
    quickSort(arr, 0, n - 1);
    clock_t end_time = clock();

    double time_taken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    printf("Time taken to sort the array: %f seconds\n", time_taken);
    
    // Print the first 10 sorted elements (or fewer if n < 10)
    printf("Sorted Array (First 10 elements):\n");
    for (int i = 0; i < (n < 10 ? n : 10); i++) // Avoid printing more than n elements
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
