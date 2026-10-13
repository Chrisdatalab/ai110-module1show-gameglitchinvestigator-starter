# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Incorrect High/Low Hint50| lower| higher| error|
| New Game Does Not Reset State| | | |
| Incorrect Attempt Counter| | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude suggested reversing the High/Low hint messages in both branches of the check_guess function. I accepted this suggestion because the outcome labels were correct, but the displayed messages were reversed. I reviewed the Git diff and confirmed that only four messages were changed. Claude also tested six inputs to verify the updated messages.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
Claude suggested an optional experiment to temporarily restore the old incorrect hint messages in a separate copy of the code. This would help verify that the tests could detect the original bug. However, I decided not to do this because it was beyond the scope of the assignment. Instead, I used pytest to verify the corrected logic. All eight tests passed. I also reviewed the code changes to confirm that the incorrect messages had been replaced.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I reviewed the code changes and compared the actual results with the expected results. I also used pytest to check whether the functions worked correctly. I considered a bug fixed when the code produced the expected results and the relevant tests passed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested check_guess(9, 50). The expected result was "Too Low" with a "Go HIGHER" message. Before the fix, the game sometimes compared numbers as strings and returned the wrong result. After the fix, the test passed. This showed that the function correctly compares integer values.
- Did AI help you design or understand any tests? How?
Yes. Claude helped me create pytest tests for the two bugs. It suggested testing numbers with different digit counts, such as 9 and 50, because string comparison could produce incorrect results. Claude also explained why the original tests failed. After updating the tests, all eight tests passed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
