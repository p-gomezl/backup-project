import os
import io
import sys

def create_files_from_backup(file_path, output_folder):
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    lines = file_contents.split(b'e#/\n')

    for line in lines[:-1]:
        split_line = line.split(b'c#:')

        file_content = split_line[1]
        filename = split_line[0].split(b'\\')[-1]

        if (split_line[0][0:3] == b'p#:'):

            filepath = output_folder.encode() + split_line[0][3:].replace(filename, b'', -1)
            fullpath = filepath + filename

            if os.path.exists(filepath):
                pass
            else:
                os.makedirs(filepath)
                
            with open(fullpath, "wb") as f:
                f.write(file_content)
                #print(filename + b' created')
        else:
            print("error")
    os.remove(file_path)

def read_files(path):
    for item in os.listdir(path):

        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):

            with open(item_path, "rb") as file:
                file_contents = file.read()

                with open("temp_backup.bin", 'ab') as outfile:
                        outfile.write(file_contents)


#path = "backup\\"
#output_folder = "output_mult\\"
file_path = "temp_backup.bin"

args = sys.argv[1:]

read_files(args[0])
create_files_from_backup(file_path, args[1])
print("Files were restored successfully!")