UnI

# OVERVIEW

UnI is a web application that matches two people together based on common personality traits and interests. The goal is to serve as
a plataform that makes socializing easier at Harvard by connecting people that have high chances of becoming friends.

# Pages
UnI has a few basic pages to ensure its main function:
- register page
- login page
- index
- personality
- lifestyle
- apology
- blog

# Basic functionality
A few functions ensure the functionality of UnI.
1) Register: we get the information from the user (name, email, password) and put it into our SQL database.
2) Login: we get information to log the user in.
3) Personality: this function gets the input of the user in the personality scale and add it to the SQL base.
4) Lifestyle: This function gets the data from the "interests and lifestyle" form and puts it into the SQL database.
5) Index: Just renders the index template.
6) Check: Check if a username is already taken (for when someone is trying to register)
7) Match: That's the algorithm that combines all the data from personality and interests scale together and sees what other person
in our database best matches with the logged user. Then, it renders a template with the name and email of the person.
8) Logout: If the user wants to log out.


# Requirements
 - Download all the files and folders.
 - To run the project, all you have to do is go "flask run" in your terminal window.
 - You need the appeople.db database

# How to use it
- First of all click on "Register" and create an account;
- Then, fill the Personality test and the Interests test;
- Then, click on "Match" and see the Magic happen!