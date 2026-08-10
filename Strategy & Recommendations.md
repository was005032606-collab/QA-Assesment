Strategy and Recommendation

E2E UI test pick was critical user journey, providing clearence on multiple levels and securing most important betting functionality.
This test checks not only appearence of success modal after making bet, but also checks correctness of all information provided by success receipt,
validating multiple information that can impact end user.

API test pick was 422 error in bet placement flow, it provides critical risk to buisness, and this error still needs to be check for security reasons,
even if UI part is providing additional layer of security. This test oriented to receive response from API bypassing UI layer to provide clearence in 
in successful rejection of request to place bet with stake under limit.

Intentionally left as manual tests was: 
UI details, since it was out of scope and require too much resources to automate.
Filters with date range and odd range, since they providing low critical impact on user journey
Exploratory checks of bet slip block, since it require a lot of work to simulate multiple clicks on place bet button(BR-04 with 409 error check)

My top recomendations will be:
Adding layer of CI/CD API and UI tests to provide stable consistent background for future tests
Proper usage of endpoints to exclude logic problems with balance during bet placement flow
Spec clarification in stake minimum
