Table of Contents
-----------------

  * Introduction to GitHub
    * Practice Quiz: Introduction to GitHub <br>
        * `01_introduction_to_github.ipynb`
  * Using a Remote Repository
    * Practice Quiz: Using a Remote Repository <br>
        * `02_using_a_remote_repository.ipynb`
  * Solving Conflicts
    * Practice Quiz: Solving Conflicts <br>
        * `03_solving_conflicts.ipynb`
  * Module Review
    * Qwiklabs Assessment: Introduction to Github


# Recap
## What is GitHub?
- For real configuration and development work, you should use a secure and private Git server, and limit the people authorized to work on it.

## Basic Interaction with GitHub
- Cloning GitHub repository

    ```bash
    $ git clone <url>
    ```
- Send all commits to repository

    ```bash
    $ git push 
    ```
- Enable credential helper to cache our credential

    ```bash
    $ git config --globabl credential.helper cache
    ```
- Pull changes from repository

    ```bash
    $ git pull
    ```

## What is a remote?
- Alongside the local development branches like master, Git keeps copies of the commits that have been submitted to the remote repository and separate branches. If someone has updated a repository since the last time you synchronize your local copy, Git will tell you that it's time to do an update. If you have your own local changes when you pull down the code from the remote repo, you might need to fix merge conflicts before you can push your own changes.
- Modify -> Stage -> Commit local changes and Fetch -> Merge -> Push.

## Working with Remotes
- When we call a git clone to get a local copy of a remote repository, Git sets up that remote repository with the default origin name. We can look at the configuration for that remote by running `git remote -v` in the directory of the repo.
- Show origin

    ```bash
    $ git remote show origin
    ```
- Remote branch (read-only)

    ```bash
    $ git branch -r
    ```
    If we want to make a change to a remote branch, we must pull the remote branch, merge it with the local branch, then push it back to its origin.

## Fetching New Changes
- Sync data

    ```bash
    $ git fetch
    $ git merge origin/master
    ```

## Updating the Local Repository
- Fetch and merge automatically

    ```bash
    $ git pull
    ```
- Get remote branch without merge

    ```bash
    $ git remote update
    ```

## The Pull-Merge-Push Workflow
```bash
# Pull but fail because conflict, do this:
$ git log -p origin/master

# Fix by opening the conflict file
$ code file

# Finish the merge
$ git add file
$ git commit

# Push
$ git push
```

## Pushing Remote Branches
```bash
$ git push -u origin <branch_name>
```

## Rebasing Your Changes
- Rebasing means changing the base commit that's used for our branch.

    ```bash
    # Checkout and pull
    $ git checkout master
    $ git pull

    # Show log all branches
    $ git log --graph --oneline --all

    # Rebase to avoid three way merge
    $ git checkout <branch_name>
    $ git rebase master

    # Merge again
    $ git checkout master
    $ git merge <branch_name>

    # Remove remote branch
    $ git push --delete origin <branch_name>
    $ git branch -d <branch_name>

    # Push
    $ git push
    ```
- We can also rebase after our teammates commit and push after we commit.

    ```bash
    # Fetch our teammates file
    $ git fetch

    # Rebase
    $ git rebase origin/master

    # Fix the code
    $ code file.py

    # Add and rebase again
    $ git add file.py
    $ git rebase --continue

    # Push
    $ git push
    ```
- Rebasing instead of merging rewrites history and maintains linearity, making for cleaner code.

