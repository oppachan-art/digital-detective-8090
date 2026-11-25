# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use basic command-line operations, practice safe file changes, explain flags and pipes, and describe package managers.

## 2. Work completed
### Command reference
| Operation | macOS/Linux command | What it does |
|---|---|---|
| Current directory | `pwd` | Prints the current folder path |
| Directory listing | `ls` | Lists visible files and folders |
| Detailed listing | `ls -la` | Includes hidden entries and file details |
| Change directory | `cd ..` | Moves to the parent folder |
| Create directory | `mkdir practice` | Creates a folder |
| Create empty file | `touch note.txt` | Creates an empty file if absent |
| Copy file | `cp note.txt copy.txt` | Creates a second copy |
| Move/rename file | `mv copy.txt renamed.txt` | Moves or renames the file |
| Display file | `cat note.txt` | Prints file contents |

Observed in this repository: `pwd` showed the mission practice folder (full personal path omitted); `ls` showed the practice file and subfolder; `ls -la` also showed hidden entries and file metadata. `cd ..` moved to the parent mission folder. Created `sample-folder`, wrote two lines to `notes.txt`, copied it to `backup.txt`, renamed that copy to `renamed-backup.txt`, and confirmed both lines with `cat`. The detailed listing was piped to `head -n 5` to show only its first lines.

### Safe file changes and notes
Replacing a file's contents removes the previous contents; appending adds text after what is already there. Copying leaves the original in place, while moving changes its location or name. `pwd` helps verify where a command will act; a directory listing shows what is there before and after changes.

A flag changes a command's options. For example, `ls -l` requests a detailed listing and `ls -a` includes hidden names. The pipe `|` sends the output of the command on its left as input to the command on its right; `ls -la | head` shows only the first few output lines. Avoid sharing paths or metadata that identify you.

A package manager provides a consistent way to find, install, update and remove software and track dependencies. On macOS, Homebrew is one example. For this assignment, inspect it if present; do not install or uninstall anything.

## 3. Commands / tools used
Ran `pwd`, `ls`, `ls -la`, `cd ..`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `printf`, and `head`; used a pipe from `ls -la` to `head -n 5` inside the assignment folder. Also checked Homebrew: version 7.0.14 was present with 46 installed formulae; no software was installed or removed.

## 4. My understanding
Commands operate relative to the current directory, so checking the location first and keeping practice inside the repository reduces mistakes. Flags adjust behavior, and a pipe connects command output to another command.

## 5. Difficulties faced
No major difficulties. I kept file operations inside the assignment practice folder.

## 6. How I resolved them
Checked the current folder before creating files, then verified the copied, renamed and appended text with a directory listing and `cat`.

## 7. Evidence / files
`terminal-practice/example.txt`, its renamed backup and the practice subfolder; no screenshot included.

## 8. Commit details
Suggested message: `Complete Terminal and file management mission`. Commit hash: https://github.com/oppachan-art/digital-detective-8090 (see Git history).
