# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages the pets, while the Pet class stores each pet's information and tasks. The Task class handles activities like feeding, walking, and medication. The Scheduler class is responsible for organizing tasks, sorting them by time, and checking for scheduling conflicts. I wanted to keep everything separated so the code would be easier to understand and manage.

**b. Design changes**

My design changed a little as I started building the app. I added due dates, priority levels, and recurring tasks to make the scheduler more useful. I also made sure the Scheduler class handled most of the scheduling logic instead of putting everything into the Pet or Task classes. This helped keep my code organized and easier to work with.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler mainly focuses on the date and time of each task. It organizes tasks in chronological order and checks if multiple activities are scheduled at the same time. I also added priority levels so users can identify which tasks are more important. I decided to focus on time first because I wanted the schedule to be easy to follow and understand.

**b. Tradeoffs**

One tradeoff I made was keeping the conflict detection simple. Right now, my scheduler only checks if two tasks are scheduled at the exact same date and time instead of checking whether their durations overlap. I think this works for a basic pet care app because it still helps users catch scheduling conflicts without making the code too complicated.

---

## 3. AI Collaboration

**a. How you used AI**

I used ChatGPT to help plan the structure of PawPal+ and understand how the different classes should work together. It helped me create the initial UML diagram and Python class skeleton. I also used AI to break down the assignment into smaller steps so I could work through each part without getting confused.

**b. Judgment and verification**

I didn't want to make the project more complicated than it needed to be, so I kept the scheduling logic simple instead of adding a lot of extra features. I reviewed the AI-generated code and tested the program to make sure it worked correctly. Running the app and checking the terminal output helped me understand what the code was doing instead of just copying it.

---

## 4. Testing and Verification

**a. What you tested**

I tested whether tasks could be added to a pet and whether marking a task complete updated its status. I also checked that tasks appeared in the correct time order and that the scheduler could identify tasks scheduled at the same time. These tests were important because they helped me make sure the main features were working properly.

**b. Confidence**

I would give my scheduler a 3 out of 5 for reliability based on the tests I've completed so far. The main features work, and my initial automated tests passed. If I had more time, I would test more situations involving recurring tasks, overlapping schedules, and multiple pets to make sure everything works correctly in different situations.

---

## 5. Reflection

**a. What went well**

The part I'm most satisfied with is getting the backend connected to the Streamlit app. It was nice seeing everything come together and actually being able to add pets, schedule tasks, and mark activities as completed. I also liked how the different classes worked together to make the app function.

**b. What you would improve**

If I had another chance to improve the project, I would add notifications to remind owners about upcoming tasks. I would also improve the scheduling system so it could consider how long each task takes and organize activities based on priority. Another improvement would be saving pet information permanently so users wouldn't lose their data when restarting the app.

**c. Key takeaway**

One important thing I learned from this project is how useful object-oriented programming can be when building an application. Breaking everything into different classes made the code easier to understand and manage. I also learned that AI can help make coding faster, but it's still important to review the code and test everything to make sure it works the way it's supposed to.
