import request

# using the model bge-m3 of Ollama
# make sure to install ollama and load the bge-m3 model locally
def create_embeddings(list_text):
  res = requests.post("http://localhost:11434/api/embed", json={"model": "bge-m3", "input": list_text})

  embedding = res.json()['embeddings']
  return embedding
