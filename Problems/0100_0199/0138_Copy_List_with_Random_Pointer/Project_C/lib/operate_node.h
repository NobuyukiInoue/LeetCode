struct Node *createNode(char *flds[], int flds_length);
int print_nodes(char* title, struct Node* node);
int** node_to_int_array(struct Node* head);
int findNodeIndex(struct Node** nodes, int nodes_length, struct Node* target);
int count_node_length(struct Node* node);
int node_free(struct Node* t);
