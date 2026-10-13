from logic_utils import check_guess


# --- Existing tests, updated to unpack (outcome, message) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: hint messages pointed the wrong way ---

def test_too_high_guess_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_guess_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug 2: numbers were compared as strings ---

def test_one_digit_guess_below_two_digit_secret_is_too_low():
    # As strings, "9" > "50", which wrongly gave "Too High"
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_three_digit_guess_above_two_digit_secret_is_too_high():
    # As strings, "100" < "50", which wrongly gave "Too Low"
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_two_digit_guess_above_one_digit_secret_is_too_high():
    # As strings, "10" < "9", which wrongly gave "Too Low"
    outcome, message = check_guess(10, 9)
    assert outcome == "Too High"
    assert "LOWER" in message
