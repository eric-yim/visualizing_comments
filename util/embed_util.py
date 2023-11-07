import os
import openai
OPEN_AI_KEY = "OPEN_AI_KEY"
api_key = os.getenv(OPEN_AI_KEY)
if api_key is None:
    print(f"Did you run:\n{OPEN_AI_KEY}=YOURKEY python3 YOUR_FILE.py\nCheck API KEY")
    import sys; sys.exit(0)
openai.api_key = api_key

class Embedder:
    def __init__(self):
        print("Using OpenAI API...")
    def embed(self, text, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']