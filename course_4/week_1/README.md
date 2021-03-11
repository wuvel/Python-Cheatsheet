Table of Contents
-----------------

  * Introduction to Debugging
    * Practice Quiz: Introduction to Debugging <br>
        * `01_introduction_to_debugging.ipynb`
  * Understanding the Problem
    * Practice Quiz: Understanding the Problem <br>
        * `02_understanding_the_problem.ipynb` 
  * Binary Searching a Problem
    * Practice Quiz: Binary Searching a Problem <br>
        * `03_binary_searching_a_problem.ipynb`
  * Module Review
    * Qwiklabs Assessment: Debugging Python Scripts

# Recap
## What is debugging?
- Troubleshooting is the process of identifying, analyzing, and solving problems.
- Debugging is the process of identifying, analyzing, and removing bugs in a system.
- We say troubleshooting when we're fixing problems in the system running the application, and debugging when we're fixing the bugs in the actual code of the application.
- Debuggers let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more.

## Problem Solving Steps
- The first step is getting information. This means gathering as much information as we need about the current state of things, what the issue is, when it happens, and what the consequences are, for example. To get this information, we can use any existing documentation that might help. One super important resource to solve a problem is the reproduction case, which is a clear description of how and when the problem appears.
- The second step is finding the root cause of the problem. But the key here is to get to the bottom of what's going on, what triggered the problem, and how we can change that.
- The final step is performing the necessary remediation. Depending on the problem, this might include an immediate remediation to get the system back to health, and then a medium or long-term remediation to avoid the problem in the future. 
- Throughout the whole process, it's important that we document what we do. We should note down the info that we get, the different things we tested to try, and figure out the root cause.

## Silently Crashing Application
- `strace` lets us look more deeply at what the program is doing. It will trace a system calls made by the program and tell us what the result of each of these calls was.
- Using `strace`:

    ```bash
    $ strace python3 file.py

    # Output into file
    $ strace -o result.strace python3 file.py
    ```
- System calls are the calls that the programs running on our computer make to the running kernel.

## "It Doesn't Work"
- Some common questions that we can ask a user that simply report something doesn't work are:
    - What were you trying to do? 
    - What steps did you follow? 
    - What was the expected result? 
    - What was the actual result? 

## Creating a Reproduction Case
- A reproduction case is a way to verify if the problem is present or not. We want to make the reproduction case as simple as possible. That way, we can clearly understand when it happens, and it makes it really easy to check if the problem is fixed or not, when we try to solve it.
- For example, where the program fail to start because of a missing directory, the reproduction case was to open the program without that directory on the computer.
- The first step is to read the logs available to you. Which logs to read, will depend on the operating system and the application that you're trying to debug.
- On Linux, you'd read system logs like /var/log/syslog and user-specific logs like the.xsession-errors file located in the user's home directory. On MacOs, on top of the system logs, you'd go through the logs stored in the library logs directory. On Windows, you'd use the Event Viewer tool to go through the event logs. 

## Finding the Root Cause
- Understanding the root cause is essential for performing the long-term remediation.
- Whenever possible, we should check our hypothesis in a test environment, instead of the production environment that our users are working with. That way, we avoid interfering with what our users are doing and we can tinker around without fear of breaking something important.
- We could use `iotop`, which is a tool similar to top that lets us see which processes are using the most input and output. Other related tools are `iostat` and `vmstat`, these tools show statistics on the input/output operations and the virtual memory operations. If the issue is that the process generates too much input or output, we could use a command like `ionice` to make our backup system reduce its priority to access the disk and let the web services use it too.
- We can check this using `iftop`, yet another tool similar to `top` that shows the current traffic on the network interfaces.
- The `rsync` command, which is often used for backing up data, includes a `-bwlimit`, just for this purpose. If that option isn't available, we can use a program like `Trickle` to limit the bandwidth being used.

## Dealing with Intermittent Issues
- The first step is to get more involved in what's going on, so that you understand when the issue happens and when it doesn't. If you're dealing with a bug and a piece of code that you maintain, you can usually modify the program to log more information related to the problem. Since you don't know exactly when the bug will trigger, you need to be thorough with the information that you log.
- Sometimes, the bug goes away when we add extra logging information, or when we follow the code step by step using a debugger. This is an especially annoying type of intermittent issue, nicknamed Heisenbug, in honor of Werner Heisenberg. He's the scientist that first described the observer effect, where just observing a phenomenon alters the phenomenon.

## What is binary search?
- Using linear search, going through a list with 1000 elements might take up to 1,000 comparisons if the element we're looking for is the last one in the list or isn't present at all. Using binary search for the same list of 1,000 elements, the worst-case is only 10 comparisons. This is calculated as the base two logarithm of the lists length, and the benefits get more and more significant the longer the list.
- But remember, that for Binary Search to work, the list needs to be sorted.
- Linear search in Python:

    ```python
    def linear_search(list, key):
        """If key is in the list returns its position in the list,
        otherwise returns -1."""
        for i, item in enumerate(list):
            if item == key:
                return i
        return -1
    ```
- Binary search in Python:

    ```python
    def binary_search(list, key):
        """Returns the position of key in the list if found, -1 otherwise.

        List must be sorted.
        """
        left = 0
        right = len(list) - 1
        while left <= right:
            middle = (left + right) // 2
            
            if list[middle] == key:
                return middle
            if list[middle] > key:
                right = middle - 1
            if list[middle] < key:
                left = middle + 1
        return -1
    ```
## Applying Binary Search in Troubleshooting
- We can quickly find out the reason for a problem in a list of possible reasons by splitting the problem in half and testing each half separately.With each iteration, the problem is cut in half. This approach is sometimes called bisecting which means dividing in two.
- When using Git for version control, we can use a Git command called bisect. Bisect receives two points in time in the Git history and repeatedly lets us try the code at the middle point between them until we find the commit that caused the breakage.

## Finding Invalid Data
- We can use the `wc` command that counts characters, words, and lines in a file. In particular, `wc -l` will print the amount of lines in a file.
- Using `head -number` and `tail -number` to bisect our data.