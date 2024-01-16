#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	while (*head && (*head)->n < number)
		head = &(*head)->next;

	new->next = *head;
	*head = new;

	return (new);
}
