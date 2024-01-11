# How to Git

## Workflow
- `main` -> Stable LTS Version, DO NOT TOUCH unless dev branch testing is complete
- `dev` -> New version that has not been tested for stability yet, create new branches from this whenever dev has updates
- `feature/<feature-name>` -> Your sandbox branch, work on your stuff here then merge to dev once tested on dev environment

## Branches
To change branches, execute below command (This also works if you are checking out to a branch that you have never pulled before but exists as a branch on GitHub)
```
git checkout <branch name>
```
To create a new branch, execute below command
```
git checkout -b <new-branch-name>
```

## Pulling
To pull from a branch, run below command
```
git pull origin <branch-name>
```

## Pushing
Stage your changes through the below command
```
git add .
```
Commit them to your local branch
```
git commit -m "<your message>"
```
If your branch is new, run below command to create a branch under the name you've given on GitHub and push it
```
git push -u origin <local-branch-name>
```
If your branch is not new, run below command to push the changes to the branch
```
git push origin <branch-name>
```
<b>NOTE: NEVER PUSH TO MASTER AND ONLY PUSH TO DEV DIRECTLY IF REALLY NECESSARY</b>

## Handling Merge Conflicts Locally When Pushing or Pulling
Should an incident where a merge conflict occurs while pulling or pushing, resolve it through your word editor and perform the steps for pushing accordingly to the branch that you initially intend to merge to

## Creating Pull Request
- Pull Requests (PR) can only be created through GitHub
- Option only opens when a particular branch has more up-to-date changes compared to other branches
- Write meaningful titles and descriptions for easier readability
- Feel free to assign a member to do code review on the top right of the PR page
- Once done, create pull request and GitHub will cross check whether the code has any merge conflicts
- If there are merge conflicts present, just follow the instructions they give through a link that is under the "merge branch" button