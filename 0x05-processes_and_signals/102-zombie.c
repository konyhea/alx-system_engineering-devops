#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid == 0)
        {
            // Child process
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
        else if (child_pid > 0)
        {
            // Parent process
            sleep(1); // Give child process time to exit
        }
        else
        {
            perror("fork");
            exit(1);
        }
    }

    infinite_while(); // Keep the parent process running

    return (0);
}
