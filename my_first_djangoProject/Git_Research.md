Git
What is git?
Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for source code management in software development, but it can be used to keep track of changes in any set of files. As a distributed revision control system it is aimed at speed, data integrity, and support for distributed, non-linear workflows. Git was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development. Its current maintainer since 2005 is Junio Hamano. As with most other distributed version control systems, and unlike most client–server systems, every Git directory on every computer is a full-fledged repository with complete history and full version tracking abilities, independent of network access or a central server. Like the Linux kernel, Git is free software distributed under the terms of the GNU General Public License version 2.
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Git is easy to learn and has a tiny footprint with lightning fast performance. It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase with features like cheap local branching, convenient staging areas, and multiple workflows.

Branching and Merging
Git has a simple branching model. It is easy to create and merge branches. Branches are cheap and easy to create and merge. Branches are used to develop features isolated from each other. The master branch is the “default” branch when you create a repository. Use other branches for development and merge them back to the master branch upon completion.

Some useful introductory git commands
git init - Create an empty Git repository or reinitialize an existing one
git add - Add file contents to the index
git commit - Record changes to the repository
git status - Show the working tree status
git remote add origin <server> - Add a remote server
git push -u origin master - Push changes to remote server (and remember the branch)
git clone <server> - Clone a repository into a new directory
git branch - List branches (the asterisk denotes the current branch)
git checkout -b <branch> - Create a new branch and switch to it
git checkout <branch> - Switch to a branch
git checkout - Switch back to the branch last checked out
git merge <branch> - Merge a branch into the active branch
git branch -d <branch> - Delete a branch
git push origin <branch> - Push a branch to your remote repository
git push origin --delete <branch> - Delete a remote branch
git pull - Fetch and merge changes on the remote server to your working directory

GitHub
GitHub is a web-based Git repository hosting service. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project. GitHub offers both plans for private repositories and free accounts which are commonly used to host open-source software projects. As of April 2016, GitHub reports having over 14 million users and more than 35 million repositories (including at least 28 million public repositories), making it the largest host of source code in the world.

Some GitHub features
    *Version control - GitHub is a distributed version control system. It allows you to     track  changes in your code and revert back to previous versions if needed
    *Issue tracking - GitHub allows you to track issues in your code. You can create issues, assign them to people, and track their progress
    *Pull requests - GitHub allows you to create pull requests. Pull requests are a way to propose changes to a repository. They are created when you want to merge your changes into the main repository
    *Wikis - GitHub allows you to create wikis for your repository. Wikis are a great way to document your project
    *Social coding - GitHub allows you to follow other users and see what they are working on. You can also see what other users are working on by looking at their public repositories
    *Code review - GitHub allows you to review code. You can review code by looking at pull requests and commenting on the code
    *Project management - GitHub allows you to manage your projects. You can create milestones and assign issues to them. You can also create labels to categorize your issues
    *Gist - GitHub allows you to create Gists. Gists are a way to share code snippets with other users

