# Hybrid Memory AI Assistant 

An AI assistant that combines short-term conversational context with long-term memory using Retrieval-Augmented Generation (RAG) to produce more context-aware and personalized responses.

---

## 🚀 Features

- Conversational AI powered by LLM APIs
- Hybrid memory system:
  - **Short-term memory** → recent conversation context
  - **Long-term memory** → stored in vector database
- Semantic search to retrieve relevant past interactions
- Context-aware response generation using RAG
- Dynamic prompt augmentation with retrieved memory

---

## 🧠 System Design

The assistant uses a hybrid memory pipeline:

1. User query is received
2. Recent conversation (short-term memory) is included
3. Query is embedded and searched in vector database
4. Relevant past memories are retrieved
5. Combined context is injected into LLM prompt
6. Response is generated and optionally stored for future use

---

## 🏗️ Architecture

User Input  
   ↓  
Embedding Model  
   ↓  
Vector DB (Context Retrieval)  
   ↓  
Prompt Augmentation  
   ↓  
LLM  
   ↓  
Response
  ↓  
Vector DB (Context Storage)

---

## 🛠️ Tech Stack

- Python
- Gemini API
- Vector Database ( Chroma )
- Embeddings (Sentence Transformer(all-mpnet-base-v2))

---

## ⚙️ Setup

```bash
git clone https://github.com/RTYROCKERS/Hybrid-Memory-AI-Assistant.git

pip install -r requirements.txt
