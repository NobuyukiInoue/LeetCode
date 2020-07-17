#include "../include/stack.h"

/** Initialize your data structure here. */

MyStack* myStackCreate() {
    MyStack *stack = (MyStack *)malloc(sizeof(MyStack));

    if (stack == NULL) {
        return NULL;
    }

    stack->size = 0;

    return stack;
}

/** Push element x onto stack. */
void myStackPush(MyStack* obj, int x) {
    if (obj == NULL) {
        return;
    }

    struct ListNode *new_node = (struct ListNode *)malloc(sizeof(struct ListNode));
    new_node->val = x;
    if (obj->node != NULL) {
        new_node->next = obj->node;
        obj->node = new_node;
    }

    obj->size++;
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack *obj) {
    if (obj == NULL) {
        return 0;
    }

    int item = obj->node->val;
    if (obj->node->next != NULL) {
        struct ListNode *tmp = obj->node;
        obj->node = obj->node->next;
        free(tmp);
    } else {
        free(obj->node);
        obj->node = NULL;
    }

    obj->size--;

    return item;
}

/* Get the top element */
int myStackTop(MyStack *obj) {
    if (obj == NULL) {
        return 0;
    }

    return obj->node->val;
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack *obj) {
    return (obj->size == 0) ? true: false;
}

/* Return val index */
int myStackSearch(MyStack *obj, int val) {
    struct ListNode *workNode = obj->node;

    for (int index = 0; workNode != NULL; index++) {
        if (workNode->val == val) {
            return index;
        }
        workNode = workNode->next;
    }

    return -1;
}

int stackSize(MyStack *obj) {
    return obj->size;
}

int myStackFree(MyStack *obj) {
    if (obj == NULL) {
        return 0;
    }
/*
    if (obj->size > 0) {
        ListNode_free(obj->node);
    }
*/
    free(obj);
    
    return 0;
}

/*
int ListNode_free(struct ListNode* node) {
    if (node == NULL)
        return 0;
    
    int result = 0;

    if (node->next != NULL) {
        result += ListNode_free(node->next);
    }

    free(node);
    result++;

    return result;
}
*/
