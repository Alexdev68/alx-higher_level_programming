#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i = 0, j = 0, len = 0, k;
	int list[1024];
	int *s_str;

	if (*head == NULL)
		return (1);
	current = *head;
	for (i = 0; current != NULL; current = current->next, i++)
		len++;
	s_str = malloc(sizeof(int) * (len + 1));
	i = 0
	for (current = *head; current != NULL; current = current->next, i++)
		s_str[i] = current->n;
	s_str[i] = '\0';

	for (k = len - 1; k >= 0; k--)
	{
		list[j] = s_str[k];
		j++;
	}
	list[j] = '\0';
	i = 0;
	j = 0;
	while (i < len && j < len)
	{
		if (s_str[i] != list[j])
			return (0);
		i++;
		j++;
	}
	free(s_str);
	return (1);
}
