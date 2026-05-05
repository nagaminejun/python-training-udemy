# import unittest

import calculation

# release_name = 'lesson'

class TestCal(object):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) != 4

# class CalTest(unittest.TestCase):
#     def setUp(self):
#         print('set up')
#         self.cal = calculation.Cal()

#     def tearDown(self):
#         print('clean up')
#         del self.cal

#     # @unittest.skip('skip!!!!!!!!')
#     @unittest.skipIf(release_name=='lesson', 'skipIf de skip!!!!')
#     def test_add_num_and_double(self):
#         cal = calculation.Cal()
#         self.assertEqual(cal.add_num_and_double(1, 1), 4)

#     def test_add_num_and_double_raise(self):
#         cal = calculation.Cal()
#         with self.assertRaises(ValueError):
#             cal.add_num_and_double('1', '1')
        
# if __name__ == '__main__':
#     unittest.main()
