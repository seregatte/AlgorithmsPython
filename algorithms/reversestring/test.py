#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import reversestring.index as index

class LearningCase(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(index.reverseString("abcd"), "dcba")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
