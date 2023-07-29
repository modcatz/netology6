import os

folder_name = "files_to_squash"

def create_summary(folder):
    file_sizes = {}
    files = os.listdir(folder)

    for file in files:
        with open(f"{folder}/{file}") as content:
            file_sizes[file] = len(content.readlines())

    file_sizes = sorted(file_sizes.items(), key=lambda x: x[1])

    with open("summary.txt", "w") as summary:
        for file, size in file_sizes:
            summary.write(file+"\n")
            summary.write(str(size)+"\n")
            with open(f"{folder}/{file}") as content:
                summary.write(content.read()+"\n")

create_summary(folder_name)