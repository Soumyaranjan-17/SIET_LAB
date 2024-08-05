#include <stdio.h>
#include "headers/array.c"


void main()
{
    int array[50];
    int len;

    // input array element
    printf("Enter the length of the array : ");
    scanf("%d", &len);
    inputarr(array, len);
    printarr(array, len);

    int key;
    printf("Enter the number to search: ");
    scanf("%d", &key);

    int index = linear_search(array, key, len);
    if (index != -1)
    {
        printf("found the element at index %d.\n", index);
    } else {
        printf("Not Found!   :(\n");
    }
}