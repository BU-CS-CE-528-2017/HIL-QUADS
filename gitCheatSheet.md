Git Cheatsheet

Two references that might help you better than I can:
    1) https://services.github.com/on-demand/downloads/github-git-cheat-sheet.p$
    2) http://ndpsoftware.com/git-cheatsheet.html

List of Git commands discussed with Peter:

- git remote -v:
-


How to fix things if you fuck up and work on master
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
