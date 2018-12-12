from time import sleep
import Page_Class as page




def click_to_login_page(driver):

    main_page = page.Mainpage(driver)
    main_page.open()
    main_page.type_clicklanguage()
    sleep(1)
    main_page.type_chooselanguage()
    sleep(1)
    main_page.type_clicbutton()
    sleep(1)
    main_page.type_clicktag()
    sleep(3)

def user_login(driver, username, password):

    login_page = page.LoginPage(driver)
    login_page.open()

    login_page.type_username(username)
    sleep(3)
    login_page.type_password(password)
    sleep(3)
    login_page.type_submit()
    sleep(5)

def press_announcement(driver):
    main_dashbaord =page.MainDashboard(driver)
    main_dashbaord.open()
    driver.maximize_window
    main_dashbaord.type_clickannouncement()
    sleep(2)

def press_dashboard(driver):
    main_dashbaord =page.MainDashboard(driver)
    main_dashbaord.open()
    #driver.maximize_window
    main_dashbaord.type_clickdashboard()
    sleep(2)

def press_home(driver):
    main_dashbaord =page.MainDashboard(driver)
    main_dashbaord.open()
    driver.maximize_window
    main_dashbaord.type_clickhome()

def press_settings(driver):
    main_dashbaord =page.MainDashboard(driver)
    main_dashbaord.open()
    #driver.maximize_window
    main_dashbaord.type_clicksetting()
    sleep(2)

def press_statistics(driver):
    main_dashbaord =page.MainDashboard(driver)
    main_dashbaord.open()
    driver.maximize_window
    main_dashbaord.type_clickstatistics()
    sleep(2)

