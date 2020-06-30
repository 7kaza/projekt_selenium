#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import random
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

product = 'gnocchi bezglutenowe'
product1 = 'mix degustacyjny ravioli 5x100g'
email = 'kal@boz.pl'
invalid_email = 'malma.pl'
name_list = ['Ala', 'Adam', 'Grzegorz', 'Karol','Karolina']
lastname_list = ['Makota', 'Nowak', 'Maj', 'Sasin', 'Bolek']
phone = '549872'
password = 'haslo123'
incorect_password ='haslo1111'
street = 'Polna 12'
postcode= '50-511'
city = 'Iwiny'


class LFRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://lafileja.pl/')
        self.driver.implicitly_wait(3)

    def testRegistrationWrongPasswordConfirmation(self):

        #1.Szukaj
        driver = self.driver
        lupa = driver.find_element_by_xpath('//a[@class="btn-lupa"]')
        #Kliknij
        lupa.click()
        self.driver.implicitly_wait(10)

        #2.Szukaj produktu
        product_input=driver.find_element_by_xpath('//input[@name="search"][@class="search-input s-grid-3"]')
        product_input.send_keys(product)
        product_input.submit()
        self.driver.implicitly_wait(10)

        #3.Wybierz z listy
        select_product=driver.find_element_by_xpath("//span[text()='Gnocchi bezglutenowe 500 g']")
        select_product.click()

        #4.Dodaj do koszyka
        buy_btn=driver.find_element_by_xpath("//*[@id='box_productfull']/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[2]/button/span")
        buy_btn.click()

        #5.Zamowienie
        order_btn=driver.find_element_by_xpath("//a[text()='Złóż zamówienie']")
        order_btn.click()
        self.driver.implicitly_wait(10)
        order1_btn=driver.find_element_by_xpath("//span[text()='Zamawiam »']")
        order1_btn.click()

        #6. Rejestracja
        registration_btn=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Zarejestruj się']")))
        registration_btn.click()

        #7.Email
        email_input=driver.find_element_by_id('input_mail')
        email_input.send_keys(email)

        #8.Imie
        name_input=driver.find_element_by_id('input_name')
        name = random.choice(name_list)
        name_input.send_keys(name)

        #9.Nazwisko
        lastname_input=driver.find_element_by_id('input_surname')
        lastname = random.choice(lastname_list)
        lastname_input.send_keys(lastname)

        #10.Telefon
        phone_input=driver.find_element_by_id('input_phone')
        phone_input.send_keys(phone)

        #11.Haslo i sprawdzenie
        password_input=driver.find_element_by_id('input_pass1')
        password_input.send_keys(password)

        password1_input=driver.find_element_by_id('input_pass2')
        password1_input.send_keys(incorect_password)

        #12.Ulica i nr domu
        street_input=driver.find_element_by_id('input_other_address')
        street_input.send_keys(street)

        #13. Kod pocztowy
        postcode_input=driver.find_element_by_id('input_zip')
        postcode_input.send_keys(postcode)

        #14.Miasto
        city_input=driver.find_element_by_id('input_city')
        city_input.send_keys(city)

        #15.Regulamin
        element = driver.find_element_by_xpath('//*[@id="box_basketaddress"]/form/fieldset/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/label')
        element.click()

        #16.Podsumowanie
        buy = driver.find_element_by_xpath('//*[@id="box_basketaddress"]/form/fieldset/div/div[2]/button[1]/span')
        buy.click()

        #17. Sprawdzenie poprawnosci wystapienia komunikatu bledu
        def check_exists_by_xpath(xpath):
            try:
               webdriver.find_element_by_xpath('//li[text()="Wprowadzone hasła są różne"]')
            except NoSuchElementException:
               return False
            return True

    def testRegistrationInvalidEmail(self):
        #1.Szukaj
        driver = self.driver
        lupa = driver.find_element_by_xpath('//a[@class="btn-lupa"]')
        #Kliknij
        lupa.click()
        self.driver.implicitly_wait(10)

        #2.Szukaj produktu
        product_input1=driver.find_element_by_xpath('//input[@name="search"][@class="search-input s-grid-3"]')
        product_input1.send_keys(product1)
        product_input1.submit()
        self.driver.implicitly_wait(10)

        #3.Wybierz z listy
        select_product1=driver.find_element_by_xpath("//span[text()='Mix degustacyjny ravioli 5x100g']")
        select_product1.click()

        #4.Dodaj do koszyka
        buy_btn=driver.find_element_by_xpath('//*[@id="box_productfull"]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[2]/button/span')
        buy_btn.click()

        #5.Zamowienie
        order_btn=driver.find_element_by_xpath("//a[text()='Złóż zamówienie']")
        order_btn.click()
        self.driver.implicitly_wait(10)
        order1_btn=driver.find_element_by_xpath("//span[text()='Zamawiam »']")
        order1_btn.click()

        #6. Rejestracja
        registration_btn=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Zarejestruj się']")))
        registration_btn.click()

        #7.Email
        email_input=driver.find_element_by_id('input_mail')
        email_input.send_keys(invalid_email)

        #8.Imie
        name_input=driver.find_element_by_id('input_name')
        name = random.choice(name_list)
        name_input.send_keys(name)

        #9.Nazwisko
        lastname_input=driver.find_element_by_id('input_surname')
        lastname = random.choice(lastname_list)
        lastname_input.send_keys(lastname)

        #10.Telefon
        phone_input=driver.find_element_by_id('input_phone')
        phone_input.send_keys(phone)

        #11.Haslo i sprawdzenie
        password_input=driver.find_element_by_id('input_pass1')
        password_input.send_keys(password)

        password1_input=driver.find_element_by_id('input_pass2')
        password1_input.send_keys(password)

        #12.Ulica i nr domu
        street_input=driver.find_element_by_id('input_other_address')
        street_input.send_keys(street)

        #13. Kod pocztowy
        postcode_input=driver.find_element_by_id('input_zip')
        postcode_input.send_keys(postcode)

        #14.Miasto
        city_input=driver.find_element_by_id('input_city')
        city_input.send_keys(city)

        #15.Regulamin
        element = driver.find_element_by_xpath('//*[@id="box_basketaddress"]/form/fieldset/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/label')
        element.click()

        #16.Podsumowanie
        buy = driver.find_element_by_xpath('//*[@id="box_basketaddress"]/form/fieldset/div/div[2]/button[1]/span')
        buy.click()

        #17. Sprawdzenie poprawnosci wystapienia komunikatu bledu
        def check_exists_by_xpath1(xpath):
            try:
               webdriver.find_element_by_xpath('Nieprawidłowy format adresu e-mail"]')
            except NoSuchElementException:
               return False
            return True

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main(verbosity=2)
