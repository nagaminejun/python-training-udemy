import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('http://www.python.org')
        self.assertIn('Python', self.driver.title)
        # time.sleep(5)

        # self.driver.find_element_by_link_text('Downloads').click() # 古い書き方で動かない。

        self.driver.find_element(By.LINK_TEXT, 'Downloads').click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'widget-title')))
        # 2番目の要素（インデックスは1）を指定
        target_element = element[1]
        self.assertEqual('Active Python releases', target_element.text)

if __name__ == "__main__":
    unittest.main()
