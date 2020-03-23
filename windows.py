
def get_new_window(driver):
    windows=driver.window_handles
    driver.switch_to.window(windows[-1])