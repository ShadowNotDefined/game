version = 0.01

##################################################
##################################################
###                                            ###
###                Quick Tools                 ###
###                 for devs                   ###
###                                            ###
##################################################
##################################################

# if q_response == "s":
# add save feature later.
# elif q_response == "y":
#          print("")
# else:
#           print("")

##################################################
##################################################
###                                            ###
###                   Modules                  ###
###                                            ###
##################################################
##################################################

import time

##################################################
##################################################
###                                            ###
###                Introduction                ###
###                                            ###
##################################################
##################################################


def get_name():
        name = input("What is your name?\n")
        name_check = input("Double checking. Your name is " + name + "? (y/n)\n")
        if name_check == "y":
                print("Hello " + name + "...\n\n")
        elif name_check == "n":
                get_name()
        else:
                print("That was not y or n. Type your name again.\nAnd follow instructions this time...")
                get_name()

print("You CANNOT Finish This. (probably)\n v" + version + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

time.sleep(10)

print("""
All answers must be y/n unless I say otherwise.

I will keep track of thing likes your sanity, happiness, intelligence
and MANY other things to.

Don't worry, all of your answers are just between us.
If you don't feel safe, feel free to diconnect from the internet.
I don't need it for anything.

My creator plans on having lots of questions.
He is also working on a save feature.
""")

if version < 1.0:
        print("Thank YOU for beta testing for version " + str(version) + "!\nIt is highly appreciated.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

get_name()



##################################################
##################################################
###                                            ###
###              Player Variables              ###
###                                            ###
##################################################
##################################################

sanity = 0

happiness = 0

intelligence = 0

luck = 0

charisma = 0


##################################################
##################################################
###                                            ###
###                Gameplay                    ###
###                                            ###
##################################################
##################################################

q1_response = input("Are you alive? (y/n)")
if q1_response == "y":
        print("I thought so.")
else:
        print("...Seriously...fine whatever...\nThis is going to be added to your data.")
        sanity = sanity - 1
        intelligence = intelligence - 1