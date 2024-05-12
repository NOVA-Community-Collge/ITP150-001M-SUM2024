import os

def count_txt_files(folder):
    count = 0
    files = os.listdir(folder)
    for filename in files:
        file_path = os.path.join(folder, filename)
        # Base case
        if filename.endswith(".txt"):
            count += 1
        # Branching recursive calls
        elif os.path.isdir(file_path):
            subcount = count_txt_files(file_path)
            count += subcount
    
    return count

starting_folder = input("Enter a folder name: ")
final_count = count_txt_files(starting_folder)
print(final_count)