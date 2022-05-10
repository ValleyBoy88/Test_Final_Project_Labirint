import pytest
from config.config import TestData
from pages.PostponePage import PostponePage
from tests.test_base import BaseTest


class TestPostponeAtHomePage(BaseTest):

    # Находим первую книгу на домашней странице и нажимаем кнопку "Отложить"
    def test_first_book_postponed(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.accept_cookies_policy()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        assert first_book.is_enabled()

    # Проверяем, что появляется попап при нажатии на кнопку "Отложить"
    def test_popup_book_postponed_appeared(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        popup_postponed = self.postponePage.find_one_element(PostponePage.POPUP_BOOK_POSTPONED)
        self.postponePage.scroll_to_element(popup_postponed)
        assert self.postponePage.is_visible(PostponePage.POPUP_BOOK_POSTPONED)

    # Проверяем, что попап исчезает при нажатии на кнопку "Закрыть"
    def test_popup_book_postponed_closed(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        popup_postponed = self.postponePage.find_one_element(PostponePage.POPUP_BOOK_POSTPONED)
        self.postponePage.scroll_to_element(popup_postponed)
        assert self.postponePage.is_visible(PostponePage.POPUP_BOOK_POSTPONED)
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        assert self.postponePage.is_not_visible(PostponePage.POPUP_BOOK_POSTPONED)

    # Находим первую книгу на домашней странице, кликаем "Отложить" и сверяем количество отложенных книг в хэдере
    def test_quantity_of_postponed_books_at_the_header(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.clear_postpone_reload_page()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        quantity_text_value_after = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        assert int(quantity_text_value_after) == 1

    # Откладываем несколько книг и сверяем количество в хэдере
    @pytest.mark.xfail
    def test_quantity_of_postponed_books_at_the_header_numerous_selection(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.clear_postpone_reload_page()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        self.selected_books = self.list_of_books[0:3]
        for book in self.selected_books:
            self.postponePage.scroll_to_element(book)
            book.click()
        quantity_text_value = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        assert int(quantity_text_value) == 3

    # Проверяем, что кнопка "Убрать из отложенных" соответствующе работает
    @pytest.mark.xfail
    def test_for_postponed_book_deletion_by_submenu_of_postpone_book(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.clear_postpone_reload_page()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        quantity_text_value = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.DELETE_POSTPONED_BOOK)
        new_quantity_text_value = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        assert int(quantity_text_value) - int(new_quantity_text_value) == 1

    # Проверяем, что название отложенной книги на домашней странице соответствует названию книги в отложенном
    def test_that_postponed_book_name_equal_to_book_added(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        self.list_of_book_names = self.postponePage.find_several_element(PostponePage.BOOKS_DESCRIPTION_COVER)
        first_book_cover = self.list_of_book_names[0].get_attribute(TestData.ATTRIBUTE_TITLE)
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        postponed_book_at_postpone_page = self.postponePage.get_element_text(PostponePage.BOOK_IN_POSTPONE_PAGE)
        assert postponed_book_at_postpone_page in first_book_cover

    # Проверяем успешное удаление всех книг при помощи кнопки "Очистить"
    def test_deletion_of_all_books_postponed_at_postpone_page(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.postponePage.do_click(PostponePage.CLEAR_POSTPONE_BUTTON)
        alert = self.driver.switch_to.alert
        alert.accept()
        assert self.postponePage.get_element_text(PostponePage.POSTPONED_BOOKS_DELETED_MESSAGE)\
               == TestData.SUCCESSFUL_DELETION

    # Проверяем, что кнопка "Выделить все" работает в соответствии с нашими ожиданиями
    def test_that_enable_all_button_work(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        for book in self.list_of_books:
            self.postponePage.scroll_to_element(book)
            book.click()
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.list_of_postponed_books = self.postponePage.find_several_element(PostponePage.CHECKBOX_POSTPONED_BOOKS)
        self.postponePage.do_click(PostponePage.SELECT_ALL_POSTPONED_BOOKS)
        for postponed_book in self.list_of_postponed_books:
            assert postponed_book.is_enabled()

    # Проверяем появление кнопки "Удалить"
    def test_that_delete_button_in_popup_work(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        for book in self.list_of_books:
            self.postponePage.scroll_to_element(book)
            book.click()
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.postponePage.do_click(PostponePage.SELECT_ALL_POSTPONED_BOOKS)
        self.all_books_to_be_deleted_list = self.postponePage.find_several_element(PostponePage.ALL_SELECTED_BOOKS)
        self.postponePage.do_click(PostponePage.DELETE_SELECTED_BOOKS)
        alert = self.driver.switch_to.alert
        alert.accept()
        for deleted_book in self.all_books_to_be_deleted_list:
            assert self.postponePage.element_is_not_visible(deleted_book)

    # Проверяем, что отложенные книги на странице "Отложено" переходят в "Корзина" при нажатии на кнопку "В КОРЗИНУ"
    def test_that_button_move_into_basket_changed_to_checkout(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.list_of_postponed_books = self.postponePage.find_several_element(
            PostponePage.MOVE_INTO_THE_BASKET_FROM_POSTPONE_BUTTON)
        last_postponed_book = self.list_of_postponed_books[0]
        self.postponePage.scroll_to_element(last_postponed_book)
        id_of_book_to_be_postponed = last_postponed_book.get_attribute(TestData.ATTRIBUTE_ID)
        last_postponed_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_POSTPONED_BOOK_MOVED_INTO_THE_BASKET)
        self.postponePage.refresh_current_url()
        self.list_of_book_to_be_checked_out = self.postponePage.find_several_element(
            PostponePage.SWITCH_TO_CHECKOUT_BOOK_INTO_THE_BASKET_FROM_POSTPONE_PAGE)
        last_book_added_to_checkout = self.list_of_book_to_be_checked_out[0]
        self.postponePage.scroll_to_element(last_book_added_to_checkout)
        id_of_book_to_be_checked_out = last_book_added_to_checkout.get_attribute(TestData.ATTRIBUTE_ID)
        assert id_of_book_to_be_postponed == id_of_book_to_be_checked_out

    # Проверяем, что после нажатия на кнопку "В КОРЗИНУ" счетчик в хэдере меняется соответствующе
    def test_that_button_move_in_below_postponed_book_basket_will_increase_basket_counter(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        initial_quantity_of_books_in_basket = self.postponePage.get_element_text(TestData.BASKET_COUNTER)
        self.list_of_postponed_books = self.postponePage.find_several_element(
            PostponePage.MOVE_INTO_THE_BASKET_FROM_POSTPONE_BUTTON)
        last_postponed_book = self.list_of_postponed_books[0]
        self.postponePage.scroll_to_element(last_postponed_book)
        last_postponed_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_POSTPONED_BOOK_MOVED_INTO_THE_BASKET)
        self.postponePage.refresh_current_url()
        new_quantity_of_books_in_basket = self.postponePage.get_element_text(TestData.BASKET_COUNTER)
        assert int(new_quantity_of_books_in_basket) - int(initial_quantity_of_books_in_basket) == 1

    # Проверяем соответствие добавленной в отложенное книги на домашней странице и книги в корзине
    @pytest.mark.xfail
    def test_that_same_book_was_postponed_then_moved_to_basket(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_THE_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.list_of_book_names = self.postponePage.find_several_element(PostponePage.BOOKS_DESCRIPTION_COVER)
        first_book_name = self.list_of_book_names[0].get_attribute(TestData.ATTRIBUTE_TITLE)
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.list_of_postponed_books = self.postponePage.find_several_element(
            PostponePage.MOVE_INTO_THE_BASKET_FROM_POSTPONE_BUTTON)
        last_postponed_book = self.list_of_postponed_books[0]
        self.list_of_postponed_book_names = self.postponePage.find_several_element(PostponePage.BOOK_IN_POSTPONE_PAGE)
        name_of_last_postponed_book = self.list_of_postponed_book_names[0].text
        self.postponePage.scroll_to_element(last_postponed_book)
        last_postponed_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_POSTPONED_BOOK_MOVED_INTO_THE_BASKET)
        self.postponePage.refresh_current_url()
        self.list_of_book_names_in_basket = self.postponePage.find_several_element(PostponePage.BOOK_IN_POSTPONE_PAGE)
        last_added_in_basket_name = self.list_of_book_names_in_basket[0].text
        assert name_of_last_postponed_book == last_added_in_basket_name
        assert last_added_in_basket_name in first_book_name
