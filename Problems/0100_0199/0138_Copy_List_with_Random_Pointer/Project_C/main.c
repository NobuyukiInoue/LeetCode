#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>


#include "lib/mylib.h"
#include "lib/node.h"
#include "lib/operate_node.h"

/* Function prototype declaration */
struct Node* copyRandomList(struct Node* head);

int loop_main(char *arg);

struct Node* copyRandomList(struct Node* head) {
    // 10ms - 21ms
    if (head == NULL) {
        return NULL;
    }

    struct Node *cur = head;
    struct Node *next, *temp, *copy;
    while (cur != NULL) {
        next = cur->next;
        temp = malloc(sizeof(struct Node));
        temp->val = cur->val;
        temp->random = NULL;
        temp->next = NULL;
        cur->next = temp;
        cur->next->next = next;
        cur = next;
    }

    cur = head;
    while (cur != NULL) {
        if (cur->random != NULL) {
            cur->next->random = cur->random->next;
        }
        cur = cur->next->next;
    }

    cur = head;
    struct Node* copyHead = head->next;
    while (cur != NULL) {
        next = cur->next->next;
        copy = cur->next;
        cur->next = next;
        if (next != NULL) {
            copy->next = next->next;
        }
        cur = next;
    }
    return copyHead;
}

int loop_main(char *arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    int flds_length = ml_contains_count(arg, "],[") + 1;
    char** flds = malloc(sizeof(char *)*flds_length);
    ml_split(arg, "],[", flds, flds_length);

    struct Node *head;
    if (strcmp(arg, "[]") == 0 || strlen(arg) == 0) {
        head = NULL;
    } else {
        head = createNode(flds, flds_length);
    }
    print_nodes("head = ", head);

    clock_t time_start = clock();

    struct Node* result = copyRandomList(head);

    clock_t time_end = clock();

    print_nodes("result = ", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    node_free(head);

    // char* flds[] free().
    ml_p_char_array_free(flds, flds_length);
    return 0;
}

int main(int argc, char *argv[])
{
#define fgets_MAX   65536
    FILE *fp;
    char line[fgets_MAX];

    if (argc < 2) {
        printf("Usage %s <testdatafile>\n", argv[0]);
        return -1;
    }

    // File Open
    fp = fopen(argv[1], "r");

    if (fp == NULL) {
        printf("%s Open Failed...\n", argv[1]);
        return -1;
    }

    while ((fgets(line, fgets_MAX - 1, fp)) != NULL) {
        ml_trim(line);
        if (*line == '\0')
            continue;
        printf("args = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
