import sys
import subprocess

class App:
    def __init__(self):
        self.interaction_started = False
        self.ai_prompted = False

    def start(self):
        print("************* Welcome! Type 'chappi' to wake Chappi up. **************")
        print("")

    def activate_interaction(self):
        self.interaction_started = True
        print("Interactive AI feature activated. Type 'bye' to deactivate chappi.")
        print("")

    def stop_interaction(self):
        self.interaction_started = False
        print("Interactive AI feature deactivated.")
        print("")

    def process_command(self, command):
        self.ai_prompted = False
        if self.interaction_started:
            if command == "bye":
                self.stop_interaction()

            elif command == "kill":
                print("Sorry to see you go, come back soon :)")
                print("When you're ready to be back, just type \"chappi\"")
                sys.exit()
            else:
                self.ai_prompted = True

        else:
            if command == "chappi":
                self.activate_interaction()
            else:
                # Execute the command directly on the command line
                print("****************************")
                subprocess.run(command, shell=True)
                print("")

    def run(self):
        self.start()
