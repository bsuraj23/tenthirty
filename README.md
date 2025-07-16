# 📘 OS Concepts & Python Codes 
**Contributed by Manish Kumar – Volunteer on 15-07-25**

This repository contains notes and example code snippets related to Operating Systems and basic Python dictionary operations. The goal is to serve as a quick reference for students and beginners.

---

## 🖥️ About Operating Systems (OS)

An **Operating System (OS)** is system software that manages computer hardware, software resources, and provides essential services for computer programs.  
It acts as an interface between the user and the hardware, handling tasks such as process scheduling, memory management, file systems, and device control.  
**Common examples include**: Windows, Linux, and macOS.

---

## 🔧 Core Functions of an Operating System

- **Process Management**  
  Handles process scheduling, multitasking, synchronization, and communication between processes.

- **Memory Management**  
  Manages memory allocation, deallocation, paging, and segmentation.

- **File System Management**  
  Organizes, stores, retrieves, and secures data on storage devices.

- **Device Management**  
  Communicates with and controls hardware components via drivers.

- **Security & Access Control**  
  Prevents unauthorized access and enforces authentication and permissions.

- **User Interface**  
  Provides CLI (Command Line Interface) or GUI (Graphical User Interface) to interact with the OS.

---

## 🧠 Types of Operating Systems

- **Batch OS** – Executes batches of jobs without user interaction (e.g., early IBM systems).  
- **Time-Sharing OS** – Supports multiple users simultaneously.  
- **Distributed OS** – Manages multiple computers as a unified system.  
- **Real-Time OS (RTOS)** – Ensures timely response in embedded systems.  
- **Mobile OS** – Designed for mobile devices (e.g., Android, iOS).

---

## 🔑 Python Dictionary Key-Value Update

```python
# Update a key-value pair in a dictionary using a specific key
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
update_key = 'b'

if update_key in d:
    d[update_key] = 10

print("Updated dictionary key-value of b to 10:")
print(d)

Updated dictionary key-value of b to 10:
{'a': 1, 'b': 10, 'c': 3, 'd': 4, 'e': 5}


# zip is used to combine two lists into a dictionary
names = ['Mike', 'John', 'Sara', 'Anna']
ages = [25, 30, 22, 28]

d = dict(zip(names, ages))
print("Dictionary created using zip:")
print(d)

---



