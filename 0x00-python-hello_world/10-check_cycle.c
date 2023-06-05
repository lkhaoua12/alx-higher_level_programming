#include "lists.h"

#define MAX_SIZE 1024

int check_cycle(listint_t *list)
{
	int i = 0, j = 0;
	listint_t *current = list;
	long unsigned list_index[MAX_SIZE];

	while(current != NULL)
	{
		list_index[i] = (long unsigned)current;
		for (j = 0; j < i; j++)
		{
			if (list_index[j] == (long unsigned)current) 
				return (1);
		}
		current = current->next;
		i++;
	}
	return (0);
}
