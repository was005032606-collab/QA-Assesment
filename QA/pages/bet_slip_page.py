from selenium.webdriver.common.by import By
from .base_page import BasePage

class BetSlipPage(BasePage):
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    PLACE_BET_BTN = (By.ID, "bet-slip-place-bet")
    SUCCESS_MODAL = (By.ID, "modal-success")
    SUCCESS_BET_ID = (By.ID, "modal-success-bet-id")
    SUCCESS_MATCH = (By.ID, "modal-success-match")
    SUCCESS_STAKE = (By.ID, "modal-success-stake")
    SUCCESS_ODDS = (By.ID, "modal-success-odds")
    SUCCESS_PAYOUT = (By.ID, "modal-success-payout")
    SUCCESS_PLACED_AT = (By.ID, "modal-success-placed-at")
    SUCCESS_CLOSE_BTN = (By.ID, "modal-success-close")
    SUCCESS_CLOSE_X = (By.ID, "modal-success-close-x")

    def enter_stake(self, amount):
        field = self.find(self.STAKE_INPUT)
        field.clear()
        field.send_keys(str(amount))

    def place_bet(self):
        self.click(self.PLACE_BET_BTN)

    def get_success_receipt(self):
        return self.find(self.SUCCESS_MODAL)

    def get_receipt_values(self):
        return {
            "bet_id": self.find(self.SUCCESS_BET_ID).text,
            "match": self.find(self.SUCCESS_MATCH).text,
            "stake": self.find(self.SUCCESS_STAKE).text,
            "odds": self.find(self.SUCCESS_ODDS).text,
            "payout": self.find(self.SUCCESS_PAYOUT).text,
        }

    def close_success_modal(self):
        self.click(self.SUCCESS_CLOSE_BTN)