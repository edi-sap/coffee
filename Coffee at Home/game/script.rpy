# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="#343D45")
define cat = Character("Fred", color="#ED872D")
define barista = Character("Barista", color="#94450B")
define lizard = Character("Lizard", color="#967117")
define them = Character("Customer", color="#967117")
define neighbor = Character("Neighbor", color="#967117")

default coffee_at_home=False
default day_plus = False

# Red Eye Vars
default attempt_flee = False
default turn_back = False
default barista_death = False
default reason_with = False
default break_door = False
default become_barista = False
default assimilate = False
default explain_it = False
default observed_corpse = False
default passed_out = False

# Brewed Vars
default engage_with_neighbor = False
default continue_to_engage = False
default brewed_customer = False
default tea_drinker = False
default awake="They pick up another one, this one lands and hits you square between the eyes. Blood starts to run over your face, blocking your vision, and you start to remember… You are the critic. You did write all of those mean things."
default cabinets_checked = False

default current_location="Bedroom"
default coffee_order="tea"
default morning_fred="meow"
default fred_fed=False
default email_checked=False


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
    
    # Morning vars, must be reset each day.
    $ fred_fed = False
    $ email_checked = False

    "Your head hurts and looking at the clock (read: cellphone) you realize you’ve overslept a bit." 

    if coffee_at_home == True:
        you "Didn't I already do this?."
        "Quiet you, I'm telling a story here."
        if passed_out == True:
            you "My head hurts from the trauma!"
            "Well, clearly you're doing something wrong." 

    "Rising out of bed, you give a stretch that makes your cat Fred proud, which he communicates by way of meow." 

    "It could also mean he is hungry."
    if coffee_at_home == True:
        you "But I already fed him today."
        "Fred disagrees."

    menu:
        "What do you do?"

        "Check messages":
            jump email
        "Go to Kitchen":
            jump kitchen

label email:
    $ email_checked=True
    "You see a message from your friend Lizard"

    #TODO make phone screen
    lizard "Check out this new coffee shop! They’re doing a $3 special for coffee this week! -- Liz"
    "Fred yells at you, seemingly in protest for paying attention to anything else."
    
    menu:
        "What do you do?"

        "Head to check out the coffee shop":
            $ coffee_at_home = True
            jump neighborhood

label kitchen:
    scene kitchen
    "Your kitchen is a bit of a mess, and your cat Fred meows at you in protest of your late slumber."

label kitchen_options:
    # You MUST EITHER check your messages or feed fred.
    menu:
        "What do you do?"

        "Check cabinets for coffee" if cabinets_checked == False:
            "Bummer! Completely empty. Guess you have to go out for coffee."
            $ cabinets_checked = True
            jump kitchen_options

        "Feed Fred" if fred_fed == False:
            $ fred_fed = True
            cat "At last! To live is to suffer."
            "says Fred, which he communicates by way of meow. Always such a concise fellow."
            jump kitchen_options

        "Head out in search of coffee":
            # $ leaving_house = True
            if fred_fed == False and email_checked == False and cabinets_checked == False:
                "Fred really insists you feed him before you leave by running underneath your legs and feet."
                jump kitchen_options
            
            else:
                jump neighborhood

label neighborhood:
    scene outside
    "The weather today is lovely, absolutely perfect light sweater weather." 
    "A nice warm beverage would absolutely pull this morning together, top ten of the year, probably." 
    if email_checked == True:
        "The new coffee shop isn’t a far walk from your house, and you see a few of your neighbors and favorite dogs on the way there." 
    if email_checked != True:
        #TODO make flyer
        "While walking, you see a sign for a new coffee shop and decide to go and check it out."
    
    "A cute golden retriever walking their human starts to pull towards you when it sees you."
    neighbor "Hey, good to see you! Have a good morning."
    "They stop and let you pet their dog, who is elated at this"
    
    if cabinets_checked == False && day_plus == True:
        $ coffee_at_home = True

    if coffee_at_home == False:
        jump normal_coffee_shop
    if coffee_at_home == True and fred_fed == False:
        jump red_eye
    if coffee_at_home == True and email_checked == False:
        jump brewed_awakening
    if coffee_at_home == True and tea_drinker == True:
        jump normal_coffee_shop


label normal_coffee_shop:
    scene shop_good

    "You arrive at the coffee shop. It’s super cozy in here."
    
    if tea_drinker == True:
        you "What is going on?"
        "Quiet you, I'm telling a story here."

    "There’s also no line, what luck! There’s only one person taking orders and making drinks. "

    "You approach"

    barista "Hi there!"
    "the barista greets you, warmly."

    barista "What can I get for you?"

    menu:
        "One cup of coffee please..."

        "with milk":
            $ coffee_order = "with milk"

        "with milk and sugar":
            $ coffee_order = "with milk and sugar"
        
        "black":
            $ coffee_order = "black"

        "actually... can I just have tea?" if tea_drinker == True:
            jump brewed_ending

    "The barista hands you your order"
    barista "One cup of coffee [coffee_order]!"
    "...and its delicious! Definitely one of the best cups of coffee you’ve ever had. "
    jump arrive_at_home

label red_eye:
# cat not fed 
    scene shop_bad
    "You arrive at the coffee shop. From the outside, you don’t hear anything, and it seems like the lights are off. Odd, but coffee shops these days have to differentiate themselves somehow, and you proceed inside."

    "When you enter it’s dark, and completely empty, save for the barista behind the counter whose back is it you."
    barista "Human life is inexplicable, and still without meaning: a fool may decide its fate."
    
    "You think to yourself, “what an odd way to take an order”, aloud you say, [coffee_order], please?"
    barista "Dead are all gods."

    "The barista starts to climb over the counter."

label red_eye_fight_loop:
# Cat not fed.
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
                "Who will wipe this caffienated sin off of you? What will you use to clean yourself?"

            "Inspect the body":
                $ observed_corpse = True
                "The barista is dead."
                menu:
                    "prod them":
                        "The barista stays dead"
                    "shout":
                        "The barista stays dead"


label red_eye_dispose_barista:

    while become_barista != True:
        menu:
            "What do you do?"

            "Sweep the beans":
                "The lights all come on, and the smell of coffee greets your nose."
                $ become_barista = True

            "Try the door":
                "Still locked."
                "You are the barista now."

label red_eye_become_barista_opening:
    "Someone walks through the door."
    "You recognize this person from your walk here, they live in the neighborhood."
    "You said hello to them"

    them "I’ve been wanting to try this place. One cup of coffee, [coffee_order], please!"

label red_eye_become_barista_ending_choice:
    menu:
        "What do you do?"
        
        "Make the coffee":
            "You’ve never run an espresso machine before," 
            "but all the knowledge that you need comes to you," 
            "as if you’ve done this one thousand times before."
            "You wash away the sin of your crime in espresso, you work the remainder of the day in this coffee shop. "
            $ assimilate = True
            jump fred_ending

        "Try to explain what happened to this person":
            you "I’m not the barista."
            them "So why are you wearing the apron and uniform?"
           
            menu: 
                "Talk about the fight":
                    you "I killed the barista. They attacked me, and bled to death on the floor, but then they turned into these coffee beans."
                    "This person is very clearly alarmed and starting to panic."
                    them "Don’t hurt me! Don’t come any closer."
                    "They pick up a nearby coffee mug." 
                    menu:
                        "Insist it's not what it looks like":
                            you "It's not what it looks like. They started it, I was protecting myself."
                            "They don't respond, fear still visibly alight in their eyes and audible their panicked breath."
                            "At this moment, they throw the mug they were holding at you." 
                            "It hits you in the head."
                            "You pass out."
                            $ passed_out = True
                            jump bedroom

                        "Attack":
                            "You swing back with the broom, poised to strike."
                            "At this moment, they throw the mug they were holding at you." 
                            "It hits you in the head."
                            "You pass out."
                            $ passed_out = True
                            jump bedroom

                "Pretend nothing happened":
                    you "I found it. It was on the floor when I got here."
                    them "Very funny. To go, please."
                    jump red_eye_become_barista_ending_choice


label brewed_awakening:
    # Do not check your phone. Need to create loop to get to the shop if no phone.
    scene shop_good
    "You arrive at the coffee shop, and there are a few people that seem to recognize you hanging around."
    "You don’t think that you remember any of them, but maybe you have one of those faces?"

    "One of them waves at you you."
    menu:
        "What do you do?"

        "Pretend you didn’t see them and look away":
            "Turning away, you see out of the corner of your eye the person looks visibly hurt."
        "Smile politely and wave in response":
            "They approach."
            $ engage_with_neighbor = True

    if engage_with_neighbor == True:
        them "Hey, how’s it going?"
        "they ask you, with recognition in their eyes."
        menu:
            "You have no idea who this is."

            "Hey! Oh, pretty good. how about you?":
                them "Oh, pretty good myself. Didn’t think I’d see you here, of all people."
                jump continue_to_engage
            "Sorry, I can’t seem to remember you...":
                "They wink at you"
                them "Laying low, I see."
                "the stranger walks away"
                jump brewed_order
    else:
        "You approach the counter, the barista is looking at you with a look on their face of what appears to be disgust."
        jump brewed_order

label continue_to_engage:
    "Well you're in this conversation now..."
    menu:
        "Oh? You didn't?":
            them "After what you said? You're a monster."
            "They laugh, clapping you on the shoulder"
            "You stand there, confused, and then the person departs."
            
        "Hah, me neither.":
            them "If they can't even get a coffee [coffee_order], right, do they even deserve to live?"
            "They laugh, clapping you on the shoulder"
            "You stand there, confused, and then the person departs."
    
    jump brewed_order



label brewed_order:
    if engage_with_neighbor == True:
        "You approach the counter, the barista is looking at you with a look on their face of… what appears to be disgust."
    else:
        "Weird."

    menu:
        "What do you do?"

        "Order a coffee":
            you "One cup of coffee, [coffee_order], please."

        "Wait. Clearly they aren’t ready to take my order":
            "The barista narrows their eyes at you"
            barista "The silent treatment? Is that how you want to play it?" 
            barista "Did you think I wouldn’t recognize you? Do you think I don’t know who you are?"
    
    barista "What are you doing here?" 
    menu:    
        "there is a definite a note of hostility in their voice."

        "Maintain your innocence, you're just ordering a coffee":
            you "Ordering a coffee... I think."
        "Try to de-escalate the situation":
            you "Woah, I don't want any trouble."

    menu:
        "How do you know who I am?":
            barista "Very funny."
            "The barista reaches under the counter and pulls out a flyer with your face on it." 
            "It reads cities #1 coffee critic destroys local coffee shop in latest review." 
            
        "I've been here before.":
            barista "I know"
            "The barista reaches under the counter and pulls out a flyer with your face on it." 
            "It reads cities #1 coffee critic destroys local coffee shop in latest review." 
            
    menu:
        "They evidence is pretty damning..."

        "There must be some mistake.":
            barista "It's insulting that you think I’m stupid enough to believe that."
        "That’s not me.":
            barista "It's insulting that you think I’m stupid enough to believe that."

    "The barista picks up a coffee cup" 

    barista "Would you like your coffee to go?" 
    "They throw the mug at you, they miss."

    menu:
        "Well that escalated quickly."

        "Head for the door":
            "You turn around and run for the door."
            "Approaching, you notice that it appears to be night outside."
            "You're getting out of here, though."
            "You open the door and step into the darkness"
            jump bedroom

        "Shout at them to stop":
            "[awake]"

    menu:
        "Well well well, if it isn't the consequences of your own actions..."
        
        "Apologize":
            $ tea_drinker = True
            you "Hey, I’m sorry… I think I did write that, but I haven’t been myself lately."
            you "I think there's something... wrong with me, and I'm stuck in a time loop until I figure it out."
            barista "Come back and order tea."
            you "What?"
            barista "Come back tomorrow, order a tea, and it'll all be over."
            you "How do you know that? Did you trap me here?"
            barista "Just do it. You have to sleep now."
            "The barista points towards the door, in which appears to be night outside"
            you "I don't want to go back out there."
            barista "You must."
            
            "You turn around and run for the door."
            "Approaching, you notice that it appears to be night outside."
            "You're getting out of here, though."
            "You open the door and step into the darkness"
            jump bedroom

        "Double down":
            $ brewed_customer = True
            you "I said what I said, and judging by the fact that you just assaulted me, I didn't say enough."
            "The barista goes glassy eyed, and starts to cry."
            "Another customer approachs you and pushes you. Its the neighbor from before."
            neighbor "What is wrong with you? Why are you such a monster? How could you be so cruel?"
            menu:
                "Double down, harder.":
                    you "They make a bad product, I'm just the messenger."
                "Question the interloper":
                    you "Who are you to involve yourself with this? Why don't you mind your own business?"

            "The person starts to push you towards the front door."
            neighbor "Why don't you just leave?"
            neighbor "Clearly no one wants you here. I don't know why anyone would want you anywhere."
            "The barista continues to sob loudly in the background, and another neighbor member has come over to soothe them."
            "Along with their dog, who once said hello to you but now looks at you with disappointment on its face."
            "Another person has opened the door, and more customers have joined in pushing you out of the coffee shop"

            "You turn around and run for the door."
            "Approaching, you notice that it appears to be night outside."
            "You're getting out of here, though."
            "You open the door and step into the darkness"
            jump bedroom

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
    jump fred_ending

label fred_ending:
    "The rest of the day passes as lovely as that first sip of coffee."
    "Your heart is warm and light."
    "Fred takes an adorable nap in the sun, and you lie down on the floor in the afternoon light to take a nap with him."
    $ day_plus = True
    if assimilate == True:
        "Fred says something."
        jump red_ending
    else:
        jump bedroom

label red_ending:
    #TODO: What is the red ending?
    "Y'all come back now, hear?"
    return

label brewed_ending:
    #TODO: This is tea nirvana. You've been having too much caffiene. 
    "Don't come back now, hear?"
    return
