#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, len = 0;
	int *s_str;

	if (head == NULL)
		return (0);
	current = *head;
	for (i = 0; current != NULL; current = current->next, i++)
		len++;
	s_str = malloc(sizeof(int) * (len + 1));

	for (current = *head; current != NULL; current = current->next, i--)
		s_str[i] = current->n;

	for (i = 0; i < len; i++, current = current->next)
	{
		if (s_str[i] != current->n)
			return (0);
	}

	free(s_str);
	return (1);
}
