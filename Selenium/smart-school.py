from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import pdb


def set_text(browser, elm_id, text):
    elem = browser.find_element_by_id(elm_id)
    elem.clear()
    elem.send_keys(text)


def login(browser, name, password):
    set_text(browser, 'identityNumber', name)
    set_text(browser, 'password', password)

    browser.find_element_by_id('loginLogoutButton').click()


def is_iframe_visible(browser, frame_id, wait):
    try:
        WebDriverWait(browser, wait).until(
            expected_conditions.presence_of_element_located((By.ID, frame_id))
        )
        return True
    except NoSuchElementException:
        return False
    except Exception as ex:
        print(ex)
        return False


def switch_to_inner_iframe(browser):
    if not is_iframe_visible(browser, 'window_63_iframe', 3):
        icon = None
        try:
            icon = browser.find_element_by_id('icon_63')
        except NoSuchElementException as e:
            print('Icon not found!')

    if icon:
        action_chains = ActionChains(browser)
        action_chains.double_click(icon).perform()

    if is_iframe_visible(browser, 'window_63_iframe', 2):
        browser.switch_to.frame(browser.find_element_by_id('window_63_iframe'))
        return True
    else:
        print("*** Couldn't open iframe!!")
        return False


def set_checkbox(checkbox, value):
    if checkbox.is_selected() == value:
        return
    checkbox.click()


def send_declaration(browser, screenshot_name, selection_values=[]):
    print('\n' + screenshot_name + ':')
    if not switch_to_inner_iframe(browser):
        exit(-1)

    if selection_values:
        for index, value in enumerate(selection_values):
            set_checkbox(browser.find_element_by_id('studentIDs_' + str(index)), value)

    btn = None
    try:
        btn = browser.find_element_by_id('saveButton')
    except NoSuchElementException as e:
        print('Already signed (no button found)')

    if btn:
        btn.click()

        WebDriverWait(browser, 4).until(
            expected_conditions.alert_is_present()
        )

        browser.switch_to.alert.accept()

    elem = browser.find_element_by_id('infoMessage')
    print('-' * 20)
    print(elem.text)
    print('-' * 20)

    browser.save_screenshot(screenshot_name + ".png")


def change_school(browser, index):
    select = Select(browser.find_element_by_id('multiUser'))
    select.select_by_index(index)


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://www.webtop.co.il/v2/default.aspx')
    browser.create_options().add_experimental_option("detach", True)

    # data = {'name': 'tbener12',
    #         'password': 'ofri2006',
    #         'Yuvaley': [True, True],   # Maayan, Adi
    #         "Mevo'ot": []}

    with open('data.txt') as json_file:
        data = json.load(json_file)

    login(browser, data['name'], data['password'])

    for index, (key, value) in enumerate(list(data.items())[2:]):
        if not value:
            continue
        if index > 0:
            browser.switch_to.default_content()
            change_school(browser, index)
        else:
            file = key + ".png"
        send_declaration(browser, key, value)

    os.system("start " + file)


if __name__ == '__main__':
    main()
