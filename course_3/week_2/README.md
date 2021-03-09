Table of Contents
-----------------

  * Advanced Git Interaction
    * Practice Quiz: Advanced Git Interaction <br>
        * `01_advanced_git_interaction.ipynb`
  * Undoing Things
    * Practice Quiz: Undoing Things <br>
        * `02_undoing_things.ipynb`
  * Branching & Merging
    * Practice Quiz: Branching & Merging <br>
        * `03_branching_and_merging.ipynb`
  * Module Review
    * Qwiklabs Assessment: Merging Branches in Git


# Recap
## Skipping the Staging Area
-  `git commit -a` is a shortcut to stage any changes to tracked files and commit them in one step. Example:

    ```bash
    # Skip staging area
    $ git commit -a -m "Added new file"
    ```
- Git uses the HEAD alias to represent the currently checked out snapshot of your project. This lets you know what the contents of your working directory should be.
- As a shortcut, it's generally easy to think of head as a pointer to the current branch.

## Getting More Information About Our Changes
- See the patch:

    ```bash
    ┌──(kali㉿kali)-[~/wuvel/wuvel-git/blog]
    └─$ git log -p              
    commit bc57b2121239b452c47a947f53afc794dc35e7c6 (HEAD -> main, origin/main, origin/HEAD)
    Author: wuvel <gedelixa@gmail.com>
    Date:   Sun Jan 3 06:08:17 2021 -0500

        Updated config file

    diff --git a/Gemfile b/Gemfile
    index ab4a9d5..9a040f4 100644
    --- a/Gemfile
    +++ b/Gemfile
    @@ -3,7 +3,7 @@ source "https://rubygems.org"
    # When you want to use a different version, change it below, save the
    # file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
    #
    -#     bundle exec jekyll serve
    +#     bundle exec jekyll serve --livereload
    #
    # This will help ensure the proper Jekyll version is running.
    # Happy Jekylling!
    diff --git a/_config.yml b/_config.yml
    index 15b511c..bf28987 100644
    --- a/_config.yml
    +++ b/_config.yml
    @@ -18,16 +18,14 @@
    # You can create any custom variable you would like, and they will be accessible
    # in the templates via {{ site.myvariable }}.
    
    -title: Your awesome title
    -email: your-email@example.com
    +title: Wuvel
    +email: gedelixa@student.ub.ac.id
    description: >- # this means to ignore newlines until "baseurl:"
    -  Write an awesome description for your new site here. You can edit this
    -  line in _config.yml. It will appear in your document head meta (for
    -  Google search results) and in your feed.xml site description.
    +  Welcome to my personal blog site.
    baseurl: "/blog" # the subpath of your site, e.g. /blog
    ...
    ```
- Show spesific commit:

    ```bash
    ┌──(kali㉿kali)-[~/wuvel/wuvel-git/blog]
    └─$ git show bc57b2121239b452c47a947f53afc794dc35e7c6
    commit bc57b2121239b452c47a947f53afc794dc35e7c6 (HEAD -> main, origin/main, origin/HEAD)
    Author: wuvel <gedelixa@gmail.com>
    Date:   Sun Jan 3 06:08:17 2021 -0500

        Updated config file

    diff --git a/Gemfile b/Gemfile
    index ab4a9d5..9a040f4 100644
    --- a/Gemfile
    +++ b/Gemfile
    @@ -3,7 +3,7 @@ source "https://rubygems.org"
    # When you want to use a different version, change it below, save the
    # file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
    #
    -#     bundle exec jekyll serve
    +#     bundle exec jekyll serve --livereload
    #
    # This will help ensure the proper Jekyll version is running.
    # Happy Jekylling!
    ../
    ```
- Show more stat:

    ```bash
    ┌──(kali㉿kali)-[~/wuvel/wuvel-git/blog]
    └─$ git log --stat                                   
    commit bc57b2121239b452c47a947f53afc794dc35e7c6 (HEAD -> main, origin/main, origin/HEAD)
    Author: wuvel <gedelixa@gmail.com>
    Date:   Sun Jan 3 06:08:17 2021 -0500

        Updated config file

    Gemfile                            |  2 +-
    _config.yml                        | 12 +++++-------
    _posts/2021-01-03-my-first-post.md | 12 ++++++++++++
    3 files changed, 18 insertions(+), 8 deletions(-)

    commit 8fdc9f7494ef87c42049aec4b9dad9e6009fd0b6
    Author: wuvel <gedelixa@gmail.com>
    Date:   Sun Jan 3 05:47:59 2021 -0500

        Updated config with baseurl

    _config.yml | 4 ++--
    1 file changed, 2 insertions(+), 2 deletions(-)

    commit 5d67fca159c49b94cfb4124d024bcb0e2debf73d
    Author: wuvel <gedelixa@gmail.com>
    Date:   Sun Jan 3 05:44:30 2021 -0500

        Created jekyll site

    .gitignore                                   |   5 ++
    404.html                                     |  25 ++++++++++
    Gemfile                                      |  30 ++++++++++++
    Gemfile.lock                                 | 268 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    _config.yml                                  |  55 +++++++++++++++++++++
    _posts/2021-01-03-welcome-to-jekyll.markdown |  29 +++++++++++
    about.markdown                               |  18 +++++++
    index.markdown                               |   6 +++
    8 files changed, 436 insertions(+)

    commit d40d56ef62b7b866d91e196fc2a42fa5f77523de
    ```
- Alternative to `diff -u`:

    ```bash
    ┌──(kali㉿kali)-[~/wuvel/wuvel-git/blog]
    └─$ git diff      
    diff --git a/.gitignore b/.gitignore
    old mode 100644
    new mode 100755
    diff --git a/404.html b/404.html
    old mode 100644
    new mode 100755
    diff --git a/Gemfile b/Gemfile
    old mode 100644
    new mode 100755
    index 9a040f4..603c511
    --- a/Gemfile
    +++ b/Gemfile
    ...
    ```
- Review changes:

    ```bash
    ┌──(kali㉿kali)-[~/wuvel/wuvel-git/blog]
    └─$ git add -p
    diff --git a/.gitignore b/.gitignore
    old mode 100644
    new mode 100755
    (1/1) Stage mode change [y,n,q,a,d,?]?
    ```
- See the changes staged but not commited:

    ```bash
    ┌──(kali㉿kali)-[~/wuvel/wuvel-git/blog]
    └─$ git diff --staged
    ```

## Deleting and Renaming Files
- Delete file in the repo:

    ```bash
    $ git rm something
    $ git commit -m "Delete ...."
    ```
- Rename file in the repo:

    ```bash
    $ git mv something.py some.py
    $ git commit -m "New name for ...."
    ```
- `.gitignore` file. Inside this file, we'll specify rules to tell git which files to skip for the current repo. Example:

    ```bash
    $ echo .DS_STORE > .gitignore
    $ git add .gitignore
    $ git commit -m "Add .gitignore, ignoring .DS_STORE"
    ```

## Undoing Changes Before Committing
- You can change a file back to its earlier committed state by using the git checkout command followed by the name of the file you want to revert:
    
    ```bash
    $ git checkout file_name
    ```
- If you need to check out individual changes instead of the whole file, you can do that using the dash p flag. This will ask you change by change if you want to go back to the previous snapshot or not:

    ```bash
    $ git checkout -p file_name
    ```
- Unstage changes:

    ```bash
    $ git reset HEAD file_name
    ```
- Ask spesific changes to reset:

    ```bash
    $ git reset -p HEAD file_name
    ```

## Amending Commits
- Overwrite previous commit:

    ```bash
    $ git commit --ammend
    ```
- Avoid amending commits that have already been made public.

## Rollbacks
- Revert commit:

    ```bash
    $ git revert HEAD
    ```
## Identifying a Commit
- The commit ID is the 40 character long string after the word commit, you really can't miss it. This long jumble of letters and numbers is actually something called a hash, which is calculated using an algorithm called SHA1.
- Revert with identifier:

    ```bash
    # Check the commit ID
    $ git log
    
    # Revert
    $ git revert <commit_id>
    ```

## What is a branch?
-  In Git, a branch at the most basic level is just a pointer to a particular commit. 
- The default branch that Git creates for you when a new repository initialized is called master.
- Branches make it really easy to experiment with new ideas or strategies and projects. When you want to add a feature or fix something, you can create a new branch and do your development there. You can merge back into the master branch, when you've got something you like, or discard your changes without negative impact if they don't work out.

## Creating New Branches
- We can use the git branch command to list, create, delete, and manipulate branches.
- We use git checkout to check out the latest snapshot for both files and for branches. 
- Checking branch:

    ```bash
    $ git branch                                                          
    * main
    ```
- Add branch

    ```bash
    $ git add branch_name
    ```
- Switch branch

    ```bash
    $ git checkout branch_name
    ```
- Create and switch branch

    ```bash
    $ git checkout -b branch_name
    ```
## Working with Branches
- Delete branch

    ```bash
    $ git branch -d branch_name
    ```

## Merging
- Merging is the term that Git uses for combining branch data and history together.
- Merging branch_name to master:

    ```bash
    # Make sure we are in the master branch
    $ git branch
    branch_name
    * master
    $ git merge branch_name
    ...
    ```
- Git uses two different algorithms to perform a merge, fast-forward and three-way merge. The merge above is an example of a fast-forward merge. This kind of merge occurs when all the commits in the checked out branch are also in the branch that's being merged. If this is the case, we can say that the commit history of both branches doesn't diverge. In these cases, all Git has to do is update the pointers of the branches to the same commit, and no actual merging needs to take place.
-  On the other hand, a three-way merge is performed when the history of the merging branches has diverged in some way, and there isn't a nice linear path to combine them via fast-forwarding. This happens when a commit is made on one branch after the point when both branches split. In our case, this could have happened if we made a commit on the master branch after creating the other branches. When this occurs, Git will tie the branch histories together with a new commit. And merge the snapshots at the two branch tips with the most recent common ancestor, the commit before the divergence. 

## Merge Conflicts
- From time to time, we might find that both the branches we're trying to merge have edits to the same part of the same file. This will result in something called a merge conflict. 
- If there is conflict, check the git status, fix the code, run `git add` and commit.
- Handy `git log` command:

    ```bash
    $ git log --graph --oneline
    * bc57b21 (HEAD -> main, origin/main, origin/HEAD) Updated config file
    * 8fdc9f7 Updated config with baseurl
    * 5d67fca Created jekyll site
    * d40d56e Initial commit
    ```
- Stop the merge and reset:

    ```bash
    $ git merge --abort
    ```

## Git Branches and Merging Cheat Sheet
| Command | Explanation & Link |
| ------- | ------------------ |
| git branch | Used to manage branches |
| git branch <name> | Creates the branch |
| git branch -d <name> | Deletes the branch |
| git branch -D <name> | Forcibly deletes the branch |
| git checkout <branch> | Switches to a branch. |
| git checkout -b <branch> | Creates a new branch and switches to it. |
| git merge <branch> | Merge joins branches together.  |
| git merge --abort | If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action. |
| git log --graph --oneline | This shows a summarized view of the commit history for a repo. |

