#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	temp = *head;
	if (number < temp->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next && number > temp->next->n)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
