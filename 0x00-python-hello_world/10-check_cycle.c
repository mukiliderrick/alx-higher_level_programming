#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Check if a sigly -linked list contains an cycle.
 * @list: Asingly-linked list.
 *
 * Return: if there is no cycle - 0.
 * if ther s a cycle -1.
 *
 */
int check_cycle(listsint_t*list)
{
	listsint_t *turtle, *hare;

	if (list == NULL || list->nect == NULL)
		return (0);

	turtle = lists->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}
