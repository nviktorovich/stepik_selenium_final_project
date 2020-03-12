from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_AND_REGISTRATION_FORM_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # for check an already registred user
    CURRENT_EMAIL_ADDRESS = (By.ID, "id_login-username")
    CURRENT_PASSWORD = (By.ID, "id_login-password")
    ENTER_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    # for check fields for registration of new user
    REGISTRATION_EMAIL_ADDRESS = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")