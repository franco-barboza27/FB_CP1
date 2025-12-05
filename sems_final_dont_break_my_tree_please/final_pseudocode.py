# FB TBAG final

# BIGGEST PRIORITITIES
    # 1) Make Rooms and menus for each room (action selections to interact with things)
    # 2) Make a player variable that I can keep track of across rooms without using global but also permanently change however I need
    # 3) Make an inventory that is kept track of and can be accessed from most places
    # 4) implement two different fighting systems that change based on choice at beginning of the game
# Later priorities
    # 5) Tun and Nan fight
    # 6.1) Figure out the test fights (Math, Chem and history)
    # 6.2) Figure out the dream fights
    # 7) Figure out the final fight
# Least prioritie-ish
    # 8) Balancing
    # 9) Dialog improvement

# POSSIBLE METHODS FOR 1)-4)
    # 1) 
        # I could make functions for each of the rooms and basically do something similar to my combat program 
        # where each function could lead to a different function
        # Each room will be very similar in code except for ones that have a combat encounter
            # room name(take Player as parameter)
                # make a menu that presents their options (ex: 1) Check desk 2) make coffee 3) Go outside
                    # count = 1 (to keep track of items in an ordered list)
                    # for every option in the menu:
                        # display the first number of a list (1)(count) and the option
                        # increase said number by 1
                    # if statement that checks what they chose
                # then, depending on that choice, execute whatever dialog needed, and if they're going to a new room, start the function for that room
                # otherwise, inspect/do whatever thing they chose
                # examples of a few menu out comes
                    # if they get an item from their action:
                        # check if they already have the item in their collected items list or not
                        # if not, put it into their inventory AND into their "collected items" list 
                    # if it's just dialog:
                        # print the dialog
                    # if they leave the room:
                        # call the function for the room they go to which should have similar code to this one because it'll be based on the same "create option menu, ask for choice, do action depending on choice"
                    # if they encounter COMBAT go to the functions for combat of 4)-7)
    # 2)
        # I need to hold stats, items, and skills inside of 
        # or with a player variable (and maybe a name as well?)
        # I would have to make this right after the user chooses a given route (4))
        # meaning the loop for the first tutorial fight will be right before
                    # combat loop:
                        # if they die, go back to the loop before by breaking this one
                        # if they win, go to the correct function (either the bedroom function or the forest function)
        # Make a player variable that is similar to the one below after they choose who to fight (4))
            # player = [{state-state:alive/dead}, {stats-name:statamount}, {statmax-name:maximum}, {skillscost-name:skillcost}, 
            # [skillsdesc], {items-name:desc}, [collected items-itemname]]
            # ("-" seperates what the thing holds and how it'll be formatted)
                # This way its all stored in one place although I'll have to use a function to do the correct thing on skills and items
                    # testing a way to get desctiptions of things and their values (it works, if the things are in the same locations so if item1 is in index 0 then item1's description should be placed in index 0 of another list):
                        # example of this code
                            # testlst = [{"val":1, "thing":3, "bloop":50}, ["This is a value it costs 1 dolla", "This is a thing it costs 3 dolla", "This is a bloop it costs 50 dolla"]]

                            # count = 0
                            # for item in testlst[0]:
                                # print(f"{item}:\n{testlst[1][count]}")
                                # count += 1


    # 3) 
    # this one gets taken care of with the in player list dict, I'll need to make a function that checks what item it is, 
    # do the effect and then remove the item from the inventory
    # However I'll need to convert the menu (like the thing that asks which one they do "1) item1, 2)item2..." 
    # into the item name because otherwise it'll be given a number(technically str) rather than the name of the item 
    # which isn't gauranteed to match each time.)
    # to seperate routes and make it more easy to manage, there will be a function for items from both worlds, use the same structure as the example below but change things inside the if statements and rename the function to match the given route
        # items FUNCTION
            # routeitems(item choice, items list(the menu used when a player chooses to uses an item), player)
                # item choice -= 1 (converts the number to be correspondent with the index of the previous list)
                # set item choice to int data type
                # item choice = itemlist[index-itemchoice] (converts the number into the name)
                # check each individual item, manually
                # the dots are for specific actions that the item does
                # ex, one may be player[0]["stat"] += 10
                    # if item choice is specific item that restores a player stat:
                        # player[index of the where the "name" stat is being stored]["stat being restored"] += 10
                        # overstat = player stat(^) minus the player statmax(player[stats maximum]["the name of stat"])
                        # player stat -= overstat (this makes sure it doesn't increase X stat over their maximum amount of the stat)
                    # or if item choice is item that does damage to the enemy
                        # return the amount of damage and the word "damage"
                        # (after each item use, check for keywords such as "damage" do the amount of damage returned by changing the enemy health by the amount, and then go to the enemy turn in the same way the combat program did turns)
                    # or if item choice is cheat sheet
                        # list of chance is [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] (10% chance of getting caught)
                        # random amount of questions answered (rand.int)
                        # see if they get caught and then set the player state to dead and return, ending the fight
                        # then, if they aren't dead, return the amoint of questions they answered
                            # Outside of the function, check if they used cheat sheet, then check if it returned as player being dead- if not do that much damage to the test
    # 4) 
    # In the dream world fighting can be done like the combat program where each entity got their own function for their turn.
    # Since in the real world, the tests dont fight back, it could just be one function with a loop checking if the player state is "dead"
    # or, if the test state is finished then, at the end of each turn it does whatever amount of groginess if neither is true

# 5)-7)

    # 5) The Tun and Nan fight
        # To begin, in this room the user will have the choice to either choose Tun or Nan after some dialog
            # have an if statement checking if they have a world route
            # after they choose, set the world route to whatever route they chose
            # 

    # 6.1
        # 6.1.0) Fight format (general code for all three fights)
            #
        # 6.1.1) math fight
            # for the debuff I can make an if statement checking if the debuff is false (0) then if it is false give them their turn
                # at the end of each turn, roll to see if they got the debuff and set it to a number (that makes sense )
            