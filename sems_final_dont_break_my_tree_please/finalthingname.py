# FB TBAG final

# BIGGEST PRIORITITIES
    # 1) Make Rooms and menus for each room (action selections to interact with things)
    # 2) Make a player variable that I can keep track of across rooms without using global but also permanently change however I need
    # 3) Make an inventory that is kept track of and can be accessed from most places
    # 4) implement two different fighting systems that change based on choice at beginning of the game

# POSSIBLE METHODS
    # 1) 
        # I could make functions for each of the rooms and basically do something similar to my combat program where each function could lead to a different function
    # 2)
        # I need to hold stats, items, and skills inside of or with a player variable (and maybe a name as well?)
        # I would have to make this right after the user chooses a given route, meaning the loop for the first tutorial fight will be right before
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
                            # player list = ["name", skills{1stskill:exp req, ...}, stats[val1/valtot, val2/valtot, val3/valtot], items[item1{things abt item}]]
                                # skills would need a function to tell more things about the skill
                                # items that are more complicated than just a stat change may require a different kind of storage
                            # player list = {name:"name", inventory:[stuff], health:100, speed:10, }...
                                # items become less specific
                                # I'd need a function for both items and skills
        # Chosen
            # player = [{stats-name:statamount}, {statmax-name:maximum}, {skillscost-name:skillcost}, [skillsdesc], {items-name:desc}]
                # This way its all stored in one place although I'll have to use a function to do the correct thing on skills and items

    # 3) this one gets taken care of with the in player list dict, I'll need to make a function that checks what item it is, do the effect and then remove the item from the inventory
        # items FUNCTION
            # itemsuse(item choice, player)
                # check each individual item, manually
                # the dots are for specific actions that the item does
                # ex, one may be player[0]["stat"] += 10
                # for a complicated one like the (planned) cheat sheet it could 
                    # if item choice == specific item:
                        # ...
                    # elif...
                        # ...
                    # elif...

                    