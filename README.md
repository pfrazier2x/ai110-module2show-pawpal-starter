# 🐾 PawPal+ — Smart Pet Care Management

## Project Overview

PawPal+ is a pet care management app built using Python and Streamlit. The goal of this project is to help pet owners stay organized by keeping track of their pets and daily responsibilities. Users can add pets, schedule tasks, and keep up with activities like feeding, walking, and medication.

## Features

- **Pet Management:** Add pets and store their name, age, and type.
- **Task Scheduling:** Schedule activities for specific pets, dates, and times.
- **Task Priorities:** Assign low, medium, or high priority to tasks.
- **Task Completion:** Mark tasks as completed.
- **Smart Sorting:** Organize scheduled tasks by date and time.
- **Conflict Detection:** Display warnings when multiple tasks are scheduled at the same time.
- **Recurring Tasks:** Automatically create the next task when a daily or weekly task is completed.
- **Interactive Interface:** Manage pets and tasks using Streamlit.

## System Architecture

The application uses four main Python classes:

- **Owner:** Stores owner information and manages pets.
- **Pet:** Stores information about each pet and its scheduled tasks.
- **Task:** Represents individual pet care activities.
- **Scheduler:** Organizes tasks, filters schedules, checks conflicts, and manages recurring activities.

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

## Testing PawPal+

The project uses pytest to verify that the application works correctly.

Run the tests using:

```bash
python -m pytest
```

### Initial Test Results

```text
2 passed in 0.03s
```

The initial tests confirm that tasks can be marked complete and that tasks can be added to pets.

Additional tests for sorting, recurring tasks, and conflict detection will be added before final submission.

**Current confidence level:** 3/5 stars — the basic functionality works, but the more advanced scheduling features still need automated verification.

## Technologies Used

- Python
- Streamlit
- Python Dataclasses
- Pytest
- Mermaid UML
- GitHub Codespaces

## Future Improvements

In the future, I would like to add notifications for upcoming tasks, improve scheduling based on priority and available time, and allow pet information to be saved permanently between sessions.
