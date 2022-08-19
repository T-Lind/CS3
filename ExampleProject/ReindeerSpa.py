from collections import namedtuple
from itertools import count
from ReindeerSpaSupport import *
from Trainer import Trainer
from Reindeer import Reindeer
import logging

# Set up the spa logger
logger = logging.getLogger(__name__)
setup_logger(logger)

trainers_in_spa = {}
reindeer_in_spa = {}

# Create a simple class which takes a reindeer name and trainer name to be used in reindeer_in_spa
ReindeerID = namedtuple('ReindeerID', 'name,trainer_name')


@debug
@CountCalls
def print_trainers():
    if len(trainers_in_spa.keys()) == 0:
        logger.debug("Tried to print trainers with no trainers in spa")
        print("No trainers in the spa!")
        return False

    print("Trainers:\n-----------------")
    for key in trainers_in_spa:
        print(trainers_in_spa[key].name)
    return True


@debug
@CountCalls
def print_reindeer():
    if len(reindeer_in_spa.keys()) == 0:
        logger.debug("Tried to print reindeer with no reindeer in spa")
        print("No reindeer in the spa!")
        return False

    print("Reindeer:\n-----------------")
    for key in reindeer_in_spa:
        print(reindeer_in_spa[key].name)
    return True


# Main loop - starts at 1 and repeats to infinity, assuming no exit
for i in count(0):
    # Print a new line if the prompt is not the first prompt
    if count is not 0:
        print()

    # Display prompt and get input
    user_input = input(f""" \
Welcome to the Reindeer Spa. Please use one of the following options:
    1. Add a new trainer to the reindeer spa
    2. Add a new reindeer to a trainer
    3. Check in a reindeer from a trainer
    4. Clean a reindeer
    5. Groom a reindeer
    6. Check out a reindeer
    7. Check out a trainer
    8. Leave the spa \n
    User input {i}: 
    """)

    # Get a numerical input from the string user input
    try:
        user_input = int(user_input)

    except ValueError as e:
        logger.error(f"ValueError in ReindeerSpa - input {user_input}! Cannot include non-ints or out of range inputs")

    # Go through menu options in reverse order

    if user_input == 8:
        # Exit the spa
        print("You have exited the spa.")
        logger.debug("Exited the spa")
        break

    elif user_input == 7:
        # Remove a trainer from the system and all their reindeer
        if print_trainers() is False:
            continue
        trainer_to_remove = input("Enter the name of a trainer to remove: ")

        if trainer_to_remove in trainers_in_spa:
            trainers_in_spa.pop(trainer_to_remove)

        else:
            logger.warning(f"Tried to input an invalid trainer- {trainer_to_remove} to remove from spa")
        # TODO: Remove reindeer who belong to this trainer

    elif user_input == 6:
        continue
        # TODO: Remove reindeer specified

    elif user_input == 5:
        if print_reindeer() is False:
            continue

    elif user_input == 4:
        continue
        # TODO: Clean reindeer

    elif user_input == 3:
        # Check in a reindeer under a trainer
        if print_trainers() is False:
            continue
        trainer_to_remove = input("Enter the name of a trainer to check in a reindeer under: ")

        if trainer_to_remove in trainers_in_spa:
            trainers_in_spa.pop(trainer_to_remove)

        else:
            logger.warning(f"Tried to input an invalid trainer- {trainer_to_remove} to remove from spa")

    elif user_input == 2:
        # Assign a reindeer under a trainer
        if print_trainers() is False:
            continue

        trainer_name = input("Input the name of the trainer to add a reindeer under:")

        # Check and see if the trainer is actually in the list of trainers
        if trainer_name not in trainers_in_spa.keys():
            logger.warning(f"Tried to input an invalid trainer- {trainer_name} under which to add a reindeer in the spa")
            continue

        # Input a reindeer name
        reindeer_name = input("Set the reindeer's name:")

        # Add a reindeer to the spa
        trainers_in_spa[trainer_name].add_reindeer(Reindeer(name=reindeer_name))


    elif user_input == 1:
        # Add a trainer to the system
        trainer_name = input("Set the trainer's name:")
        trainers_in_spa[trainer_name] = Trainer(name=trainer_name)

        if print_trainers() is False:
            continue
