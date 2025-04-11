#Authors: Sajid Ihsan Abdullah and Denis
#Date: 04 April, 2025
#Description: Making Event Planner which incorporates if statements, for and while loops.

print("Welcome to the Event Planner!")
print("Let's create the best event!") 

#Get event type from user 
#Using loop to prompt user to input again if the input is incorrect

while True:
    event_type=input(str("Enter the event type, options are casual or formal: ")).strip().lower()
    if event_type== "formal" or event_type=="casual":
        break
    print("Error: Please enter either formal or casual")


#Get event location from user
#Using loop to prompt user to input again if the input is incorrect

while True:
    event_location=input(str("Enter the event location, options are indoor or outdoor: ")).strip().lower()
    if event_location=="indoor" or event_location=="outdoor":
        break
    print("Error: Please enter either indoor or outdoor")


#Event selection

print("Select the type of event from the list below:")

if event_type=="casual" and event_location=="indoor":
    print("1. Birthday Party")
    print("2. Gender Reveal Party")
    print("3. Halloween")
    print("4. Easter")
    print("5. Christmas")
    print("6. Thanksgiving")
    print("7. None of the above")
    events_list=["Birthday Party","Gender Reveal Party", "Halloween", "Easter", "Christmas", "Thanksgiving","None of the above"]
elif event_type=="casual" and event_location=="outdoor":
    print("1. Outdoor Birthday Party")
    print("2. Outdoor Gender Reveal Party")
    print("3. Outdoor Barbeque")
    print("4. Family/Friends Picnic")
    print("5. None of the above")
    events_list=["Outdoor Birthday Party", "Outdoor Gender Reveal Party", "Outdoor Barbeque", "Family/Friends Picnic", "None of the above"]
elif event_type=="formal" and event_location=="indoor":
    print("1. Conferences")
    print("2. Workshop")
    print("3. Indoor Wedding")
    print("4. None of the above")
    events_list=["Conferences","Workshop", "Indoor Wedding", "None of the above"]
elif event_type=="formal" and event_location=="outdoor":
    print("1. Oudoor Wedding")
    print("2. Company Picnic")
    print("3. Charities/Fundraisers")
    print("4. None of the above")
    events_list=["Outdoor Wedding", "Company Picnic", "Charities/Fundraiser", "None of the above"]



while True:
    try:
        events_choice=int(input("Enter the number of the event to choose: "))
        if (events_choice)>=1 and (events_choice)<=(len((events_list))):
            event=events_choice
            break
        else:
            print("Error: Enter a valid number from 1-",(len(events_list)))
    except TypeError as e:
        print("Error", e)


        
    
    


    
    
