test analysis

defects: business rules(3) - min stake = 1.00
	validation rules(4.1) field:stake - min stake = 1.01


core function conditions:
2.1 Match list - changing odds change previous choice
2.3 Place Bet - loading state -> success/failure 
3 Business rules 
4 validation rules
5.3 API

test scenarios

TS-01 Happy path: success in placing bet
Priority: critical
Risk rationale: main user journey, loss in money and user trust
Precondition: user balance is 20.00
Steps:
	Pick match and side (1) - home odds
	input stake 10.00
	click place bet
Expected result:
	button shows "Placing..."
	in-progress state - success
	balance gets reduced by 10.00
	shows Success Receipt with full correct information

TS-02 Negative test: placing bet with stake that bigger than balance
Priority: critical
Risk rationale: main user journey, loss in money and posiible company debts
Precondition: user balance is 20.00
Steps:
	Pick match and side (1) - home odds
	input stake 100.00
	click place bet
Expected result:
	button shows "Placing..."
	in-progress state - failure
	error modal appearence with full and correct information

TS-03 Boundary negative test: placing bet with stake under/over minimal possible range
Priority: High
Risk rationale: main user journey, loss in money and posiible company debts
Precondition: user balance is 20.00 / 120.00
Steps:
	Pick match and side (1) - home odds
	input stake 0.99 / 100.01
	click place bet
Expected result:
	button shows "Placing..."
	in-progress state - failure
	error modal appearence with full and correct information

TS-04 Testing rebet and close option after bet placing failure by symulating failure path
Priority: High
Risk rationale: main user journey, loss in money and posiible company debts
Precondition: user balance is 20.00
Steps:
	Pick match and side (1) - home odds
	input stake 10.00
	simulate error by activating script that changes my API request
	click place bet
	after error message appearing click rebet/close
Expected result:
	succsessful bet placement with full information that user already wrote / cancelling bet placement
	shows Success Receipt with full correct information
	correct financial operation with user balance


tests chosen: TS-01 TS-03 TS-04
