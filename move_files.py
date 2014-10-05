import os, shutil, string




def make_folders_from_list(parent_folder, your_list):
    for item in your_list:
        os.mkdir(parent_folder + item)

def move_files(original_files, parent_folder, your_list):
    os.chdir(original_files) 

    source = os.listdir(original_files)

    for each_file in source:
        first_letter = each_file[0]
        shutil.copy(each_file, parent_folder + first_letter)


def main():
    alphabet = string.lowercase

    alpha_list = []

    for letter in alphabet:
        alpha_list.append(letter)

    original_files = "/Users/greglaughlin/Desktop/Hackbright/Week 1 Project/original_files"
    parent_folder = "/Users/greglaughlin/Desktop/Hackbright/Week 1 Project/organized_files/"

    make_folders_from_list(parent_folder, alpha_list)
    move_files(original_files, parent_folder, alpha_list)

main()

