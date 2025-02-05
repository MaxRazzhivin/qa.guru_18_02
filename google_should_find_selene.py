from selene import browser, be, have

def test_successful_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_failed_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('html').should(have.no.text('Some additional info'))

# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_successful_search_duckgo():
    browser.open('https://duckduckgo.com/')
    browser.element('#searchbox_input').type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('github.com'))


def test_successful_search_yandex():
    browser.open('https://ya.ru')
    browser.element('#text').type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('github.com'))
