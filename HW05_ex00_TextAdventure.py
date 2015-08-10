#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Global variable
your_name = sys.argv[1]

# Body
def infinite_stairway_room(count=0):
    global your_name
    # Don't print this after every time you take the stairs!
    if count == 0:
        print "%s ,you walk through the door to see a dimly lit hallway." % (your_name)
        print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    print "What next?"
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print 'You take the stairs'
        if (count > 0):
            print "but you're not happy about it"
        infinite_stairway_room(count + 1)
    # option 2 == back away
    if next == "back away":
        print dead("Smart choice.")

def gold_room():
    global your_name
    print "%s, this room is full of gold.  How much do you take?" % (your_name)

    next = raw_input("> ")
    try:
        how_much = int(next)
    except:
        dead("Man, learn to type a number.")
    else:
        if how_much < 50:
            print "Nice, you're not greedy, you win!"
            exit(0)
        else:
            dead("You greedy bastard!")
    #This doesn't work if the number is, say, 55, 22, etc
    # if "0" in next or "1" in next:
    #     how_much = int(next)
    # else:
    #     dead("Man, learn to type a number.")

    # if how_much < 50:
    #     print "Nice, you're not greedy, you win!"
    #     exit(0)
    # else:
    #     dead("You greedy bastard!")


def bear_room():
    global your_name
    print "%s ,there is a bear here." % (your_name)
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next in ("take","honey"):
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next in ("open","door") and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    global your_name
    print "%s ,here you see the great evil Cthulhu." % (your_name)
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def back_room():
    global your_name
    print "%s, you are now in the back room. It's filled with awkward programmers. Go on, introduce yourself, don't be shy." % (your_name)
    raw_input("> ")
    print "Nobody cares. So you soon start programming Python, and never leave."
    exit(0)

##############################################################################
def main():
    global your_name
    # START the TextAdventure game
    print "%s , you are in a dark room." % (your_name)
    print "You can either choose to go through the left door, or the right door. If none entices you, you can choose to go on further. OR, are you bold enough to enter the back room?"
    #print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")
    #Case sensitive
    if next.lower() == "left":
        bear_room()
    elif next.lower() == "right":
        cthulhu_room()
    elif next.lower() == "further":
        infinite_stairway_room()
    elif next.lower() == "back":
        back_room()
    else: 
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
