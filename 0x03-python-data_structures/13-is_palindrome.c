#include "lists.h"

/**
 * reverseList - Reverses a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Pointer to the head of the reversed list
 */

listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *first_half, *second_half, *mid_node = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}
	second_half = reverseList(slow);
	first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->data != second_half->data)
		{
			reverseList(second_half);
			return (0);
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverseList(second_half);
	return (1);
}
