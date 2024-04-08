from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from crewai_tools import WebsiteSearchTool
search_tool = WebsiteSearchTool()


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(name="gpt-3.5-turbo", temperature=0.7)
    #    self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    #    self.Ollama = Ollama(model="openhermes")

    def searcher(self):
        return Agent(
            role="Searches a web page for the data elements needed.",
            backstory=dedent(f"""Your are an expert web searcher.  Your are able to look for a specific webpage and extract the data elements needed."""),
            goal=dedent(f"""For the first date listed after today's date, store the begining date of the class."""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

#    def agent_2_name(self):
#        return Agent(
#            role="Define agent 2 role here",
#            backstory=dedent(f"""Define agent 2 backstory here"""),
#            goal=dedent(f"""Define agent 2 goal here"""),
#            # tools=[tool_1, tool_2],
#            allow_delegation=False,
#           verbose=True,
#           llm=self.OpenAIGPT35,
      # )
