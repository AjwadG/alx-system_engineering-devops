#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * infinite_while -  endless sleep
 *
 * Return: allways 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * Return: allways 0
 */

int main(void)
{
	int i;
	pid_t id;

	for (i = 0; i < 5; i++)
	{
		id = fork();
		if (!id)
			return (0);
		printf("Zombie process created, PID: %d\n", id);
	}

	infinite_while();
	return (0);
}
