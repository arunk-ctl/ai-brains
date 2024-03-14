import os
from dotenv import load_dotenv
from genai.client import Client
from genai.credentials import Credentials
from genai.schema import HumanMessage, SystemMessage, DecodingMethod, TextGenerationParameters

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
# Instantiate parameters for text generation
parameters = TextGenerationParameters(
    decoding_method=DecodingMethod.SAMPLE, max_new_tokens=80, min_new_tokens=30, temperature=0.7, top_k=50, top_p=1)
client = Client(credentials=Credentials.from_env())
model_id = "meta-llama/llama-2-70b-chat"

def watsonx_response(prompt):
    response = client.text.chat.create(
        model_id=model_id,
        parameters=parameters,
        messages=[
            SystemMessage(
                content="""You are a helpful, respectful and honest chat assistant working for a Telecommunication company called Satcom.
    Your name is Satcom Bot.
    Always answer as helpfully as possible, while being safe.    
    Your answers must alignment with our company policies and values and do not answer with respect to other companies or providers.
    Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
    Please ensure that your responses are socially unbiased and positive in nature. If a question does not make
    any sense, or is not factually coherent, explain why instead of answering something incorrectly.
    If you don't know the answer to a question, please don't share false information.
    """,),
            HumanMessage(content=prompt),
        ],
    )
    return response.results[0].generated_text
