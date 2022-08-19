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

for i in count(1):
    user_input = input(""" \
Welcome to the Reindeer Spa. Please use one of the following options:
    1. Add a new trainer to the reindeer spa
    2. Add a new reindeer to a trainer
    3. Check in a reindeer from a trainer
    4. Clean a reindeer
    5. Groom a reindeer
    6. Check out a reindeer
    7. Check out a trainer
    8. Leave the spa \n
    """)

    # Get user input
    try:
        user_input = int(user_input)

    except ValueError as e:
        logger.error(f"ValueError in ReindeerSpa - input {user_input}! Cannot include non-ints or out of range inputs")

    # Go through options in reverse order

    if user_input == 8:
        print("You have exited the spa.")
        break

    if user_input == 7:
        if len(trainers_in_spa.keys()) == 0:
            print("No trainers in the spa!")
            continue
        print("Trainers:\n-----------------")
        for trainer, _ in trainers_in_spa:
            print(trainer)
        trainer_to_remove = input("Enter the name of a trainer to remove: ")

        if trainer_to_remove in trainers_in_spa:
            trainers_in_spa.pop(trainer_to_remove)

        else:
            logger.warning(f"Tried to input an invalid trainer- {trainer_to_remove} to remove from spa")

    if user_input == 6:
        continue
        # remove reindeer

    if user_input == 5:
        if len(reindeer_in_spa.keys()) == 0:
            print("No reindeer in the spa!")
            continue

        print("Reindeer:\n-----------------")
        for reindeer, _ in reindeer_in_spa:
            print(reindeer.name)

    if user_input == 4:
        continue
        # Clean reindeer

    if user_input == 3:
        if len(trainers_in_spa.keys()) == 0:
            print("No trainers in the spa to check in under!")
            continue
        print("Trainers:\n-----------------")
        for trainer, _ in trainers_in_spa:
            print(trainer)
        trainer_to_remove = input("Enter the name of a trainer to add a reindeer under: ")

        if trainer_to_remove in trainers_in_spa:
            trainers_in_spa.pop(trainer_to_remove)

        else:
            logger.warning(f"Tried to input an invalid trainer- {trainer_to_remove} to remove from spa")

    if user_input == 2:
        continue
        # Add a new reindeer to a trainer

    if user_input == 1:
        trainer_name = input("Set the trainer's name:")
        trainers_in_spa[trainer_name] = Trainer(name=trainer_name)
