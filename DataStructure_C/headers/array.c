#include<stdio.h>
#include "array.h"

void printarr(int arr[], int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\b\n");
}

void inputarr(int arr[], int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("ENTER THE %d th element : ", i + 1);
        scanf("%d", &arr[i]);
    }
}

int linear_search(int arr[], int element, int length)
{

    for (int i = 0; i < length; i++)
    {
        if (arr[i] == element)
        {
            return ++i;
        }
    }

    return -1;
}

