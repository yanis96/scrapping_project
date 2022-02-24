import time
import unittest
from scrap import *

class Test_scrap(unittest.TestCase):

    def setUp(self):
        self.driver = Scrap('C:\\ChromeDriver\\chromedriver.exe')
        self.url = "https://www.thomann.de/fr/index.html"
        self.xpath_cookie = '/html/body/div[1]/div/div/div/div[2]/div[2]/button[1]'
        self.xpath_element = '/html/body/div[3]/div/div[1]/div[1]/div[2]/div/div/ul/div/li[1]'
        self.xpath_element_to_scroll = '//*[@id="topseller"]/div/div[2]/div/div[2]/a'
        time.sleep(1)

    def tearDown(self):
        self.driver.close_browser()

    def test_go_to_website(self):
        self.driver.go_to_web_site(self.url)

    def test_close_cookie(self):
        self.driver.go_to_web_site(self.url)
        time.sleep(2)
        self.driver.close_cookie(self.xpath_cookie)
        time.sleep(2)

    def test_click_element(self):
        self.driver.go_to_web_site(self.url)
        time.sleep(2)
        self.driver.close_cookie(self.xpath_cookie)
        time.sleep(2)
        self.driver.click_element(self.xpath_element)
        time.sleep(2)

    def test_scroll_to_element(self):
        self.driver.go_to_web_site(self.url)
        time.sleep(2)
        self.driver.close_cookie(self.xpath_cookie)
        time.sleep(2)
        self.driver.click_element(self.xpath_element)
        time.sleep(2)
        self.driver.scroll_to_element(self.xpath_element_to_scroll)
        time.sleep(2)
