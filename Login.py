from time import  sleep

def login(driver,username,password):
    role_path = '//div[@class="rolelist"]/ul/li[3]'
    driver.find_element_by_name('username').send_keys(username)
    # password
    driver.find_element_by_name('password').send_keys(password)
    # role_name
    driver.find_element_by_id('role_name').click()
    sleep(1)
    driver.find_element_by_xpath(role_path).click()
    sleep(1)
    # login
    driver.find_element_by_id('login').click()
    sleep(2)
