import time
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
        element = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,".brand"), "Event Dashboard")
            )
        header = self.driver.find_element_by_css_selector('.brand').text
        self.assertIn("Event Dashboard", header)

    def test_graph_exists(self):
        self.driver.get("http://kibana:4345f83228a74062335ec75caa5bceacf597bd549662389b50b@204.232.187.36:8443/")
        element = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,".brand"), "Event Dashboard")
            )
        a = self.driver.find_element_by_class_name('kibana-container')
        b = a.find_element_by_class_name('kibana-row')
        c = b.find_element_by_class_name('row-control')
        d = c.find_element_by_class_name('panel-container')
        self.assertIn("OPENSTACK EVENTS", d.text)

    def test_log_section_exists(self):
        self.driver.get("http://kibana:4345f83228a74062335ec75caa5bceacf597bd549662389b50b@204.232.187.36:8443/")
        element = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,".brand"), "Event Dashboard")
            )
        logs = self.driver.find_element_by_class_name("table-hover")
        self.assertIn("@timestamp host module logmessage", logs.text)

    def test_log_content_exists(self):
        self.driver.get("http://kibana:4345f83228a74062335ec75caa5bceacf597bd549662389b50b@204.232.187.36:8443/")
        element = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,".brand"), "Event Dashboard")
            )
        pointer = self.driver.find_element_by_css_selector('tr.pointer')
        pointer.click()
        table = self.driver.find_element_by_css_selector('table.table-details')
        tbody = table.find_element_by_css_selector('tbody')
        log = tbody.find_elements_by_tag_name('tr')

        for i, v in enumerate(log, start=1):
            if "message" in v.text:
                if "logmessage" in v.text:
                    pass
                else:
                    child = i
        css = "tr.ng-scope:nth-child({0}) > td:nth-child(3)".format(child)
        mess_content = tbody.find_element_by_css_selector(css).text
        self.assertNotNone(mess_content)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
