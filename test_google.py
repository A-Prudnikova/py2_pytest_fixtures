import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture(scope='session')
def browser_size():
    browser.open('https://google.com').driver.maximize_window()


@pytest.fixture(scope='session')
def input_data():
    browser.element('[name="q"]').type('selene').press_enter()


def test_search_positive(browser_size, input_data):
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_negative(browser_size, input_data):
    browser.element('#search').should(have.no.text('Tortuga'))
