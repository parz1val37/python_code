import request

def create_embeddings(list_text):
  res = requests.post("http://localhost:11434/api/embed", json={"model": "bge-m3", "input": list_text})

  embedding = res.json()['embeddings']
  return embedding
