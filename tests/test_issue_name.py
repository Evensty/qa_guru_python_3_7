import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


# Чистый Selene (без шагов)
def test_issue_name():
    browser.open("https://github.com")
    s(".header-search-input").click().type("eroshenkoam/allure-example").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    s('#issue_65_link').should(have.exact_text('с днем археолога!'))


# Лямбда шаги через with allure.step
def test_issue_name_dynamic_steps():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Проверяем наличие issue с заданным именем")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с именем 'с днем археолога!'"):
        s('#issue_65_link').should(have.exact_text('с днем археолога!'))


# Шаги с декоратором @allure.step
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Maxim Veselov")
@allure.feature("Задачи в репозитории")
@allure.story("Проверяем наличие issue с заданным именем")
@allure.link("https://github.com", name="Testing")
def test_issue_name_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_be_name_with_name('с днем археолога!')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с именем 'с днем археолога!'")
def should_be_name_with_name(name):
    s('#issue_65_link').should(have.exact_text(name))
