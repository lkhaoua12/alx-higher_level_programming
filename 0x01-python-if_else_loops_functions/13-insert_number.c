#include "lists.h"
/**
 * insert_node - isnert a node in a sorted list.
 * head: pointer to the firt node in the list.
 * number: member of the listint_t struct.
 * Return: a pointer to the head.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)); 
	listint_t *current = *head; 
	listint_t *prev = NULL; 
	
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || current->n >= number)
	{
		new_node->next = *head;
		*head = new_node; 
		return (*head);
	}
	while (current != NULL)
	{

		if (number <= current->n)
		{
			break;
		}
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	new_node->next = current;
	return (*head);
}
