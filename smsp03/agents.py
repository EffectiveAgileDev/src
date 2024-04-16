from crewai import Agent
from langchain.agents import load_tools

# Create Tools

# Human Tools
human_tools = load_tools(["human"])

from crewai_tools import (
    ScrapeElementFromWebsiteTool,
    SerperDevTool,
    WebsiteSearchTool,
    XMLSearchTool
)

load_data_tool = ScrapeElementFromWebsiteTool()
search_tool = SerperDevTool()
web_search_tool = WebsiteSearchTool()
XML_search_tool = XMLSearchTool()


class ClassAutomaticSocialMediaAgents():
    def posting_manager(self):
        return Agent(
            role="Posting Manager",
            goal="""Oversee the Social Media Posing preparation process including data retrieval, title ideation, 
                the posts for each class in the data set for the social media platoforms of X, Facebook and LinkedIn, and email announcement creation required to make a social media post. Use the encoding utf-8 that supports emojis.  
                """,
            backstory="""As a methodical and detailed oriented managar, you are responsible for overseeing the preparation of Social Media posts for each class.
                When creating Social Media Posts, you follow the following process to create a post that has a high chance of success:
                1. Search the website to create a list of the future classes storing the beginning date, end date, class title, city location, venue location address, and registration link.
                2. For each class in the list, examine the number of days in advance of the class start and create the appropriate posting the class.
                3. Write a title for each post using the post type class, title, city location, and the number of days in advance of the class start.
                4. Create a post each class in the dataset for X, Facebook, and Linkedin using the title and the class details.
                5. Create an email announcement for each class using the title and the class details.
                """,
                          
            allow_delegation=True,
            verbose=True,
            
        )
                

    def listing_data_fill(self):
        return Agent(
            role="Listing Data Fill",
            goal="""Fill in the data for the future classes including the begining date, end date, class title, class description, city location, venue location address, 
            and registration link for each class that starts over 6 days from today's date. Use the encoding utf-8 that supports emojis.""",
            backstory="""As a detail oriented and methodical data entry specialist, you are responsible for filling in the data for the 
            future classes that start over 6 days from today's date. Be sure to import all future classes that are over 6days from today's date. Save the data in the class data for future reference.""",
            allow_delegation=True,
            verbose=True, 
            tools=[XML_search_tool]
            )

    def post_type_picker(self):
        return Agent(
            role="Post Type Picker",
            goal="""Pick the post type for each class based on the number of days in advance of the class start.Use the encoding utf-8 that supports emojis.""",
            backstory="""As a methodical and detail oriented post type picker, you are responsible for picking the post type for each class based on the number 
            of days in advance of the class start.  Make sure you set a post type for all future classes that are 6 days or more from today's date.  Save the post type in the class data for future reference. """,
            allow_delegation=True,
            verbose=True,
            )

    def title_creator(self):
        return Agent(
            role="Title Creator",
            goal="""Create a title for each post using the post type, class title, city location.""",
            backstory="""As a creative and detail oriented title creator, you are responsible for creating a title for the post using the post type, class title, 
            city location, and the number of days in advance of the class start.  Make sure that you createatitle for each class over 6 days from today's date.  The title should not be over 25 characters long and should be engaging and informative.
            Use the encoding utf-8 that supports emojis.
            
            It is vital that you ONLY ask for human feedback after you've created the title.
            Do NOT ask the human to create the title for you.""",
            allow_delegation=True,
            verbose=True,
            tools=[web_search_tool],
            )
    #tools=[human_tools,search_tool,web_search_tool],
    
    def create_X_post(self):
        return Agent(
            role="Create X Post",
            goal="""Create a post for each class in the dataset trargeting the social media platform X using the title and the class details for each class in the dataset. Use the encoding utf-8 that supports emojis.""",
            backstory="""As a detail oriented and methodical post creator, you are responsible for creating a post for each class in the date set for X using the title and the class details.  
            An X post is limited to 280 characters and should contain the class title, class description, start date, certification, location, and registration link.
            Use the encoding utf-8 that supports emojis.  Make sure you create a post for each class over 6 days from today's date.
            """,
            allow_delegation=True,
            verbose=True,
            )

    
    def create_FB_post(self):
        return Agent(
            role="Create Facebook Post",
            goal="""Create a post for Facebook using the title and the class details for each class in the dataset. Use the encoding utf-8 that supports emojis.""",
            backstory="""As a detail oriented and methodical post creator, you are responsible for creating a post for Facebook using the title and the class details.  
            A Facebook post is limited to 2000 characters and should contain the class title, class description, start date, certification, location, and registration link.
            Use the encoding utf-8 that supports emojis. Make sure you create a post for each class over 6 days from today's date.
            """,
            allow_delegation=True,
            verbose=True,
            )

    def create_LI_post(self):
        return Agent(
            role="Create LinkedIn Post",
            goal="""Create a post for LinkedIn using the title and the class details for each class in the data set.Use the encoding utf-8 that supports emojis.""",
            backstory="""As a detail oriented and methodical post creator, you are responsible for creating a post for LinkedIn using the title and the class details.  
            A LinkedIn post is limited to 3000 characters and should contain the class title, class description, start date, certification, location, and registration link. 
            Use the encoding utf-8 that supports emojis.  Make sure you create a post for each class over 6 days from today's date.
            """,
            allow_delegation=True,
            verbose=True,
            )