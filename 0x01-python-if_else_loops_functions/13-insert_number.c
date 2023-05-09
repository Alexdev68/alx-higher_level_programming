#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;
	int i;
	int pos;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	i = 0;
	if (number > 1024)
	{
		while (current != NULL)
		{
			current = current->next
			i++;
		}
		new_node->next = current->next;
		current->next = new_node;

	}

	pos = 0;
	if (number > 4 && number < 98)
	{
		pos += 4;
	}
	if (number < 0)
	{
		pos += 0;
	}
	while (i < pos)
	{
		current = current->next;
		i++;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
