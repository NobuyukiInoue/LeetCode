#include "../include/stack.h"

/**
    Implement Queue by 64k segments.
 */

void push(Queue *queue, int new_val) {
    queue->index++;
    queue->segment[queue->index] = new_val;
}

int pop(Queue *queue) {
    if (queue->index >= 0) {
        queue->index--;
        return queue->segment[queue->index + 1];
    } else {
        return 0;
    }
}

int top(Queue *queue) {
    if (queue->index >= 0) {
        return queue->segment[queue->index];
    } else {
        return 0;
    }
}

int size(Queue *queue) {
    return queue->index + 1;
}

bool isEmpty(Queue *queue) {
    if (queue->index == 0) {
        return true;
    } else {
        return false;
    }
}

int search_from_front(Queue *queue, int val) {
    for (int i = 0; i <= queue->index; i++) {
        if (queue->segment[i] == val) {
            return i;
        }
    }
    return -1;
}

int search_from_tail(Queue *queue, int val) {
    for (int i = queue->index; i >= 0; i--) {
        if (queue->segment[i] == val) {
            return i;
        }
    }
    return -1;
}
