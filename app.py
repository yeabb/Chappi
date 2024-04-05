import sys
import subprocess

class App:
    def __init__(self):
        self.interaction_started = False
        self.ai_prompted = False

    def start(self):
        print("Welcome to Chappi. Type 'fire' to activate interactive AI feature.")

    def activate_interaction(self):
        self.interaction_started = True
        print("Interactive AI feature activated. Type 'water' to deactivate interactive AI feature.")

    def stop_interaction(self):
        self.interaction_started = False
        print("Interactive AI feature deactivated.")

    def process_command(self, command):
        self.ai_prompted = False
        if self.interaction_started:
            if command == "water":
                self.stop_interaction()

            elif command == "kill":
                print("Sorry to see you go, come back soon :)")
                print("When you're ready to be back, just type \"Chappi\"")
                sys.exit()
            else:
                # get the prompt *****************************
                print("Processing command:", command)
                self.ai_prompted = True

        else:
            if command == "fire":
                self.activate_interaction()
            else:
                # Execute the command directly on the command line
                subprocess.run(command, shell=True)

    def run(self):
        self.start()
