#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;


int check_cycle(listint_t *list);
#endif