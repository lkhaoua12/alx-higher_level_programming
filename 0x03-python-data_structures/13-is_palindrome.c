
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
        int is_palindrome = 1;
        listint_t *current = *head;
        listint_t *reversed = reverseLinkedList(*head);

        while (current != NULL)
        {
                if (current->n != reversed->n)
                {
                        is_palindrome = 0;
                        break;
                }
                current = current->next;
                reversed = reversed->next;
        }

        reverseLinkedList(reversed);

        return is_palindrome;
}
