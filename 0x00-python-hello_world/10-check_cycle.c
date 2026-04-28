#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to the head of list
 * Return: 1 if cycle exists, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	/* Handle empy list or single node */
	if (list == NULL || list->next==NULL)
	{
		return (0);
	}

	slow = list; /* moves 1 step at a time */
	fast = list->next; /* moves 2 steps at a time */

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast) /* if they meet, then it's a cycle */
		{
			return (1);
		}

		slow = slow->next; /* 1 step */
		fast = fast->next->next; /* 2 steps */
	}

	return (0); /* fast reached NULL, then no cycle */
}
