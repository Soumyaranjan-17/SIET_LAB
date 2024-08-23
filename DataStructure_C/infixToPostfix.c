// Design develop and implement a program in c to convert an expression from infix to postfix using stack

#include <stdio.h>
#include <ctype.h>


void display(){
    printf("Stack: ");
    for (int i = top; i >= 0; i--)
        printf("%c ", stack[i]);
    printf("\n");
}


int precedence(char op)
{
    switch (op)
    {
    case '^':
        return 3;
    case '*':
    case '/':
        return 2;
    case '+':
    case '-':
        return 1;
    default:
        return -1;
    }
}

char stack[20];
int top = -1;

void push(char op)
{
    stack[++top] = op;
}

char pop()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
        return '\0';
    }
    return stack[top--];
}

void main()
{
    char exp[20];
    char *e, x;

    printf("Enter the infix expression: ");
    scanf("%s", exp);

    e = exp;

    printf("The postfix expression is: ");
    while (*e)
    {
        if (isalnum(*e))
        {
            printf("%c", *e);
        }
        else if (*e == '(')
        {
            push(*e);
        }
        else if (*e == ')')
        {
            while ((x = pop()) != '(')
                printf("%c", x);
        }
        else
        {
            while (top != -1 && precedence(stack[top]) >= precedence(*e))
                printf("%c", pop());
            push(*e);
        }
        e++;
    }
    printf("\n");
    while (top != -1)
    {
        printf("%c", pop());
    }
}