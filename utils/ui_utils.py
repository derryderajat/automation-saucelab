import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class UIUtils:
    def __init__(self, driver, timeout=10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.screenshot_dir = "reports/screenshots/failed"
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def wait_for(self, condition, locator):
        """Waits for a specific condition to be met for a web element."""
        return self.wait.until(condition(locator))
    
    def find_element(self, locator):
        """Finds a web element on the page."""
        return self.wait_for(EC.presence_of_element_located, locator)
    
    def find_elements(self, locator):
        """Finds web elements on the page."""
        return self.wait_for(EC.presence_of_all_elements_located, locator)

    def click(self, locator):
        """Clicks on a web element."""
        try:
            element = self.wait_for(EC.element_to_be_clickable, locator)  # Wait until the element is clickable
            element.click()
            print("Element has been clicked.")
        except InterruptedError:
            self._take_screenshot("interrupted_error")
            print("Element is not clickable due to another element obstructing it.")
        except TimeoutError:
            self._take_screenshot("timeout_error")
            print("Element was not clickable within the timeout period.")
        except Exception as e:
            self._take_screenshot("click_error")
            print(f"Exception occurred: {e}")
            raise

    def send_keys(self, locator, text):
        """Sends keys to a web element."""
        try:
            element = self.wait_for(EC.visibility_of_element_located, locator)
            if element.is_displayed() and element.is_enabled():
                element.clear()
                element.send_keys(text)
                print(f"Sent keys '{text}' to element.")
            else:
                raise Exception("Element is not interactable")
        except Exception as e:
            self._take_screenshot("send_keys_error")
            print(f"Exception occurred: {e}")
            raise
        
    def wait_for_element_to_be_visible(self, locator):
        """Waits for a web element to be visible."""
        return self.wait_for(EC.visibility_of_element_located, locator)
    
    def wait_for_element_to_be_clickable(self, locator):
        """Waits for a web element to be clickable."""
        return self.wait_for(EC.element_to_be_clickable, locator)
    
    def get_text(self, locator):
        """Gets the text of a web element."""
        element = self.find_element(locator)
        return element.text
    
    def is_element_present(self, locator):
        """Checks if a web element is present on the page."""
        try:
            self.find_element(locator)
            return True
        except:
            return False
        
    def is_element_visible(self, locator):
        """Checks if a web element is visible on the page."""
        try:
            self.wait_for_element_to_be_visible(locator)
            return True
        except:
            return False
    
    def scroll_to_element(self, locator):
        """Scrolls the page to the web element."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def select_option_by_value(self, locator, value):
        """Selects an option from a dropdown by value."""
        try:
            element = self.find_element(locator)
            Select(element).select_by_value(value)
            print(f"Selected option with value '{value}'.")
        except Exception as e:
            self._take_screenshot("select_option_by_value_error")
            print(f"Exception occurred: {e}")
            raise
    
    def select_option_by_visible_text(self, locator, text):
        """Selects an option from a dropdown by visible text."""
        try:
            element = self.find_element(locator)
            Select(element).select_by_visible_text(text)
            print(f"Selected option with visible text '{text}'.")
        except Exception as e:
            self._take_screenshot("select_option_by_visible_text_error")
            print(f"Exception occurred: {e}")
            raise
    
    def handle_alert(self, action='accept'):
        """Handles browser alerts by accepting or dismissing them."""
        try:
            alert = self.wait_for(EC.alert_is_present, None)
            if action == 'accept':
                alert.accept()
                print("Alert accepted.")
            elif action == 'dismiss':
                alert.dismiss()
                print("Alert dismissed.")
        except Exception as e:
            self._take_screenshot("handle_alert_error")
            print(f"Exception occurred: {e}")
            raise

    def execute_script(self, script):
        """Executes JavaScript on the page."""
        return self.driver.execute_script(script)
    
    def take_screenshot(self, file_name):
        """Takes a screenshot of the current page."""
        self.driver.save_screenshot(file_name)
    
    def switch_to_frame(self, locator):
        """Switches to an iframe."""
        try:
            element = self.find_element(locator)
            self.driver.switch_to.frame(element)
            print("Switched to iframe.")
        except Exception as e:
            self._take_screenshot("switch_to_frame_error")
            print(f"Exception occurred: {e}")
            raise
    
    def switch_to_default_content(self):
        """Switches back to the default content from an iframe."""
        self.driver.switch_to.default_content()
    
    def drag_and_drop(self, source_locator, target_locator):
        """Performs drag and drop action."""
        try:
            source_element = self.find_element(source_locator)
            target_element = self.find_element(target_locator)
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
            print("Performed drag and drop.")
        except Exception as e:
            self._take_screenshot("drag_and_drop_error")
            print(f"Exception occurred: {e}")
            raise

    def is_on_page(self, keyword):
        """Check if the current browser URL contains the expected keyword."""
        current_url = self.driver.current_url
        print(f"CURRENT_URL: {current_url}")
        return keyword in current_url

    def _take_screenshot(self, error_type):
        """Takes a screenshot and saves it to the failed directory."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"{self.screenshot_dir}/{error_type}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_filename)
        print(f"Screenshot saved to {screenshot_filename}")
