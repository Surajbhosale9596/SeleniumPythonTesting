import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formsubmission(self,getData):
        log = self.getlogger()
        homePage=HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(),getData["gender"])

        homePage.submitForm().click()
        time.sleep(5)
        alertText = homePage.getSuccessMessage().text

        assert "Success" in alertText
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.getTestData("TestsCase2"))
    def getData(self,request):
        return request.param
