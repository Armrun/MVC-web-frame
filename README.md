# 🚀 MVC Web Framework

A lightweight Python Web **MVC** framework built on top of **Socket** system call and **HTTP** protocols. It supports core features such as custom routing, template rendering, **ORM**-based database access, and concurrent request handling — ideal for learning web architecture fundamentals and backend engineering design.

![Demo](https://github.com/Armrun/MVC-web-frame/blob/master/static/webframework.gif?raw=true)


## 🌐 HTTP Server

- Implements HTTP server using native Python **socket**
- Supports request listening, response sending, Keep-Alive, etc.
- Custom parsing and construction of raw **HTTP** messages
- Wraps requests into `Request` **objects** for use in the framework
- Built-in thread pool for handling **concurrent connections**


## 🧱 MVC Architecture

### 🧩 Model (M) — ORM via Meta Programming

- Utilizes Python metaclasses to define **ORM** mappings with **Join** support
- Provides base methods for database operations (select, insert, update, delete)
- Supports instantiating and abstracting data models

### 🎨 View (V) — Jinja2 Template Rendering

- Integrates `Jinja2` for template rendering and data binding
- Supports template inheritance, component reuse, and modular views
- Compatible with HTML and **JSON** response formats

### ⚙️ Controller (C) — Routing and Module Management

- Uses **high-order functions** and hash tables to implement routing dispatch
- Supports **decorators** to register view functions and apply permission checks
- Routing supports regex matching and parameter binding


## ✨ Framework Features

- ✅ Routing and Permission-check decorators for controllers
- ✅ ORM supporting **transaction** management, **Join** and relational mapping, **Auto-generates** database tables and compatible with **MySQL** with **Expressive query syntax**
- ✅ Supports HTML / JSON / Form / Redirect / Error responses
- ✅ Static file serving (CSS / JS / images, etc.)



## 🧰 Tech Stack

- Native Python socket / threading
- Jinja2 template engine
- MySQL support via custom ORM abstraction


## 📦 Example: Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize the MySQL database
python reset.py

# Start the server
python server.py
