#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	char *s_str;
	int i = 0, j = 0, len = 0, k;

	if (current == NULL)
		return (1);
	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	s_str = malloc(sizeof(char) * (len + 1));

	for (current = *head; current != NULL; current = current->next, i++)
		s_str[i] = current->n;
	s_str[i] = '\0';

	char r_str[len + 1];

	for (k = len - 1; k >= 0; k--)
	{
		r_str[j] = s_str[k];
		j++;
	}
	r_str[j] = '\0';
	i = 0;
	j = 0;
	while (i < len && j < len)
	{
		if (s_str[i] != r_str[j])
			break;
		i++;
		j++;
	}
	if (s_str[i] == '\0' && r_str[j] == '\0')
		return (1);
	free(s_str);
	return (0);
}
