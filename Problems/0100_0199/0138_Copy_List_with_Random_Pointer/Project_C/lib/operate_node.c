#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "mylib.h"
#include "node.h"
#include "operate_node.h"

struct Node *createNode(char *flds[], int flds_length)
{
    char *nums[2];
    struct Node **nodes;

    nodes = malloc(sizeof(struct Node*)*flds_length);

    for (int i = 0; i < flds_length; i++) {
        int temp_length = ml_contains_count(flds[i], ",") + 1;
        char** temp = malloc(sizeof(char *)*flds_length);
        ml_split(flds[i], ",", temp, temp_length);
        int val = strtol(temp[0], NULL, 10);

        struct Node* new_node = malloc(sizeof(struct Node));
        new_node->val = val;
        new_node->random = NULL;
        new_node->next = NULL;
        nodes[i] = new_node;
    }

    struct Node* head = nodes[0];
    struct Node* cur = head;
    for (int i = 0; ; i++) {
        int temp_length = ml_contains_count(flds[i], ",") + 1;
        char** temp = malloc(sizeof(char *)*flds_length);
        ml_split(flds[i], ",", temp, temp_length);
        if (strcmp(temp[1], "null") != 0) {
            int random = strtol(temp[1], NULL, 10);
            cur->random = nodes[random];
        }
        if (i == flds_length - 1) {
            break;
        }
        cur->next = nodes[i + 1];
        cur = cur->next;
    }
    return head;
}

int print_nodes(char* title, struct Node* node)
{
    if (node == NULL) {
        printf("%s[]\n", title);
        return 0;
    }

    int node_length = count_node_length(node);
    int **int_node_arr = node_to_int_array(node);
    printf("%s[[%d, %d]", title, int_node_arr[0][0], int_node_arr[0][1]);
    for (int i = 1; i < node_length; i++) {
        printf(", [%d, %d]", int_node_arr[i][0], int_node_arr[i][1]);
    }
    printf("]\n");

    return node_length;
}

int** node_to_int_array(struct Node* head)
{
    int nodes_length = count_node_length(head);
    struct Node** nodes = malloc(sizeof(struct Node *)*nodes_length);
    struct Node* cur = head;
    for (int i = 0; cur != NULL; i++) {
        nodes[i] = cur;
        cur = cur->next;
    }
    int** flds = malloc(sizeof(int **)*nodes_length);
    cur = head;
    for (int i = 0; cur != NULL; i++) {
        flds[i] = malloc(sizeof(int [2]));
        flds[i][0] = cur->val;
        flds[i][1] = findNodeIndex(nodes, nodes_length, cur->random);
        cur = cur->next;
    }
    return flds;
}

int findNodeIndex(struct Node** nodes, int nodes_length, struct Node* target)
{
    if (target == NULL) {
        return -1;
    }
    for (int i = 0; i < nodes_length; i++) {
        if (target == nodes[i]) {
            return i;
        }
    }
    return -1;
}

int count_node_length(struct Node* node)
{
    if (node == NULL) {
        return 0;
    }
    
    int count = 0;
    if (node->next != NULL) {
        count += count_node_length(node->next);
    }
    return ++count;
}

int node_free(struct Node *node) {
    if (node == NULL) {
        return 0;
    }
    
    int count = 0;
    if (node->next != NULL) {
        count += node_free(node->next);
    }

    free(node);
    
    return ++count;
}
