#include "lists.h"

/**
 * check_cycle - checks for a loop in a list
 * @list: input linked list
 * Return: returns 1 if loop exists, 0 if no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;
	while (tortoise && hare && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
