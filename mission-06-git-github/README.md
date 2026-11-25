# Mission 6 — Git and GitHub

## 1. Task / objective
Explain Git operations, create a branch, make a learning update and open a Pull Request.

## 2. Work completed
| Git operation | What it does |
|---|---|
| Check status | `git status` shows changed, staged and untracked files |
| Stage changes | `git add path` selects changes for the next commit |
| Create a commit | `git commit -m "message"` records staged changes in local history |
| View history | `git log --oneline` summarizes commits |

Staging prepares selected changes; committing records that prepared snapshot in the repository history. A branch is an independent line of work. A Pull Request asks to review and integrate changes from one branch into another; it makes discussion and review possible before merging.

### My Learning
On the `update-about` branch, I added this summary: “Staging selects the changes for a commit, while committing records them in history. A branch lets me prepare an update separately, and a Pull Request gives others a place to review it before it is merged.”

Branch: `update-about`. Pull Request: (to be recorded after opening the Pull Request). The PR will remain open because the assignment says to merge only if the instructor requests it.

## 3. Commands / tools used
`git status`, `git add`, `git commit`, `git log --oneline`, `git switch -c update-about`, `git push -u origin update-about`; GitHub website for Pull Request. Used these Git operations in this repository and GitHub CLI/website for hosting and review.

## 4. My understanding
Git tracks local history; GitHub hosts a remote copy for sharing and collaboration. A commit is local until pushed. Branches and Pull Requests support review before integration.

## 5. Difficulties faced
No major difficulties. The PR is intentionally left open pending instructor direction.

## 6. How I resolved them
Checked repository status and the diff before staging, committed the README update on a separate branch, pushed the branch and opened a Pull Request.

## 7. Evidence / files
Branch: `update-about`. Pull Request URL: (to be recorded after opening the Pull Request). No credentials or tokens are stored in the repository.

## 8. Commit details
Suggested message: `Complete Git and GitHub collaboration mission`. Commit hash and push confirmation: [filled after push].
