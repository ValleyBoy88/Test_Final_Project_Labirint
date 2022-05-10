from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage


class BasketPage(BasePage):
    REMOVE_ALL_GOODS_IN_BASKET = None
    BASKET_URL = "https://www.labirint.ru/cart/"

    QUANTITY_TO_ENTER = "10"

    # Локатор для лого "Лабиринт", который возвращает на домашнюю страницу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # Локатор для кнопки "В КОРЗИНУ" под каждой книгой
    PUT_THE_BOOK_INTO_BASKET = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), "В КОРЗИНУ")]')
    # Локатор цены
    PRICE_OF_THE_BOOK = (By.XPATH, '//span[@class="price-val"]')
    # Локатор финальной суммы на странице Корзина
    PURCHASE_FINAL_SUM = (By.ID, "basket-default-sumprice-discount")
    # Локатор кнопки "Очистить корзину"
    CLEAN_THE_BASCET = (By.XPATH, '//a[@class="b-link-popup" and contains(text(), "Очистить корзину")]')
    # Локатор сообщения "Ваша корзина пуста. Почему?"
    BASKET_IS_EMPTY = (By.XPATH, '//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and contains(text(), '
                                 '"Ваша корзина пуста. Почему?")]')
    # Локатор попап сообщения кнопки "Оформить"
    POPUP_CHECKOUT_BUTTON = (By.XPATH, '//a[@class="color_white btn btn-small btn-primary basket-go '
                                       'analytics-click-js"]')
    # Локатор ввода количества
    QUANTITY_OF_EACH_ITEM_IN_THE_BASKET = (By.XPATH, '//input[@class="quantity"]')
    # Локатор кнопки увеличения количества товаров в Корзине
    INCREASE_THE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-increase btn-increase-cart"]')
    # Локатор кнопки уменьшения количества товаров в Корзине
    DECREASE_THE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-lessen btn-lessen-cart"]')
    # Локатор кнопки "Начать оформление"
    CHECKOUT_BUTTON = (By.XPATH, '//input[@class="btn btn-small btn-more"]')
    # Локатор кнопки "Оформить и оплатить"
    CHECKOUT_AND_PAY = (By.XPATH, '//input[@value="Оформить и оплатить"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Получаем цену книги"""

    @staticmethod
    def price_by_int(element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)

    """Удаляем все товары из Корзины и возвращаемся на домашнюю страницу"""

    def remove_all_good_in_basket_and_reload_page(self):
        quantity = self.get_element_text(TestData.BASKET_COUNTER)
        if int(quantity) != 0:
            self.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
            self.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
            self.do_click(BasketPage.LABIRINT_MAIN_LOGO)

    def remove_all_goods_in_basket_and_reload_page(self):
        pass

    def find_several_elements(self, PUT_THE_BOOK_INTO_BASKET):
        pass
