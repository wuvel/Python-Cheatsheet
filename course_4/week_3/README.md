Table of Contents
-----------------

  * Why Programs Crash
    * Practice Quiz: Why Programs Crash <br>
        * `01_why_programs_crash.ipynb`
  * Code that Crashes
    * Practice Quiz: Code that Crashes <br>
        * `02_code_that_cashes.ipynb` 
  * Handling Bigger Incidents
    * Practice Quiz: Handling Bigger Incidents <br>
        * `03_handling_bigger_incidents.ipynb`
  * Module Review
    * Qwiklabs Assessment: Fixing Errors in Python Scripts <br>

# Recap
## Systems That Crash
- As a first step, you tried looking at the logs to see if there's any error that may point to what's happening.
- You'll also want to use these S.M.A.R.T tools which can help detect errors and even try to anticipate problems before they affect the computer's performance. 

## Understanding Crashing Applications
- On Mac OS we generally use the console app to look at logs and the event Viewer on Windows.
- If there are no errors or the errors aren't useful we can try to find out more info by enabling sling debug logging.
-  The first thing is to check if the issue is caused by a new version of the application itself. Maybe there's a bug in the new version that causes the crash or maybe the way that we're using the application is no longer supported. It could also be that a library or service used by our application changed and they no longer work well together or it could be that there was a configuration change in the overall environment.
- To find the root cause of a crashing application will want to look at all available logs figure out what changed trace the system or library calls the program makes and create the smallest possible reproduction case.

## What to do when you can't fix the program?
- A Wrapper is a function or program that provides a compatibility layer between two functions or programs so they can work well together. Using Wrappers is a pretty common technique when the expected output and input formats don't match.
- You might want to consider running the application inside a virtual machine or maybe a container.
- Watchdog is a process that checks whether a program is running and when it's not starts the program again.

## Internal Server Error
- Sort files with last modified:

    ```bash
    $ ls -lt
    total 1052
    drwxr-xr-x 5 kali kali   4096 Mar 13 05:52 Desktop
    drwxrwxrwx 1 kali kali   4096 Mar 13 05:52 KaliShared
    drwxr-xr-x 3 kali kali   4096 Mar 12 19:04 Downloads
    ```
- Listing network connection:

    ```bash
    $ sudo netstat -nlp

    # We'll use -n to print numerical addresses instead of resolving host names. L to only check out the sockets that are listening for connection, and P to print the process ID and name to which each socket belongs.
    ```

## Accessing Invalid Memory
- Accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't assigned to it. When this happens, the OS will raise an error like segmentation fault or general protection fault.
- The variables that store memory addresses are called pointers.
- Common programming errors that lead to segmentation faults or segfaults include forgetting to initialize a variable, trying to access a list element outside of the valid range, trying to use a portion of memory after having given it back, and trying to write more data than the requested portion of memory can hold.
- Microsoft compilers can also generate debugging symbols in a separate PDB file.
- One of the trickiest things about this invalid memory business is that we're usually dealing with undefined behavior. This means that the code is doing something that's not valid in the programming language.
- Valgrind is a very powerful tool that can tell us if the code is doing any invalid operations no matter if it crashes are not and Dr. Memory is a similar tool that can be used on both Windows and Linux.

## Unhandled Errors and Exceptions
- The traceback shows the lines of the different functions that were being executed when the problem happened.
- The logging module sets debug messages to show up when the code fails.  
- If your program is crashing with an unhandled error, you want to first do some debugging to figure out what's causing the issue. Once you figured it out, you want to make sure that you fix any programming errors and that you catch any conditions that may trigger an error.

## Debugging a Segmentation Fault
- Core files store all the information related to the crash so that we or someone else can debug what's going on.
- Generate core files:

    ```bash
    $ ulimit -c unlimited
    $ ./example
    Segmentation fault
    ```
- Debug:

    ```bash
    $ gdb -c core example

    # Backtrace the command
    (gdb) backtrace
    (gdb) up
    (gdb) list

    # Print value
    (gdb) print i
    ```

## Debugging a Python Crash
- The Byte Order Mark or BOM which is used in UTF-16 to tell the difference between a file stored using Little-endian and Big-endian. Our file is in UTF-8 so it doesn't need the BOM. But some programs still include it and this is tripping up our script. 
- Debug:

    ```bash
    $ pdb3 update.py products.csv
    # Continue the program
    (pdb) continue

    # Print variable
    (pdb) print(row)
    ```

- Force python to use encoding:

    ```python
    with open(filename, 'r', encoding='utf-8-sig') as products:
        ...
    ```

## Crashes in Complex Systems
- Whenever possible, the best strategy is to roll back the changes that you suspect are causing the issue, even if you aren't 100% sure if this is the actual cause. If your infrastructure allows easy rollbacks, try that before doing any further investigation.
- Looking at the available logs, figuring out what changed since the system was last working, rolling back to a previous state, removing faulty servers from the pool, or deploying new servers on demand.

## Communication and Documentation During Incidents
- When working on a problem, it's always a good idea to document what you're doing in a bug or ticket. If there's no such system at your company, then use a doc, a text file, or Wiki, or whatever you have access to.
- Documenting what you do, lets you keep track of what you've tried and what the results were.
- This communications lead needs to know what's going on and provide timely updates on the current state and how long until the problem's resolved.
- Incident Commander or Incident Controller needs to look at the big picture and decide what's the best use of the available resources.

## Writing Effective Postmortems
- Postmortems are documents that describe details of incidence to help us learn from our mistakes. When writing a postmortem, the goal isn't to blame whoever caused the incident, but to learn from what happened to prevent the same issue from happening again.
- To do this, we usually document what happened, why it happened, how it was diagnosed, how it was fixed, and finally figure out what we can do to avoid the same event happening in the future. 
- Remember to focus that paragraph on what you can do better, not on whatever mistake caused the incident.

