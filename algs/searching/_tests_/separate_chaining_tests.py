import unittest

from searching.separate_chaining import SeparateChainingST


class SeparateChainingTestCase(unittest.TestCase):

    def test_separate_chaining(self):
        # given
        st = SeparateChainingST()

        # expect
        self.assertEqual(0, st.size)
        st.insert('key_1', 'value_1')
        self.assertEqual(1, st.size)
        self.assertEqual('value_1', st.get('key_1'))
        st.insert('key_1', 'value_2')
        self.assertEqual(1, st.size)
        self.assertEqual('value_2', st.get('key_1'))
        st.insert('key_2', 'value_3')
        self.assertEqual(2, st.size)
        self.assertEqual('value_3', st.get('key_2'))
        st.delete('key_1')
        self.assertEqual(1, st.size)
        self.assertEqual(None, st.get('key_1'))
        st.delete('key_2')
        self.assertEqual(0, st.size)
        self.assertEqual(None, st.get('key_2'))
        st.delete('key_non_existing')
        self.assertEqual(0, st.size)


if __name__ == '__main__':
    unittest.main()
