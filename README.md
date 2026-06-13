#  Social Media Marketplace API

A production-ready backend service built using **FastAPI**, designed to power a hybrid platform combining **social media interactions** and a **digital marketplace**.

This project demonstrates industry-standard backend practices including **secure authentication, modular architecture, database design, and scalable API development**.





## Overview
The **Social Media Marketplace API** enables users to:

* Create and interact with posts
* Engage through likes and comments
* List and browse products
* Build a foundation for a full-stack social commerce platform

The system is designed with **extensibility and maintainability** in mind, making it suitable for real-world applications.

---

##  Features

###  Authentication & Authorization

* JWT-based authentication
* Secure password hashing (Argon2)
* Protected routes using dependency injection

###  User Management

* User registration and login
* Unique email validation
* Secure credential handling

### Social Media

* Create and manage posts
* Like posts (duplicate prevention)
* Comment on posts
* Retrieve post interactions

###  Marketplace

* Create product listings
* Associate products with sellers
* Fetch product catalog

---

##  Architecture

The application follows a **layered architecture**:

```text id="e7xt6j"
Client → API Routes → Services → Database (SQLModel)
```

### Layers:

* **Routes** → Handle HTTP requests
* **Services** → Business logic
* **Models** → Database schema
* **Schemas** → Data validation
* **Dependencies** → Authentication & shared logic






##  API Overview

### Authentication

* `POST /auth/register` → Register user
* `POST /auth/login` → Login & get token

### Posts

* `POST /posts/` → Create post
* `GET /posts/` → Get posts

### Likes

* `POST /likes/{post_id}` → Like post

### Comments

* `POST /comments/{post_id}` → Add comment
* `GET /comments/{post_id}` → Get comments

### Products

* `POST /products/` → Create product
* `GET /products/` → List products

---

##  Security

* Passwords hashed using **Argon2**
* JWT tokens used for authentication
* Protected endpoints via dependency injection
* Input validation using Pydantic

---

##  Scalability Considerations

* Modular architecture for easy expansion
* Separation of concerns (routes/services/models)
* Ready to integrate:

  * PostgreSQL
  * Redis (caching)
  * Celery (background tasks)

---

##  Future Enhancements

*  Order & payment system
*  Follow/Unfollow users
*  Media uploads (Cloudinary / S3)
*  Search & filtering
*  Pagination & performance optimization
*  Docker + CI/CD pipeline

---

##  Learning Outcomes

This project highlights:

* REST API design with FastAPI
* JWT authentication implementation
* Clean backend architecture
* Database modeling & relationships
* Real-world backend problem solving

---

##  Author

**Raghu Narayana**
Backend Developer (Aspiring)

* Python | FastAPI | SQL
* Passionate about scalable backend systems

