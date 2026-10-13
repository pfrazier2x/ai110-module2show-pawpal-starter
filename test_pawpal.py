
from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


# Test 1: Check task completion
def test_task_completion():
    task = Task("Feed Dog", "08:00")

    task.mark_complete()

    assert task.completed is True


# Test 2: Check adding tasks to pets
def test_task_addition():
    pet = Pet("Max", 3, "Dog")
    task = Task("Walk", "09:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Walk"


# Test 3: Check chronological sorting
def test_sorting():
    pet = Pet("Max", 3, "Dog")

    pet.add_task(Task("Walk", "10:00"))
    pet.add_task(Task("Breakfast", "08:00"))

    owner = Owner("Preston")
    owner.add_pet(pet)

    scheduler = Scheduler()
    tasks = scheduler.sort_by_time(owner.get_all_tasks())

    assert len(tasks) == 2
    assert tasks[0][1].description == "Breakfast"
    assert tasks[1][1].description == "Walk"


# Test 4: Check filtering tasks by pet
def test_filtering():
    owner = Owner("Preston")

    dog = Pet("Max", 3, "Dog")
    cat = Pet("Luna", 2, "Cat")

    dog.add_task(Task("Walk", "09:00"))
    cat.add_task(Task("Feed", "08:00"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()

    results = scheduler.filter_tasks(
        owner.get_all_tasks(),
        pet_name="Max"
    )

    assert len(results) == 1
    assert results[0][0] == "Max"
    assert results[0][1].description == "Walk"


# Test 5: Check daily recurring tasks
def test_daily_recurrence():
    pet = Pet("Max", 3, "Dog")
    today = date.today()

    task = Task(
        description="Walk",
        time="09:00",
        frequency="Daily",
        due_date=today
    )

    pet.add_task(task)

    scheduler = Scheduler()
    next_task = scheduler.mark_task_complete(pet, task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date == today + timedelta(days=1)
    assert next_task.completed is False
    assert len(pet.tasks) == 2


# Test 6: Check weekly recurring tasks
def test_weekly_recurrence():
    pet = Pet("Max", 3, "Dog")
    today = date.today()

    task = Task(
        description="Bath",
        time="12:00",
        frequency="Weekly",
        due_date=today
    )

    pet.add_task(task)

    scheduler = Scheduler()
    next_task = scheduler.mark_task_complete(pet, task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date == today + timedelta(days=7)
    assert len(pet.tasks) == 2


# Test 7: Check scheduling conflicts
def test_conflict_detection():
    owner = Owner("Preston")

    dog = Pet("Max", 3, "Dog")
    cat = Pet("Luna", 2, "Cat")

    dog.add_task(Task("Walk", "08:00"))
    cat.add_task(Task("Feed", "08:00"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()

    conflicts = scheduler.detect_conflicts(
        owner.get_all_tasks()
    )

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]
    assert "Max" in conflicts[0]
    assert "Luna" in conflicts[0]
