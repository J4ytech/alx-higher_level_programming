#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: double pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *current;
    int *arr, size = 0, i, j;
    
    /* Empty list is palindrome */
    if (*head == NULL)
        return (1);
    
    /* Count nodes */
    current = *head;
    while (current != NULL)
    {
        size++;
        current = current->next;
    }
    
    /* Allocate array */
    arr = malloc(sizeof(int) * size);
    if (arr == NULL)
        return (0);
    
    /* Copy values to array */
    current = *head;
    i = 0;
    while (current != NULL)
    {
        arr[i] = current->n;
        current = current->next;
        i++;
    }
    
    /* Check palindrome */
    i = 0;
    j = size - 1;
    while (i < j)
    {
        if (arr[i] != arr[j])
        {
            free(arr);
            return (0);
        }
        i++;
        j--;
    }
    
    free(arr);
    return (1);
}

