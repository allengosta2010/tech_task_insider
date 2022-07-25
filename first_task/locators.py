from selenium.webdriver.common.by import By


class MainPageLocators():
    HOME_ELM           = (By.CSS_SELECTOR, ".home .home-page")
    MORE_ELM           = (By.XPATH,        "//span[text()='More']")
    CAREERS_ELM        = (By.XPATH,        "//h5[text()='Careers']")
    LOCATIONS_INFO_ELM = (By.CSS_SELECTOR, '[id="career-our-location"] [id="location-slider"] .location-figure')
    CAREERS_INFO_ELM   = (By.CSS_SELECTOR, '.career-load-more .job-item')
    LIFE_ELM           = (By.XPATH,        "//h2[text()='Life at Insider']")
    ALL_TEAMS_BTN      = (By.CSS_SELECTOR, '[id="career-find-our-calling"] .btn')
    QA_ELM             = (By.XPATH,        "//h3[text()='Quality Assurance']")
    ALL_QA_JOBS_BTN    = (By.CSS_SELECTOR, '[id="page-head"] .btn')
    LOCATIONS_ELM      = (By.CSS_SELECTOR, '[name="filter-by-location"]')
    DEPARTMENTS_ELM    = (By.CSS_SELECTOR, '[name="filter-by-department"]')
    JOBS_LIST_ELM      = (By.CSS_SELECTOR, '[id="jobs-list"]')
    POSITION_TITLE_ELM = (By.CSS_SELECTOR, '.position-title')
    POSITION_DEPT_ELM  = (By.CSS_SELECTOR, '.position-department')
    POS_LOCATION_ELM   = (By.CSS_SELECTOR, '.position-location')
    APPLY_LIST_BTN     = (By.CSS_SELECTOR, '.position-list-item-wrapper .btn')
    POSITION_ELM       = (By.CSS_SELECTOR, '.position-list-item')
    ACCEPT_COOKIES_BTN = (By.CSS_SELECTOR, '[id="wt-cli-accept-all-btn"]')
