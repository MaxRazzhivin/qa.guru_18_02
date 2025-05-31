from selene import browser, have


def test_succesfull_login(open_niffler):
    browser.element('[name=username]').type('stasd')
    browser.element('[name=password]').type('ratatui07')
    browser.element('button[type="submit"]').click()
    browser.element('#spendings').should(have.text('History of Spendings'))
    browser.quit()


def test_succesfull_login_with_enter(open_niffler):
    browser.element('[name=username]').type('stasd')
    browser.element('[name=password]').type('ratatui07').press_enter()
    browser.element('#spendings').should(have.text('History of Spendings'))
    browser.quit()


def test_unsuccesfull_login_with_wrong_credentials(open_niffler):
    browser.element('[name=username]').type('stasd')
    browser.element('[name=password]').type('ratatui07x').press_enter()
    browser.element('.form__error').should(have.text('Неверные учетные данные пользователя'))
    browser.quit()


def test_succesfull_login_check_username(open_niffler):
    browser.element('[name=username]').type('stasd')
    browser.element('[name=password]').type('ratatui07').press_enter()
    browser.element('#spendings').should(have.text('History of Spendings'))
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('.link.nav-link').should(have.text('Profile')).click()
    browser.element('#username').should(have.value('stasd'))
    browser.quit()


def test_succesfull_logout(open_niffler):
    browser.element('[name=username]').type('stasd')
    browser.element('[name=password]').type('ratatui07').press_enter()
    browser.element('#spendings').should(have.text('History of Spendings'))
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('ul.MuiList-root.MuiList-padding.MuiMenu-list li:last-child').click()
    browser.element('div[role="dialog"]').should(have.text('Want to logout?'))
    browser.element('div[role="dialog"] button:nth-child(2)').click()
    browser.element('.form__register').should(have.text('Create new account'))
