from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "Searching for the webpage that has the list of classes is a good starting point."

    def find_web_page(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Find the webpage that has the list of classes and extract the data elements needed.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
        """
            ),
            expected_output="The list of futher classes and the begining date of the first class after today's date.",
            agent=agent,
        )

#    def task_2_name(self, agent):
#        return Task(
#            description=dedent(
#                f"""
#            Take the input from task 1 and do something with it.
#                                       
#            {self.__tip_section()}
#
#            Make sure to do something else.
#       """
#            ),
#            expected_output="Expected output here",
#            agent=agent,
     #   )
