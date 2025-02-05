from selene import browser, have, be

def test_google_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_failed_search(open_browser):
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('html').should(have.no.text('Some additional info'))

def test_successful_search_duckgo(open_duckgo):
    browser.element('#searchbox_input').type('kjlkdfmglkmdfkl').press_enter()
    browser.element('html').should(have.text('По запросу kjlkdfmglkmdfkl результаты не найдены.'))

