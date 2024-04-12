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

# 2. Create Tasks

tasks = ClassAutomaticSocialMediaTasks()

manage_social_media_posts = tasks.manage_social_media_posts(
    agent=posting_manager,
    class_URL="https://effectiveagiledev.com/DesktopModules/EventPlannerModule/EventRSSFeed.ashx?tabModuleId=1740&moduleId=967&portalId=0&tabid=157"
)

manage_listing_data_fill = tasks.manage_listing_data_fill(
    agent=listing_data_fill,
    class_URL="https://effectiveagiledev.com/DesktopModules/EventPlannerModule/EventRSSFeed.ashx?tabModuleId=1740&moduleId=967&portalId=0&tabid=157"
)

manage_post_type_picker = tasks.manage_post_type_picker(
    agent=post_type_picker
)

manage_title_creator = tasks.manage_title_creator(
    agent=title_creator
)


# Create a new Crew instance
crew = Crew(
    agents=[posting_manager,
            listing_data_fill,
            post_type_picker,
            ],
    tasks=[manage_social_media_posts,
           manage_listing_data_fill,
           manage_post_type_picker,
           manage_title_creator],

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