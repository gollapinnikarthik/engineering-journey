Linux Foundations
Overview
This section documents my understanding of Linux fundamentals, focusing on how the operating system manages files, directories, processes, users, and permissions.
The goal is to understand not only how Linux commands work, but also why they behave the way they do.
Core Concepts
The learning areas covered include:
Filesystem navigation: Understanding directory structures, absolute and relative paths.
File management: Creating, copying, moving, searching, and deleting files.
Shell utilities: Working with pipes, redirection, aliases, and command documentation.
Symbolic links: Understanding references to files and directories.
Process management: Inspecting, monitoring, and terminating processes.
Users and permissions: Understanding ownership, groups, access control, and directory traversal.
Learning Philosophy
The emphasis is on conceptual understanding, troubleshooting, and practical applications rather than collecting routine command exercises.
Complex scenarios and important edge cases are documented separately to demonstrate how Linux concepts work together.
1. Linux Filesystem and Path Resolution
Absolute vs Relative Paths
Linux organizes files and directories in a hierarchical filesystem beginning at the root directory (/).
Absolute Path
Starts from /.
Specifies a location independently of the current working directory.
Example: /home/dell/company/reports/sales.txt
Relative Path
Resolves from the current working directory.
Its meaning changes depending on where the user is currently located.
Example: ../reports/sales.txt
Important Path References
Reference
Meaning
/
Filesystem root
~
Current user’s home directory
.
Current directory
..
Parent directory
pwd
Display current working directory
Why Path Resolution Matters
A relative path is interpreted using the process’s current working directory.
For example, reports/sales.txt can refer to different files depending on where the command is executed.
An absolute path removes that dependency.
Engineering Considerations
Use absolute paths when scripts must reference a predictable location.
Use relative paths when working within a known project structure.
Understand the current working directory before executing destructive operations.
Directory execute (x) permission controls traversal, even when the target file has read or write permission.
Key takeaway: Linux resolves paths before accessing files, and filesystem permissions determine whether the requested access is allowed.
2. File Management and Searching
Core Concepts
Linux provides commands to create, copy, move, rename, delete, and locate files.
The most important distinction is understanding how these operations interact with filesystem paths and permissions.
Moving vs Copying
cp creates a copy of a file, preserving the original.
mv moves or renames a file without retaining the original at its previous path.
rm removes directory entries and should be used carefully because normal removal does not send files to a recycle bin.
The source and destination can use absolute or relative paths.
Searching with find and grep
find searches the filesystem for files and directories based on criteria such as name, type, and permissions.
grep searches text for matching patterns.
The difference is important:
find identifies filesystem objects.
grep identifies matching text within input or files.
Targeted File Operations
Recursive operations can unintentionally affect files that require different permissions.
For example:
find reports -type d -exec chmod 700 {} +
find reports -type f -name "*.txt" -exec chmod 600 {} +
This approach gives directories traversal permission while restricting ordinary text files to read and write access for the owner.
Key Lessons
Always understand the working directory before performing file operations.
Use quoted patterns such as "*.txt" when the pattern must be interpreted by find rather than expanded by the shell.
Use targeted operations instead of applying recursive changes indiscriminately.
Verify the results of file management commands before continuing with dependent operations.
3. Shell Utilities, Pipes and Redirection
Pipes (
|
)
A pipe connects commands by sending the standard output of one command to the standard input of another.
This allows multiple commands to work together without creating intermediate files.
Practical Example:
ps aux | grep '[p]ython' | head -n 5
This command:
Retrieves running processes using ps aux.
Filters processes containing python.
Displays only the first five matching lines.
The [p]ython pattern avoids matching the grep command itself.
Input and Output Redirection
Linux provides different ways to control where command output is written.
Operator
Purpose
>
Redirect output, replacing existing content
>>
Append output without removing existing content
<
Read standard input from a file
2>
Redirect standard error
`
`
Practical Example:
grep -i "error" server.log | wc -l > error_count.txt
This searches a log file for lines containing error, ignoring case, counts matching lines, and saves the result to error_count.txt.
Important: Standard output and standard error are separate streams. A normal pipe only forwards standard output.
Aliases
Aliases provide shortcuts for frequently used commands.
alias details='ls -la'
Aliases created interactively are normally temporary.
To make an alias available in future interactive Bash sessions, add its definition to ~/.bashrc.
Manual Pages
Linux provides built-in command documentation through man.
Useful navigation controls:
/pattern — Search within the manual.
n — Next matching occurrence.
N — Previous matching occurrence.
q — Exit the manual.
Key Lessons
Pipes allow commands to perform more complex operations together.
Redirection controls where input and output flow.
> overwrites existing file content, whereas >> appends.
Aliases improve command-line efficiency but do not replace understanding the underlying commands.
Manual pages provide a reliable reference for command options and behaviour.
4. Symbolic Links
What Is a Symbolic Link?
A symbolic link (symlink) is a filesystem entry that stores a path referring to another file or directory.
Unlike a regular file copy, a symbolic link does not contain a separate copy of the target’s data.
Creating and Inspecting Links
ln -s TARGET LINK_NAME
ls -l LINK_NAME
readlink LINK_NAME
ln -s creates a symbolic link.
ls -l displays the link and its target path.
readlink displays the path stored in the link.
Relative Path Resolution
A relative target path in a symbolic link is resolved from the directory containing the link, not from the shell’s current working directory.
Consider this structure:
project/
├── config/
│   └── app.conf
└── service/
   └── current.conf -> ../config/app.conf
When accessed through service/current.conf, Linux follows the relative target path to config/app.conf.
Broken Symbolic Links
A symbolic link becomes dangling (broken) when its stored path no longer resolves to an existing target.
For example, moving or deleting config/app.conf without updating the link can make service/current.conf unusable.
The symbolic link itself may still exist even though its target is missing.
Deleting Links vs Deleting Targets
rm service/current.conf
Removing this symbolic link deletes the link itself, not the target file config/app.conf.
This distinction is important when managing application configuration files and shared resources.
Key Lessons
Symbolic links store paths rather than copies of target data.
Relative link targets are resolved from the link’s parent directory.
Moving a target can break existing links.
Removing a symbolic link normally leaves its target unchanged.
Symbolic links are useful for configuration management and organizing shared resources.
5. Process Management
Understanding Linux Processes
A process is a running instance of a program.
Linux assigns each process a unique Process ID (PID) while it exists. Processes also have attributes such as ownership, parent process, state, and resource usage.
Inspecting Processes
Common tools include:
Command
Purpose
ps aux
Display a snapshot of running processes
top
Monitor processes and resource usage interactively
pgrep -af python
Find processes matching python and display their command lines
kill
Send a signal to a process
Important distinction: ps provides a snapshot, while top continually refreshes process information.
Understanding Signals
The kill command sends signals to processes. It does not necessarily terminate them immediately.
Two important signals are:
SIGTERM (15)
The default signal sent by kill.
Requests that a process terminate.
Gives the process an opportunity to handle the signal and perform cleanup.
SIGKILL (9)
Forces process termination.
Cannot be caught, blocked, or ignored by the target process.
Does not allow application-level cleanup.
Practical Engineering Scenario
Suppose a Python application stops responding.
First, identify and inspect its process:
pgrep -af python
ps -o pid,ppid,user,stat,cmd -p 12345
Here, 12345 represents the identified PID.
Request graceful termination:
kill -TERM 12345
If the process does not terminate and forced termination is appropriate:
kill -KILL 12345
Important: Confirm the correct PID before sending signals, especially on shared systems.
Ownership and Permissions
A regular user can generally signal processes they own.
Sending signals to processes owned by other users typically requires elevated privileges.
Key Lessons
Processes have identities, ownership, states, and resource consumption.
Signals are a communication mechanism between the operating system and processes.
Prefer graceful termination before forced termination.
Process inspection should come before process termination.
A process may restart automatically if managed by another service or supervisor.
6. Users, Groups and Permissions
Understanding Linux Ownership
Linux uses file ownership and permissions to control access to filesystem objects.
Each file and directory has:
Owner: The user account that owns the object.
Group: The group associated with the object.
Others: Users who are neither the owner nor members of the owning group.
Traditional Linux permission checks select the applicable category: owner, group, or others. These permission categories are not added together.
File Permissions vs Directory Permissions
The meaning of read (r), write (w), and execute (x) depends on whether the object is a file or directory.
Permission
Regular File
Directory
r
Read file contents
List directory entries
w
Modify file contents
Modify directory entries
x
Execute the file
Traverse or access entries by name
Important: Having permission to read a file does not automatically mean a user can access it. The user must also have traversal (x) permission on the directories in its path.
Numeric Permissions
Linux represents traditional permissions using octal values:
r = 4
w = 2
x = 1
Examples:
chmod 750 projects
chmod 640 report.txt
750 means the owner has rwx, the group has r-x, and others have no permissions.
640 means the owner has rw-, the group has r--, and others have no permissions.
Managing Ownership
sudo chown alice:analytics report.txt
sudo chgrp analytics report.txt
chown changes ownership.
chgrp changes group ownership.
chmod modifies permission bits.
Changing ownership and changing permissions are separate operations.
Engineering Scenario: Deleting a File Without Reading It
Consider:
drwxrwx---  alice analytics  reports/
-rw-------  alice analytics  reports/secret.txt
Assume bob belongs to analytics, is not the owner, and can traverse the parent directories.
Can bob read secret.txt?
No. The file grants read permission only to its owner, alice.
Can bob delete secret.txt?
Yes, under ordinary directory permission rules.
The directory grants members of analytics write and execute permissions.
Deleting a file removes its directory entry. It does not require read or write permission on the file itself.
This assumes no additional restrictions, such as sticky-bit rules, filesystem attributes, or access-control policies.
Directory Traversal Without Listing
A user with directory execute permission but no read permission may access an entry if its name is already known and the entry’s own permissions allow the operation.
However, without directory read permission, the user cannot normally list the directory’s contents.
This demonstrates why directory permissions and file permissions must be evaluated separately.
Practical Troubleshooting
When investigating a permission-denied error:
Identify the account performing the operation.
Check the owner, group, and permission bits.
Verify traversal permissions on every directory in the path.
Determine whether the operation requires file permissions, directory permissions, or both.
Consider additional restrictions such as ACLs, sticky bits, and filesystem attributes.
Key Lessons
File permissions and directory permissions control different operations.
Directory execute permission enables traversal.
Deleting a file generally depends on its parent directory permissions, not the file’s read permission.
File ownership does not automatically grant access through inaccessible parent directories.
Correct permissions require understanding the intended operation, not simply applying chmod recursively.
7. Engineering Lessons and Troubleshooting
A Systematic Troubleshooting Approach
Linux problems become easier to diagnose when the underlying behavior is understood rather than commands being memorized.
When something fails, I follow these principles:
Verify the current location: Check the working directory and confirm whether paths are absolute or relative.
Inspect before modifying: Examine files, ownership, permissions, or running processes before making changes.
Understand the operation: Determine whether the action requires reading file contents, modifying a file, traversing a directory, or changing directory entries.
Identify dependencies: Check whether symbolic links point to valid targets and whether parent directories permit access.
Use targeted changes: Avoid unnecessarily broad permission changes, destructive commands, and forced process termination.
Verify the result: Confirm that the operation achieved its intended outcome without affecting unrelated resources.
Important Engineering Takeaways
File ownership and directory access are separate concerns.
Relative paths depend on context, including the working directory or a symbolic link’s location.
A successful command does not guarantee that all intended changes were made.
Error messages are starting points for investigation, not reasons to immediately elevate privileges.
Understanding how Linux manages files, users, and processes helps build safer and more reliable workflows.
Final Reflection
Learning Linux has reinforced the importance of understanding how systems behave internally.
The objective is not to memorize every command but to develop the ability to investigate problems, reason about system behavior, and apply the appropriate solution.
