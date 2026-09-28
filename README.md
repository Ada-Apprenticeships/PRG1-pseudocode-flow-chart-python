# Day 1: Questions on the three examples

You have three short Python programs in this Codespace:

- `example1.py`
- `example2.py`
- `example3.py`

You are not being asked to write any code today. You are being asked to read
these, run them, and work out what they do and why they do it that way.

## How to work through this

1. Run the program first, before reading it properly. Watch what it does.
2. Then read it line by line and match it against the pseudocode and flowchart
   you worked through with your partner.
3. Answer the questions out loud with your partner before writing anything
   down. If you cannot say it out loud, you do not understand it yet.
4. Where a question says "predict first", commit to an answer before you run
   it. Getting a prediction wrong is far more useful than getting it right.

To run a program, open the terminal and type, for example:

```
python example1.py
```

If `python` is not recognised, use `python3` instead.

---

## Example 1: Taxi Fare Calculator

Run it with a distance of `4` miles and a waiting time of `10` minutes.

1. Some of the names in this program are written in capitals and some in lower
   case. What is the difference between the two groups? How could you work
   that out from the code alone, without anyone telling you?

2. Look at the line that collects the distance. It has `float(...)` wrapped
   around `input(...)`. Predict what would happen if you removed `float` and
   its brackets, then try it. Why does it behave that way?

3. The taxi firm puts its per-mile rate up to £1.45. Which single line changes?
   Which lines definitely do not?

4. Run it again and type a negative distance, such as `-5`. What does the
   program do?

> **Something to think about**
>
> The program accepted the negative distance quite happily and gave you an
> answer. Is that a fault in the program, or is it working exactly as it was
> written? Those are two different questions, and the difference between them
> is most of what debugging actually is.

---

## Example 2: Free Delivery Checker

Run it twice. First with an order total of `25` and a weight of `12`. Then
with an order total of `45` and a weight of `15`.

1. In the second run, the order is over the free delivery threshold **and**
   it is heavy. Which delivery charge did the program apply, and which line of
   code decided that?

2. Find the decision that can only ever be reached when the first decision was
   false. How can you tell, just from reading, that it is unreachable
   otherwise?

3. The pseudocode has `ENDIF` to mark where each branch finishes. This Python
   has nothing of the sort. So how does Python know where a branch stops?

4. Predict, then check: an order total of exactly `40` with a weight of `20`.
   Which charge applies, and why does the exact boundary matter?

> **Something to think about**
>
> Once free delivery applies, weight is never checked at all. A 30kg order
> over £40 ships free. Is that a mistake in the code, or a decision the shop
> made? You cannot tell by reading the program. Think about what you would
> need to know, and who you would have to ask, to find out. This is the
> everyday reality of reading code you did not write.

---

## Example 3: Fitness App Rep Counter

Run it with a target of `5`. Press Return three times, then type `STOP`.

1. This loop can finish in two completely different ways. What are they? Which
   one happened in the run above?

2. What is `user_stopped` actually for? The loop already checks the rep count,
   so why is a second thing being tracked at all?

3. Predict first, then run it: set the target to `0`. Does the loop body run
   even once? What message do you get? Is that message honest?

4. In the pseudocode this program uses `DETECT` rather than `INPUT`, because
   the signal is meant to come from a sensor on a phone, not from someone
   typing. The Python uses `input()` because there is no sensor here. Does
   swapping one for the other change the logic of the program in any way?

> **Something to think about**
>
> This loop checks its condition *before* running the body, which is why a
> target of `0` behaves the way it does. Some languages offer a loop that
> checks its condition at the end instead, so the body always runs at least
> once. What kind of program would actually want that? Do not try to settle
> this now. We come back to it properly when we cover iteration.

---

## Across all three

- Which of the three programs would be hardest to explain to someone who has
  never seen code before? What specifically makes it harder?

- Every one of these programs trusts whoever is typing to enter something
  sensible. Pick each program in turn and find one input that would break it
  or produce nonsense. You do not need to fix anything, just find them.

- If you had to describe what each program does in a single sentence, without
  using any of the variable names, could you? Try it. That is the skill this
  whole module is built around.
