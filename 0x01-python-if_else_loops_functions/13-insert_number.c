#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cn;
	listint_t *new_node;
	int i;

	cn = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	i = 0;
	if (number < 0 || *head == NULL)
	{
		new_node->n = number;
		if (*head == NULL)
			new_node->next = NULL;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	if (number > 1024)
	{
		new_node = (add_nodeint_end(&cn, number));
		return (new_node);
	}
	while (cn->next != NULL)
	{
		if (number < cn->n)
		{
			i--;
			break;
		}
		cn = cn->next;
		i++;
	}

	new_node->next = cn->next;
	cn->next = new_node;


	return (new_node);
}
