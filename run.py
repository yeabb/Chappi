from app import App
from prompt_constructor import Prompt_Constructor
from anthropic import AnthropicBedrock
import requests
import boto3
import json
import ast
import subprocess
import getpass


def main():
    username = str(getpass.getuser())
    while True:
        app = App()
        app.run()
        while True:
            if app.interaction_started:
                chappi = ('''                       
 /\_/\  
( o.o ) 
 > ^ <                  
''')            
                combinied = f"{chappi}\n{username} > "
                print (combinied, end='')
                ai_feature_indicator = ""
            else:
                ai_feature_indicator = username + " " + "> "
            command = input(ai_feature_indicator)
            app.process_command(command)
            if app.ai_prompted:
                prompt_constructor = Prompt_Constructor()
                prompt = prompt_constructor.construct(command)

                client = AnthropicBedrock() 
                message = client.messages.create(
                    max_tokens=1024,
                    messages=[
                        {
                            "role": "user",
                            "content": str(prompt),
                        }
                    ],
                    model="anthropic.claude-3-sonnet-20240229-v1:0",
                )
                
                response_json_string = message.model_dump_json(indent=2)
                response_dict = json.loads(response_json_string)  

                message_id = response_dict['id']
                content = list(response_dict['content'])
                # print(content)
                model = response_dict['model']
                role = response_dict['role']
                stop_reason = response_dict['stop_reason']
                usage = response_dict['usage']          
                
               
                response_dict = json.loads(content[0]["text"])

                command_resp = response_dict['command']
                confidence_number = response_dict['confidence_number']
                
                if float(confidence_number) > 0.5:
                    print("****************************")
                    print(command_resp)
                    subprocess.run(command_resp, shell=True)
                else:
                    print("****************************")
                    print(command_resp)
                    print("****************************")

                



if __name__ == "__main__":
    main()