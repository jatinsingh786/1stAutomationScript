import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

path = '/home/jatin/Downloads/chromedriver'

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()


    def test_tabc(self):

        driver = self.driver
        driver.get('https://www.toolsqa.com/automation-practice-form/')


        a = driver.find_element_by_css_selector('div.wpb_wrapper > h1').text
        self.assertEqual(a,'Practice Automation Form')
        time.sleep(1)

        driver.find_element_by_partial_link_text('Partial').click()
        time.sleep(1)

        driver.find_element_by_link_text('Link Test')
        time.sleep(1)

        driver.find_element_by_name('firstname').send_keys('Krishna')


       #send keys to last name
        driver.find_element_by_name('lastname').send_keys('kriti')
        time.sleep(1)


        #select sex as male
        driver.find_element_by_id('sex-1').click()
        time.sleep(1)

        #select years of experience as 5
        driver.find_element_by_id('exp-4').click()
        time.sleep(1)


        #send date as 12/12/12
        driver.find_element_by_css_selector('#datepicker').send_keys('12/12/12')
        time.sleep(1)

        driver.find_element_by_class_name('checkbox').click()
        time.sleep(1)

        driver.find_element_by_id('photo').send_keys('/home/jatin/Downloads/selenium-server-standalone-3.141.59.jar')
        time.sleep(1)

        driver.find_element_by_link_text('Test File to Download').click()
        time.sleep(3)

        driver.find_element_by_id('tool-2').click()
        time.sleep(2)

        select = Select(driver.find_element_by_xpath('//*[@id="continents"]'))
        select.select_by_visible_text('Antartica')
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="selenium_commands"]').send_keys('Wait Commands')
        time.sleep(3)

        driver.find_element_by_id('submit').click()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()