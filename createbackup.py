import os
import io
import sys
from PIL import Image

def read_files_in_folder(folder_path):
    for item in os.listdir(folder_path):

        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):

            with open(item_path, "rb") as file:

                file_contents = file.read()
                with open("output.bin", 'ab') as outfile:
                    toWrite = b'p#:' + file.name.encode() + b'c#:' + file_contents + b'e#/\n'
                    outfile.write(toWrite)

        elif os.path.isdir(item_path):

            read_files_in_folder(item_path)

def save_chunks(folder):
    chunk_size = 512 * 1024 * 1024
    file_num = 1
    while True:
        chunk = buffer.read(chunk_size)
        if not chunk:
            break
        with open(f"{folder}output{file_num}.bin", "wb") as f:
            f.write(chunk)
        file_num += 1
        print(f"chunk {file_num}")

def save_files(folder):
    with open("output.bin", "rb") as file:
        file_contents = file.read()

    size_file = 536870912
    file_count = (len(file_contents) + size_file - 1) // size_file

    # Write the data to files
    for i in range(file_count):
        start = i * size_file
        end = start + size_file
        file_path = os.path.join(folder, f"output_{i}.bin")
        with open(file_path, "wb") as f:
            f.write(file_contents[start:end]) 
    
    os.remove("output.bin")
    


#output_folder = "backup\\"
#dir_path = "folder1\\"
args = sys.argv[1:]
buffer = io.BytesIO()

read_files_in_folder(args[0])
save_files(args[1])
print("Backup file created successfully!")
