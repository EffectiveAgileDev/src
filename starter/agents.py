from crewai import Agent
from langchain.agents import load_tools

# Human Tools
human_tools = load_tools(["human"])


class ClassAutomaticSocialMediaAgents():
    def posting_manager(self):
        return Agent(
            role="Posting Manager",
            goal="""Oversee the Social Media Posing prepration process including data retrieval, title ideation, 
                the posts on X, Facebook and Linkedin, and email announcement creation reqired to make a social media post.
                """,
            backstory="""As a methodical and detailed oriented managar, you are responsible for overseeing the preperation of Social Mdeia posts for each class.
                When creating Social Mdeia Posts, you follow the following process to create a post that has a high chance of success:
                1. Search the website to ceate a list of the future classes storing the begining date, end date, class title, city location, venue location address, and registration link.
                2. For each class in the list, examine the number of days in advance of the class start and create the appopriate posting the class.
                3. Write a title for post using the post type class, title, city location, and the number of days in advance of the class start.""",
                #4. Create a post for X, Facebook, and Linkedin using the title and the class details.
                #5. Create an email announcement for the class using the title and the class details.
                #""",
            allow_delegation=True,
            verbose=True,
        )


    def listing_data_fill(self):
        return Agent(
            role="Listing Data Fill",
            goal="""Fill in the data for the future classes including the begining date, end date, class title, city location, venue location address, 
            and registration link for each class that starts over 6 days from today's date.""",
            backstory="""As a detail oriented and methodical data entry specialist, you are responsible for filling in the data for the future classes that start over 6 days from today's date.""",
            allow_delegation=True,
            verbose=True, 
        )

    def post_type_picker(self):
        return Agent(
            role="Post Type Picker",
            goal="""Pick the post type for the class based on the number of days in advance of the class start.""",
            backstory="""As a methodical and detail oriented post type picker, you are responsible for picking the post type for the class based on the number of days in advance of the class start.""",
            allow_delegation=True,
            verbose=True,
        )

    def title_creator(self):
        return Agent(
            role="Title Creator",
            goal="""Create a title for the post using the post type, class title, city location.""",
            backstory="""As a creative and detail oriented title creator, you are responsible for creating a title for the post using the post type, class title, 
            city location, and the number of days in advance of the class start.  The title should not be over 25 characters long and should be engaging and informative.
            
            It is vital that you ONLY ask for human feedback after you've created the title.
            Do NOT ask the human to create the title for you.""",
            allow_delegation=True,
            verbose=True,
            tools=human_tools,
        )
    
    #def create_X_post(self):
        #TODO: Implement create X post

    
    #def create_FB_post(self):
        #TODO: Implement create FB post

    #def create_IG_post(self);
        #TODO: Implement create IG post

    #def create_WS_post(self):
        #todo: Implement create WS post

    #def create_email(self):
        #todo: Implement create email