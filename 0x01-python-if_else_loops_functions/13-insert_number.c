#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;
	int i;

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
		new_node = (add_nodeint_end(&current, number));
		return (new_node);
	}
	else if (number < 0)
	{
		new_node->next = *head;
		*head = new_node;
	}
	if (i > 4 && i <= 98)
	{
		while (i < 4)
		{
			current = current->next;
			i++;
		}

		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
