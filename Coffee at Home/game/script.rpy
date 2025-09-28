# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="#343D45")
define cat = Character("Fred", color="#ED872D")
define barista = Character("Barista", color="#94450B")
define lizard = Character("Lizard", color="#967117")
define them = Character("Customer", color="#967117")

default coffee_at_home=False
default fred_fed=False
default email_checked=False
default first_day=True
default current_location="Bedroom"
default coffee_order="tea"
default morning_fred="meow"

# The game starts here.
label start:
    "You awake on a crisp fall morning" 
    "the sun gently shines through the curtains next to your bed, kissing you on the cheek."

    "Except you didn't want kisses, you want coffee."

label bedroom:
    scene bedroom
    # play music "Destiny.mp3"
    if morning_fred != "meow":
        cat "[morning_fred]"

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
    if coffee_at_home == False:
        jump normal_coffee_shop
    if coffee_at_home == True and fred_fed == False:
        jump red_eye
    if coffee_at_home == True and email_checked == False:
        jump brewed_awakening

label normal_coffee_shop:
    scene shop

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
    jump arrive_at_home

label red_eye:
    scene shop
    "You arrive at the coffee shop. From the outside, you don’t hear anything, and it seems like the lights are off. Odd, but coffee shops these days have to differentiate themselves somehow, and you proceed inside."

    "When you enter it’s dark, and completely empty, save for the barista behind the counter whose back is it you."
    barista "Human life is inexplicable, and still without meaning: a fool may decide its fate."
    
    "You think to yourself, “what an odd way to take an order”, aloud you say, [coffee_order], please?"
    barista "Dead are all gods."

    "The barista starts to climb over the counter."


default attempt_flee = False
default turn_back = False
default barista_death = False
default reason_with = False
default break_door = False

label red_eye_fight_loop:
    while barista_death == False:
        menu:
            "What do you do?"

            "Run away" if reason_with == False:
                $ reason_with = True
                "You run back to the front door, only to find it locked itself behind you."
                menu:
                    "Turn back" if turn_back == False:
                        $ turn_back = True
                        "The barista is in front of you"
                        jump red_eye_fight_loop
                    "Throw yourself against the door" if break_door == False:
                        $ break_door = True
                        "You throw the weight of your fear against it, but the door an in immovable object."
                        jump red_eye_fight_loop
                    "Attack": 
                        "They crumple like a paper cup."
                        $ barista_death = True
                        jump post_red_eye_fight
            "Attempt to reason" if reason_with == False:
                $ reason_with = True 
                you "Woah, I didn’t mean anything by it."
                "The barista coontinues to climb towards you, and begins to growl"
                jump red_eye_fight_loop
            "Attack":
                "You punch the barista in the face. They crumple like a paper cup."
                jump post_red_eye_fight


default observed_corpse = False
label post_red_eye_fight:
    "They lie on the ground, still, cold, dead. Before your eyes their lifeless body begins to decay" 
    "at first glance. Falling away from a human form into what appears to be dirt"
    "but on a second glance, you see that they are becoming a pile of coffee beans."
    
    while observed_corpse == False:
        menu:
            "What do you do?"
            "Inspect the pile":
                "As you lean down to inspect the pile further, something catches your eyes"
                "you find that a dust pan and a small hand broom have appeared in your hands. "
                "“Where did those come from?” You ask yourself." 
                "Then, you notice yourself wearing an apron,"
                "much like the one the former Barista was wearing. "

            "Inspect myself":
                "You observe your body, still shaking a little from the altercation." 
                "Your arms covered in a thin layer of goosebumps,"
                "there are coffee stains on your clothes, and you hands have coffee grounds all over them." 
                "Who will wipe this coffee off of you? What water will you use to clean yourself?"

            "Inspect the body":
                $ observed_corpse = True
                "The barista is dead."
                menu:
                    "prod them":
                        "The barista stays dead"
                    "shout":
                        "The barista stays dead"
    menu:
        "What do you do?"
        "Sweep the beans":
            "The lights all come on, and the smell of coffee greets your nose."
            "Someone walks through the door, “I’ve been wanting to try this place. One cup of coffee, [coffee_order], please!” "
        "Try the door":
            "Still locked."
            "You are the barista now."
            
    menu:
        "What do you do?"
        
        "Make the coffee":
            "You’ve never run an espresso machine before," 
            "but all the knowledge that you need comes to you," 
            "as if you’ve done this one thousand times before."
            "You wash away the sin of your crime in espresso, you work the remainder of the day in this coffee shop. "
            jump arrive_at_home
        "Try to explain what happened to this person":
            you "I’m not the barista."
            them "So why are you wearing the apron and uniform?"
            menu: 
                "I killed the barista.":
                    you "They attacked me, and bled to death on the floor, but then they turned into these coffee beans."
                    them "Don’t hurt me! Don’t come any closer."
                    "This person is very clearly alarmed and starting to panic."
                    "They pick up a nearby coffee mug and throw it at you. It hits you in the head."
                    "You pass out."
                    jump bedroom

                "I found it.":
                    them "Very funny. To go, please"
                #TODO Direct to either “Make the coffee” or “Try to explain”

label brewed_awakening:
    scene shop
    "How did you find this place?"

label arrive_at_home:
    scene kitchen
    "You arrive at home, what a nice little coffee shop."
    
    menu:
        "Did you finish your coffee?"

        "Save it for later.":
            "Fred greets you"
            $ morning_fred = "And once you are awake, you shall remain awake eternally."
            "and you assume he would like a pet. You pet Fred."
            $ coffee_at_home = True

        "I did finish it, yum!":
            "Fred greets you"
            $ morning_fred = "Was that life? Well then, once more!"
            "and you assume he would like a pet. You pet Fred."

    "The rest of the day passes as lovely as that first sip of coffee."
    "Your heart is warm and light. Fred takes an adorable nap in the sun, and you lie down on the floor in the afternoon light to take a nap with him."

    jump bedroom

    return
