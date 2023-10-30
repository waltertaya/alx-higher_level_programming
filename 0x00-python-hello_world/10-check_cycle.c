#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    if (list == NULL)
        return (0);

    while (slow != NULL && fast != NULL && fast->next != NULL)
    {
        slow = slow->next; /* slow pointer moves 1 node */
        fast = fast->next->next; /* fast pointer moves 2 nodes */

        if (slow == fast) /* if they meet, there is a loop */
            return (1);
    }
    return (0);
}