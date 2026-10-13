
from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Feed Dog", "08:00")
    task.mark_complete()
    assert task.completed is True


def test_task_addition():
    pet = Pet("Max", 3, "Dog")
    task = Task("Walk", "09:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
