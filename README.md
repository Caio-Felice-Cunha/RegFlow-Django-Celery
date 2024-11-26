# RegFlow+  

RegFlow+ is a modern Django application integrated with Celery to demonstrate the power of distributed programming. The project showcases a streamlined user registration workflow for events or courses, emphasizing scalability, performance, and user-centric communication.  

## Key Features  
1. **User Registration Workflow**  
   - Users register for an event or course and are redirected to a confirmation page with their details.  
   - A personalized invitation (PNG file) is automatically generated featuring their name and event date.  

2. **Automated Notifications**  
   - Users receive a confirmation email with event details and acknowledgment of successful registration.  

3. **Asynchronous Task Management with Celery**  
   - Time-intensive tasks, such as generating invitations and sending emails, are offloaded to Celery workers.  
   - This ensures a seamless and responsive user experience.  

## Why RegFlow+?  
RegFlow+ is designed for developers looking to:  
- Integrate **Celery** with **Django** for handling asynchronous tasks.  
- Improve application performance by offloading resource-heavy processes.  
- Build real-world, user-centric applications with robust registration workflows.  

## Technologies Used  
- **Django**: Backend framework for building web applications.  
- **Celery**: Distributed task queue for managing asynchronous jobs.  
- **Redis**: Message broker for Celery workers.  
- **Pillow**: Python Imaging Library for generating personalized invitations.  

## How It Works  
1. **Registration**: A user fills out the registration form and submits their details.  
2. **Background Tasks**:  
   - Celery generates a personalized PNG invitation with the user's name and event date.  
   - Celery sends a confirmation email containing event details and acknowledgment.  
3. **Confirmation**: The user is redirected to a confirmation page displaying their subscription details.  

## Getting Started  

### Prerequisites  
- Python 3.8+  
- Redis server  
- Virtual environment tool (optional but recommended)  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/Caio-Felice-Cunha/RegFlow-Django-Celery/
   cd regflow-plus  
