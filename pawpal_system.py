
from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "Once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)
    priority: str = "Medium"

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    age: int
    pet_type: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Collect tasks from all pets."""
        return [
            (pet.name, task)
            for pet in self.pets
            for task in pet.tasks
        ]


class Scheduler:
    def sort_by_time(self, tasks):
        """Sort tasks by due date and time."""
        return sorted(
            tasks,
            key=lambda item: (
                item[1].due_date,
                item[1].time
            )
        )

    def filter_tasks(self, tasks, pet_name=None, completed=None):
        """Filter tasks by pet or completion status."""
        results = tasks

        if pet_name:
            results = [
                item for item in results
                if item[0] == pet_name
            ]

        if completed is not None:
            results = [
                item for item in results
                if item[1].completed == completed
            ]

        return results

    def detect_conflicts(self, tasks):
        """Find tasks scheduled at the same date and time."""
        conflicts = []
        seen = {}

        for pet_name, task in tasks:
            key = (task.due_date, task.time)

            if key in seen:
                conflicts.append(
                    f"Conflict: {seen[key]} and "
                    f"{pet_name} both have tasks at {task.time}"
                )
            else:
                seen[key] = pet_name

        return conflicts

    def mark_task_complete(self, pet, task):
        """Complete a task and schedule its next occurrence."""
        if task.completed:
            return None

        task.mark_complete()

        frequency = task.frequency.lower()

        if frequency == "daily":
            days = 1
        elif frequency == "weekly":
            days = 7
        else:
            return None

        next_task = Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            due_date=task.due_date + timedelta(days=days),
            priority=task.priority
        )

        pet.add_task(next_task)
        return next_task
