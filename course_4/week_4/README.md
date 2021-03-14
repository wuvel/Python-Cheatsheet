Table of Contents
-----------------

  * Managing Computer Resources
    * Practice Quiz: Managing Computer Resources <br>
        * `01_managing_computer_resources.ipynb`
  * Managing Our Time
    * Practice Quiz: Managing Our Time <br>
        * `02_managing_our_time.ipynb` 
  * Making Our Future Lives Easier
    * Practice Quiz: Making Our Future Lives Easier <br>
        * `03_making_our_future_lives_easier.ipynb`
  * Module Review
    * Qwiklabs Assessment: Debugging and Solving Software Problems <br>
        * `04_start_date_report.py`

# Recap
## Memory Leaks and How to Prevent Them
- A memory leak, happens when a chunk of memory that's no longer needed is not released. If the memory leak is small, we might not even notice it, and it probably won't cause any problems. But, when the memory that's leaked becomes larger and larger over time, it can cause the whole system to start misbehaving.
- To understand how this works, let's look into what these languages do. First, they request the necessary memory when we create variables, and then they run a tool called Garbage collector, that's in charge of freeing the memory that's no longer in use. To detect when that's the case, the garbage collector looks at the variables in use and the memory assigned to them and then checks if there any portions of the memory that aren't being referenced by any variables. 
- We can use a memory profiler to figure out how the memory is being used. 
- For profiling C and C plus plus programs, we'll use Valgrind.

## Network Saturation
- The latency is the delay between sending a byte of data from one point and receiving it on the other. This value is directly affected by the physical distance between the two points and how many intermediate devices there are between them. 
- The bandwidth is how much data can be sent or received in a second. 
- Traffic shaping is a way of marking the data packets sent over the network with different priorities. To avoid having huge chunks of data, use all the bandwidth.
- There are limits to how many connections a single server can have, which will prevent new connections.  

## Dealing with Memory Leaks
- Terminal with long scroll buffer:

    ```bash
    $ uxterm

    # Filling up the scroll buffer
    $ od -cx /dev/urandom

    # Top and SHIFT + M to order memory
    $ top
    ```
    The scroll buffer is that nifty feature that lets us scroll up and see the things that we executed and their output.

    Top column: The column labeled RES is the dynamic memory that's preserved for the specific process. The one labeled SHR is for memory that's shared across processes, and the one labeled VIRT lists all the virtual memory allocated for each process. This includes; process specific memory, shared memory, and other shared resources that are stored on disk but maps into the memory of the process. 
- Using profiler for Python:

    ```python
    # Import
    from memory_profiler import profile

    # Add profiler before main function
    # This type of label is called a decorator and it's used in Python to add extra behavior to functions without having to modify the code. 
    @profile
    def main():
        something
    ```

## Getting to the Important Tasks
- Eisenhower Decision Matrix. When using this method, we split tasks into two different categories: urgent and important.
- Technical debt is the pending work that accumulates when we choose a quick-and-easy solution instead of applying a sustainable long-term one. 

## Prioritizing Tasks
- The first step is to make a list of all of the tasks that need to get done.
- Once you have the list, you can check the real urgency of the tasks.
- Look at the rest of the list and assess the importance of each issue.
- Once you have a list of the most important tasks to work on, you'll want to have a rough idea of how much effort they'll take.
- The key here is to always work on important tasks.

## Estimating the Time Tasks Will Take
- Avoid being overly optimistic with your time estimates. The best way to do this is to compare the task that you're trying to do with similar tasks that you've done before.

## Dealing with Hard Problems
- One piece of advice I found really valuable is to develop code in small, digestible chunks. 
- Try writing the tests for the program before the actual code to help you keep focus on your goal. 
- If you're building a system or deploying an application, having documentation that states what the end goal should be, and the steps you took to get there can be really helpful. To both keep you on track, and figure out any problems that might turn up along the way.

## Proactive Practices
- If we're the ones writing the code, one thing we can do is to make sure that our code has good unit tests and integration tests.
- If our tests have good coverage of the code, we can rely on them to catch a wide array of bugs whenever there's a change that may break things. 
- Another step in this direction is to have a test environment, where we can deploy new code before shipping it to the rest of our users.
- Deploy software in phases or canaries. What this means is that instead of upgrading all computers at the same time and possibly breaking all of them at the same time, you upgrade some computers first and check how they behave.
- Another method that can help us is having centralized logs collection. This means there's a special server that gathers all the logs from all the servers or even all the computers in the network. That way, when we have to look at those logs, we don't need to connect to each machine individually, we can comb through all the logs together in a centralized server. 

## Preventing Future Problems
- If you have to work around an issue in an application developed by someone else, it's important that you report a bug to the relevant developers. 
- On the flip side, if you have to work around an issue in the software that you own, make sure that you write a test that catches the problem.

## More About Preventing Future Breakage
- Preventing future breakage is a bit of a dynamic subject. Probably the most useful techniques here are identifying, isolating, and managing problem domains and failure domains. 
- Problem Domains just describe the complexity of a given problem that one is trying to solve. Let’s look at an example below:
    - For example: counting the number of occurrences of a specific word in one of Shakespeare’s plays, like Hamlet. This is an indexing problem. And its problem domain is fairly limited in scope. It’s a single word, and a single play. A bit of BASH could easily solve this problem. So the problem domain is small, and the technical solution is fairly simple.
    - However, if the scope is widened slightly to include all of Shakespeare’s plays, the problem domain becomes larger. Any software solution used to try and solve this indexing problem has to now handle various logic that it did not have to handle before, like consolidating word occurrences in various plays. I.e. the word ‘Brevity’ may occur at least once in Hamlet, and N number of times in various other plays. Managing N occurrences of ‘Brevity’ over M works of Shakespeare is an order of magnitude more complex in terms of describing the problem domain. A bit of BASH could solve this problem, but it might be difficult.
- If the problem becomes slightly more complex, such as finding the occurrences of various synonyms to a given word, then the problem domain becomes equally large. Managing original words, their synonyms, and their hit-count across multiple works of Shakespeare is even MORE complex.
- Like problem domains, failure domains just describe the complexity of a system. Except, instead of describing the various problems a system tries to solve, failure domains describe various sub-systems which may fail. Using the Shakespeare example again, if one of your systems is responsible for managing the full text of the works of Shakespeare (a content server), that might be a single failure domain. If another system is responsible for actually searching that content and counting the words (an indexer), that is a separate failure domain. Some failure domains can be within other failure domains. For example, if an indexer fails, the content server may not fail. But if a content server fails, the indexer will probably also fail.
