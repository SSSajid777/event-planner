#Authors: Sajid Ihsan Abdullah and Denis
#Date: 04 April, 2025
#Description: Making Event Planner which incorporates if statements, for and while loops.

print("Welcome to the Event Planner!")
print("Let's create the best event!") 

#Get event type from user 
#Using loop to prompt user to input if the input is incorrect

while True:
    event_type=input("Enter the event type, options are casual or formal (case sensitive): ")
    if event_type== "formal" or event_type=="casual":
        break
    print("Error: Please enter either formal or casual (case sensitive)")


#Get event location from user
#Using loop to prompt user to input if the input is incorrect

while True:
    event_location=input("Enter the event location, options are indoor or outdoor(case sensitive): ")
    if event_location=="indoor" or event_location=="outdoor":
        break
    print("Error: Please enter either indoor or outdoor (case sensitive)")



    
    
