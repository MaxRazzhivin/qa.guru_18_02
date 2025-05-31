from selene import browser, have, be


def test_google_search(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))


def test_failed_search(open_google):
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('html').should(have.no.text('Some additional info'))
