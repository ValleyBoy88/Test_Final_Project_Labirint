import time
from config.config import TestData
from pages.BasketPage import BasketPage
from tests.test_base import BaseTest


class TestBasketFromHomePage(BaseTest):

    # Находим первую книгу на главной странице, получаем цену, кладем в корзину и сверяем цену в корзине
    def test_first_book_moved_into_the_basket_and_price_is_the_same(self, fist_book_button_move_into_basket=None):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_goods_in_basket_and_reload_page()
        # Находим все кнопки "В КОРЗИНУ" 
        self.list_of_buttons_move_into_the_basket = self.basketPage.find_several_elements(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # Находим кнопку "В КОРЗИНУ" первой книги
        fist_book_button_move_into_the_basket = self.list_of_buttons_move_into_the_basket[0]
        # Находим все цены книг
        self.list_of_books_prices = self.basketPage.find_several_elements(BasketPage.PRICE_OF_THE_BOOK)
        # Находим цену первой книги
        first_book_price_element = self.list_of_book_prices[0]
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # Нажимаем кнопку "В КОРЗИНУ" на первой книге
        fist_book_button_move_into_basket.click()
        # Закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # Нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # Находим все цены всех книг в Корзине на странице Корзина
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # Находим цену первой книги в корзине на странице Корзина
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        assert first_book_price == first_book_price_in_basket

    # Проверяем, что кнопка "Очистить корзину" отображается
    def test_that_clear_basket_button_clean_basket(self):
        self.basketPage = BasketPage(self.driver)
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим и добавляем в корзину первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # Нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # Находим все цены всех книг в Корзине на странице Корзина
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # Находим цену первой книги в корзине на странице Корзина
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        self.basketPage.do_click(BasketPage.CLEAN_THE_BASCET)
        result = self.basketPage.get_element_text(BasketPage.BASKET_IS_EMPTY)
        assert self.basketPage.element_is_not_visible(price_of_first_book_string)
        assert result.lower() == TestData.MESSAGE_OF_THE_EMPTY_BASKET.lower()

    # Находим первую книгу на главной странице, получаем цену, кладем в корзину и сверяем цену в корзине с финальной
    # суммой заказа "Подытог без учета доставки"
    def test_first_book_moved_into_basket_and_price_is_the_same_and_equal_to_final_sum(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим кнопку "В КОРЗИНУ" первой книги на главной странице
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # находим все цены всех книг
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # находим цену первой книги на главной странице
        first_book_price_element = self.list_of_book_prices[0]
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # нажимаем кнопку "В КОРЗИНУ" первой книги
        fist_book_button_move_into_basket.click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все цены всех книг в корзине на странице Корзина
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # находим цену первой книги на странице Корзина
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # получаем финальную сумму
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price and first_book_price_in_basket) == int(final_sum)

    def test_that_button_in_popup_window_leads_to_basket(self):
        self.basketPage = BasketPage(self.driver)
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим кнопку "В КОРЗИНУ" первой книги на главной странице
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # нажимаем кнопку "В КОРЗИНУ" первой книги
        fist_book_button_move_into_basket.click()
        # нажимаем кнопку "Оформить" в попап меню
        self.basketPage.find_several_element(BasketPage.POPUP_CHECKOUT_BUTTON)[0].click()
        assert self.basketPage.get_current_url() == BasketPage.BASKET_URL

    # Проверяем соответствие количества положенной книги "В КОРЗИНУ"
    def test_that_initial_quantity_of_item_added_in_basket_is_one(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим кнопку "В КОРЗИНУ" первой книги на главной странице и нажимаем
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все поля ввода всех книг
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_THE_BASKET)
        # находим поле ввода последней добавленной нами книги
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # находим количество последней добавленной нами книги
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1

    # Проверяем, что количество добавленной в корзину книги увеличивается при нажатии на кнопку button "+"
    def test_that_quantity_of_item_added_in_basket_can_be_increased(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим и добавляем "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" на главной странице
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все поля ввода количества
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_THE_BASKET)
        # находим поле ввода последней добавленной нами книги
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # находим количество последней добавленной нами книги
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # находим все кнопки "+" 
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.INCREASE_THE_QUANTITY_OF_ITEM)
        # увеличиваем количество последней добавленной нами книги, нажав на кнопку "+"
        self.list_of_increase_buttons[0].click()
        # получаем количество последней добавленной нами книги
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(new_quantity_of_first_book) - int(quantity_of_first_book) == 1

    # Проверяем, что количество добавленной "В КОРЗИНУ" книги изменяется с введением числа в поле ввода
    def test_that_quantity_can_be_set_by_enter_digits_into_input_field(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим и добавляем "В КОРРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все поля ввода количества
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_THE_BASKET)
        # находим поле ввода последней добавленной нами книги
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # находим количество последней добавленной нами книги
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # вводим количество
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # получаем количество последней добавленной нами книги
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1
        assert int(new_quantity_of_first_book) == int(BasketPage.QUANTITY_TO_ENTER)

    # Проверяем, что количество добавленной "В КОРЗИНУ" книги уменьшится при нажатии на кнопку "-"
    def test_that_quantity_can_decreased_by_pressing_decrease_button(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим и добавляем "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все поля ввода количества
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_THE_BASKET)
        # находим количество последней добавленной нами книги
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # вводим количество
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # получаем количество последней добавленной нами книги
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # находим все кнопки "-" 
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.DECREASE_THE_QUANTITY_OF_ITEM)
        # уменьшаем количество последней добавленной нами книги, нажав на кнопку "-"
        self.list_of_increase_buttons[0].click()
        # получаем количество последней добавленной нами книги
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) - int(new_quantity_of_first_book) == 1

    def test_that_sum_will_raise_accordingly_to_quantity_of_the_increased_item(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим и добавляем "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все поля ввода количества
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_THE_BASKET)
        # находим все цены всех книг на странице Корзина
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # находим цену первой книги на странице Корзина
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # находим поле ввода последней добавленной нами книги
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # вводим количество в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        time.sleep(5)
        # находим все цены всех книг в корзине на странице  Корзина
        self.list_of_book_prices_in_basket_new = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # находим цену первой книги на странице Корзина
        price_of_first_item = self.list_of_book_prices_in_basket_new[0]
        new_price = self.basketPage.price_by_int(price_of_first_item)
        assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER)) == new_price

    # Проверяем, что финальная сумма "Подытог без учета доставки" меняется при изменении количества
    def test_that_final_sum_will_raise_accordingly_whit_increased_quantity(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # добавляем 2 книги в Корзину
        for book in self.list_of_buttons_move_into_basket[0:2]:
            book.click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # находим все поля ввода количества
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_THE_BASKET)
        # находим все цены всех книг в корзине на странице "Корзина"
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.PRICE_OF_THE_BOOK)
        # находим цену первой книги на странице Корзина
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # находим цену второй книги на странице Корзина
        price_of_second_book_string = self.list_of_book_prices_in_basket[1]
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        second_book_price_in_basket = self.basketPage.price_by_int(price_of_second_book_string)
        # находим поле ввода последней добавленной нами книги
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        time.sleep(5)
        # получаем финальную сумму
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER) + second_book_price_in_basket) == int(
            final_sum)

    # Проверяем, что кнопка "Оформить" отображается
    def test_that_start_checkout_button_open_checkout_page(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # находим все кнопки "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(
            BasketPage.PUT_THE_BOOK_INTO_BASKET)
        # находим кнопку "В КОРЗИНУ" первой книги и нажимаем
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем попап
        self.basketPage.do_click(TestData.CLOSE_THE_POPUP)
        # нажимаем кнопку "Корзина" в хэдере
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_THE_HEADER)
        # нажимаем кнопку "Начать оформление"
        self.basketPage.do_click(BasketPage.CHECKOUT_BUTTON)
        # ждем, пока появится кнопка
        self.basketPage.is_visible(BasketPage.CHECKOUT_AND_PAY)
        current_url = self.basketPage.get_current_url()
        assert current_url == BasketPage.BASKET_URL + "checkout/"
