# Git Exercise

### Basics

1. Branch Practice 
* Create a branch A, B, and C both locally and remotely
* Check that all three exist remotely and locally
* Delete branch A locally
* Delete branch B remotely
* Delete branch C locally and remotely
* You should be able to see A on github, B on your computer, and not able to see C anymore anywhere


2. Multiple Committs 

You do not have to push only one commit at a time to the remote repository. To do this, follow these steps
* Create a branch in your local repository
* Create a file 
* Add it to staging and commit it to your local repository
* Create a new file and add some lines to the original file
* Add new changes and file to staging and commit it to the local repository
* Push your changes to the remote repository and they should be in two different commits, visible by checking the branch you created.

Hint - You are only supposed to push once

## Advanced

3. Revert Changes

Git is powerful in that it allows you to rollback unwanted changes or because a bug was introduced. You try it - 

* Create a local branch
* Create a file and add one line to it
* Commit these changes to local repository
* Add another line and commit, then do it again so that there are 3 lines and 3 commits.
* Push commits to the remote repository
* Revert the changes so that there is only one line in the file

4. Merge Conflicts

A merge conflict occurs when two users are trying to edit the same line, but we can only choose 1 version of this. Create a new file called merge.sh, add the code below, and run it using the command `sh merge.sh`

```
mkdir git-repo
cd git-repo
git init
touch my_code.sh
git add my_code.sh
echo "echo Hello" > my_code.sh
git commit -am 'initial'
git checkout -b new_branch
echo "echo \"Hello World\"" > my_code.sh
git commit -am 'first commit on new_branch'
git checkout master
echo "echo \"Hello World!\"" > my_code.sh
git commit -am 'second commit on master'
git merge new_branch
```
# Bash

Tips
* You can use tab to autocomplete commands. 
* The up arrow can cycle through your command history(and down).
* ctrl-c kills a program
* crlc-d logs you out of bash
* !! runs the last command 
* echo "hello" just prints out hello to you (STDOUT)
* Real paths - /home/josh
* Relative paths - ../josh
* sudo allows a user to become a superuser, giving them the ability to do anything

For this, you should resort to googling and man pages. This will be more of a practice in how well you can google since you know what commands to use already.

1. Find

Use `find` to locate your `.gitconfig` file 

2. Grep

Grep this file to find all the lines that mention the keyword "file" and redirect the output into a new file called output.txt

3. Piping

Create a file that prints out your UIN in python

Then use the `|` operator to encrypt it and decrypt it. Make a crypt.py file with this code, which uses xor encryption.

```
print(int(input()) ^ 123456789)
```

# Advanced 
4. Scripting

Lets make a bash script that will take in the input of a commit message and deploy changes to the current branch. You can run this by doing `sh filename.sh` where filename.sh is the script you make. You can name it whatever you want. 
