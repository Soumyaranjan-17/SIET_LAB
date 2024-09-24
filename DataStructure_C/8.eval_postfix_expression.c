#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100

// Define the Stack structure with typedef
typedef struct {
    int top;
    int capacity;
    int* array;
} Stack;

// Function to create a stack of given initial capacity
// Initializes size of stack as 0
Stack* createStack(int initialCapacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    if (!stack) {
        printf("Memory allocation failed\n");
        return NULL;
    }
    stack->capacity = initialCapacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    if (!stack->array) {
        printf("Memory allocation failed\n");
        free(stack);
        return NULL;
    }
    return stack;
}

// Stack is full when top is equal to the last index
int isFull(Stack* stack) {
    return stack->top == stack->capacity - 1;
}

// Stack is empty when top is -1
int isEmpty(Stack* stack) {
    return stack->top == -1;
}

// Function to add an item to stack. It increases top by 1
void push(Stack* stack, int item) {
    if (isFull(stack)) {
        printf("Stack overflow\n");
        return;
    }
    stack->array[++stack->top] = item;
}

// Function to remove an item from stack. It decreases top by 1
int pop(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack underflow\n");
        return -1; // Return a sentinel value indicating an error
    }
    return stack->array[stack->top--];
}

// Function to get the top item of stack without removing it
int peek(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1; // Return a sentinel value indicating an error
    }
    return stack->array[stack->top];
}

// Function to evaluate postfix expression
int evaluatePostfix(const char* exp) {
    Stack* stack = createStack(strlen(exp));
    if (!stack) {
        return -1;
    }

    int i;
    // Scan all characters one by one
    for (i = 0; exp[i]; ++i) {
        // If the scanned character is an operand (number here), push it to the stack
        if (isdigit(exp[i])) {
            push(stack, exp[i] - '0');
        } else {
            // The scanned character is an operator
            int val1 = pop(stack);
            int val2 = pop(stack);

            switch (exp[i]) {
                case '+':
                    push(stack, val2 + val1);
                    break;
                case '-':
                    push(stack, val2 - val1);
                    break;
                case '*':
                    push(stack, val2 * val1);
                    break;
                case '/':
                    if (val1 != 0) {
                        push(stack, val2 / val1);
                    } else {
                        printf("Error: Division by zero.\n");
                        free(stack->array);
                        free(stack);
                        return -1;
                    }
                    break;
                default:
                    printf("Error: Unsupported operator %c\n", exp[i]);
                    free(stack->array);
                    free(stack);
                    return -1;
            }
        }
    }

    int result = pop(stack);

    // Free stack memory
    free(stack->array);
    free(stack);

    return result;
}

int main() {
    char exp[] = "231*+9-";
    printf("Postfix evaluation: %d\n", evaluatePostfix(exp));
    return 0;
}

// OUTPUT

// Postfix evaluation: -4
