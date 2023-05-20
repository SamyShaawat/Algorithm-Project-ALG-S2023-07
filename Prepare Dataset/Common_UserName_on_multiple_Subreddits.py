import os
import csv

def search_files_for_common_usernames(path_to_files, output_file):
    usernames = []
    for filename in os.listdir(path_to_files):
        if filename.endswith(".txt"):
            with open(os.path.join(path_to_files, filename), "r") as file:
                for line in file:
                    username = line.strip()
                    if username not in usernames:
                        usernames.append(username)

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Files"])
        for username in usernames:
            row = [username]
            for filename in os.listdir(path_to_files):
                if filename.endswith(".txt"):
                    with open(os.path.join(path_to_files, filename), "r") as file:
                        if username in file.read():
                            row.append(filename)
            writer.writerow(row)

    print(f"Usernames found. Output written to {output_file}.")

path_to_files = "../project/subreddits"
output_file = "../project/dataset.csv"
search_files_for_common_usernames(path_to_files, output_file)