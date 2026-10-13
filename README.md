# 🐾 PawPal+ — Smart Pet Care Management

## Project Overview

PawPal+ is a pet care management app built using Python and Streamlit. The goal of this project is to help pet owners stay organized by keeping track of their pets and daily responsibilities. Users can add pets, schedule tasks, and keep up with activities like feeding, walking, and medication.

## Features

- **Pet Management:** Add pets and store their name, age, and type.
- **Task Scheduling:** Schedule activities for specific pets, dates, and times.
- **Task Priorities:** Assign low, medium, or high priority to tasks.
- **Task Completion:** Mark tasks as completed.
- **Smart Sorting:** Organize scheduled tasks by date and time.
- **Conflict Detection:** Display warnings when multiple tasks are scheduled at the same date and time.
- **Recurring Tasks:** Automatically create the next task when a daily or weekly task is completed.
- **Interactive Interface:** Manage pets and tasks using Streamlit.

## System Architecture

The application uses four main Python classes:

- **Owner:** Stores owner information and manages pets.
- **Pet:** Stores information about each pet and its scheduled tasks.
- **Task:** Represents individual pet care activities.
- **Scheduler:** Organizes tasks, filters schedules, checks conflicts, and manages recurring activities.

The final UML diagram is available in `diagrams/uml_final.mmd`.

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Run the command-line demonstration:

```bash
python main.py
```

## Demo Walkthrough

1. Open the PawPal+ application.
2. Enter the owner's name.
3. Add a pet by entering its name, age, and type.
4. Schedule a task by selecting the pet, date, time, frequency, and priority.
5. View scheduled activities in the Pet Care Schedule section.
6. Mark a task as completed.
7. Review any scheduling conflict warnings.

### Sample CLI Output

```text
=== Today's Schedule ===
08:00 | Max | Breakfast | Medium
08:00 | Luna | Feed Luna | Medium
09:00 | Max | Morning Walk | Medium

=== Scheduling Conflicts ===
Conflict: Max and Luna both have tasks at 08:00
```

## Smarter Scheduling

PawPal+ uses several scheduling methods:

- `sort_by_time()` sorts tasks chronologically.
- `filter_tasks()` filters tasks by pet name or completion status.
- `detect_conflicts()` identifies tasks scheduled at identical dates and times.
- `mark_task_complete()` completes a task and generates its next occurrence when it repeats daily or weekly.

The scheduler focuses on organizing tasks by date and time. Users can assign priority levels, but the current version does not automatically rearrange tasks based on priority or duration.

## Testing PawPal+

I used pytest to check that the main features of my application work correctly. Testing helped me verify that tasks can be added, completed, organized, and scheduled properly.

### How to Run Tests

```bash
python -m pytest -v
```

### Automated Tests

The project includes seven automated tests:

1. **Task Completion:** Checks that a task can be marked as completed.
2. **Task Addition:** Checks that tasks can be added to a pet.
3. **Task Sorting:** Checks that tasks appear in chronological order.
4. **Task Filtering:** Checks that tasks can be filtered by pet.
5. **Daily Recurrence:** Checks that completing a daily task schedules another task for the following day.
6. **Weekly Recurrence:** Checks that completing a weekly task schedules another task seven days later.
7. **Conflict Detection:** Checks that tasks scheduled at the same time are identified.

### Test Results

Run `python -m pytest -v` and paste the actual terminal results here before submitting.

**Confidence Level:** 4/5 stars, provided all seven tests pass.

The main features are working based on my testing so far. I would still like to improve how the scheduler handles overlapping tasks, task durations, and priority-based scheduling.

## Technologies Used

- Python
- Streamlit
- Python Dataclasses
- Pytest
- Mermaid UML
- GitHub Codespaces

## Future Improvements

In the future, I would like to add notifications for upcoming tasks, improve scheduling based on priority and available time, and allow pet information to be saved permanently between sessions.
