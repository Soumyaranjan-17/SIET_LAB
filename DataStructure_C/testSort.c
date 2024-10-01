#include <stdio.h>

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void main()
{
    int arr[] = {7, 1, 5, 55, 11, 12, 4, 44, 6, 67};
    int l = sizeof(arr) / sizeof(arr[0]);
    // printf("%d", l);

    int r = l;
    for (int i = 0; i < l / 2; i++)
    {
        printf("Running outer loop %d\n", i);

        int *L = &arr[i];
        int *S = &arr[i];

        printf("initial L is = %d\n", *L);
        printf("initial S is = %d\n", *S);

        for (int j = i; j < l - i; j++)
        {
            // printf("%d\n", j);
            // printf("%d\n", *S);
            printf("Step %d : value of L = %d, S = %d\n", j, *L, *S);
            if (arr[j] > *L)
            {
                printf("Array[%d] is grater than %d | setting L to address of arr[%d]\n", arr[j], *L, j);
                L = &arr[j];
                // printf("%d", L);
            }

            if (arr[j] < *S)
            {
                printf("Array[%d] is smaller than %d | setting S to address of arr[%d]\n", arr[j], *S, j);

                S = &arr[j];
            }
            printf("Final L = %d, S = %d\n", *L, *S);
        }
        // swap(&arr[j], S);
        // swap(&arr[l - 1 - i], L);
    }

    for (int i = 0; i < l; i++)
    {
        printf("%d ,", arr[i]);
    }

    // int a = 10;
    // int b = 20;

    // printf("A= %d, B = %d", a, b);

    // swap(&a, &b);
    // printf("A= %d, B = %d", a, b);
}