#include "lists.h"
/**
 * insert_node - isnert a node in a sorted list.
 * head: pointer to the firt node in the list.
 * number: member of the listint_t struct.
 * Return: a pointer to the head.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(*head)); 
	listint_t *current = *head; 
	listint_t *prev = NULL; 
	
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || current->n < number)
	{
		*head = new_node; 
		return (*head);
	}
	current = *head;
	while (current != NULL)
	{
		prev = current; 
		current = current->next;
		if (number > prev->n && number < current->n)
		{
			prev->next = new_node;
			new_node->next = current;
			return (*head);
		}
	}
	current->next = new_node;
	return (*head);
}
