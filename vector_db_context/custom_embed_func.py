from chromadb import Documents,EmbeddingFunction,Embeddings
from typing import Dict,Any
from chromadb.utils.embedding_functions import register_embedding_function

@register_embedding_function
class CustomEmbeddingFunction(EmbeddingFunction):
    def __init__(self,model):
        self.model=model
    @staticmethod
    def __name()->str:
        return "custom-ef"
    
    def __call__(self,input:Documents)->Embeddings:
        embeddings=self.model._model.encode(input).tolist()#self.model in case of sentence transformer ef is a wrapper the _model is the one with encode method
        return embeddings
    
    def get_config(self)->Dict[str,Any]:
        return dict(model=self.model)
    
    @staticmethod
    def build_from_config(config:Dict[str,Any])->EmbeddingFunction:
        return CustomEmbeddingFunction(config['model'])
        

