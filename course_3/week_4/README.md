Table of Contents
-----------------

  * Pull Requests
    * Practice Quiz: Pull Requests <br>
        * `01_pull_requests.ipynb`
  * Code Reviews
    * Practice Quiz: Code Reviews <br>
        * `02_code_reviews.ipynb`
  * Managing Projects
    * Practice Quiz: Managing Collaboration <br>
        * `03_managing_collaboration.ipynb`
  * Module Review
    * Qwiklabs Assessment: Pushing Local Commits to Github


# Recap
## A Simple Pull Request on GitHub
- Forking is a way of creating a copy of the given repository so that it belongs to our user. In other words, our user will be able to push changes to the forked copy, even when we can't push changes to the other repo. 
- Create fork of a repo -> work on that repo -> add something -> pull request.
- A pull request is a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree. 

## Squashing Changes
- Rebase interactive

  ```bash
  $ git rebase -i master
  ```
  The default action here is pick which takes the commits and rebases them against the branch we selected. When we choose squash, the commit messages are added together and an editor opens up to let us make any necessary changes. When we choose fix up, the commit message for that commit is discarded. 
- Scenario

  ```bash
  $ git rebase -i master #or main

  pick xxx1 <commit_message>
  pick xxx2 <commit_message>

  # Combine both commits and modify commit description using squash
  pick xxx1 <commit_message>
  squash xxx2 <commit_message>

  # Save the file and edit the combined commit message
  <commit_message_combined>

  # Save and exit
  # Check the log
  $ git show                                         
  commit 0896ce56f55122a01c86fd9a053e1d80142007e4 (HEAD -> add-test-file)
  Author: Muhammad Fikri Ashari <gedelixa@gmail.com>
  Date:   Wed Mar 10 10:18:17 2021 -0500

      Add hello world program in Python including input name and print out the name

  diff --git a/hello_world.py b/hello_world.py
  new file mode 100644
  index 0000000..cbf317e
  --- /dev/null
  +++ b/hello_world.py
  @@ -0,0 +1,4 @@
  +#!/usr/bin/env python3
  +
  +name = input("What is your name: ")
  +print("Hello, {}".format(name))
  \ No newline at end of file

  # Success!
  # Try to git push
  $ git push --set-upstream origin add-test-file                                                                                                     128 ⨯
  Username for 'https://github.com': wuvel
  Password for 'https://wuvel@github.com': 
  To https://github.com/wuvel/practice-git.git
  ! [rejected]        add-test-file -> add-test-file (non-fast-forward)
  error: failed to push some refs to 'https://github.com/wuvel/practice-git.git'
  hint: Updates were rejected because the tip of your current branch is behind                                                                               
  hint: its remote counterpart. Integrate the remote changes (e.g.
  hint: 'git pull ...') before pushing again.
  hint: See the 'Note about fast-forwards' in 'git push --help' for details.

  # Replace old commits with the new one with force push
  $ git push -f --set-upstream origin add-test-file                                                                

  Enumerating objects: 4, done.
  Counting objects: 100% (4/4), done.
  Delta compression using up to 6 threads
  Compressing objects: 100% (3/3), done.
  Writing objects: 100% (3/3), 426 bytes | 426.00 KiB/s, done.
  Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
  To https://github.com/wuvel/practice-git.git
  + 13092ca...0896ce5 add-test-file -> add-test-file (forced update)
  Branch 'add-test-file' set up to track remote branch 'add-test-file' from 'origin'.
  ```

## What are code reviews?
- Doing a code review means going through someone else's code, documentation or configuration and checking that it all makes sense and follows the expected patterns. 

## How to Use Code Reviews in GitHub
- Scenario

  ```bash
  # Fix the code
  # Commit with amend
  $ git commit -a --amend                                                                                                                            129 ⨯
  [add-test-file b10f312] Add hello world program in Python including input name and print out the name
  Date: Wed Mar 10 10:18:17 2021 -0500
  2 files changed, 12 insertions(+), 1 deletion(-)
  create mode 100644 hello_world.py

  # Check status
  $ git status           
  On branch add-test-file
  Your branch and 'origin/add-test-file' have diverged,
  and have 1 and 1 different commits each, respectively.
    (use "git pull" to merge the remote branch into yours)

  nothing to commit, working tree clean

  # Force push
  $ git push -f --set-upstream origin add-test-file 

  Enumerating objects: 6, done.
  Counting objects: 100% (6/6), done.
  Delta compression using up to 6 threads
  Compressing objects: 100% (4/4), done.
  Writing objects: 100% (4/4), 570 bytes | 570.00 KiB/s, done.
  Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
  To https://github.com/wuvel/practice-git.git
  + 0896ce5...b10f312 add-test-file -> add-test-file (forced update)
  Branch 'add-test-file' set up to track remote branch 'add-test-file' from 'origin'.
  ```

## Managing Collaboration
-  If you're a project maintainer, it's important that you are reply promptly to pull requests and don't let them stagnate. The more time that passes until a pull request gets reviewed, the more likely it is that there's a new commit that causes a conflict when you try to merge in the change.
-  When it comes to coordinating who does what and when, a common strategy for active software projects is to use an issue tracker.

## Tracking Issues
- An issue tracker tells us the tasks that need to be done, the state they're in and who's working on them. The system also let's us add comments to the issue, these comments can be super helpful. They can give us more details about the problem, explain a way to solve it, or detail how to test if it's been solved. 
- If you're fixing an issue through a pull request, it's possible to automatically close the issue directly once the code is merged. To do this, you need to include a string like closes:#4 in your commit message or as a part of the description of your pull request. Once the code gets merged into the main tree, GitHub will automatically close the issue with a message linking it to the new commit. Example:

  ```md
  Update blablabla

  Also add blabla
  Closes #1
  ```

## Continuous Integration
- A continuous integration system will build and test our code every time there's a change. This means that it will run whenever there's a new commit in the main branch of our code. It will also run for any changes that come in through pull request. In other words, if we have continuous integration configured for our project, we can automatically run our tests using the code in a pull request.
- Once we have our code automatically built and tested, the next automation step is continuous deployment which is sometimes called continuous delivery or CD. Continuous deployment means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time. 
- Pipelines specify the steps that need to run to get the result you want. For a simple Python Project, the pipeline could be to just run the automated tests. For a web service written in Go, the pipeline could be compiled the program, run the unit tests and integration tests and finally deploy the code to a test instance.
- Another concept that turns up when doing CICD is artifacts. This is the name used to describe any files that are generated as part of the pipeline. This typically includes the compiled versions of the code but can include other generated files like PDFs for the documentation or OS specific packages for easy installation. 
- Make sure the authorized entities for the test servers are not the same entities authorized to deploy on the production servers. That way, if there's any kind of compromise in the pipeline, your production server is not affected.
- Always have a plan to recover your access in case your pipeline gets compromised.