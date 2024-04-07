from flask import Flask, request, jsonify
import requests
import boto3
import json

app = Flask(__name__)

LLM_MODEL_API_URL = 'https://your_llm_model_api_endpoint'

@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    data = request.get_json()
    prompt = data.get('prompt')


    bedrock = boto3.client(service_name = "bedrock-runtime")
    payload ={
        "prompt":"[INST]" + prompt_data + "[/INST]",
        "max_gen_len":512,
        "temperature":0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = ""

    response = bedrock.invoke_model(
        body = body,
        model_id = model_id
    )
    if response.status_code == 200:
        return jsonify({'response': response.json()}), 200
    else:
        return jsonify({'error': 'Failed to process prompt'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# bedrock = boto3.client(service_name = "bedrock-runtime")

                # payload ={
                #     "prompt":"" + prompt + "[/INST]",
                #     "max_tokens_to_sample":512,
                #     "temperature":0.5,
                #     "top_p": 0.9
                # }

                # body = json.dumps(payload)
                # model_id = "anthropic.claude-v2"

                # response = bedrock.invoke_model(
                #     body = body,
                #     modelId = model_id,
                #     accept = "application/json",
                #     contentType = "application/json"
                # )
                # response_body = json.loads(response.get("body").read())
                # response_text = response_body.get("completion")
                # print(response_text)