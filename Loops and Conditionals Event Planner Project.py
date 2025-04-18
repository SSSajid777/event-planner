#Authors: Sajid Ihsan Abdullah and Denis
#Date: 04 April, 2025
#Description: Making Event Planner which incorporates if statements, for and while loops.

#import OpenAI
from openai import OpenAI

OPEN_AI_KEY=" "
#use your own API Key, the code won't work without it.



client=OpenAI(api_key=OPEN_AI_KEY)






print("Welcome to the Event Planner!")
print("Let's create the best event!") 

#Get event type from user 
#Using loop to prompt user to input again if the input is incorrect

while True:
    event_type=input(str("Enter the event type, options are casual or formal: ")).strip().lower()
    if event_type== "formal" or event_type=="casual":
        break
    else:
        print("Error: Please enter either formal or casual")
    


#Get event location from user
#Using loop to prompt user to input again if the input is incorrect

while True:
    event_location=input(str("Enter the event location, options are indoor or outdoor: ")).strip().lower()
    if event_location=="indoor" or event_location=="outdoor":
        break
    else:
        print("Error: Please enter either indoor or outdoor")
    


#Event selection

print("Select the event from the list below:")

if event_type=="casual" and event_location=="indoor": #events for casual and indoor
    print("1. Birthday Party")
    print("2. Gender Reveal Party")
    print("3. Halloween")
    print("4. Easter")
    print("5. Christmas")
    print("6. Thanksgiving")
    print("7. None of the above")
    events_list=["Birthday Party","Gender Reveal Party", "Halloween", "Easter", "Christmas", "Thanksgiving","None of the above"] #keeping the options in a list
elif event_type=="casual" and event_location=="outdoor": #events for casual and outdoor
    print("1. Outdoor Birthday Party")
    print("2. Outdoor Gender Reveal Party")
    print("3. Outdoor Barbeque")
    print("4. Family Picnic")
    print("5. None of the above")
    events_list=["Outdoor Birthday Party", "Outdoor Gender Reveal Party", "Outdoor Barbeque", "Family Picnic", "None of the above"] #keeping the options in a list
elif event_type=="formal" and event_location=="indoor": #events for formal and indoor
    print("1. Conferences")
    print("2. Workshop")
    print("3. Indoor Wedding")
    print("4. None of the above")
    events_list=["Conferences","Workshop", "Indoor Wedding", "None of the above"]  #keeping the options in a list
elif event_type=="formal" and event_location=="outdoor": #events for formal and outdoor
    print("1. Oudoor Wedding")
    print("2. Company Picnic")
    print("3. Charities/Fundraisers")
    print("4. None of the above")
    events_list=["Outdoor Wedding", "Company Picnic", "Fundraiser", "None of the above"]  #keeping the options in a list



while True:  #looping so that user has to input again if user gives a wrong input
    try:
        events_choice=int(input("Enter the number of the event to choose: "))  #user inputs the number of event from the list  
        if (events_choice)>=1 and (events_choice)<=(len((events_list))):
            event=events_list[events_choice-1]
            break
        else:
            print("Error: Enter a valid number from 1-",(len(events_list)))
    except:
        print("Error: Please enter a valid number")


#if none of the above is chosen

if event=="None of the above":
    while True:
        print("Since you chose none of the above, let's ask ChatGPT to help!")
        completion= client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
        {"role":"system", "content": "You are an event planner app"},
        {"role":"user","content": "Suggest 5 event types for" + event_type + " " + event_location + " event ideas with budget tips, weather tips, most frugal way to host the event, fun facts, food cost per person. Give budget options for number of attendees (example if 50 attendees and food cost per person is 20, what the budget should be) )"}
        ]
    )
        print(completion.choices[0].message.content) 
        #print("Thank you for using the Event Planner!")
        #break

else:
    if event=="Birthday Party":
        min_budget=300
        food_cost=12
        theme="Decorate venue with balloons"
        tip="Buy balloons in bulk from wholesale stores"
    elif event=="Gender Reveal Party":
        min_budget=250
        food_cost=10
        theme="Reveal gender with balloons instead of powder to save money"
        tip="Buy ballons in bulk from wholesale stores"
    elif event=="Halloween":
        min_budget=400
        food_cost=15
        theme="The theme should be spooky, carve pumpkins and wear a costume"
        tip="Buy costumes when they are in discount"
    elif event=="Christmas":
        min_budget=500
        food_cost=20
        theme="Decorate Christams tree with lights and buy gifts"
        tip="Buy gifts when they are in discount"
    elif event=="Thanksgiving":
        min_budget=350
        food_cost=18
        theme="Cook a turkey and enjoy the meal with family"
        tip="Buy turkey a day or 2 before Thanksgiving so that it is fresh"
    elif event=="Outdoor Birthday Party":
        min_budget=350
        food_cost=12
        theme="Have fun activities for children"
        tip="Tell the birthday child to hit a pinata, after which candies fall"
    elif event=="Outdoor Barbeque":
        min_budget=300
        food_cost=12
        theme="Enjoy eating Barbeque outside"
        tip="Buy meat in bulk from wholesale stores"
    elif event=="Family Picnic":
        min_budget=200
        food_cost=8
        theme="Enjoy sharing a meal with family/friends outside"
        tip="Make it potluck style to share cost"
    elif event=="Conferences":
        min_budget=1500
        food_cost=30
        theme="Dress code shoeuld be formal"
        tip="Provide digital materials instead of paper to save cost"
    elif event=="Workshop":
        min_budget=1200
        food_cost=20
        theme="Have interactive activities to do for hands-on experience"
        tip="For the best activities, charge a small fee to reduce cost"
    elif event=="Indoor Wedding":
        min_budget=10000
        food_cost=80
        theme="Elegant Decorations and have a cake for the bride and broom to cut"
        tip="Host the event on weekends or holidays so that people do not miss the wedding"
    elif event=="Outdoor Wedding":
        min_budget=10000
        food_cost=45
        theme="Outdoor site should have garden with flowers and lights"
        tip="Host the event on weekends or holidays so that people do not miss the wedding"
    else:
        event=="Fundraiser"
        min_budget=2500
        food_cost=25
        theme="Have tap to pay so that it is easier for people to donate"
        tip="Give attendees brochure about the impact of donations to encourage people to donate"



        
#Get attendees

while True:
    try:
        attendees=int(input("Enter the number of attendees: "))
        if attendees>0:
            break
    
    except:
        print("Error: Enter a positive integer")



#Get budget

while True:
    try:
        budget=float(input("Enter your budget: $"))
        if budget>0:
            if budget<min_budget:
                print("Warning:Your budget is less than the minimum budget.")
                while True:
                    confirm_budget=input("Are you sure you want to proceed with this budget?(yes/no): ").strip().lower()
                
                    if confirm_budget=="no":
                        print("Please enter a new budget")
                        break
                    elif confirm_budget=="yes":
                        break
                    else:
                        print("Enter either yes or no")
                if confirm_budget=="yes":
                    break
            else:
                    break
    except TypeError as e:
        print("Error, e")
                    




            
            
        
    
    
        
        
            
       
            

#total food cost calculation

food_cost_total=attendees*food_cost
food_cost_round=round(food_cost_total,2)
print("Your total food cost will be: $" + str(food_cost_round))



#import random
import random

#Random Weather advice for outdoor events


if event_location=="outdoor":
    weather=random.choice(["Sunny","Rainy","Cloudy","Windy","Snowy"])
    print("Weather Forecast:",weather)

    if weather=="Sunny":
        print("Weather Tip: Provide sunscreen and shaded areas")
    elif weather=="Rainy":
        print("Weather Tip: Consider renting a tent")
    elif weather=="Snowy":
        print("Weather Tip: Consider renting a tent and arrange heaters and warm drinks")
    elif weather=="Windy":
        print("Weather Tip: Set all decorations and tables securely")
    else:
        print("Weather Tip: Tell attendees to bring umbrella in case of rain")



print("Thank you for using our Event Planner!")       







