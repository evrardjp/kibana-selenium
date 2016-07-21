import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KibanaOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def test_login(self):
        self.driver.get("http://kibana:4345f83228a74062335ec75caa5bceacf597bd549662389b50b@204.232.187.36:8443/")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,".brand"))
            )
        finally:
            header = self.driver.find_element_by_css_selector('.brand').text
            self.assertIn("Event Dashboard", header)

    # def test_graph_exists(self):
    #     self.driver.get("http://kibana:4345f83228a74062335ec75caa5bceacf597bd549662389b50b@204.232.187.36:8443/")
    #     a = self.driver.find_element_by_class_name('kibana-container')
    #     b = a.find_element_by_class_name('kibana-row')
    #     c = b.find_element_by_class_name('row-control')
    #     d = c.find_element_by_class_name('panel-container')
    #     self.assertIn("OPENSTACK EVENTS", d.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
