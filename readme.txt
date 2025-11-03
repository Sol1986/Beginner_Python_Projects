## 🧠 10 Mini Flask Backend Projects (Beginner → Intermediate)

Each project has:

* **Concepts learned**
* **Task overview**
* **Subgoals / stretch features**

---

### **1. Quote of the Day API**

**Concepts:** Flask routes, JSON response
**Goal:** Create a simple API that returns a random quote when `/quote` is visited.

**Subgoals:**

* Store quotes in a list or dictionary.
* Add a `/quotes` endpoint that returns all quotes.
* Let users submit new quotes via a POST request.

---

### **2. To-Do List API**

**Concepts:** CRUD operations, request methods (GET, POST, PUT, DELETE)
**Goal:** Build a small RESTful API for managing to-dos.

**Subgoals:**

* Use an in-memory Python list to store tasks.
* Add route handlers for creating, reading, updating, and deleting tasks.
* Later, connect it to a SQLite database with SQLAlchemy.

---

### **3. Visitor Counter**

**Concepts:** Application state, sessions, cookies
**Goal:** Track how many times a user has visited your site.

**Subgoals:**

* Store visits using Flask’s session.
* Display the number of visits on the home page.
* Save visit logs in a text file.

---

### **4. Simple Weather Dashboard**

**Concepts:** External APIs, JSON parsing, rendering templates
**Goal:** Fetch real-time weather using the OpenWeatherMap API.

**Subgoals:**

* Let users enter their city.
* Show current temperature, humidity, and conditions.
* Extend it to a 5-day forecast using a separate route.

---

### **5. Joke Generator Website**

**Concepts:** Jinja templates, dynamic HTML rendering
**Goal:** Display random jokes on a webpage.

**Subgoals:**

* Use Flask templates (`render_template`).
* Add a button to fetch a new joke.
* Fetch jokes from a public joke API (like “icanhazdadjoke”).

---

### **6. User Registration System**

**Concepts:** Forms, hashing passwords, input validation
**Goal:** Create endpoints for `/register` and `/login`.

**Subgoals:**

* Use bcrypt or werkzeug for password hashing.
* Store users in SQLite.
* Return JWT tokens after login.

---

### **7. Feedback Collector**

**Concepts:** Forms + Database integration (SQLAlchemy)
**Goal:** Let users submit anonymous feedback and display them in admin view.

**Subgoals:**

* Create a `Feedback` model (name, email optional, message).
* Save submissions in the database.
* Add `/admin/feedback` route protected by a password.

---

### **8. File Upload & Gallery**

**Concepts:** File handling, static folders
**Goal:** Allow users to upload images and view them in a gallery.

**Subgoals:**

* Store uploads in a “uploads/” folder.
* Display uploaded images with HTML template.
* Add file type validation.

---

### **9. Basic Blog API**

**Concepts:** Relational data, foreign keys, blueprints
**Goal:** Create posts and comments.

**Subgoals:**

* Create Post and Comment models.
* Use SQLAlchemy relationships.
* Add pagination and simple search by title.

---

### **10. Expense Tracker**

**Concepts:** Full CRUD + authentication + database
**Goal:** A small REST API to track income and expenses by user.

**Subgoals:**

* Register/login system (JWT).
* CRUD for expenses.
* Calculate total balance per user.
* Add export to CSV.

---

## 🔁 Suggested Learning Order

| Stage | Project                  | Focus                     |
| ----- | ------------------------ | ------------------------- |
| 1     | Quote of the Day         | Basic routes & JSON       |
| 2     | To-Do List API           | CRUD & REST               |
| 3     | Visitor Counter          | State & cookies           |
| 4     | Simple Weather Dashboard | External APIs             |
| 5     | Joke Generator           | Templates                 |
| 6     | User Registration        | Auth & hashing            |
| 7     | Feedback Collector       | Forms + DB                |
| 8     | File Upload & Gallery    | File I/O                  |
| 9     | Basic Blog               | Blueprints + DB relations |
| 10    | Expense Tracker          | Full mini backend         |

