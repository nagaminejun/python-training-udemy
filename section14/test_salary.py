import unittest
from unittest.mock import MagicMock
from unittest import mock
import salary


class TestSalary(unittest.TestCase):

    def setUp(self):
        """テストメソッドが実行されるたびに、事前に呼ばれる準備コード"""
        # 1. パッチを当てる場所を予約
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        # 2. パッチを開始し、生成されたMockを self に保存してどこからでも使えるようにする
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        # ここで salary.py 内の requests.get が走り、ConnectionError になる
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        # s.calculation_salary()
        # s.calculation_salary()
        self.assertEqual(s.calculation_salary(), 101)
        # mock.assert
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        print('呼び出し：', s.bonus_api.bonus_price.call_count)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        # ここで salary.py 内の requests.get が走り、ConnectionError になる
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        # 以下は、20250年だとこの関数が呼ばれないことを期待する関数
        s.bonus_api.bonus_price.assert_not_called()

    # @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    # def test_calculation_salary_patch(self, mock_bonus):
    #     s = salary.Salary(year=2017)
    #     print(mock_bonus)
    #     # s.bonus_api.bonus_price = MagicMock(return_value=1)
    #     self.assertEqual(s.calculation_salary(), 101)
    #     # s.bonus_api.bonus_price.assert_not_called()
    #     mock_bonus.assert_called()

    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        print(mock_bonus)
        print(mock_bonus.name)

        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        # s.bonus_api.bonus_price.assert_not_called()
        mock_bonus.assert_called()

    def test_calculation_salary_patch_side_effect(self):
        # def f(year):
        #     return year * 2

        self.mock_bonus.side_effect = [
            1,
            2,
            3,
            ValueError('Bankrupt!!!')
        ]

        # 1回目
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)

        # 2回目
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)

        # 3回目
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)

        # 4回目
        s = salary.Salary(year=2017)
        with self.assertRaises(ValueError):
            print('テストが実行されたかチェック')
            s.calculation_salary()
            print('テストが実行されたかチェック２')

    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    def test_calculation_salary_patch_class(self, MockRest):

        # mock_rest = MockRest.return_value
        mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        # s.bonus_api.bonus_price.assert_not_called()
        mock_rest.bonus_price.assert_called()
