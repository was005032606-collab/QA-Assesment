from pages.match_list_page import MatchListPage
from pages.bet_slip_page import BetSlipPage

def test_successful_bet_placement_e2e(driver):

    MATCH_ID = "premier-league-manutd-chelsea"

    match_list = MatchListPage(driver)
    bet_slip = BetSlipPage(driver)

    match_list.select_home_odds(MATCH_ID)
    bet_slip.enter_stake(1.00)
    bet_slip.place_bet()

    modal = bet_slip.get_success_receipt()
    assert modal.is_displayed()

    values = bet_slip.get_receipt_values()

    assert values["bet_id"].startswith("#B-")
    assert values["match"] == "Chelsea vs Manchester Utd"
    assert values["stake"] == "€1.00"

    stake_num = float(values["stake"].replace("€", ""))
    odds_num = float(values["odds"])
    payout_num = float(values["payout"].replace("€", ""))
    assert payout_num == round(stake_num * odds_num, 2)
