

# paise lelega

# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings
# import os

# env_path = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..", ".env")
# )

# load_dotenv(env_path)

# api_key = os.getenv("OPENAI_API_KEY")

# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-large",
#     dimensions=64,
#     api_key=api_key
# )

# vector = embeddings.embed_query("you are going to learn gen ai")
                          
# print(vector)
# print(len(vector))

#-------------------------------------------

# free 

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

vector = model.encode("you are going to learn gen ai")

print(vector)
print(len(vector))