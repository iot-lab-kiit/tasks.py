import inspect
import unittest

from io import StringIO
from unittest.mock import patch

import basic.strings as strings

class TestStrings(unittest.TestCase):
    def test_self_source(self):
        """
        Test printing out source code of own file
        """
        with patch('sys.stdout', new = StringIO()) as stdout:
            strings.self_source()
            self.assertEqual(inspect.getsource(strings), stdout.getvalue())
