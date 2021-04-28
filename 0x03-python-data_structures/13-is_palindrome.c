#include "lists.h"

/**
 * is_palindrome - checks a linked list to see if palindrome
 * @head: pointer to the first member of list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *front_check, *back_check;
	int count = 0, countc, i, j, z;

	if (head == NULL)
		return (1);
	front_check = *head;
	back_check = *head;
	while (back_check != NULL)
	{
		back_check = back_check->next;
		count++;
	}
	countc = count;
	back_check = *head;
	count--;
	for (z = 0; z < count; z++)
		back_check = back_check->next;
	count--;
	for (i = 0; i < countc / 2; i++)
	{
		if (front_check->n == back_check->n)
		{
			front_check = front_check->next;
			back_check = *head;
			for (j = 0; j < count; j++)
				back_check = back_check->next;
			count--;
		}
		else
			return (0);
	}
return (1);
}
