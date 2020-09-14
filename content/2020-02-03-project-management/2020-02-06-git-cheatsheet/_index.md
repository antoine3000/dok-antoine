---
title: Git cheatsheet
---

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Useful commands

Start a project from scratch: `git init` and then `git remote add origin {repository-url}`

Pull the last commits from the distant server: `git pull`

Add all the modifications to the stack: `git add .`

Do a commit with a description: `git commit -m "message"`

Push the commit(s) on the distant server: `git push`

Discard the changes on uncommited files: `git checkout .`

Create a new branch: `git branch {new-branch}`

Merge the current branch with another: `git merge {other-branch}`

Delete a local branch: `git branch -d {local-branch}`

Delete a remote branch: `git push origin --delete {remote-branch}`

Change your working branch: `git checkout {branch-name}`

### Visualization

Get the repo's status `git status` or the repo's history: `git log`

Get the list of branches:  `git branch ` or `git branch -v` to get more info

Get the the commit-tree of all branches: `git log --oneline --abbrev-commit --all --graph --decorate --color`

### Configuration

Keep the password in memory for the next 8 hours: `git config --global credential.helper 'cache --timeout 28800'`

Add a shortcut to add and commit at the same time: `git config --global alias.ac '!git add -A && git commit'` and then `git ac -m "message"`

Configure an alias to display the commit-tree:  `git config --global alias.gg 'log --oneline --abbrev-commit --all --graph --decorate --color'` and then use `git gg`
