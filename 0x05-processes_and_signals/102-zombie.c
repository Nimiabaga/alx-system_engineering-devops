#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <time.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always returns 0
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
 * main - Entry point of the program, creates 5 zombie processes
 *
 * Return: Always returns 0
 */
int main(void)
{
	int process_count;
	pid_t zombie_pid;

	for (process_count = 0; process_count < 5; process_count++)
	{
		zombie_pid = fork();

		if (!zombie_pid)
			return (0);

		printf("Zombie process created, PID: %d\n", zombie_pid);
	}

	infinite_while();
	return (0);
}
