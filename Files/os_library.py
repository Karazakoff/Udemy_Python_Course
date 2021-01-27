import os
import shutil
import send2trash
print(os.getcwd())
print(os.listdir('/home/mercy/Desktop'))
# shutil.move('/home/mercy/Desktop/Python_Course/Udemy_Python_Course/text.txt', os.getcwd())
file_path = '/home/mercy/Desktop/Python_Course/Udemy_Python_Course/Complete-Python-3-Bootcamp/12-Advanced Python Modules/Example_Top_Level'
for folder, sub_folder, files in os.walk(file_path):
    print(f"You are currently in this Directory: {folder}")
    print()
    print("The sub_folders are: ")
    for sub_f in sub_folder:
        print(f'\t The Subfolder {sub_f}')
    print()
    print("the files")
    for f in files:
        print(f'\t File {f}')
# send2trash.send2trash('text.txt')
