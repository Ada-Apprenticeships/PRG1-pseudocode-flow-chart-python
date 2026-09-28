"""
Day 1, Example 1: Taxi Fare Calculator (sequence only)
 
Python version of the pseudocode in Day1_PseudocodeFlowchart_Examples.md.
Written to follow the pseudocode line for line, top to bottom, so the two can
be read side by side. No functions, no loops, no conditions: just sequence.
 
Trace to check: distance_miles = 4, waiting_minutes = 10 gives a fare of 10.80
"""
 
BASE_CHARGE = 3.50
RATE_PER_MILE = 1.20
RATE_PER_MINUTE_WAITING = 0.25
 
distance_miles = float(input("Distance travelled in miles: "))
waiting_minutes = float(input("Waiting time in minutes: "))
 
distance_charge = distance_miles * RATE_PER_MILE
waiting_charge = waiting_minutes * RATE_PER_MINUTE_WAITING
 
total_fare = BASE_CHARGE + distance_charge + waiting_charge
 
print(f"Your fare is £{total_fare:.2f}")