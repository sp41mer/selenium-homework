# coding=utf-8
from seismograph.ext import selenium


class PostPage(selenium.Page):
    __url_path__ = '/avto.mobile/topic/66155670481722'

    post_text = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='posting_form_text_field'
        )
    )

    def makeGroupComment(self):
        form = self.browser.find_element_by_css_selector("form.comments_add_form")
        form.click()
        # self.browser.execute_script(''' window.scrollBy(0,250) ''')
        form.set('hmm..')
        button = self.browser.find_element_by_css_selector("button.button-pro.form-actions_yes")
        button.click()

        comment = self.browser.find_elements_by_css_selector("div.comments_text")[-1]

        if comment.text == 'hmm..':
            assert True
        else:
            assert False
