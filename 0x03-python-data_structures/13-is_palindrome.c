#include "lists.h"
#include <stdlib.h>

listint_t* reverseLinkedList();
listint_t* createNode();
listint_t* cloneLinkedList();
listint_t* reverseLinkedList();

int is_palindrome(listint_t** head)
{
        int is_palindrome = 1;
        listint_t* new_list;
        listint_t* current;
        listint_t* new_current;

        new_list = cloneLinkedList(*head);
        new_list = reverseLinkedList(new_list);
        current = *head;
        new_current = new_list;

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
        listint_t* clonedHead;
        listint_t* current;
        listint_t* clonedCurrent;

        if (head == NULL)
        {
                return NULL;
        }

        clonedHead = createNode(head->n);
        current = head->next;
        clonedCurrent = clonedHead;

        while (current != NULL)
        {
                listint_t* newNode = createNode(current->n);
                clonedCurrent->next = newNode;
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
