#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct Node - singly linked list node
 * @data: integer data
 * @next: pointer to the next node
 *
 * Description: Defines a node in a singly linked list.
 */
typedef struct Node
{
    int data;
    struct Node *next;
} Node;

/**
 * print_linked_list - Prints the elements of a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: The number of nodes in the list.
 */
size_t print_linked_list(const Node *head);

/**
 * add_node_end - Adds a new node at the end of a linked list.
 * @head: Pointer to the head of the linked list.
 * @data: Integer data for the new node.
 * Return: Pointer to the new node.
 */
Node *add_node_end(Node **head, const int data);

/**
 * free_linked_list - Frees the memory allocated for a linked list.
 * @head: Pointer to the head of the linked list.
 */
void free_linked_list(Node *head);

/**
 * insert_node - Inserts a node into a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Integer data for the new node.
 * Return: Pointer to the new node.
 */
Node *insert_node(Node **head, int number);

#endif /* LISTS_H */
