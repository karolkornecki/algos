import unittest

from parameterized import parameterized

from regular_expression.nfa import NFA


class NFATestCase(unittest.TestCase):

    @parameterized.expand([
        ("AABD", True),
        ("AAAAAABD", True),
        ("ABD", True),
        ("ABBD", True),
        ("ACD", True),
        ("AACD", False),
        ("AAAC", False),
    ])
    def test_nfa(self, text, result):
        # given
        regexp = "((A*B|AC)D)"
        # when
        nfa = NFA(regexp)
        # then
        self.assertEqual(result, nfa.recognizes(text))
