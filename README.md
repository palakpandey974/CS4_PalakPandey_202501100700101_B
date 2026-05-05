# Log File Analyzer using Python

A simple Python project that performs log file analysis using file handling operations such as `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, and `seek()`.

Based on the case study requirements in 

---

# Features

* Read log file using different file methods
* Count INFO, WARNING, and ERROR logs
* Create separate filtered log files
* Search logs by keyword
* Demonstrate file pointer operations using `seek()`

---

# Problem Statement

Given a log file `CS4.txt`, perform the following tasks:

## Task 1: Basic File Reading

* Read the file using:

  * `read()`
  * `readline()`
  * `readlines()`
* Print:

  * Total number of lines
  * First 2 lines
  * Last 2 lines

## Task 2: Log Classification

Count the occurrences of:

* INFO
* WARNING
* ERROR

Store the result in a dictionary.

## Task 3: Write Filtered Files

Create:

* `info_logs.txt`
* `warning_logs.txt`
* `error_logs.txt`

Store corresponding logs in each file.

## Task 4: Search Feature

* Ask user for a keyword
* Print matching lines
* Save matching lines into `search_result.txt`

## Task 5: File Pointer Operations

Use `seek()` to:

* Move to beginning
* Move to middle
* Display specific file contents

---

# Approach

1. Open and read the file using different file methods.
2. Store all lines using `readlines()`.
3. Loop through lines to classify logs.
4. Save filtered logs into separate files.
5. Take user input for keyword search.
6. Use `seek()` to demonstrate file pointer movement.

---

# Project Structure

```text id="8oc5cp"
Log-File-Analyzer/
│
├── casestudy4.py
├── CS4.txt
├── info_logs.txt
├── warning_logs.txt
├── error_logs.txt
├── search_result.txt
└── README.md
```

---

# Sample Input File (CS4.txt)

```text id="dd6mv4"
2026-04-01 10:15:32 INFO User login success user_id=101
2026-04-01 10:17:45 ERROR Database connection failed
2026-04-01 10:20:10 WARNING Disk space running low
2026-04-01 10:25:30 INFO File uploaded successfully
2026-04-01 10:28:00 INFO User logout success
2026-04-01 10:30:55 ERROR Timeout while connecting to server
2026-04-01 10:32:11 INFO User logged in again
2026-04-01 10:40:00 WARNING CPU temperature high
2026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully
```

---

# Sample Output

```text id="6ck0zv"
Total lines: 10

First 2 lines:
2026-04-01 10:15:32 INFO User login success user_id=101
2026-04-01 10:17:45 ERROR Database connection failed

Last 2 lines:
2026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully

Log Counts: {'INFO': 5, 'WARNING': 2, 'ERROR': 3}

Filtered files created successfully.

Enter keyword to search (INFO/WARNING/ERROR): ERROR

Matching lines:
2026-04-01 10:17:45 ERROR Database connection failed
2026-04-01 10:30:55 ERROR Timeout while connecting to server
2026-04-01 10:45:50 ERROR Failed to write file

First 50 characters:
2026-04-01 10:15:32 INFO User login success user_i

After seek(0):
2026-04-01 10:15:32 INFO User login success user_i

From middle:
necting to server
2026-04-01 10:32:11 INFO User lo

Last 100 characters:
026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully
```

---

# Concepts Used

* File Handling in Python
* File Pointer Operations
* Dictionaries
* Lists
* Loops
* String Searching

---

# How to Run

```bash id="dk4m4p"
python casestudy4.py
```

Make sure `CS4.txt` is in the same folder as the Python file.

---

# Requirements

* Python 3.x

---

# Author

Palak Pandey
Engineering Student
