#The Django Blog – Reddit-Style Forum Application
Project Overview
The Django Blog is a Reddit-style discussion forum built using Python and Django.
The application allows users to create discussion posts, view posts, comment, edit, and delete content, providing full CRUD functionality in a database-driven full-stack web application.
The purpose of this project is to demonstrate backend development skills using Django, relational databases, and templating, in line with Code Institute Assignment 3 (L5 Diploma in Web Application Development) assessment criteria.
User Experience (UX)
Target Audience
Users who want to create and participate in online discussions
Users familiar with forum or Reddit-style layouts
Users accessing the application on desktop or mobile devices
User Stories
As a user, I want to view all discussion posts
As a user, I want to create a new post
As a user, I want to comment on a post
As a user, I want to edit my own posts
As a user, I want to delete my own posts
As a user, I want clear feedback when actions succeed or fail
Features
Implemented Features
Create new discussion posts
View a list of all posts
View individual post details
Add comments to posts
Edit existing posts
Delete posts
Database-driven content (no hard-coded data)
Responsive layout using HTML and CSS
User feedback messages on actions (success / error)
Future Features
User authentication (login/logout)
Post voting system (upvotes/downvotes)
User profiles
Categories or tags
Data Model
The application uses a relational database (SQLite during development).
Models
Post
Title
Content
Author
Created date
Comment
Post (Foreign Key)
Content
Created date
Relationships:
One Post can have many Comments
Each Comment belongs to a single Post
This structure supports clear CRUD operations and matches the project domain.
Technologies Used
Python
Django
HTML5
CSS3
SQLite (development)
Git & GitHub
Testing
Manual Testing
All core functionality was manually tested to ensure correct behaviour.
Feature
Action
Expected Result
Outcome
View posts
Open homepage
List of posts displayed
Pass
Create post
Submit valid form
Post saved to database
Pass
Create post
Submit empty form
Error message shown
Pass
Edit post
Update post content
Changes saved
Pass
Delete post
Confirm deletion
Post removed
Pass
Add comment
Submit comment
Comment displayed
Pass
Responsive design
Resize screen
Layout adjusts correctly
Pass
Validation Testing
Forms validate required fields
Empty submissions are rejected
User feedback is provided for errors
Code Validation
Python code follows PEP8 guidelines
HTML validated using W3C Validator
CSS validated using Jigsaw Validator
Defensive Design
User input is validated through Django forms
Errors are handled gracefully
Users receive feedback when actions succeed or fail
Invalid actions do not crash the application
Deployment
The project is designed to be deployed to a cloud platform (e.g. Heroku or Render).
Deployment Steps
Clone the repository
Install dependencies
Run migrations
Start the Django server
Configure environment variables if deploying live
Git Version Control
Git was used throughout development
Meaningful commit messages were written
Each feature was committed separately where possible
GitHub was used for remote storage
Accessibility
Semantic HTML used throughout
Clear navigation structure
Readable fonts and contrast
Responsive layout for multiple devices
Credits
Django documentation
Code Institute learning material
Assessment Alignment
This project meets the requirements for:
Full CRUD functionality
Data-driven Django application
Clear project purpose
Database modelling
Testing evidence
Clean, readable code
UX and accessibility considerations
Author
Chaz Eldred