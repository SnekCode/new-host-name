import os
import re
import glob
import sys
import argparse

def rename_files(files_glob):
    print(files_glob)
    for file_path in files_glob:
        with open(file_path, 'r') as file:
            content = file.read()
            match = re.search(r'new_host_name\s*=\s*"([^"]+)"', content)
            if match:
                _, *extensions = os.path.splitext(file_path)
                new_name = match.group(1)
                new_path = os.path.join(os.path.dirname(file_path), new_name) + ''.join(extensions)
                print(new_path)
                print(extensions)
                os.rename(file_path, new_path)
                print(f"Renamed file: {file_path} to {new_path}")



if __name__ == '__main__':
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description='Rename files based on new_host_name value.')
    parser.add_argument('file_glob', help='Glob pattern for files')
    file_glob = sys.argv[1:]

    if sys.platform == 'win32':
        file_glob = glob.glob(file_glob[0])

    # Call the rename_files function with the provided glob pattern
    rename_files(file_glob)