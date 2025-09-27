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
default current_location="Bedroom"
default coffee_order="tea"

# The game starts here.
label start:
    "You awake on a crisp fall morning, the sun gently shines through the curtains next to your bed, kissing you on the cheek."

    "Except you didn't want kisses, you want coffee."

label bedroom:
    scene bedroom
    # play music "Destiny.mp3"
    "Coffee: [coffee_at_home]"
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
        
        "Go to the kitchen" if current_location !="kitchen":
            jump kitchen

label kitchen:
    scene kitchen
    $ current_location="kitchen"

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
    scene outside
    "The weather today is lovely, absolutely perfect light sweater weather." 
    "A nice warm beverage would absolutely pull this morning together, top ten of the year, probably." 
    "The new coffee shop isn’t a far walk from your house, and you see a few of your neighbors and favorite dogs on the way there." 
    "“Good morning!” some of them say, including the dogs."
    jump coffee_shop

label coffee_shop:
    scene shop

    "Coffee: [coffee_at_home]"
    if coffee_at_home == False:
        "You arrive at the coffee shop. It’s super cozy in here. There’s also no line, what luck! There’s only one person taking orders and making drinks. "

        "You approach"

        barista "'Hi there!' the barista says to you, warmly. "

        barista "What can I get for you?"

        menu:
            "One cup of coffee please..."

            "with milk":
                $ coffee_order = "with milk"

            "with milk and sugar":
                $ coffee_order = "with milk and sugar"
            
            "black":
                $ coffee_order = "black"

        "The barista hands you your order"
        barista "One cup of coffee [coffee_order]!"
        "...and its delicious! Definitely one of the best cups of coffee you’ve ever had. "

    if coffee_at_home == True:
        "Oh dear."

label arrive_at_home:
    scene kitchen
    "You arrive at home, what a nice little coffee shop."
    
    menu:
        "Did you finish your coffee?"

        "Save it for later.":
            "Fred greets you,"
            # TO DO: Move Fred Responses to the start of the day for a bit more fun text
            cat "And once you are awake, you shall remain awake eternally."
            "which again, he mostly communicates by way of “meow” and you assume he would like a pet. You pet Fred."
            $ coffee_at_home = True

        "I did finish it, yum!":
            "Fred greets you,"
            cat "Was that life? Well then, once more!"
            "which again, he mostly communicates by way of “meow” you must assume means he would like a pet. You pet Fred."

    "The rest of the day passes as lovely as that first sip of coffee."
    "Your heart is warm and light. Fred takes an adorable nap in the sun, and you lie down on the floor in the afternoon light to take a nap with him."

    jump bedroom

    return
