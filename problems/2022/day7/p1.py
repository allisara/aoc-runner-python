from inspect import currentframe
from msilib import _directories
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "95437"

folders: list[str] = ["/"]
files: dict[str, int] = {"/": 0}
dir_sizes: dict[str, int] = {}

current_path = "/"


def get_parsed_file(command: str):
    size, filename = command.split(" ")
    # print(size)
    # print(filename)
    size = int(size)
    parsed_file = (size, filename)

    # print(parsed_file)

    return parsed_file


def get_new_path(path: str, command: str) -> str:
    # Returns new file path as a string.
    # Command should not include "$ cd"

    # Go to root
    if command == "/":
        path = "/"

    # Go up one layer (..)
    elif command == "..":
        path = path[:path.rfind("/")]
        if path == "":
            path = "/"

    # Go down one layer
    else:
        if path == "/":
            path = ""
        path += "/" + command

    return path


# take in a file string and add it to files
def process_file(input: str, current_path: str):
    new_file = get_parsed_file(input)
    if current_path == "/":
        filepath = current_path + new_file[1]
    else:
        filepath = current_path + "/" + new_file[1]
    filesize = new_file[0]
    files[filepath] = filesize

    return


# take in the string that appears after "dir", add it to current_path,
# and add the new path to folders
def process_dir_line(new_folder: str, current_path: str):
    folders.append(get_new_path(current_path, new_folder))

    return


def run_command(input: str):
    global current_path

    if "$ ls" in input:
        return

    elif "$ cd" in input:
        command = input.split()[2]
        global current_path
        current_path = get_new_path(current_path, command)
        return

    elif "dir " in input:
        command = input.split()[1]
        process_dir_line(command, current_path)
        return

    else:
        process_file(input, current_path)
        return

    return


def p1() -> str:
    # Solve code here, return string to submit

    for line in dataset:
        run_command(line)

    # print(folders)
    # print(files)

    for folder in folders:
        dir_sizes[folder] = 0
        # print(dir_sizes)
        for name in files.keys():
            if name.startswith(folder):
                size_to_add: int = files[name]
                dir_sizes[folder] += size_to_add

    print(dir_sizes)

    answer = 0

    for value in dir_sizes.values():
        if value <= 100_000:
            answer += value

    # f = {"/": 0}
    # f["/"] = f.get("/", 0) + 1
    # f["path"] = f.get("path", 0) + 1
    # f["path"] = f.get("path", 0) + 1

    # print(get_parsed_file("123 test"))

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
