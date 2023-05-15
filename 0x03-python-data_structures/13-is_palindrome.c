#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i, j, len = 0;
	char s_str[20];

	for (i = 0; current != NULL; current = current->next, i++)
	{
		len++;
	}
	if (len == 1 || len == 0)
	{
		return (1);
	}

	i = 0;
	for (current = *head; current != NULL; current = current->next, i++)
	{
		s_str[i] = current->n;
	}

	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (s_str[i] != s_str[j])
		{
			return (0);
		}
	}
	return (1);
}
