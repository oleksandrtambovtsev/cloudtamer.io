import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.phptravels.net/home")

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        driver: WebDriver = self.driver

    # TEST CASE #1:

        # Select hotel:
        driver.find_element_by_css_selector(".select2-choice").click()
        time.sleep(2)
        hotel_select = driver.find_element_by_css_selector(".select2-choice")
        time.sleep(2)
        hotel_select.send_keys("Alzer Hotel Istanbul")
        time.sleep(2)
        hotel_select.send_keys(Keys.ENTER)

        # Click to open drop down to select Check in:
        driver.find_element_by_css_selector(".col-6.o2").click()
        time.sleep(2)

        # Select current date:
        driver.find_element_by_css_selector(".datepicker--cell.-current-").click()
        time.sleep(2)

        # Select Check out date:
        driver.find_element_by_xpath("//body/div[@id='datepickers-container']/div[2]/div[1]/div[1]/div[2]/div[28]").click()
        time.sleep(2)

        # Select children:
        driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/button[1]").click()
        driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/button[1]").click()
        time.sleep(4)

        # Click on 'Search' button
        driver.find_element_by_xpath("//div[@class='col-lg-2 col-sm-12 col-xs-12']/button[@class='btn btn-primary btn-block']").click()
        time.sleep(4)

    # TEST CASE #2
        print("TEST CASE #2")
        self.driver.get("https://www.phptravels.net/home")
        # Select the 'Flights' tab:
        driver.find_element_by_css_selector(".text-center.flights").click()
        time.sleep(2)

        # Check if the 'One Way' radio button is checked by default:
        radio_button = driver.find_element_by_xpath("//input[@id='flightSearchRadio-2']")
        self.assertTrue(radio_button.is_selected())
        print("'One Way' radio button is checked by default")

        # Check if the correct labels exist - 'From', 'To', 'Depart', 'Adults', 'Child', and 'Infant':

        if driver.find_element_by_xpath("//label[text()='From']"):
            print("'From' ...exists")

        if driver.find_element_by_xpath("//label[text()='To']"):
            print("'To' ...exists")

        if driver.find_element_by_xpath("//label[text()='Depart']"):
            print("'Depart' ...exists")

        if driver.find_element_by_xpath("//label[text()='Adults ']"):
            print("'Adults' ...exists")

        if driver.find_element_by_xpath("//label[text()='Child ']"):
            print("'Child' ...exists")

        if driver.find_element_by_xpath("//label[text()='infant ']"):
            print("'infant' ...exists")

        # Clicking the 'Economy' dropdown:
        driver.find_element_by_xpath("//span[contains(text(), 'Economy')]").click()
        time.sleep(2)

        # Selecting First class:
        driver.find_element_by_xpath("//li[contains(text(),'First')]").click()
        time.sleep(2)

    # TEST CASE #3:
        print("TEST CASE #3")
        self.driver.get("https://www.phptravels.net/home")
        # Select the 'Flights' tab:
        driver.find_element_by_css_selector(".text-center.flights").click()

        # Click 'Round Trip' button":
        driver.find_element_by_xpath("//label[contains(text(),'Round Trip')]").click()
        time.sleep(2)

        # Check if 'Return date' field exist:
        elem = driver.find_elements_by_xpath("//div[@class='hidediv col-6'][@style='display: block;']")
        if len(elem) > 0:
            print("Round Trip: 'Return date' field  ...exists")
        else:
            print("Round Trip: 'Return date' field  ...doesn't exist")

        # Click 'One Way' button":
        driver.find_element_by_xpath("//label[contains(text(),'One Way')]").click()
        time.sleep(2)

        # Check if 'Return date' field exist:
        elem = driver.find_elements_by_xpath("//div[@class='hidediv col-6'][@style='display: block;']")
        if len(elem) > 0:
            print("One Way: 'Return date' field  ...exists")
        else:
            print("One Way: 'Return date' field  ...doesn't exist")

    # TEST CASE #4
        print("TEST CASE #4")
        # 'for' loop that clicks on each of the following tabs (Hotels, Flights, Boats, Rentals, Tours, and Cars)
        name = [".text-center.hotels", ".text-center.flights", ".text-center.boats", ".text-center.rentals", ".text-center.tours", ".text-center.cars"]
        for x in name:
            self.driver.find_element_by_css_selector(x).click()
            time.sleep(2)
        # validate that the SEARCH button appears after clicking the tab
            search = driver.find_elements_by_xpath("//button[contains(text(),'Search')]")
            if search:
                print(x + " button is present")
            else:
                print(x + " button is not present")

if __name__ == '__main__':
    unittest.main()
