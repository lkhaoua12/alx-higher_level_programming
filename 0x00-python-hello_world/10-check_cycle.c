#include "lists.h"

#define MAX_SIZE 100000

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	int list_index[MAX_SIZE];

	while (current != NULL)
	{
		if (list_index[(long unsigned)current % MAX_SIZE])
			return (1);
		else
			list_index[(long unsigned)current % MAX_SIZE] = 1;
		current = current->next;
	}
	return (0);
}
