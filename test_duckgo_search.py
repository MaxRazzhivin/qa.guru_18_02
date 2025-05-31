from selene import browser, have


def test_successful_search_duckgo(open_duckgo):
    browser.element('#searchbox_input').type('kjlkdfmglkmdfkl').press_enter()
    browser.element('html').should(have.text('По запросу «kjlkdfmglkmdfkl» ничего не найдено.'))
