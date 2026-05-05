# ---------------- FILE PATH ----------------
# Keep CS4.txt in same folder as this script
file_path = "CS4.txt"


# ---------------- TASK 1: BASIC FILE READING ----------------

# read()
with open(file_path, "r") as f:
    content = f.read()

# readline()
with open(file_path, "r") as f:
    first_line = f.readline()
    second_line = f.readline()

# readlines()
with open(file_path, "r") as f:
    lines = f.readlines()

# Total number of lines
print("Total lines:", len(lines))

# First 2 lines
print("\nFirst 2 lines:")
for line in lines[:2]:
    print(line.strip())

# Last 2 lines
print("\nLast 2 lines:")
for line in lines[-2:]:
    print(line.strip())


# ---------------- TASK 2: LOG CLASSIFICATION ----------------

log_counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for line in lines:
    if "INFO" in line:
        log_counts["INFO"] += 1
    if "WARNING" in line:
        log_counts["WARNING"] += 1
    if "ERROR" in line:
        log_counts["ERROR"] += 1

print("\nLog Counts:", log_counts)


# ---------------- TASK 3: WRITE FILTERED FILES ----------------

info_lines = []
warning_lines = []
error_lines = []

for line in lines:
    if "INFO" in line:
        info_lines.append(line)
    if "WARNING" in line:
        warning_lines.append(line)
    if "ERROR" in line:
        error_lines.append(line)

# Writing into files
with open("info_logs.txt", "w") as f:
    f.writelines(info_lines)

with open("warning_logs.txt", "w") as f:
    f.writelines(warning_lines)

with open("error_logs.txt", "w") as f:
    f.writelines(error_lines)

print("\nFiltered files created successfully.")


# ---------------- TASK 4: SEARCH FEATURE ----------------

keyword = input("\nEnter keyword to search (INFO/WARNING/ERROR): ")

search_results = []

print("\nMatching lines:")
for line in lines:
    if keyword in line:
        print(line.strip())
        search_results.append(line)

# Save results
with open("search_result.txt", "w") as f:
    f.writelines(search_results)


# ---------------- FILE POINTER (SEEK) OPERATIONS ----------------

with open(file_path, "r") as f:

    # Read first 50 characters
    print("\nFirst 50 characters:")
    print(f.read(50))

    # Move to beginning
    f.seek(0)
    print("\nAfter seek(0):")
    print(f.read(50))

    # Move to middle
    f.seek(len(content)//2)
    print("\nFrom middle:")
    print(f.read(50))

# Last 100 characters (FIXED METHOD)
print("\nLast 100 characters:")
print(content[-100:])