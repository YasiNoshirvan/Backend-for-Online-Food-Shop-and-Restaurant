# Restaurant Management and Online Food Ordering System

This repository contains a Python project developed for the **Advanced Computer Programming** course during my bachelor's degree.

The project is a console-based restaurant management and online food ordering system implemented using object-oriented programming concepts in Python.

---

## 📌 Project Overview

The system simulates a simple restaurant ordering platform where two types of users can interact with the program:

- **Clerk / Staff**
- **Customer**

The clerk can manage the restaurant menu, while customers can register, log in, order food, increase their account balance, and pay for their orders.

---

## ✨ Features

### 👨‍💼 Clerk Features

- Staff login using username and password
- View the list of available foods
- Change the price of existing food items
- Add new food items to the restaurant menu
- Display clerk information

### 👤 Customer Features

- Customer registration
- Customer login
- View available food items
- Order food by selecting item index and quantity
- Continue or finish ordering
- View total bill
- Increase account balance
- Pay using account balance
- Pay in cash if balance is not enough

---

## 🧱 Object-Oriented Design

The project was implemented using Python classes and inheritance.

Main classes:

| Class | Description |
|---|---|
| `Food` | Represents food items with index, name, and price |
| `User` | Parent class for common user attributes such as username and password |
| `Clerck` / `Clerk` | Inherits from `User` and manages food items and prices |
| `Customer` | Inherits from `User` and manages customer information, orders, and account balance |

---

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming
- Classes and Inheritance
- File Handling
- Exception Handling
- Console-Based User Interaction

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YasiNoshirvan/REPOSITORY-NAME.git
