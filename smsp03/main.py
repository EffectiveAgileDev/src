from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)
# 1. Create Agents
from agents import ClassAutomaticSocialMediaAgents
from tasks import ClassAutomaticSocialMediaTasks 

# Setup Agents 
agents = ClassAutomaticSocialMediaAgents()

posting_manager = agents.posting_manager()
listing_data_fill = agents.listing_data_fill()
post_type_picker = agents.post_type_picker()
title_creator = agents.title_creator()
create_X_post= agents.create_X_post()
create_FB_post = agents.create_FB_post()
create_LI_post = agents.create_LI_post()


# 2. Create Tasks

tasks = ClassAutomaticSocialMediaTasks()

manage_social_media_posts = tasks.manage_social_media_posts(
    agent=posting_manager,
    class_URL="D:\Users\RodClaar\src\smsp03\EventRSSFeed.xml"
)

manage_listing_data_fill = tasks.manage_listing_data_fill(
    agent=listing_data_fill,
    class_URL="D:\Users\RodClaar\src\smsp03\EventRSSFeed.xml"
)

manage_post_type_picker = tasks.manage_post_type_picker(
    agent=post_type_picker
)

manage_title_creator = tasks.manage_title_creator(
    agent=title_creator
)

manage_create_X_post = tasks.manage_create_X_post(
    agent=create_X_post
)

manage_create_FB_post = tasks.manage_create_FB_post(
    agent=create_FB_post
)

manage_create_LI_post = tasks.manage_create_LI_post(
    agent=create_LI_post
)


# Create a new Crew instance
crew = Crew(
    agents=[posting_manager,
            listing_data_fill,
            post_type_picker,
            title_creator,
            create_X_post,
            create_FB_post,
            create_LI_post,
            ],
    tasks=[manage_social_media_posts,
           manage_listing_data_fill,
           manage_post_type_picker,
           manage_title_creator,
           manage_create_X_post,
           manage_create_FB_post,
           manage_create_LI_post,
           ],

    process=Process.hierarchical,
    max_rpm=100,
    share_crew=True,
    full_output=True,
    manager_llm=OpenAIGPT4
)

# Kick of the crew
results = crew.kickoff()

print("Crew usage", crew.usage_metrics)

print("Crew work results:")
print(results)