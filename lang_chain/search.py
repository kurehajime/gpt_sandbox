from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)
tools = load_tools(["google-search"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)

res = agent.run("鹿児島の明日の天気で俳句を作って")
print(res)