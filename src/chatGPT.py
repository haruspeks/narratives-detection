
import os
import json
import pandas as pd
from openai import OpenAI

class ChatGPT:

    discussions=[{"role": "system", "content": "You are a helpful assistant."}]
    client = None
    self = None
    prompt = """ 
    The following text contains posts delimited with <post> XML tags.
     
    For each post find a narrative in the post with the attributes: 
    
    Title 
    Characters
    Plot
    Theme
    Point of View
    Moral

    Add each narrative to a list (if there are 100 posts there should be 100 narratives) and output the list as a json array.
"""
    
    def __init__(self):
        key = os.environ.get('OPENAI_API_KEY')
        self.client = OpenAI(api_key=str(key))
        self.df = pd.read_csv('./data/5G.csv')
    
    def _create_narrative(self, text: str):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                    {'role': 'system', 'content': f'You are an expert in narratology with deep knowledge of Qanon designed to output JSON. {self.prompt}'},
                    {'role': 'user', 'content': f'{text}'},
                ]
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content


    def analyse(self, text: str): 
        list = self.df['content'].head(200).to_string(index=False).split('\n')
        text = '\n\n'.join(f'<post>{str(x)}</post>' for x in list)

        print(text)
        result = self._create_narrative(text)
        # result = "self._create_narrative(text)"
        return json.loads(result)

    def _get_embedding(self, text, model="text-embedding-ada-002"):
        
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input = [text], model=model)['data'][0]['embedding']

    def create_embeddings(self):
        print(self.df.columns)
       
        self.df['embedding'] = self.df.combined.apply(lambda x: self._get_embedding(x, model='text-embedding-ada-002'))
        self.df.to_csv('data/embedded.csv', index=False)
        
        return self.df['embedding']



        

