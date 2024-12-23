# brahmastra/brahmastra.py

import os.path
import time
import undetected_chromedriver as uc
from fake_useragent import UserAgent


class Brahmastra:
    def __init__(self, binary_path=None, user_data_dir=None):
        """
        Initialize the Brahmastra class.

        :param binary_path: Path to the browser binary. If None, the default browser binary is used.
        :param user_data_dir: Path to the user data directory. If None, the default user data directory is used.
        """
        self.binary_path = binary_path
        self.user_data_dir = os.path.expanduser(user_data_dir) if user_data_dir else None
        self.brahmastra = None
        self.user_agent_instance = UserAgent()

    def _get_random_user_agent(self):
        """
        Generate a random user agent using the fake_useragent library.
        Returns a default user agent if an error occurs.
        """
        try:
            return self.user_agent_instance.random
        except Exception as e:
            print(f"Error generating user agent: {e}")
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

    def initialize_brahmastra(self):
        """
        Initialize the undetected Chromedriver with custom options.
        """
        try:
            user_agent = self._get_random_user_agent()

            options = uc.ChromeOptions()
            options.add_argument(f"--user-agent={user_agent}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-infobars")
            options.add_argument("--profile-directory=Default")
            options.add_argument("--disable-plugins-discovery")

            if self.user_data_dir:
                options.add_argument(f"--user-data-dir={self.user_data_dir}")
            if self.binary_path:
                options.binary_location = self.binary_path

            self.brahmastra = uc.Chrome(options=options)

            self.brahmastra.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': '''
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                '''
            })
            return self.brahmastra
        except uc.exceptions.WebDriverException as e:
            print(f"Error initializing Brahmastra: {e}")
            self.quit_brahmastra()
            raise

    def quit_brahmastra(self):
        """
        Quit the Brahmastra and clean up resources.
        """
        if self.brahmastra:
            try:
                self.brahmastra.quit()
            except Exception as e:
                print(f"Error quitting Brahmastra: {e}")
            finally:
                self.brahmastra = None

    def example_use(self, url):
        """
        An example method to navigate to a URL and print the page title.

        :param url: The URL to navigate to.
        """
        if not self.brahmastra:
            raise RuntimeError("Brahmastra not initialized. Call initialize_brahmastra() first.")
        try:
            self.brahmastra.get(url)
            time.sleep(5)
            print("Page title:", self.brahmastra.title)
        except Exception as e:
            print(f"Error navigating to {url}: {e}")