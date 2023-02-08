# import os
# os.environ["OPENAI_API_KEY"] = "とーくん"
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
llm = OpenAI(temperature=.7)

# あらすじを書くChainを作成
template = """あなたは小説家です。
小説のタイトルが与えられた場合、そのタイトルのあらすじを{line}行以内で書くのがあなたの仕事です。

タイトル:{title}
あらすじ:"""
template1 = PromptTemplate(
    input_variables=["title", 'line'],
    template=template
)
chain1 = LLMChain(
    llm=llm,
    prompt=template1,
    output_key="novel"
)

# 俳句にするChainを作成
template = """与えられたあらすじをもとに５・７・５の俳句を1つ作ってください。
input:{novel}
output:"""
template2 = PromptTemplate(
    input_variables=["novel"],
    template=template
)
chain2 = LLMChain(
    llm=llm,
    prompt=template2,
    output_key="haiku"
)

# 2つのChainを連結したChainを作成
allchain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["title", "line"],
    output_variables=["novel", "haiku"],
    verbose=True
)

output = allchain({"title": "ザリガニ人間の社会", "line": "3"})
print(output["novel"])
print(output["haiku"])
