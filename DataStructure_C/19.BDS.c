#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Function to insert a node into the BST
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) return createNode(data);
    if (data < root->data) root->left = insert(root->left, data);
    else if (data > root->data) root->right = insert(root->right, data);
    return root;
}

// In-order Traversal
void inOrder(struct Node* root) {
    if (root) {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

// Pre-order Traversal
void preOrder(struct Node* root) {
    if (root) {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// Post-order Traversal
void postOrder(struct Node* root) {
    if (root) {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}

// Search function
struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->data == key) return root;
    return (key < root->data) ? search(root->left, key) : search(root->right, key);
}

int main() {
    struct Node* root = NULL;
    int elements[] = {6, 9, 5, 2, 8, 15, 24, 14, 7, 8, 5, 2};
    int n = sizeof(elements) / sizeof(elements[0]);

    // Insert elements into the BST
    for (int i = 0; i < n; i++) {
        root = insert(root, elements[i]);
    }

    int choice, key;
    do {
        printf("\n1. In-order  2. Pre-order  3. Post-order  4. Search  5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: inOrder(root); break;
            case 2: preOrder(root); break;
            case 3: postOrder(root); break;
            case 4:
                printf("Enter element to search: ");
                scanf("%d", &key);
                if (search(root, key)) printf("%d found.\n", key);
                else printf("%d not found.\n", key);
                break;
            case 5: printf("Exiting...\n"); break;
            default: printf("Invalid choice\n");
        }
    } while (choice != 5);

    return 0;
}
