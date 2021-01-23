import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SPX:
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".navigation__desktop-item")
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card")
    CHOOSE_SIZE = (By.CSS_SELECTOR, ".mb-3.js-variant")
    ADD_TO_CART = (By.CSS_SELECTOR, ".js-add-to-cart")
    CART_PAGE = (By.CSS_SELECTOR, ".go-basket-btn")
    MAIN_PAGE = (By.CSS_SELECTOR, '.header__icon')
    website = "https://www.spx.com.tr"
    IS_ON_CAT_PAGE = (By.CSS_SELECTOR, ".pz-breadcrumb__link")
    IS_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".pz-tab__item.active.flex-column.mr-3")
    SIZE = (By.CSS_SELECTOR, ".mb-sm-3.mb-2")
    CART_BUTTON = (By.CSS_SELECTOR, ".js-add-to-cart")
    IS_ON_CART_PAGE = (By.CSS_SELECTOR, ".basket__complete")
    IS_ON_MAIN_PAGE = (By.CLASS_NAME, "hero-slider")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert "SPX - Sport Point Extreme" in self.driver.title
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[2].click()

        is_on_cat = self.wait.until(ec.presence_of_all_elements_located(self.IS_ON_CAT_PAGE))[1].text

        assert is_on_cat == "KADIN"
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[6].click()

        assert self.wait.until(ec.presence_of_element_located(self.IS_ON_PRODUCT_PAGE)).is_displayed()

        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[1].click()

        assert self.wait.until(ec.presence_of_element_located(self.SIZE)).is_displayed()

        assert self.wait.until(ec.presence_of_element_located(self.CART_BUTTON)).is_displayed()

        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()

        assert self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].text == "SEPETE EKLE", 'Sepete Gidilemedi'

        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).click()

        assert self.wait.until(ec.presence_of_all_elements_located(self.IS_ON_CART_PAGE))[0].text == "SEPETİ ONAYLA", 'Sepet sayfasında değilsin'

        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()

        assert self.wait.until(ec.presence_of_element_located(self.IS_ON_MAIN_PAGE)).is_displayed()

SPX().test_navigate()


