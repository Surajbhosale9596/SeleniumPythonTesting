from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver=driver
    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle=(By.XPATH,"//div[@class='card h-100']")
    cardfooter = (By.XPATH, "div/button")
    checkOutFirst=(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOutSecond = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardfooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOutSecond).click()
        confiemPage=ConfirmPage(self.driver)
        return ConfirmPage