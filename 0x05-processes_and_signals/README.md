# Understanding Processes and Signals

## Introduction
Processes and signals are fundamental concepts in Unix-like operating systems. Understanding how processes work and how signals can be used to interact with them is crucial for developing robust and efficient software.

## Processes
A process is an instance of a running program. Each process has its own memory space, set of resources, and unique process identifier (PID). When a program is executed, it becomes a process.

### Key Concepts:
- **PID (Process Identifier):** A unique identification number assigned to each process.
- **Parent and Child Processes:** A parent process creates child processes. Child processes inherit certain characteristics from their parent.
- **Process State:** A process can be in one of several states such as running, sleeping, stopped, or terminated.
- **Process Control Block (PCB):** Data structure containing information about a process, including its PID, state, priority, etc.

## Signals
Signals are software interrupts used in Unix-like operating systems to notify processes of various events or to request specific actions. Signals can be sent by the kernel, other processes, or the user.

### Common Signals:
- **SIGINT (Interrupt):** Sent by pressing Ctrl+C. Default action is to terminate the process.
- **SIGTERM (Termination):** Signal to terminate a process. Allows the process to perform cleanup before exiting.
- **SIGKILL (Kill):** Unconditionally terminates a process. Cannot be caught or ignored by the process.
- **SIGHUP (Hangup):** Typically used to reload configuration files or restart daemons.
- **SIGSTOP and SIGCONT:** Used to stop and resume a process, respectively.
- **SIGCHLD (Child Status Changed):** Sent to the parent process when a child process terminates or stops.

### Handling Signals
Processes can handle signals by defining signal handlers. Signal handlers are functions that are executed in response to receiving a signal.

### Example Signal Handling in Bash:
```bash
#!/bin/bash

# Define a signal handler function
handle_signal() {
    echo "Received SIGTERM. Cleaning up and exiting..."
    cleanup_and_exit
}

# Set up trap to catch SIGTERM
trap handle_signal SIGTERM

# Main loop
while true; do
    echo "Running..."
    sleep 1
done

# Function to clean up and exit
cleanup_and_exit() {
    # Cleanup code goes here
    exit 0
}
# Processes and Signals
==========================

## What is a Process?
-----------------------

A process is an instance of a program running on a computer. It has its own memory, CPU registers, and system resources. Processes are used to execute programs, handle tasks, and manage system resources.

## What is a Signal?
--------------------

A signal is a software interrupt sent to a process to notify it of an event or request. Signals can be used to:

* Terminate a process (e.g., `SIGTERM`, `SIGKILL`)
* Interrupt a process (e.g., `SIGINT`, `SIGSTOP`)
* Request a process to perform an action (e.g., `SIGHUP`, `SIGUSR1`)

## Types of Signals
--------------------

### Termination Signals

* `SIGTERM` (15): Request a process to terminate gracefully
* `SIGKILL` (9): Forcefully terminate a process (cannot be ignored)

### Interrupt Signals

* `SIGINT` (2): Interrupt a process (e.g., Ctrl+C)
* `SIGSTOP` (19): Stop a process (e.g., Ctrl+Z)

### Other Signals

* `SIGHUP` (1): Hangup (e.g., terminal closed)
* `SIGUSR1` (10): User-defined signal 1
* `SIGUSR2` (12): User-defined signal 2

## Sending Signals
-----------------

Signals can be sent using the `kill` command, `pkill` command, or the `signal` function in programming languages.

### Example: Sending a Signal
