import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_file_name, 'w') as my_zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        my_zip_file.write(file_path, arcname=arcname)
        elif compress_type == 'tar':
            with tarfile.open(compressed_file_name, 'w') as my_tar_file:
                my_tar_file.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == 'tgz':
            with tarfile.open(compressed_file_name, 'w:gz') as my_tgz_file:
                my_tgz_file.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            raise ValueError("Unsupported compression type")

        print(f"Compression successful. File saved as {compressed_file_name}")
    except Exception as e:
        print(f"Compression failed: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    
    if not os.path.exists(folder_path):
        print("Error: Folder not found.")
        return

    compress_types = ['zip', 'tar', 'tgz']
    print("Available compression types:")
    for i, compress_type in enumerate(compress_types, start=1):
        print(f"{i}. {compress_type}")

    try:
        choice = int(input("Select the desired compression type (1/2/3): "))
        if 1 <= choice <= len(compress_types):
            compress_type = compress_types[choice - 1]
            compress_folder(folder_path, compress_type)
        else:
            print("Invalid choice. Please select a valid compression type.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
