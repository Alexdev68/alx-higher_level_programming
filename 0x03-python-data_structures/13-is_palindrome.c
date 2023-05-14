#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i, j, len = 0, count = 0;
	int *s_str;

	for (i = 0; current != NULL; current = current->next, i++)
	{
		len++;
	}
	if (len == 1 || len == 0)
	{
		return (1);
	}

	s_str = malloc(sizeof(int) * len);
	i = 0;
	for (current = *head; current != NULL; current = current->next, i++)
	{
		s_str[i] = current->n;
	}

	count = i;
	i = 0;
	j = count - 1;
	while (i < j)
	{
		if (s_str[i] != s_str[j])
		{
			free(s_str);
			return (0);
		}
		i++;
		j--;
	}
	free(s_str);
	return (1);
}
