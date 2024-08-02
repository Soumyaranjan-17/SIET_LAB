#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int value;
    int row_position;
    int column_position;
    struct Node *next;
};

void create_new_node(struct Node **start, int non_zero_element, int row_index, int column_index)
{
    struct Node *temp, *r;
    temp = *start;
    if (temp == NULL)
    {
        temp = (struct Node *)malloc(sizeof(struct Node));
        temp->value = non_zero_element;
        temp->row_position = row_index;
        temp->column_position = column_index;
        temp->next = NULL;
        *start = temp;
    }
    else
    {
        while (temp->next != NULL)
            temp = temp->next;
        r = (struct Node *)malloc(sizeof(struct Node));
        r->value = non_zero_element;
        r->row_position = row_index;
        r->column_position = column_index;
        r->next = NULL;
        temp->next = r;
    }
}

void PrintList(struct Node *start)
{
    struct Node *temp = start;
    printf("row_position: ");
    while (temp != NULL)
    {
        printf("%d ", temp->row_position);
        temp = temp->next;
    }
    printf("\n");

    temp = start;
    printf("column_position: ");
    while (temp != NULL)
    {
        printf("%d ", temp->column_position);
        temp = temp->next;
    }
    printf("\n");

    temp = start;
    printf("Value: ");
    while (temp != NULL)
    {
        printf("%d ", temp->value);
        temp = temp->next;
    }
    printf("\n");
}

int main()
{
    int sparseMatrix[4][5] =
        {
            {0, 0, 3, 0, 4},
            {0, 0, 5, 7, 0},
            {0, 0, 0, 0, 0},
            {0, 2, 6, 0, 0}};

    struct Node *start = NULL;

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (sparseMatrix[i][j] != 0)
            {
                create_new_node(&start, sparseMatrix[i][j], i, j);
            }
        }
    }

    PrintList(start);

    return 0;
}
