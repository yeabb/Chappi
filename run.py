from app import App
from prompt_constructor import Prompt_Constructor
import requests



EC2_API_URL = 'http://your_ec2_instance_ip:5000/process_prompt'

def main():
    while True:
        app = App()
        app.run()
        while True:
            if app.interaction_started:
                ai_feature_indicator = "@Chappi:)"
            else:
                ai_feature_indicator = ">"
            command = input(ai_feature_indicator)
            app.process_command(command)
            if app.ai_prompted:
                prompt_constructor = Prompt_Constructor()
                prompt = prompt_constructor.contruct(command)
                try:
                    response = requests.post(EC2_API_URL, json={'prompt': prompt})
                    if response.status_code == 200:
                        print(response.json().get('response'))
                    else:
                        print( 'Error: Failed to process prompt')
                except Exception as e:
                    print( f'Error: {str(e)}')


if __name__ == "__main__":
    main()