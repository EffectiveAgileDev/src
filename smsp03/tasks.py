from crewai import Task, Agent
from textwrap import dedent


class ClassAutomaticSocialMediaTasks():
    def manage_social_media_posts(self, agent, class_URL):
                return Task(
            description=dedent(f"""Oversee the Social Media Post prepration process including listed class lookup, title ideation, 
                post creation. The ultimate goal is for you post each listed class to X, FaceBook and LinkdIn social media platforms.
                               
                The Class URL is is: {class_URL}
                             
                Each post should contain the following details:
                - Class Title
                - Class Description
                - Class Start Date
                - Class Certification
                - Class Location
                
                                    
                # Potential High CTRO Titles:
                - Last Chance to Register for the ScrumMaster Class in Portland
                - Save Now with Early Bird Pricing for the ScrumMaster Class in Portland
                - ScrumMaster Class in Portland: Register Today and Save
                - ScrumMaster Class in Portland: Early Bird Pricing Ends Soon
                - Register Now for In-Person ScroumMaster Class in Bellevue
                - In-Persson Training for Scrum Is Better!
            """),

            agent=agent,
            output_file="output/SocialMediaPosts.txt",
            expected_output=dedent(f""" Create a report with each listed class and all of the Social Media Postes created for each class.               
            """)
        )

    
    def manage_listing_data_fill(self, agent, class_URL):
        return Task(
            description=dedent(f"""Fill in the data for the future classes listed at the class_URL including the begining date, end date, class title, city location, venue location address, 
            and registration link for each class that starts over 6 days from today's date.
            """),

            agent=agent,
            output_file="output/ListingDataFill.csv",
            expected_output=dedent(f""" Create a report with each listed class and all of the data filled for each class.               
            """)
        )

    def manage_post_type_picker(self, agent):
        return Task(
            description=dedent(f"""Pick the post type for the class based on the type of class and the number of days in advance of the class start. 
                               if the couse title contains the word 'virtual' the post type should be "Virtual Class".  
                               Otherwise, if the start date of the clss is > 6 days but less than 14 days from today, the post type should be "Last Chance Pricing". 
                               If the start date of the class is > 14 days from today and less than 30 days from today, the post type should be "In-Person Training".
                               If the start date of the class is > 30 days from today, the post type should be "Early Bird Pricing".
            """),

            agent=agent,
            output_file="output/PostTypePicker.txt",
            expected_output=dedent(f""" Create a report with each listed class and the post type picked for each class.               
            """)
        )

    def manage_title_creator(self, agent):
        return Task(
            description=dedent(f"""Create a title for the post using the post type, class title, city location. The title should not be over 25 characters long and 
            should be engaging and informative.  If the class title contains the word 'virtual' the title should contain the string 'Virtual Class'.
            """),

            agent=agent,
            output_file="output/TitleCreator.txt",
            expected_output=dedent(f""" Create a report with each listed class and the title created for each class.               
                """)
        )
    
    def manage_create_X_post(self, agent):
          return Task(
            description=dedent(f"""Create a post for X using the title and the class details. An X post is limited to 280 characters and should 
            contain the class title, class description, start date, certification, location, and registration link. """),
          
          agent=agent,
          output_file="output/CreateXPost.txt",
          expected_output=dedent(f""" Create a report with each listed class and the X post created for each class.               
            """)
          )
    
    def manage_create_FB_post(self, agent):
        return Task(
            description=dedent(f"""Create a post for Facebook using the title and the class details. The post should contain the class title, class description, 
            start date, certification, location, and registration link. """),
          
          agent=agent,
          output_file="output/CreateFBPost.txt",
          expected_output=dedent(f""" Create a report with each listed class and the Facebook post created for each class.               
            """)
        )
    
    def manage_create_LI_post(self, agent):
        return Task(
            description=dedent(f"""Create a post for LinkedIn using the title and the class details. The post should contain the class title, class description, 
            start date, certification, location, and registration link. """),
          
          agent=agent,
          output_file="output/CreateLIPost.txt",
          expected_output=dedent(f""" Create a report with each listed class and the LinkedIn post created for each class.               
            """)
        )
        