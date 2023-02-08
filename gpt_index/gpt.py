from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)
response = index.query("クレイジーな人を無視したら、世界は変わる?")
print(response)