from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)
response = index.query("世界を変える人が四角い穴に打ち込むものは何?")
print(response)