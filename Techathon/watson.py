import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url)  # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="sample", min_new_tokens=1, max_new_tokens=200, temperature=0.5)

model = Model("flan-t5-xl-pt-qFLVBm54-2023-10-30-11-23-30", params=params, credentials=creds)

def watsonx_response(prompt):
    prompt2=""
    response = model.generate([prompt, prompt2])
    return response[0].generated_text

