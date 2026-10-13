### 1b. Design Changes

My design changed as I started implementing the scheduling features. I added due dates and priority levels to the Task class so users could organize their pet care activities better. I also added recurring task functionality to the Scheduler class so daily and weekly tasks could automatically be scheduled again after completion.

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and Priorities

My scheduler mainly considers the date and time of each task. It sorts activities in chronological order and checks whether multiple tasks are scheduled at the same time. I also included priority levels so users can see which tasks are more important, although the current schedule is organized by time rather than priority.

### b. Tradeoffs

One tradeoff I made was keeping conflict detection simple. My scheduler only checks whether tasks have the exact same date and time instead of checking whether their durations overlap. I think this is reasonable for a basic pet care app because it makes the system easier to understand while still helping users identify scheduling issues.

## 3. AI Collaboration

### b. Judgment and Verification

I reviewed the AI-generated code instead of assuming everything was correct. One decision was to keep the scheduling logic simple rather than adding more complicated features before the basic system worked. I checked the results by running the application and using pytest to make sure tasks could be added and marked complete.

## 4. Testing and Verification

### a. What You Tested

I tested whether tasks could be added to a pet and whether marking a task complete updated its status. I also ran the command-line demo to check that tasks appeared in chronological order and that the scheduler displayed a warning when two tasks had the same time. These checks were important because they helped me confirm that the main parts of the application were working together.

### b. Confidence

I would give my current system a 3 out of 5 for reliability. The basic features work, and my first two automated tests passed. If I had more time, I would test more situations involving recurring tasks, multiple pets, and overlapping schedules to make sure the system handles different situations correctly.

## 5. Reflection

### a. What Went Well

The part I'm most satisfied with is getting the Python backend connected to the Streamlit interface. I liked seeing the project go from a basic class design to an actual app where users can add pets, schedule activities, and mark tasks as completed.

### b. What You Would Improve

If I had more time, I would improve how the scheduler handles task priorities and overlapping activities. I would also add a way to save pet information permanently so users wouldn't lose their data when starting a new session.

### c. Key Takeaway

One important thing I learned is how much easier it is to build an application when the code is organized into separate classes. I also learned that AI can help speed up development, but I still need to understand the code and test it to make sure everything works correctly.
