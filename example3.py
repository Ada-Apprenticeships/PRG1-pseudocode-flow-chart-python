"""
Day 1, Example 3: Fitness App Rep Counter (sequence + selection + iteration)
 
Trace to check: target_reps = 5, three reps then STOP, ends with
"Session ended early. You did 3 reps."
"""
 
target_reps = int(input("Target number of reps: "))
 
rep_count = 0
user_stopped = False
 
while rep_count < target_reps and user_stopped is False:
    # Stands in for DETECT in the pseudocode.
    next_rep_or_stop_signal = input("Press Return for a rep, or type STOP: ").strip().upper()
 
    if next_rep_or_stop_signal == "STOP":
        user_stopped = True
    else:
        rep_count = rep_count + 1
        print(f"Rep count: {rep_count}")
 
# The loop can end two different ways, so this check works out which happened.
if rep_count == target_reps:
    print("Target reached! Well done.")
else:
    print(f"Session ended early. You did {rep_count} reps.")