Table of Contents
-----------------

  * Understanding Slowness
    * Practice Quiz: Understanding Slowness <br>
        * `01_understanding_slowness.ipynb`
  * Slow Code
    * Practice Quiz: Slow Code <br>
        * `02_slow_code.ipynb` 
  * When Slowness Problems Get Complex
    * Practice Quiz: When Slowness Problems Get Complex <br>
        * `03_when_slowness_problems_get_complex.ipynb`
  * Module Review
    * Qwiklabs Assessment: Performance Tuning in Python Scripts <br>
        * `04_dailysync.ipynb`

# Recap
## Intro to Module 2: Slowness
- There's a bunch of different things we can do if our system is too slow. The most obvious one is closing any applications we don't need at the moment. This works because it helps us free some of the resources in our computer, like CPU time, RAM, or video memory. That way the program that we want to run faster will have access to more of these resources. 
- Closing any other elements that take resources, like browser tabs or open files in a document editor, can also help.

## Why is my computer slow?
-  The general strategy for addressing slowness is to identify the bottleneck of our script, or our system to run slowly. The bottleneck could be the CPU time as we just mentioned. But it could also be time spent reading data from disk waiting for data transmitted over the network, moving data from disk to RAM, or some other resource that's limiting the overall performance.
- On MacOS, the OS ships with a tool called Activity Monitor which lets us see what's using the most CPU, memory, energy, disk, or network. 
- On Windows, there's a couple of OS tools called Resource Monitor and Performance Monitor which also let us analyze what's going on with the different resources on the computer including CPU, memory, disk and network. 

## How Computers Use Resources
- If it's a variable that's currently being used in a function, the data will be in the CPU's internal memory, and our program will retrieve it really fast. If the data is related to a running program but maybe not the currently executing function, it will likely be in RAM, and our program will still get to a pretty fast. If the data is in a file, our program will need to read it from disk, which is much slower than reading it from RAM, and worse than reading from disk, is reading information from over the network.
- A web proxy is a form of cache. It stores websites, images, or videos that are accessed often by users behind the proxy. So they don't need to be downloaded from the Internet every time.
- OS will just remove from RAM anything that's cached, but not strictly necessary. If there's still not enough RAM after that, the operating system will put the parts of the memory that aren't currently in use onto the hard drive in a space called swap.
- Steps to do if we find our computer slowed:
    - First, if there are too many open applications and some can be closed, close the ones that aren't needed. 
    - Or if the available memory is just too small for the amount that computer is using, add more RAM to the computer. 
    - The third reason is that one of the running programs may have a memory leak, causing it to take all the available memory. 
- A memory leak means that memory which is no longer needed is not getting released.

## Possible Causes of Slowness
- The first step is to look into when the computer is slow. If it's slow when starting up, it's probably a sign that there are too many applications configured to start on boot.
- You can try to reduce the size of the files involved. If the file is a log file, you can use a program like `logrotate` to do this for you.
- If instead the computer becomes sluggish after days of running just fine, and the problem goes away with a reboot, it means that there's a program that's keeping some state while running that's causing the computer to slow down.
- Yet another source of slowness is malicious software. Of course, we always want to keep your computer clean of any malicious software, but we can feel the effects of malicious software even if they aren't installed.

## Slow Web Server
- Using `ab` for benchmarking:

    ```bash
    # -n 500 for 500 requests
    $ ab -n 500 google.com/                                                                                                                             22 ⨯
    This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking google.com (be patient)
    Completed 100 requests
    Completed 200 requests
    Completed 300 requests
    Completed 400 requests
    Completed 500 requests
    Finished 500 requests


    Server Software:        gws
    Server Hostname:        google.com
    Server Port:            80

    Document Path:          /
    Document Length:        219 bytes

    Concurrency Level:      1
    Time taken for tests:   23.604 seconds
    Complete requests:      500
    Failed requests:        0
    Non-2xx responses:      500
    Total transferred:      264000 bytes
    HTML transferred:       109500 bytes
    Requests per second:    21.18 [#/sec] (mean)
    Time per request:       47.207 [ms] (mean)
    Time per request:       47.207 [ms] (mean, across all concurrent requests)
    Transfer rate:          10.92 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:       18   22  44.7     20    1020
    Processing:    21   25  19.5     23     318
    Waiting:       21   25  19.5     23     318
    Total:         40   47  49.0     43    1050

    Percentage of the requests served within a certain time (ms)
    50%     43
    66%     44
    75%     44
    80%     44
    90%     46
    95%     52
    98%     58
    99%     85
    100%   1050 (longest request)
    ```
- Using `nice` to start process with different priority and `renice` to change priority process that already running. Priority on linux are 0 - 19 and lowest possible priority which is 19.

    ```bash
    # using pidof to get the Process ID
    for pid in $(pidof process_name); do renice 19 $pid; done
    ```

- Terminate processes with a stop signal without kill the processes completely using `killall`.

    ```bash
    $ killall -STOP process_name
    ```

- Continue the process and wait until it finished.

    ```bash
    $ for pid in $(pidof process_name); do while kill -CONT $pid; do sleep 1; done; done
    ```
## Writing Efficient Code
- We should always start by writing clear code that does what it should and only try to make it faster if we realize that it's not fast enough.
- As a rule, we aim first to write code that's readable, easy to maintain and easy to understand, because that lets us write code with less bugs. But remember, trying to optimize every second out of a script is probably not worth your time.
- The first step is to keep in mind that we can't really make our computer go faster. If we want our code to finish faster, we need to make our computer do less work.
- A profiler is a tool that measures the resources that our code is using, giving us a better understanding of what's going on.
- Because of how profilers work, they are specific to each programming language. So we would use gprof to analyze a C program but use the c-Profile module to analyze a Python program.
- Expensive actions are those that take a long time to complete. Expensive operations include parsing a file, reading data over the network or iterating through a whole list.

## Using the Right Data Structures
- As a rule of thumb, if you need to access elements by position or will always iterate through all the elements, use a list to store them. This could be a list of all computers in the network, of all employees in the company, or of all products currently on sale for example. 
- On the flip side, if we need to look up the elements using a key, we'll use a dictionary. This could be the data associated to a user which we'd look up using their username, the IP associated to a computer using the host name, or the data associated to a product using the internal product code. 

## Expensive Loops
- If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop.
- Another thing to remember about loops is to break out of the loop once you found what you were looking for.

## Keeping Local Results
- To sum all of this up, remember that you'll want to look for strategies that let you avoid doing expensive operations. First, check if these operations are needed at all. If they are, see if you can store the intermediate results to avoid repeating the expensive operation more than needed.

## Slow Script with Expensive Loop
- Measure how long script gonna take to run with `time`:

    ```bash
    $ time python3 caesar.py 
    plaintext = Infosec
    ciphertext = Pumvzlj
    python3 caesar.py  0.01s user 0.01s system 72% cpu 0.029 total
    ```
    **Real** is the amount of actual time that it took to execute the command. This value is sometimes called wall-clock time because it's how much time a clock hanging on the wall would measure no matter what the computer's doing. **User** is the time spent doing operations in the user space. **Sys** is the time spent doing system level operations. The values of user and sys won't necessarily add up to the value of real because the computer might be busy with other processes.

- Using `pprofile3` in Python to measure the function time:

    ```bash
    $ pprofile3 -f callgrind -o profile.out python3 caesar.py

    # Open the profile using kcachegrind
    $ kcachegrind profile.out
    ```

## Parallelizing Operations
- There's actually a whole field of computer science called concurrency, dedicated to how we write programs that do operations in parallel. 
- If a computer has more than one core, the operating system can decide which processes get executed on which core, and no matter the split between cores, all of these processes will be executing in parallel. Each of them has its own memory allocation and does its own IO calls. The OS will decide what fraction of CPU time each process gets and switch between them as needed. 
- A very easy way to run operations in parallel is just to split them across different processes, calling your script many times each with a different input set, and just let the operating system handle the concurrency. 
- Threads let us run parallel tasks inside a process. This allows threads to share some of the memory with other threads in the same process.
-  In Python, we can use the Threading or `AsyncIO modules` to do this. These modules let us specify which parts of the code we want to run in separate threads or as separate asynchronous events, and how we want the results of each to be combined in the end. 

## Slowly Growing in Complexity
- You can add a caching service like memcached which keeps the most commonly used results in RAM to avoid querying the database unnecessarily.
- If the website gets used a lot, you might need to add a caching service like Varnish. This would speed up the load of dynamically created pages.
- This still might not be enough. So you need to distribute your service across many different computers and use a load balancer to distribute the requests. 

## Using Threads to Make Things Go Faster
- Python thread:

    ```python
    from concurrent import futures

    # Using threads
    executor = futures.ThreadPoolExecutor()

    # Using processor
    executor = futures.ProcessPoolExecutor()

    executor.submit(something)

    print('Waiting for all threads to finish.')
    executor.shutdown()
    ```
    To be able to run things in parallel, we'll need to create an executor. This is the process that's in charge of distributing the work among the different workers. The futures module provides a couple of different executors, one for using threads and another for using processes. We'll go with the ThreadPoolExecutor for now. we'll add a message saying that we're waiting for all threads to finish, and then call the shutdown function on the executor. This function waits until all the workers in the pool are done, and only then shuts down the executor.
-  Threads use a bunch of safety features to avoid having two threads that try to write to the same variable.


#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)