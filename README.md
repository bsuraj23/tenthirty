#Manish Kumar Volunter on 15-07-25
#15-07-25 codes

#ABOUT OS
An Operating System (OS) is system software that manages computer hardware, software resources, and provides essential services for computer programs. 
It acts as an interface between the user and the hardware, handling tasks such as process scheduling, memory management, file systems, and device control. 
Common examples include Windows, Linux, and macOS.

# Types of Operating Systems:
Batch OS – Executes batches of jobs without user interaction (e.g., early IBM systems).
Time-Sharing OS – Allows multiple users to access the system simultaneously.
Distributed OS – Manages a group of independent computers as a single system.
Real-Time OS (RTOS) – Responds to inputs within a guaranteed time frame (used in embedded systems).
Mobile OS – Designed for smartphones and tablets (e.g., Android, iOS).

#Core Functions of an Operating System:
Process Management
Manages running programs (called processes), including multitasking, process scheduling, synchronization, and inter-process communication.

Memory Management
Allocates and deallocates memory space to processes. Handles virtual memory, paging, and segmentation.

File System Management
Organizes, stores, retrieves, and secures data on storage devices.

Device Management
Controls and communicates with hardware devices (e.g., keyboards, printers, disks) using drivers.

Security & Access Control
Protects system resources from unauthorized access and enforces permissions and user authentication.

User Interface
Provides interfaces like CLI (Command Line Interface) or GUI (Graphical User Interface) for users to interact with the system.
#KEY-VALUE PAIR

#Update a key-value pair in a dictionary using a specific key
d={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
update_key = 'b'
if update_key in d:
    d[update_key] = 10
print("Updated dictionary key-value of b to 10:")
print(d)

#ZIP FILE IN DICT

#zip is used to combine two lists into a dictionary
names=['Mike', 'John', 'Sara', 'Anna']
ages=[25, 30, 22, 28]
d = dict(zip(names, ages))
print("Dictionary created using zip:")
print(d)



