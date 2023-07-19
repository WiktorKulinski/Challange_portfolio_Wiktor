import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scouts Panel'
    add_a_player_button_xpath = "//div[2]/div/div/a/button/span[1]"
    english_language_listbox_xpath = "//div[2]/div/div"
    polski_option_xpath = "//div[3]/ul/li[1]"
    invalid_data_text_xpath = "// div[3] / span"
    expected_invalid_data_text = "Identifier or password invalid."

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, pasword):
        self.field_send_keys(self.password_field_xpath, pasword)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_page_title(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def click_english_language_listbox(self):
        self.click_on_the_element(self.english_language_listbox_xpath)

    def click_polski_language_option(self):
        self.click_on_the_element(self.polski_option_xpath)

    def invalid_data(self):
        self.assert_element_text(self.driver, self.invalid_data_text_xpath, self.expected_invalid_data_text)


