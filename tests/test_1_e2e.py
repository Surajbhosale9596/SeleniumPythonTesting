import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log=self.getlogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItem()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()

        # i=-1
        # for card in cards:
        #     i=i+1
        #     cardText = card.text
        #     log.info(cardText)
        #     if cardText == "Blackberry":
        #         checkoutpage.getCardFooter()[i].click()

        for card in cards:
            productName = card.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresece("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is"+successText)

        assert "Success! Thank you!" in successText

        self.driver.close

        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        # cards=self.driver.find_element_by_css_selector(".card-title a")
        # i=-1
        # for card in cards:
        #     i=i+1
        #     cardtext=card.text
        #     print(cardtext)
        #     if cardtext=='Blackberry':
        #         self.driver.find_element_by_css_selector(".card-footer button")[i].click()
        #
        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        #
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        # self.driver.find_element_by_id("country").send_keys("ind")
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "India")))
        # self.driver.find_element_by_link_text("India").click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element_by_css_selector("input[type='submit']").click()
        # textmatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        #
        # assert "Success! Thank you!" in textmatch
