# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from smth.Auth import AuthManager
import time

from pages.group_post_page import PostPage as GPP

suite = selenium.Suite(__name__)


def auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())


@suite.register
def test_get_author_group(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(3)
    content = feed_page.getPopularContent()
    time.sleep(3)
    element, url = feed_page.getAuthor(content)
    element.click()
    time.sleep(3)
    return url in browser.current_url


@suite.register
def test_get_post(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    content.click()
    time.sleep(3)
    url = browser.current_url
    return "/topic/" in url


@suite.register
def test_get_post(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    before = feed_page.getStatusLikes()
    feed_page.makeLikeOnOwnPost()
    after = feed_page.getStatusLikes()
    return before != after


@suite.register
def test_make_self_comment(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    feed_page.makeSelfComment(content, feed_page)


# ERROR
@suite.register
def test_make_comment(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    feed_page.makeComment(content, feed_page)


# Fail
@suite.register
def test_make_like(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    feed_page.makeLikeOnSelfComment(content, feed_page)


# OK
@suite.register
def test_make_double_like(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    feed_page.makeDoubleLike(content, feed_page)


# ERROR
@suite.register
def test_make_someone_like_comment(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    feed_page.makeLikeForSomemoneComment(content, feed_page)


# ERROR
@suite.register
def test_make_group_comment(case, browser):
    auth(case, browser)

    post_page = GPP(browser)
    post_page.open()
    time.sleep(1)
    post_page.makeGroupComment()


@suite.register
def test_make_repost(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    val = feed_page.makeRepost()
    return val == u'Опубликовано!'


@suite.register
def test_make_two_likes(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    time.sleep(1)
    feed_page.makeLikeTwoLikes()

@suite.register
def test_make_one_likes(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    time.sleep(1)
    feed_page.makeOneLike()


@suite.register
def test_make_repost_by_double_click(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    val = feed_page.makeDoubleClickRepost()
    return val == u'Опубликовано!'


@suite.register
def test_make_repost_and_delete(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    time.sleep(1)
    val = feed_page.makeRepost()
    if val == u'Опубликовано!':
        profile_page = ProfilePage(browser)
        profile_page.open()
        return profile_page.delete_my_post()
    else:
        return False