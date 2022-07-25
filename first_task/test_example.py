import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators

link = "https://useinsider.com/"


class TestInsiderPage:

    @pytest.mark.smoke
    def test_case_01(self, browser):
        browser.get(link)

        cookies = browser.find_element(*MainPageLocators.ACCEPT_COOKIES_BTN)
        cookies.click()
        time.sleep(10)
        assert browser.find_element(*MainPageLocators.HOME_ELM), "Home page is not opened"

    @pytest.mark.smoke
    def test_case_02(self, browser):
        browser.implicitly_wait(5)
        more_elm = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(MainPageLocators.MORE_ELM)
        )
        more_elm.click()

        careers_elm = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(MainPageLocators.CAREERS_ELM)
        )
        careers_elm.click()

        browser.implicitly_wait(5)

        assert browser.find_element(*MainPageLocators.LOCATIONS_INFO_ELM), "Locations block is not opened"
        assert browser.find_element(*MainPageLocators.CAREERS_INFO_ELM), "Teams block is not opened"
        assert browser.find_element(*MainPageLocators.LIFE_ELM), "Life block is not opened"

    @pytest.mark.smoke
    def test_case_03(self, browser):
        all_teams_btn = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(MainPageLocators.ALL_TEAMS_BTN)
        )
        browser.execute_script("arguments[0].click();", all_teams_btn)

        qa_elm = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(MainPageLocators.QA_ELM)
        )
        browser.execute_script("arguments[0].click();", qa_elm)

        browser.implicitly_wait(5)

        all_qa_jobs = browser.find_element(*MainPageLocators.ALL_QA_JOBS_BTN)
        browser.execute_script("arguments[0].click();", all_qa_jobs)

        locations_select = Select(browser.find_element(*MainPageLocators.LOCATIONS_ELM))
        locations_select.select_by_visible_text("Istanbul, Turkey")

        browser.implicitly_wait(5)

        departments_select = Select(browser.find_element(*MainPageLocators.DEPARTMENTS_ELM))
        departments_select.select_by_visible_text("Quality Assurance")

        assert browser.find_element(*MainPageLocators.JOBS_LIST_ELM), "Jobs list is not presented"

    @pytest.mark.smoke
    def test_case_04(self, browser):
        browser.execute_script("window.scrollBy(0,350)", "")
        time.sleep(10)

        position_titles = browser.find_elements(*MainPageLocators.POSITION_TITLE_ELM)
        for title in position_titles:
            assert 'Quality Assurance' or 'QA' in title.text, 'Title does not contain Quality Assurance text'

        position_departments = browser.find_elements(*MainPageLocators.POSITION_DEPT_ELM)
        for department in position_departments:
            assert 'Quality Assurance' in department.text, 'Department does not contain Quality Assurance text'

        position_locations = browser.find_elements(*MainPageLocators.POS_LOCATION_ELM)
        for locations in position_locations:
            assert 'Istanbul, Turkey' in locations.text, 'Location does not contain Istanbul, Turkey text'

        apply_now_btns = browser.find_elements(*MainPageLocators.APPLY_LIST_BTN)
        for btn in apply_now_btns:
            assert btn.text in 'Apply Now', 'Button does not contain Apply Now text'

    @pytest.mark.smoke
    def test_case_05(self, browser):
        apply_now_btns = browser.find_elements(*MainPageLocators.APPLY_LIST_BTN)
        position = browser.find_elements(*MainPageLocators.POSITION_ELM)[0]
        hover = ActionChains(browser).move_to_element(position)
        hover.perform()
        browser.execute_script("arguments[0].click();", apply_now_btns[0])

        browser.implicitly_wait(15)
        assert browser.window_handles[1], "Redirection does not work"
