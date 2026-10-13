
from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Preston")

dog = Pet("Max", 3, "Dog")
cat = Pet("Luna", 2, "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Morning Walk", "09:00", "Daily"))
dog.add_task(Task("Breakfast", "08:00", "Daily"))
cat.add_task(Task("Feed Luna", "08:00", "Daily"))

scheduler = Scheduler()

tasks = scheduler.sort_by_time(owner.get_all_tasks())

print("=== Today's Schedule ===")

for pet_name, task in tasks:
    print(
        f"{task.time} | {pet_name} | "
        f"{task.description} | {task.priority}"
    )

print("\n=== Scheduling Conflicts ===")

for conflict in scheduler.detect_conflicts(tasks):
    print(conflict)
