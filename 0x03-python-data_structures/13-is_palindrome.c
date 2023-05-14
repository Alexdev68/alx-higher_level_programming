#include "lists.h"

/**
 * is_palindrome - This function checks if a linked list is a palindrome
 * @head: This is a pointer to the head of the linked list
 * Return: This returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	int stack[1024], top = 0;

	while (fast && fast->next)
	{
		stack[top++] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (slow->n != stack[--top])
			return (0);
		slow = slow->next;
	}

	return (1);


}
