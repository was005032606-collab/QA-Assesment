from selenium.webdriver.common.by import By
from .base_page import BasePage

class MatchListPage(BasePage):
    def _odds_locator(self, match_id, outcome):
        return (By.ID, f"odds-{match_id}-{outcome}")

    def select_home_odds(self, match_id):
        self.click(self._odds_locator(match_id, "home"))

    def select_draw_odds(self, match_id):
        self.click(self._odds_locator(match_id, "draw"))

    def select_away_odds(self, match_id):
        self.click(self._odds_locator(match_id, "away"))

    def get_odds_value(self, match_id, outcome):
        locator = self._odds_locator(match_id, outcome)
        element = self.find(locator)
        value_span = element.find_element(By.CSS_SELECTOR, ".oddsButtonValue")
        return value_span.text