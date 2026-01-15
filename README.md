# The Django Blog – Reddit-Style Forum Application

## Live Site
https://thedjangoblog-5115dd98e142.herokuapp.com/blog/

## Repository
https://github.com/chazeldred55-code/thedjangoblog

---

## Project Purpose & Rationale

The Django Blog is a **Reddit-style discussion forum** developed as part of **Unit 3: Back End Development** for the **Level 5 Diploma in Web Application Development**.

The purpose of this project is to design and build a **fully functional, database-driven Full Stack web application** that allows users to create, read, update, and delete discussion content. The project focuses on **server-side logic, relational data modelling, CRUD functionality, testing, deployment, and security**, while also considering **UX design and accessibility**.

The target audience is users who are familiar with forum-style platforms and want a simple, intuitive space to create and engage in online discussions. The application purpose is immediately clear to new users through its layout, navigation, and functionality.

---

## User Experience (UX)

### Target Audience

- Users who want to create and participate in online discussions
- Users familiar with Reddit or forum-style platforms
- Users accessing the application on desktop or mobile devices

### User Stories

- As a user, I want to view all discussion posts
- As a user, I want to create a new post
- As a user, I want to comment on a post
- As a user, I want to edit my own posts
- As a user, I want to delete my own posts
- As a user, I want clear feedback when actions succeed or fail

### UX Design Decisions

- Clear information hierarchy using semantic HTML
- Consistent layout across all pages
- Immediate visual feedback for user actions
- Confirmation prompts for destructive actions (delete)
- Responsive layout for mobile, tablet, and desktop
- Simple colour palette and readable typography
- No unnecessary pop-ups or autoplay media

Accessibility considerations include readable contrast, semantic markup, and intuitive navigation.

---

## Features

### Implemented Features

- Create new discussion posts
- View a list of all posts
- View individual post details
- Add comments to posts
- Edit existing posts
- Delete posts
- Database-driven content (no hard-coded data)
- User feedback messages for success and error states
- Responsive design using HTML and CSS

### Future Features

- User authentication (login/logout)
- Post voting system (upvotes/downvotes)
- User profiles
- Categories or tags

---

## Data Model

The application uses a **relational database** (SQLite during development), designed to reflect a real-world discussion forum domain.

### Entity Relationship Overview

#### Post Model

| Field | Type |
|-----|-----|
| title | CharField |
| content | TextField |
| author | CharField |
| created_date | DateTimeField |

#### Comment Model

| Field | Type |
|-----|-----|
| post | ForeignKey (Post) |
| content | TextField |
| created_date | DateTimeField |

### Relationships

- One **Post** can have many **Comments**
- Each **Comment** belongs to one **Post**

The schema supports efficient CRUD operations and ensures data integrity through relational constraints.

---

## Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **SQLite** (development)
- **Git & GitHub**
- **Heroku / Render** (deployment)

---

## CRUD Functionality

The application fully implements **Create, Read, Update, and Delete** operations:

- **Create:** Users can add posts and comments
- **Read:** Users can view all posts and individual post details
- **Update:** Users can edit existing posts
- **Delete:** Users can delete posts with confirmation
- All CRUD actions are immediately reflected in the UI

---

## Testing

### Manual Testing



| Feature           | Action            | Expected Result      | Outcome |
|-------------------|-------------------|----------------------|---------|
| View posts        | Load homepage     | Posts are displayed | Pass    |
| Create post       | Submit valid form | Post saved           | Pass    |
| Create post       | Submit empty form | Error shown          | Pass    |
| Edit post         | Update content    | Changes saved        | Pass    |
| Delete post       | Confirm deletion  | Post removed         | Pass    |
| Add comment       | Submit comment    | Comment displayed    | Pass    |
| Responsive layout | Resize screen     | Layout adapts        | Pass    |

### View posts – Homepage
![Homepage](https://github.com/user-attachments/assets/d5fc3ec6-9b6d-4fe9-9957-f5389af48aaf)

### Load homepage
![Posts displayed](https://github.com/user-attachments/assets/51ce1009-4fb0-4eed-ba89-e3862d5dda7f)

### Validation Testing

- Required form fields enforced
- Empty submissions rejected
- Error messages displayed clearly
- Django form validation used throughout

### Code Validation

- Python follows **PEP8**
- HTML validated with **W3C Validator**
- CSS validated with **Jigsaw Validator**

All discovered bugs were fixed during development. No known unresolved bugs remain.

---

## Defensive Design

- All user input validated through Django forms
- Errors handled gracefully without application crashes
- User feedback provided for both success and failure
- Invalid URLs redirect users appropriately

---

## Deployment

### Deployment Platform
Designed for deployment to **Heroku or Render**.

### Deployment Steps

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Configure environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
4. Run migrations:
   ```bash
   python manage.py migrate
