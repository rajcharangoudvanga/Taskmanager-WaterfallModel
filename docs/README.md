# Task Manager Project (Waterfall Model Documentation)

## 1. Requirements

### Functional Requirements
- User can **register and log in**
- User can **add new tasks**
- User can **edit existing tasks**
- User can **delete tasks**
- User can **mark tasks as complete**
- User can **view tasks on a dashboard**

### Non-functional Requirements
- Simple, user-friendly UI
- Data stored persistently in a database (SQLite)
- Secure login system (hashed passwords)
- Should run locally and be deployable online

### Acceptance Criteria
- Login works with valid credentials; shows error otherwise
- Tasks are saved and retrievable across sessions
- Users can only view/manage their own tasks
