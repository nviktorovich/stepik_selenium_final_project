from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:

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
    TEST_PASSWORD = 'StepByStep12'


class ProductPageLocators:

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_PRODUCT_TITLE = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasePageLocators:

    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LinksLocators:

    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"


class BasketPageLocators:

    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    BASKET_CONTAIN = (By.CSS_SELECTOR, 'div[id="content_inner"] p')
    EMPTY_BASKET_MSG = 'Your basket is empty.'
    ITEMS_TO_BY_NOW = (By.CSS_SELECTOR, 'row[class="row"] h2')