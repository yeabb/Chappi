import subprocess
from time import sleep


class Command_Executor:
    def __init__(self):
        pass



    def process_logs(self, log_file_path):
        errors = []
        with open(log_file_path, 'r') as file:
            for line in file:
                if 'FAILED' in line:
                    errors.append("\n" + line.strip())
        return '\n'.join(errors)


    def process_common_command(self, command_resp):
        subprocess.run(command_resp, shell=True)


    def execute_command(self, response_dict):
        confidence_number = response_dict['confidence_number_and_flag'][0]
        flag_number = response_dict['confidence_number_and_flag'][1]
        if float(confidence_number) > 0.5:
            if(flag_number == 1):
                command_resp = response_dict['command']
                print("****************************")
                print(command_resp)
                self.process_common_command(command_resp)
            else:
                file_name = response_dict['file_name']
                print("processing log files...")
                sleep(0.5)
                print(self.process_logs(file_name))


        else:
            print("****************************")
            print(response_dict['command'])
            print("The command printed above had a confidence score below 0.5, so it was not executed")
            print("****************************")

