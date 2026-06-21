# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game purpose is a classic guess the number for users to play. You can change difficultly and have hints on while the user guesses a number. It is created with bugs to test the developer to fix bugs using ai

- [ ] Detail which bugs you found.
1.Code generates the wrong logic. If guess is lower than answer then system generates too high and vice versa. this logic is incorrect

2.Code does not print result if hint is unchecked. it should not give too high or too low hints but should still output if the guess is incorrect or correct.

- [ ] Explain what fixes you applied.
1. Switched the comment of the logic in that part of the code. if guess is lower than answer then print too low and vice versa

2. Added an additional if statement that basically prints wrong answer if the guess is incorrect even if the hint box is unchecked.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. entered in a value of 1 
2. system returns too low
3. entered in a value of 30
4. system returns too low
5. entered in a value of 60 
6. system return too low
7. continue until i enter 100 
8. system return too high and game over
9. started new game
10. unchecked hints
11. entered in a value of 30
12. system doesnt output anything 
13. number of tries goes down

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
ameglitchinvestigator-starter> pytest
================ test session starts ================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-
rootdir: C:\Users\11791\OneDrive\Desktop\ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.13.0
collected 7 items                                    

tests\test_game_logic.py .......               [100%]

================= 7 passed in 1.23s =================

============================================================================== test session starts ===============================================================================
rootdir: C:\Users\11791\OneDrive\Desktop\ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.13.0
collected 5 items                                                                                                                                                                 

tests\test_game_logic.py .....                                                                                                                                              [100%]

=============================================================================== 5 passed in 1.21s ================================================================================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
