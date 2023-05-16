# create a python test template using unittest
# The rename function is in src/rename.py
# the test file is in ./test.file.txt
# the rename function should use regex ex to rename the file based on the value of new_host_name
# example of new_host_name: new_host_name = 'cr12-pr32'
# file should be renamed to cr12-pr32.file.txt
# test.file.txt should be copied before each test
# test.file.txt should be deleted after each test

import unittest
import unittest
import os
import shutil
import glob

from ..rename import rename_files

template_file = './tests/test.txt'

class TestRename(unittest.TestCase):
    def test_rename(self):
        test_file ="./tests/test.copy.txt"
        # make a copy of test.file.txt

        shutil.copy(template_file, test_file)
        file_name = glob.glob(test_file)
        print(file_name)
        rename_files(file_name)
        # check if the file was renamed
        self.assertTrue(os.path.exists('./tests/213-east.txt'))
        # delete the renamed file
        os.remove('./tests/213-east.txt')

    def test_rename_globs(self):
        file_names = glob.glob("./tests/*.txt")
        copied_file_names = []
        # make a copy of test.file.txt
        for file_name in file_names:
            copy= file_name.replace('.txt', '.copy.txt')
            shutil.copy(file_name, copy)
            copied_file_names.append(copy)
        rename_files(copied_file_names)
        # check if the file was renamed
        self.assertTrue(os.path.exists('./tests/213-east.txt'))
        self.assertTrue(os.path.exists('./tests/test-1.txt'))
        self.assertTrue(os.path.exists('./tests/test-2.txt'))
        # delete the renamed file
        os.remove('./tests/213-east.txt')
        os.remove('./tests/test-1.txt')
        os.remove('./tests/test-2.txt')


if __name__ == '__main__':
    unittest.main()