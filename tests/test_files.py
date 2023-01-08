import os
from unittest import TestCase

from python_utils import files


class Test(TestCase):
    def test_file_to_utf8(self):
        test_dir = "../logs/"
        change_file = files.file_to_utf8(test_dir)
        change_path = os.path.join("../logs/", change_file)

        self.assertEqual('utf-8', files.get_encoding_type(change_path))
