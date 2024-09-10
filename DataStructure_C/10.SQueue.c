// Write a menu driven C program to create a queue using array and preform Enqueue, Dequeue and Display operation.
#include <stdio.h>
#include <stdlib.h>

#define MAX 50

int queue[MAX];
int front = -1, rear = -1;

void enqueue();
void dequeue();
void display();

int main() {
    int ch;
    printf("1. ENQUEUE \n");
    printf("2. DEQUEUE \n");
    printf("3. DISPLAY \n");
    printf("4. EXIT \n");

    while (1) {
        printf("\nEnter your choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1: 
                enqueue();
                break;
            case 2: 
                dequeue();
                break;
            case 3: 
                display();
                break;
            case 4: 
                exit(0);
            default: 
                printf("Invalid option\n");
        }
    }
    return 0;
}

void enqueue() {
    int item;
    if (rear == MAX - 1) {
        printf("\nQueue is Full\n");
    } else {
        if (front == -1) {
            front = 0;
        }
        printf("Insert element into queue: ");
        scanf("%d", &item);
        rear = rear + 1;
        queue[rear] = item;
    }
}

void dequeue() {
    if (front == -1 || front > rear) {
        printf("\nQueue is Empty\n");
    } else {
        printf("\nDeleted: %d\n", queue[front]);
        front = front + 1;
        // Reset front and rear if queue becomes empty after dequeue
        if (front > rear) {
            front = rear = -1;
        }
    }
}

void display() {
    int i;
    if (front == -1 || front > rear) {
        printf("\nQueue is Empty\n");
    } else {
        printf("\nQueue Elements are:\n");
        for (i = front; i <= rear; i++) {
            printf(" %d ", queue[i]);
        }
        printf("\n");
    }
}

// #include <stdio.h>
#include <stdlib.h>

#define MAX 50

int queue[MAX];
int front = -1, rear = -1;

void enqueue();
void dequeue();
void display();

int main() {
    int ch;
    printf("1. ENQUEUE \n");
    printf("2. DEQUEUE \n");
    printf("3. DISPLAY \n");
    printf("4. EXIT \n");

    while (1) {
        printf("\nEnter your choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1: 
                enqueue();
                break;
            case 2: 
                dequeue();
                break;
            case 3: 
                display();
                break;
            case 4: 
                exit(0);
            default: 
                printf("Invalid option\n");
        }
    }
    return 0;
}

void enqueue() {
    int item;
    if (rear == MAX - 1) {
        printf("\nQueue is Full\n");
    } else {
        if (front == -1) {
            front = 0;
        }
        printf("Insert element into queue: ");
        scanf("%d", &item);
        // rear = rear + 1;
        queue[++rear] = item;
    }
}

void dequeue() {
    if (front == -1 || front > rear) {
        printf("\nQueue is Empty\n");
    } else {
        printf("\nDeleted: %d\n", queue[front]);
        front = front + 1;
        // Reset front and rear if queue becomes empty after dequeue
        if (front > rear) {
            front = rear = -1;
        }
    }
}

void display() {
    int i;
    if (front == -1 || front > rear) {
        printf("\nQueue is Empty\n");
    } else {
        printf("\nQueue Elements are:\n");
        for (i = front; i <= rear; i++) {
            printf(" %d ", queue[i]);
        }
        printf("\n");
    }
}

// OUTPUT

// 1. ENQUEUE 
// 2. DEQUEUE 
// 3. DISPLAY 
// 4. EXIT 
// 
// Enter your choice: 1
// Insert element into queue: 12
// 
// Enter your choice: 1
// Insert element into queue: 23
// 
// Enter your choice: 1
// Insert element into queue: 34
// 
// Enter your choice: 3
// 
// Queue Elements are:
//  12  23  34 
// 
// Enter your choice: 2
// 
// Deleted: 12
// 
// Enter your choice: 3
// 
// Queue Elements are:
//  23  34 

