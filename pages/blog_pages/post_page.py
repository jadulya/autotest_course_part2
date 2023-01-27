# pages/blog_pages/post_page.py

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей отображения поста (пример URL -- /blog/page/1/test-post/ или /blog/page/1)
class PostPage(BasePage):
    POST_TEXT = (By.CSS_SELECTOR, ".container p+p")
    EDIT_BUTTON = (By.ID, "edit")
    TITLE = (By.TAG_NAME, "h1")
    DELETE_BUTTON = (By.ID, "delete")
    CONFIRM_DELETE_BUTTON = (By.ID, "confirmedDelete")

    def check_post_text(self, text):
        post_text = self.wait_until_visible(self.POST_TEXT)
        assert post_text.text == text, "Неверный текст"

    def open_edit_page(self):
        self.wait_until_clickable(self.EDIT_BUTTON).click()

    def check_title_changed(self, new_title):
        assert self.wait_until_visible(self.TITLE).text == new_title, "Заголовок не был отредактирован"

    def delete_post(self):
        self.wait_until_clickable(self.DELETE_BUTTON).click()
        self.wait_until_clickable(self.CONFIRM_DELETE_BUTTON).click()


