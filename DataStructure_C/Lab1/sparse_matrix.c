#include<stdio.h>

int main(){
	int sparce_matrix[4][5] = {
        {0,0,2,0,9},
        {1,0,0,0,2},
        {3,0,0,1,0},
        {1,0,0,0,2}
    };

    int size = 0;
    for(int i = 0; i<4; i++){
        for (int j = 0; j < 5; j++)
        {
            if (sparce_matrix[i][j] != 0)
            {
                size++;
            }   
        }
    }

    printf("%d\n", size);

    int matrix[3][size];
    int k = 0;
    for (int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 5; j++){
            if (sparce_matrix[i][j] != 0)
            {
                matrix[0][k] = i;
                matrix[1][k] = j;
                matrix[2][k] = sparce_matrix[i][j];
                k++;
            }
            
        }
    }
    
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
        
    }
    
    return 0;

}
