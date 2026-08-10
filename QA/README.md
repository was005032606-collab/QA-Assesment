# QA Automation Framework — Single Bet Placement

Contains 2 automated tests:
- **E2E UI test** — full happy-path bet placement journey (Selenium)
- **API test** — business rule validation via direct HTTP requests

## Project Structure

```
qa/
├── pages/
│   ├── __init__.py
│   ├── base_page.py          # shared wait/click/find helpers
│   ├── match_list_page.py    # match list page object
│   └── bet_slip_page.py      # bet slip + success modal page object
├── tests/
│   ├── api/
│   │   └── test_stake_validation.py
│   └── ui/
│       └── test_place_bet_e2e.py
├── conftest.py                # pytest fixtures (driver, api headers/url)
├── pytest.ini                 # pytest config
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository and navigate into the `qa/` folder:
   ```bash
   cd qa
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   ChromeDriver is managed automatically by Selenium 4.6+ (Selenium Manager) — no separate driver install needed, as long as Chrome (latest desktop) is installed on the machine.

4. Set your test user ID in `conftest.py` (`USER_ID` constant) to match the ID provided for the assignment.

## Running the Tests

Run the full suite:
```bash
pytest -v
```

Run only API tests (fast, no browser):
```bash
pytest tests/api/ -v -m api
```

Run only UI tests:
```bash
pytest tests/ui/ -v -m ui
```

## Configuration

- `BASE_URL` and `USER_ID` are defined in `conftest.py`.
- The app is accessed with the required `?user-id=<id>` query parameter for the UI, and the `x-user-id` header for API calls (per spec section 5.1).
- `pytest.ini` sets `pythonpath = .` so that `pages/` resolves correctly as an importable package regardless of which subfolder a test file lives in.

## Test Selection Rationale

Brief summary — full reasoning is in the Strategy & Recommendations note:

- **E2E UI test** (`test_place_bet_e2e.py`): covers the core revenue-generating user journey (select odds → enter stake → place bet → verify success receipt, including payout = stake × odds correctness). Highest business risk if broken.
- **API test** (`test_stake_validation.py`): verifies a business rule (stake validation) is enforced independently at the API layer, since client-side UI validation alone doesn't guarantee backend protection against direct API calls.

## Known Limitations

- Tests assume a stable test match (`matchId`) is present in the application's match catalog; a more robust version would fetch a valid `matchId` dynamically via `GET /api/matches` before each run.
- No test isolation/reset mechanism is currently wired in (see Strategy note — recommended: `POST /api/reset-balance` as an `autouse` fixture) — running tests back-to-back may be affected by balance state from prior runs.
