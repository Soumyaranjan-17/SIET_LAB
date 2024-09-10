#include <stdio.h>
#include <stdlib.h>

#define MAX 10

int stack[MAX];
int top = -1;

void push(int);
int pop();
void display();
int isEmpty();
int isFull();

void main()
{
    int choice, item;

    while (1)
    {
        printf("\n1. Push\n2. Pop\n3. Display\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:

            if (isFull())
            {
                printf("Stack Overflow\n");
                break;
            }

            printf("Enter the item to push: ");
            scanf("%d", &item);
            push(item);
            break;
        case 2:
            if (isEmpty())
            {
                printf("Stack Underflow\n");
                break;
            }
            item = pop();
            if (top != -1)
                printf("Popped item: %d\n", item);
            break;
        case 3:
            if (isEmpty())
            {
                printf("Stack is empty\n");
                break;
            }

            display();
            break;
        case 4:
            exit(0);
        default:
            printf("Invalid choice\n");
        }
    }
}

void push(int item)
{
    if (isFull())
    {
        printf("Stack Overflow\n");
        return;
    }
    else
        stack[++top] = item;
}

int pop()
{
    {
        return stack[top--];
    }
}

void display()
{
    int i;
    if (isEmpty())
    {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack elements are: ");
    for (i = top; i >= 0; i--)
        printf("%d ", stack[i]);
    printf("\n");
}

int isFull()
{
    return top == MAX - 1;
}

int isEmpty()
{
    return top == -1;
}
