# Task Manager App (Waterfall Model)

## Project Overview
The **Task Manager App** is a simple web application built using **Flask** and **SQLite** that allows users to manage tasks efficiently.  
Users can **add, edit, delete, and update the status** of tasks. The project follows the **Waterfall software development methodology**, demonstrating clear phases from Requirements to Deployment.

---

## Waterfall Model Phases

### 1. Requirements Phase
- Defined project scope: Create a simple task manager.  
- Functional requirements:
  - Add a new task
  - Edit an existing task
  - Delete tasks
  - Update task status (Pending/Completed)  
- Non-functional requirements:
  - Web-based, responsive UI using Bootstrap  
  - Lightweight and easy to deploy  

### 2. Design Phase
- Created **ERD** for tasks and database schema: Task table with `id`, `title`, `description`, `status`.  
- Wireframes designed for **task listing**, **task addition**, and **editing forms**.  

### 3. Implementation Phase
- Developed Flask application using **MVC structure**:
  - `models.py` → Task model
  - `routes.py` → Routes for CRUD operations
  - `templates/` → HTML pages using Bootstrap
- Fully functional CRUD features:
  - Add, edit, delete, mark as completed/pending

### 4. Testing Phase
- **Unit tests** created using **pytest**:
  - Test home page loads
  - Test adding tasks
  - Test updating task status
- All tests passed successfully ✅  

### 5. Deployment Phase
- App can be run locally using:
```bash
export FLASK_APP=app
flask run

