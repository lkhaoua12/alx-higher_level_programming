#include "lists.h"
#include <stdlib.h>

listint_t *reverseLinkedList(listint_t *head)
{
        listint_t *previous = NULL;
        listint_t *current = head;

        while (current != NULL)
        {
                listint_t *nextNode = current->next;
                current->next = previous;
                previous = current;
                current = nextNode;
        }

        return previous;
}

int is_palindrome(listint_t **head)
{
        listint_t *slow = *head;
        listint_t *fast = *head;
        listint_t *prev_slow = *head;
        listint_t *second_half = NULL;
        int is_palindrome = 1;
	if (*head == NULL || (*head)->next == NULL)
		return 1;
        if (*head != NULL && (*head)->next != NULL)
        {
                while (fast != NULL && fast->next != NULL)
                {
                        fast = fast->next->next;
                        prev_slow = slow;
                        slow = slow->next;
                }

                if (fast != NULL)
                {
                        slow = slow->next;
                }

                second_half = reverseLinkedList(slow);

                while (second_half != NULL)
                {
                        if ((*head)->n != second_half->n)
                        {
                                is_palindrome = 0;
                                break;
                        }

                        *head = (*head)->next;
                        second_half = second_half->next;
                }

                reverseLinkedList(slow);

                if (fast != NULL) 
                {
                        prev_slow->next = slow;
                        slow->next = second_half;
                }
                else
                {
                        prev_slow->next = second_half;
                }
        }

        return is_palindrome;
}
