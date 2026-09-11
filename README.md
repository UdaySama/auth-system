# Auth System

A learning-focused authentication system built incrementally with Python.

The project currently starts as a simple **CLI-based authentication application** using Python fundamentals and in-memory data. The plan is to gradually evolve it into a full-stack authentication system with a **React + Vite client**, JSON-based persistence, and eventually a proper backend/database architecture.

## 🚀 Current Features

* User registration
* User login
* Credential validation
* Prevent duplicate registration
* Login/logout state management
* Change password
* Password validation during password change
* Input validation
* Integer/menu choice validation
* Menu handling based on authentication state

## 🛠️ Current Technology

* Python
* Python Dictionaries
* Functions
* Conditional statements
* Loops
* Exception handling
* Input validation

## 📁 Current Project Structure

```text
auth-system/
│
├── main.py
└── README.md
```

## 🔄 Planned Development

This project will be developed step by step.

### Phase 1 — Python CLI

* [x] Registration
* [x] Login
* [x] Logout
* [x] Change password
* [x] Input validation
* [x] Menu/option validation
* [ ] Refactor authentication logic into reusable functions
* [ ] Improve project structure

### Phase 2 — JSON Data Storage

The current in-memory user data will be replaced with a `data.json` file.

Planned structure:

```text
auth-system/
│
├── backend/
│   ├── main.py
│   └── data.json
│
└── README.md
```

Planned functionality:

* Store users in `data.json`
* Read user data from JSON
* Create users
* Update user data
* Validate login using stored data
* Persist password changes

### Phase 3 — Backend

The CLI application will gradually evolve into a backend API.

Planned technologies:

* Python
* FastAPI
* Pydantic
* REST APIs
* SQLAlchemy
* PostgreSQL

### Phase 4 — React Client

A frontend will be added using:

* React
* Vite
* JavaScript
* REST API integration

Planned frontend features:

* Registration page
* Login page
* Home/dashboard
* Change password
* Logout
* API communication with the backend

### Phase 5 — Production-Oriented Improvements

Future improvements may include:

* Proper password hashing
* Authentication tokens
* User-specific authorization
* Automated testing
* Docker
* Better project architecture
* Error handling
* API documentation

## 🎯 Project Goal

The goal of this project is to understand how an authentication system is built **from the fundamentals upward**, rather than jumping directly into a framework.

The project will gradually move through:

```text
Python Fundamentals
        ↓
CLI Authentication
        ↓
JSON Persistence
        ↓
FastAPI Backend
        ↓
PostgreSQL Database
        ↓
React + Vite Client
        ↓
Full-Stack Authentication System
```

## 📌 Project Status

**Current status:** 🚧 In Development

The project is currently in the Python CLI stage and is being developed incrementally as part of hands-on backend and full-stack learning.
