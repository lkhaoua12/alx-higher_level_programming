#include "lists.h"
#include <stdlib.h>

listint_t* reverseLinkedList(listint_t* head);
listint_t* createNode(int data);
listint_t* cloneLinkedList(listint_t* head);
listint_t* reverseLinkedList(listint_t* head);

int is_palindrome(listint_t** head)
{
        int is_palindrome = 1;
        listint_t* new_list = cloneLinkedList(*head);
        new_list = reverseLinkedList(new_list);
        listint_t* current = *head;
        listint_t* new_current = new_list;

        while (current != NULL)
        {
                if (current->n != new_current->n)
                {
                        is_palindrome = 0;
                        break;
                }
                current = current->next;
                new_current = new_current->next;
        }
	free_listint(new_list);
        return is_palindrome;
}

listint_t* createNode(int data)
{
        listint_t* newNode = (listint_t*)malloc(sizeof(listint_t));

        newNode->n = data;
        newNode->next = NULL;
        return newNode;
}

listint_t* cloneLinkedList(listint_t* head)
{
        if (head == NULL)
        {
                return NULL;
        }

        /* Create a new head node */
        listint_t* clonedHead = createNode(head->n);

        /* Keep track of the current nodes in both lists */
        listint_t* current = head->next;
        listint_t* clonedCurrent = clonedHead;

        while (current != NULL)
        {
                /* Create a new node with the same data */
                listint_t* newNode = createNode(current->n);

                /* Set the next pointer of the cloned node */
                clonedCurrent->next = newNode;

                /* Move to the next nodes in both lists */
                current = current->next;
                clonedCurrent = clonedCurrent->next;
        }

        return clonedHead;
}

listint_t* reverseLinkedList(listint_t* head)
{
        listint_t* previous = NULL;
        listint_t* current = head;

        while (current != NULL)
        {
                listint_t* nextNode = current->next;
                current->next = previous;
                previous = current;
                current = nextNode;
        }

        return previous;
}
