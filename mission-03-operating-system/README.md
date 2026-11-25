# Mission 3 — Understand the operating system

## 1. Task / objective
Observe system information and processes, explain paths and permissions, and describe OS responsibilities.

## 2. Work completed
### Privacy-safe observations
| Information | What it tells you | Your observation |
|---|---|---|
| OS/system details | OS family and version | macOS 27.2.1 (Darwin; device name omitted). |
| Current account identity | Which local account runs a command | Local account runs commands; username redacted. |
| Available/used storage | Capacity and space in use | Approximately 926 GiB total, 13 GiB used and 785 GiB available at the time of observation; filesystem details omitted. |
| System activity | Snapshot of running processes | A brief process snapshot showed operating-system services and active applications. Process names and PIDs were omitted. |

A process is a running instance of a program. A PID is the operating system's numeric identifier for a process while it is running. Examples commonly include a browser and a text editor; the exact processes depend on what is open.

An absolute path begins at the filesystem root; a relative path is interpreted from the current directory. Example relative path: `mission-03-operating-system/README.md`. Absolute path: [use a redacted form such as `/…/digital-detective-8090/mission-03-operating-system/README.md`].

| Permission | Meaning | Example |
|---|---|---|
| `r` | Read contents | Open a text file |
| `w` | Change contents | Edit a file |
| `x` | Run a file; on a directory, traverse/access it | Run a script or enter a folder |

### OS responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules and stops running programs | Shares CPU time among apps |
| Memory management | Allocates RAM and keeps processes' memory separate | Gives a browser memory while it runs |
| Device management | Coordinates software access to hardware | Sends a print job to a printer |
| File management | Organizes files, folders and storage | Saves a document in a folder |
| User interface / shell | Lets a person interact graphically or with commands | Desktop or Terminal |
| Security and permissions | Controls accounts and allowed access | Limits who can edit a file |

## 3. Commands / tools used
Used `sw_vers` for OS version, `df -h /` for storage, and `ps` for a process snapshot. Account, device and process identifiers were omitted.

## 4. My understanding
The operating system coordinates programs, memory, devices, files and access. A path identifies a location, and permissions express what an owner or other users may do with a file.

## 5. Difficulties faced
No major difficulties. I omitted account, device and process identifiers from the notes.

## 6. How I resolved them
Recorded only the broad OS version and rounded storage totals; process names and PIDs were not copied.

## 7. Evidence / files
Privacy-safe system summary is included above; no screenshot or identifying output included.

## 8. Commit details
Suggested message: `Document operating system and file management`. Commit hash: https://github.com/oppachan-art/digital-detective-8090 (see Git history).
