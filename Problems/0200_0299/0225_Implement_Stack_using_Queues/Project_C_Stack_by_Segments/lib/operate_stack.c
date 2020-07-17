#include <time.h>
#include "../include/operate_stack.h"

/**
    Implement Queue by 64k segments.
 */

#define MAX    65535

/* Create a stack */
MyStack* myStackCreate() {
    MyStack *stack = (MyStack *)malloc(sizeof(MyStack));
    stack->index = 0;
    stack->size = MAX;
    stack->queue = (Queue **)malloc(sizeof(Queue *)*MAX);
    stack->queue[0] = (Queue *)malloc(sizeof(Queue));
    stack->queue[0]->index = -1;
    return stack;
}

/* Push element x onto stack */
void myStackPush(MyStack *stack, int element) {
    if (stack == NULL) {
        return;
    }

    if (stack->queue[stack->index]->index < MAX) {
        push(stack->queue[stack->index], element);

    } else {
        if (stack->index + 1 >= stack->size) {
            fprintf(stderr, "stackPush() error.\nSegment count is Max\n");
        }

        stack->index++;
        stack->queue[stack->index] = (Queue *)malloc(sizeof(Queue));
        stack->queue[stack->index]->index = -1;

        push(stack->queue[stack->index], element);
    }
}

/* Removes the element on top of the stack */
int myStackPop(MyStack *stack) {
    if (stack == NULL) {
        return 0;
    }

    if (stack->queue[stack->index]->index < 0) {
        if (stack->index > 0) {
            free(stack->queue[stack->index]);
            stack->index--;
        }
    }

    return pop(stack->queue[stack->index]);
}

/* Get the top element */
int myStackTop(MyStack *stack) {
    if (stack == NULL) {
        return 0;
    }

    return top(stack->queue[stack->index]);
}

/* Return whether the stack is empty */
bool myStackEmpty(MyStack *stack) {
    if (stack == NULL) {
        return true;
    }

    if (stack->index == 0 && stack->queue[stack->index]->index == -1) {
        return true;
    }

    return false;
}

/* Return val index */
int stackSearch_from_front(MyStack *stack, int val) {
    int res;
    for (int i = 0; i <= stack->index; i++) {
        if ((res = search_from_front(stack->queue[i], val)) != -1) {
            return i*65536 + res;
        }
    }
    return -1;
}

/* Return val index */
int stackSearch_from_tail(MyStack *stack, int val) {
    int res;
    for (int i = stack->index; i >= 0; i--) {
        if ((res = search_from_tail(stack->queue[i], val)) != -1) {
            return i*65536 + res;
        }
    }
    return -1;
}

/* Return stack Size */
int myStackSize(MyStack *stack) {
    return (stack->index)*65536 + size(stack->queue[stack->index]);
}

/* Destroy the stack */
void myStackFree(MyStack *stack) {
    if (stack == NULL) {
        return;
    }

    for (int i = stack->index; i >= 0; i--) {
        free(stack->queue[i]);
    }

    free(stack);
}
