

class Prompt_Constructor:
    def __init__(self):
        pass

    def contruct(self, command):
        dirtyPrompt = command
        cleanPrompt = """
        Imagine you're the interactive terminal interface on a user's MacBook. The user has provided the following prompt seeking assistance with a Zsh command. Before providing a response, thoroughly analyze the prompt and generate the most suitable Zsh command that aligns with the user's request 
        """