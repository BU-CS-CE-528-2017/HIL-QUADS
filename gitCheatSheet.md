# Git Cheatsheet

###Two references that tell you almost every useful git command:

    https://services.github.com/on-demand/downloads/github-git-cheat-sheet
    http://ndpsoftware.com/git-cheatsheet.html

###How to update your fork when upstream updates happen

    git checkout master
    git fetch class
    git merge class/master
    git push origin master

###How to fix things if you screw up and work on master:

    git checout -b new-master class/master
    git branch -m master test-branch
    git branch -m new-master master
    git status
    git branch
    git checkout test-branch
    git status
    git branch set-upstream to=class/master test-branch
    git rebase
    git rebase
    git status
    git push origin <name of current branch>
    On Github: check the pull requests
