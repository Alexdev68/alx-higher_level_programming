#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - This checks if a cycle exists in a linked list
 * @list: This represents the head of the linked list
 * Return: This returns 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *end;

	if (list == NULL)
	{
		return (0);
	}

	head = list;
	end = head->next;

	while(end != NULL && head != NULL && head->next != NULL)
	{
		if (end->next == head)
		{
			return (1);
		}
		end = end->next;
	}
	return (0);
}
