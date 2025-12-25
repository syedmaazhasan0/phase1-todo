# 📝 Python Console Todo Application

A simple **console-based Todo application built using Python** that allows users to manage their tasks directly from the terminal.  
Each user has their own saved todo list, protected by a username and password, and all data is stored persistently using `.txt` files.

---

## 🚀 Features

### ✅ User Authentication
- Login using **username and password**
- New users are created automatically
- Existing users must enter the correct password
- Each user has a **separate todo list**

### ✅ Core Todo Features
- Add new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed

### ✅ Persistent Storage
- Todos are saved in `.txt` files
- Tasks are **never overwritten or deleted automatically**
- When a user exits and re-enters, their **previous todos are restored**

---

## 🧠 How It Works

- The app runs entirely in the **terminal**
- User credentials are stored in `users.txt`
- Each user has a separate file:
