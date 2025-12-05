# FB TBAG final

# BIGGEST PRIORITITIES
    # 1) Make Rooms and menus for each room (action selections to interact with things) (aim to create modular room functions that require very minimal fundamental code changes from room to room(modular))
    # 2) Make a player variable that I can keep track of across rooms without using global but also permanently change however I need
    # 3) Make an inventory that is kept track of and can be accessed from most places
    # 4) implement two different fighting systems that change based on choice at beginning of the game
# Later priorities
    # 5) Skills function
    # 6) Tun and Nan fight
    # 7) Figure out the test fights (Math, Chem and history)
    # 8) Figure out the dream fights
    # 9) Figure out the final fight
# Least priority-ish
    # ) Balancing
    # ) Dialog improvement

# POSSIBLE METHODS FOR 1)-4)
    # 1) 
        # I could make functions for each of the rooms and basically do something similar to my combat program 
        # where each function could lead to a different function
        # Each room will be very similar in code except for ones that have a combat encounter
            # room name(take Player as parameter)
                # make a menu that presents their options (ex: 1) Check desk 2) make coffee 3) Go outside
                # depending on that choice, execute whatever dialog needed, and if they're going to a new room, start the function for that room
                # otherwise, inspect/do whatever thing they chose
                    # if they get an item from their action: 
                        # put it into their inventory and into their "collected items" (expanded on slightly in 2))
                        # before that though, check if they already have the item in their collected items list or not
                    # if it's just dialog:
                        # print the dialog
                    # if they leave the room:
                        # call the function for the room they go to with whatever needed arguments
                    # if they encounter COMBAT go to 4)-7)
    # 2)
        # I need to hold stats, items, and skills inside of 
        # or with a player variable (and maybe a name as well?)
        # I would have to make this right after the user chooses a given route, 
        # meaning the loop for the first tutorial fight will be right before
            # (example)
                # infinite loop:
                    # display("which will you choose")
                    # create the player to have the stats corresponding to the choice

                    # combat loop:
                        # if they die, go back to the loop before by breaking this one
                        # if they win, go to the correct function
        # possible data types for easy storage
            # LISTS, DICTIONARIES and CLASSES
                    # Allow me to store multiple values of different kinds
                        # possible specific ways
                            # player list = ["name", skills{1stskill:exp req, ...}, 
                            # stats[val1/valtot, val2/valtot, val3/valtot], items[item1{things abt item}]]
                                # skills would need a function to tell more things about the skill
                                # items that are more complicated than just a stat change may require a different kind of storage
                            # player list = {name:"name", inventory:[stuff], health:100, speed:10, }...
                                # items become less specific
                                # I'd need a function for both items and skills
        # Chosen (may be tweaked a little bit but this should be what it roughly looks like)
            # player = [{state-state:alive/dead, level:num, exp:num}, {stats-name:statamount}, {statmax-name:maximum}, {skillscost-name:skillcost}, 
            # [skillsdesc], {items-name:desc}, [collected items-itemname]]
            # ("-" seperates what the thing holds and how it'll be formatted)
                # This way its all stored in one place although I'll have to use a function to do the correct thing on skills and items
                    # testing a way to get desctiptions of things and their values (it works, if the things are in the same locations):

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
        # items FUNCTION
            # itemsuse(item choice, player)
                # check each individual item, manually
                # the dots are for specific actions that the item does
                # ex, one may be player[0]["stat"] += 10
                    # if item choice == specific item:
                        # ...
                    # elif...
                        # ...
                    # elif...
                        # for a complicated(one that does more than change a stat) one like the (planned) cheat sheet it could be:
                        # random amount of questions answered
                        # check weighted random to see if they get caught and then set the player state to dead and return, ending the fight
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
            # if not, ask them something like "Do you want to choose Tun's side or Nan's side?"
            # after they choose, set the world route to whatever route they chose
            # Then, check which route they chose and use the corresponding battle function with the corresponding battle
                # Tun and Non battle function should take the player as a parameter
    # 6)
        # 6.0\) Fight format (general code for all three fights)
            #
            # 6.0.1) math fight
                # for the debuff I can make an if statement checking if the debuff is false (0) then if it is false give them their turn (because the debuff skips turns and gives them sleepiness)
                    # at the end of each turn, roll to see if they got the debuff and set it to a number (that makes sense, too many would be OP)
    # 7)
    # 8)
    # Depends on how things go V
    # 9)
    # 10)