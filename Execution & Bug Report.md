
BR-01(TS-01) Happy path report potantial payout defect
Severity: High
Preconditions: balance 40.00
Reproduction steps: 
	Pick match and side (1) - home odds Manchester Utd - Chelsea
	input stake 10.00 (odd 2.45)
	click place bet
Expected vs Actual result:
	Expected: 24.50
	Actual: 20.00
Business Impact: severe loss in reputation and trust from users
**Remark: there is bugs found that might impact main user journey found during exploratory checks, listed in BR-04


BR-02(TS-03) Test passed with no further defects

BR_03(TS-04) Test passed with no further defects

BR-04(Exploratory tests)
	01- Balance test:
	Severity: Critical
	Preconditions: balance 40.00
	Reproduction steps: 
		Pick match and side (1)
		input stake 40.00
		click place bet
		close receipt
		Pick match and side (1)
		input stake 40.00
		click place bet
		close receipt
		reload page
	Expected vs Actual result:
	Expected: reject in conformation on placing bet due to insufficient ballance
	Actual: accepted bet placing and negative balance
	Business Impact: severe balance abuse and money loss

02-Place bet stress test:
	Severity: Critical
	Preconditions: balance 40.00
	Reproduction steps:
		Pick match and side (1)
		input stake 40.00
		click place bet
		after loading state appear repeatedly clicking on place bet
	Expected vs Actual result:
	Expected: no actions due to processing current bet (409 error)
	Actual: repeated bet placement with same amount, odds on same side,
	match with multiple error messages appering that sometimes close themself with inactive rebet button 
	Business Impact: severe balance abuse and money loss
