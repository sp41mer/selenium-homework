# coding=utf-8
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException
from seismograph.ext.selenium.exceptions import PollingTimeoutExceeded


class ElsePostPage(selenium.Page):
    __url_path__ = '/profile/573666484126/statuses/65858517120414'

    active_menu = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='sc-menu __reshare __noarrow sc-menu__top'
        )
    )

    @selenium.polling.wrap(delay=1)
    def wait_repost(self):
        self.browser.execute_script('''$("div[data-l*='t,now']").last().find('a').click()''')
        if u'Поделиться' in self.active_menu.text:
            raise WebDriverException(msg='Timeout at waiting repost someone post')

    @selenium.polling.wrap(delay=1, exceptions=(PollingTimeoutExceeded, WebDriverException))
    def open_menu(self):
        self.browser.execute_script('''$(':button[tsid=reshareMenu]').last().click()''')
        self.active_menu.wait()

    def make_repost(self):
        self.wait_repost()
        return self.active_menu.text
