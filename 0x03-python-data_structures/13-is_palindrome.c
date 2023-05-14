#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i = 0, j = 0, len = 0, k;
	int list[1024];
	char *s_str;

	if (current == NULL)
		return (0);
	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	s_str = malloc(sizeof(char) * (len + 1));
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
			break;
		i++;
		j++;
	}
	if (s_str[i] == '\0' && list[j] == '\0')
		return (1);
	free(s_str);
	return (0);
}
