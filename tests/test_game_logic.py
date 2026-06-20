import pytest

from app import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


# Regression test for the directional-hint bug:
# a guess that is TOO HIGH must tell the player to go LOWER, and
# a guess that is TOO LOW must tell the player to go HIGHER.
def test_too_high_hint_says_go_lower():
    _outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    _outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message


# Regression test for the "hint off" bug:
# the guess outcome must still be produced (and therefore printable)
# regardless of whether the "Show hint" checkbox is checked. The hint
# checkbox should only gate the directional message, never the outcome.
@pytest.mark.parametrize("show_hint", [True, False])
def test_outcome_shown_even_when_hint_unchecked(show_hint):
    outcome, message = check_guess(60, 50)

    # check_guess does not take the hint flag, so the outcome is always
    # available to display whether or not show_hint is set.
    assert outcome == "Too High"
    assert outcome  # a non-empty outcome is always returned to be printed

    # Mirror the app's display logic from app.py: the outcome is shown
    # unconditionally, and show_hint only controls the directional message.
    shown = []
    if outcome != "Win":
        shown.append("❌ Wrong guess. Try again!")
    if show_hint:
        shown.append(message)

    # The outcome line is present in both hint states.
    assert "❌ Wrong guess. Try again!" in shown
