import pytest

import calculation

# release_name = 'lesson'
is_release = True

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
    
    def setup_method(self, method): # method 変数の中身 ＝ TestCal.test_add_num_and_double
        print('method→{}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method→{}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip!!!')
    @pytest.mark.skipif(is_release == False, reason='skip!!!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
            # cal.add_num_and_double(1, 1)

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
        
# if __name__ == '__main__':
#     unittest.main()
