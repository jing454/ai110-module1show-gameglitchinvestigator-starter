# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

hint does not display result
guess is backward (go higher if guess is higher)

Says game over when i have 1 attempt left out of nowhere
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|1 |Either should say correct or higher | said lower even though it says guess 1-100 and nothing is lower than 1| No error was output in the console|


|unchecked show hints| should no longer show any hints like go lower go higher| doesnt show hints but also doesnt show if it's correct or incorrect| no error in console


|100 |should give me a score of 0 since i did not guess the right number at all|gave me a score of -15 which logically shouldn't be possible | no error in console
NOTE: additionally, score goes haywire. sometimes it says 0 then 5 then 0 even though input is repeated with same value


|last input was 100 (wrong and game finished) and then clicked new game| should start a new game|clicked start a new game but nothing happened| no error in console (note: for some reason i cannot replicate it again with the same last input)


|guessed with 2 attempt remaining| if wrong, should say incorrect and let me guess 1 more time | actual: says game over and gives me solution even though i have 1 attempt left | no error in console
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used claude and imported into VS code for this project. One example the ai was correct about was how the logic of "GO LOWER" and "GO HIGHER" was incorrect. I orginally thought it was an input issue but the AI pointed the specific issue on line x clearly. One weird thing that the ai did was pointing out another issue in the code but was unrelated to the current bug. It was talking about how when the guess was 2, it would say game over (which was another bug i later then realized). I then looked through the code and realized that this bug was completely seperated from the incorrect TOO HIGH or TOO low logic. I told the ai to write pytest which tests the code and ran it with pytest (i asked it so that i can run it with pytest too)
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For the logic TOO HIGH or TOO low problem, i told the ai to write a pytest and tested myself with it. i then ran streamlit and tested via the website too and it worked correctly. It correctly idenified the issue. It also explained the pytest logic that it wrote

For the logic where it doesnt display the outcome i told the ai to design a pytest so that it and me can run it and make sure it works correctly. i also launched streamlit and tested the website and it worked just fine. it also explained the pytest logic that it wrote
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

streamlit is used to generate a website like react but it is used mainly for python. "Reruns" means the the page refreshes when an action was made on the website from the start of the code (the code basically reruns at the start). So in this case, if you click submit guess, the code reruns app.py from the start all over again

problem is that everytime we rerun, the variable gets erased. So if you're score is 5 and you press submit, it'll go to 0 since code runs from the start and resets your score

This is where session state comes into play. Session-state basically tells the code: hey, this should survive reruns. this means that this value should not be resetted. One example of this is the secret number. We dont want the secret number that we're guessing to be resetted since this completely ruins the game's logic and makes it act randomly
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Defintely is to use ai for bug fixes and help me locate the issue. Instead of looking through the entire code line by line and trying to figure out what is the error, i can use ai to find it in like 30 seconds. However, i shouldnt follow ai randomly as i saw it can make mistakes and bring up completely different issues

- What is one thing you would do differently next time you work with AI on a coding task?

To use ai as more of a error catcher and a issue solver. Also to use it responsbility and know what's it talking about before blindly applying fixes 


- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think that ai generated code is fine but it's def still up to the user to apply fixes and apply some stuff yourself. For example, in web dev, ai can help you design the logic and how to create things but in the end it's up to you to deal with the UX stuff. Additionally, you should also know what the ai generated codes are saying instead of following it blindly as it can make mistakes and may not be able to catch some errors.