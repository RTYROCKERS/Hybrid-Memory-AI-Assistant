import chromadb
from custom_embed_func import CustomEmbeddingFunction
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
#db_client=chromadb.Client()
#for persistent memory
#from chromadb.config import Settings(whats the use?)
db_client=chromadb.PersistentClient(path="../dbase")
ef=CustomEmbeddingFunction(SentenceTransformerEmbeddingFunction('all-mpnet-base-v2'))
collection=db_client.get_or_create_collection(name="memory",embedding_function=ef)
# collection.add(
#     ids=["101","102","103"],
#     documents=["my name is ruchir and age is 20","i like chocolates","name is Khan"]
# )
# results=collection.query(
#     query_texts=["what is my name?"],
#     n_results=2
# )
# print(results)
#Notes:
#- UNEXPECTED    :can be ignored when loading from different task/architecture; not ok if you expect identical arch.
# happens because loading a model that was trained to do something specific (like predict words or classify sentiment),
# but the embedding function only needs the base layers (the "body") to create vectors. 
# The weights for that specific task (the "head") are now "unexpected" because the embedding code doesn't include them.