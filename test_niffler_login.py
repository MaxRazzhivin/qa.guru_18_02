from selene import browser, have

def test_succesfull_login():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345')
    browser.element('button[type="submit"]').click()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_succesfull_login_with_enter():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_unsuccesfull_login_with_wrong_credentials():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('123456').press_enter()

    browser.element('[class="form__error"]').should(have.text('Неверные учетные данные пользователя'))
    browser.quit()

def test_succesfull_login_check_username():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.element('button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-sizeLarge css-1obba8g"]').click()
    browser.element('li[class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-z5w4ww"]').click()
    browser.element('#username').should(have.value('stas'))
    browser.quit()

    # todo check username in profile


def test_succesfull_logout():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.element(
        'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-sizeLarge css-1obba8g"]').click()
    browser.element('ul.MuiList-root.MuiList-padding.MuiMenu-list li:last-child').click()
    browser.element('div[role="dialog"]').should(have.text('Want to logout?'))
    browser.element('div[role="dialog"] button:nth-child(2)').click()
    browser.element('[class=form__register]').should(have.text('Create new account'))

    # todo check logout