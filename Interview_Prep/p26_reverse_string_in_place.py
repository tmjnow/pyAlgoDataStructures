"""

Note: Python does not have immutable strings but we can get the "spirit" of the problem by converting it to a list and
       not using auxiliary space
"""
import unittest


def reverse_in_place(string):
    """

    :param string:
    :type string: str
    :return:
    """
    string = list(string)
    left_pointer = 0
    right_pointer = len(string) - 1
    while left_pointer < right_pointer:
        string[left_pointer], string[right_pointer] = \
            string[right_pointer], string[left_pointer]
        right_pointer -= 1
        left_pointer += 1
    return ''.join(string)


def alt_reverse_in_place(string):
    string = list(string)
    for i in range((len(string) // 2)):
        swap = string[i]
        end_index = len(string) - (i + 1)
        string[i] = string[end_index]
        string[end_index] = swap
    return ''.join(string)


class MyTestCases(unittest.TestCase):
    def test_reverse_in_place(self):
        test_string = 'abcdefg'
        self.assertEqual(reverse_in_place(test_string), 'gfedcba')
        test_string = 'Z'
        self.assertEqual(reverse_in_place(test_string), 'Z')
        test_string = 'ab'
        self.assertEqual(reverse_in_place(test_string), 'ba')
