#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int segment[65536];
    int index;
} Queue;

void push(Queue *queue, int new_val);
int pop(Queue *queue);
int top(Queue *queue);
int size(Queue *queue);
bool isEmpty(Queue *queue);
int search_from_front(Queue *queue, int val);
int search_from_tail(Queue *queue, int val);
