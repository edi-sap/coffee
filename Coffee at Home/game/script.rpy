# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="#343D45")
define cat = Character("Fred", color="#ED872D")
define barista = Character("Barista", color="#94450B")
define lizard = Character("Lizard", color="#967117")

default coffee_at_home=False
default fred_fed=False
default email_checked=False
default first_day=True
defautl current_location="Bedroom"

# The game starts here.
label start:
    show bedroom
    # play music "Destiny.mp3"

    "You awake on a crisp fall morning, the sun gently shines through the curtains next to your bed, kissing you on the cheek."

    "Except you didn't want kisses, you want coffee."

    "Your head hurts and looking at the clock (read: cellphone) you realize you’ve overslept a bit." 

    "Rising out of bed, you give a stretch that makes your cat Fred proud, which he communicates by way of meow. It could also mean he is hungry."

    menu:
        "What do you do?"

        "Check email":
            jump email
        "Go to Kitchen":
            jump kitchen

label email:
    $ email_checked=True
    "You see an email forwarded from your friend Lizard,"
    lizard "Check out this new coffee shop! They’re doing a $3 special for coffee this week! -- Liz"
    "Fred yells at your in protest for paying attention to anything else."
    
    menu:
        "What do you do?"

        "Head to check out the coffee shop":
            jump neighborhood
        
        "Go to the kitchen":
            jump kitchen

label kitchen:
    show kitchen
    current_location="kitchen"
    
    default kitchen_information = "Your kitchen is a bit of a mess, and your cat Fred meows at you in protest of your late slumber."
    default cabinet_information = "Bummer! Completely empty. Guess you have to go out for coffee."

    if email_checked == True:
        "[kitchen_information]"
    else: 
        "[kitchen_information] Your phone beeps, indicating a new notification."
        
    menu:
        "What do you do?"

        "Check cabinets for coffee":
            "[cabinet_information]"

        "Feed Fred":
            cat "At last! To live is to suffer."
            "says Fred, which he communicates by way of meow. Always such a concise fellow."

        "Check email":
            if email_checked == False:
                jump email
            else:
                "No new messages."

label neighborhood:
    show outside
    "Outside"

    return
