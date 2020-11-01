from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Spammer:
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(15)
        self.driver.get("https://web.whatsapp.com/")

    def find_contact(self):
        name = input("Enter the contact name: ")

        try:
            element = self.driver.find_element_by_css_selector(
                "span[title='{}']".format(name)
            )
            element.click()
        except NoSuchElementException:
            print("No user found with that name.")

    def send_msg(self):
        textbox = self.driver.find_element_by_xpath(
            "//*[@id=\"main\"]/footer/div[1]/div[2]/div/div[2]"
        )

        message = input("What message should I spam?\n")
        amt = int(input("How many messages should I send?\n"))

        for i in range(amt):
            textbox.send_keys(message)

            send_button = self.driver.find_element_by_xpath(
                "//*[@id=\"main\"]/footer/div[1]/div[3]/button/span"
            )
            send_button.click()

            print("Sent {}.".format(i))
            sleep(0.5)


# Initialize spammer class
module = Spammer()

# Find the spam victim
module.find_contact()

# Send messages
module.send_msg()

# Quit the selenium driver
module.driver.quit()
