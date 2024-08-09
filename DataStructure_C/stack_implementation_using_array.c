#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

struct stack {
    int info;

    
};


struct stack s[SIZE];
int top = -1;


void push(int);
void pop();
void disp();

int main() {
    int ch, item;

    // Main loop
    while (1) {
        printf("1-push\n");
        printf("2-pop\n");
        printf("3-display\n");
        printf("4-exit\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1:
                printf("Enter a number: ");
                scanf("%d", &item);
                push(item);
                break;
                
            case 2:
           	pop();
           	break;
            case 3:
		disp();
		break;
	    case 4:
	    	printf("Exiting...");
	    	break;
        }
    }
    return 0; // Return from main
}

void push(int x) {
    if (top >= SIZE - 1) {
        printf("Stack is full and can cause overflow\n");
    } else {
        top++;
        s[top].info = x;
    }
}

void pop() {
    if (top == -1) {
        printf("Stack is empty and can cause underflow\n");
    } else {
        printf("The deleted item is %d\n", s[top].info);
        top--;
    }
}

void disp() {
    if (top == -1) {
        printf("Stack is empty\n");
    } else {
        for (int i = top; i >= 0; i--) {
            printf("%d ", s[i].info);
        }
    }
}

