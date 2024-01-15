#define LISTS_H
#ifndef LISTS_H

#include <stdlib.h>

/*8
 * struct listint_s - singly linked list
 * @i: integer
 * @nxtn: Marks next node
 *
 */
typedef struct listint_s
{
	int i;
	struct listint_s nxtn;
}
listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int i);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /*LISTS_H */
