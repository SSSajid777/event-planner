#Authors: Sajid Ihsan Abdullah and Denis
#Date: 04 April, 2025
#Description: Making Event Planner which incorporates if statements, for and while loops.

print("Welcome to the Event Planner!")
 

#Get event type from user 
#Using loop to 

while True:
    event_type=input("Enter the event type, options are casual or formal (case sensitive): ")
    if event_type== "formal" or event_type=="casual":
        break
    print("Error: Please enter either formal or casual (case sensitive)")
    
