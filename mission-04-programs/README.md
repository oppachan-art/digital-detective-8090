# Mission 4 — How programs run

## 1. Task / objective
Create and run a one-line Python program and compare compiled and interpreted execution.

## 2. Work completed
Created `hello.py` with `print("Hello from Python")`. Running `python3 hello.py` with Python 3.14.7 displayed `Hello from Python`.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation/execution happens | Usually translates source into another form before execution | Usually reads and executes instructions at runtime |
| Typical output | Executable or intermediate code | Program output as instructions execute |
| Example | C compiler such as GCC | Python interpreter such as CPython |
| One advantage | Compiled output can run quickly without translating source each time | Fast edit-run cycle and useful interactive exploration |

A compiler generally translates source before the program runs, often producing machine code or another intermediate form. An interpreter executes the program by reading instructions at runtime. The distinction is not absolute: language implementations can combine compilation and interpretation. Python is commonly run by an interpreter, while C is commonly compiled.

## 3. Commands / tools used
`python3 hello.py`; Python 3.14.7 and the Terminal. Output observed: `Hello from Python`.

## 4. My understanding
Both approaches turn programmer-written instructions into actions the computer can carry out. They differ mainly in when and how translation happens.

## 5. Difficulties faced
No major difficulties; the one-line program ran successfully.

## 6. How I resolved them
Saved the print statement in `hello.py` and ran it with Python 3.

## 7. Evidence / files
`hello.py` (create this file in this folder).

## 8. Commit details
Suggested message: `Compare compilers and interpreters`. Commit hash: https://github.com/oppachan-art/digital-detective-8090 (see Git history).
