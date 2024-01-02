#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;
    if (list == NULL)
        return (0);
    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next; /* 1 hop */
        fast = fast->next->next; /* 2 hops */
        if (slow == fast) /* fast caught up to slow, so there is a loop */
            return (1);
    }
    return (0);
}

