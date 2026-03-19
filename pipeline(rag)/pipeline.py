import uuid
import json
from google.genai import types
class Rag_pipeline:
    def __init__(self,llm,collection):
        self.collection=collection
        self.llm=llm
    def run(self,query:str):
        retrieval=self.collection.query(
            query_texts=[query],
            n_results=5
        )
        context="\n".join(retrieval['documents'][0])
        prompt=f"""
        Context:
        {context}
        Query:
        {query}
        Note:
         Return JSON:
        {{
            "response": "...",
            "summary": "..."
        }}
        The summary should combine query + context + answer within 50 words.
        """
        answer=self.llm.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_level='low'),
                system_instruction="You are a personalised ai assistant",
                response_mime_type='application/json'
            )
        ).text
        # print(answer)
        answer=json.loads(answer)
        # self.collection.add(
        #     ids=[str(uuid.uuid4())],#can i add like a static variable to my collection that increments with each record
        #     documents=[answer['summary']],
        #     metadatas=[{"source": "chat_memory"}]
        # )
        return answer['response']


