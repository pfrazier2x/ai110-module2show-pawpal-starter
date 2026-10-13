
import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 PawPal+")
st.write("Your personal pet care management assistant!")

# Keep pet information saved during the session
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Preston")

owner = st.session_state.owner
scheduler = Scheduler()

# Sidebar
with st.sidebar:
    st.header("👤 Owner Information")
    owner.name = st.text_input("Owner Name", value=owner.name)
    st.write(f"Total Pets: {len(owner.pets)}")

# Add a pet
st.header("🐶 Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet Name")
    pet_age = st.number_input(
        "Pet Age", min_value=0, max_value=30, value=1
    )
    pet_type = st.selectbox(
        "Pet Type", ["Dog", "Cat", "Other"]
    )

    add_pet = st.form_submit_button("Add Pet")

    if add_pet:
        if pet_name.strip():
            if any(
                pet.name.lower() == pet_name.strip().lower()
                for pet in owner.pets
            ):
                st.warning("A pet with that name already exists.")
            else:
                owner.add_pet(
                    Pet(pet_name.strip(), pet_age, pet_type)
                )
                st.success(f"{pet_name} added successfully!")
        else:
            st.warning("Please enter a pet name.")

# Show pets
st.header("🐾 My Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(
            f"🐾 {pet.name} | {pet.pet_type} | "
            f"Age: {pet.age} | Tasks: {len(pet.tasks)}"
        )
else:
    st.info("No pets added yet.")

st.divider()

# Schedule tasks
st.header("📅 Schedule a Task")

if owner.pets:
    with st.form("task_form"):
        selected_pet = st.selectbox(
            "Select Pet",
            [pet.name for pet in owner.pets]
        )

        task_description = st.text_input(
            "Task Description",
            placeholder="Morning Walk"
        )

        task_date = st.date_input(
            "Task Date", value=date.today()
        )

        task_time = st.time_input(
            "Task Time"
        )

        frequency = st.selectbox(
            "Frequency", ["Once", "Daily", "Weekly"]
        )

        priority = st.selectbox(
            "Priority", ["Low", "Medium", "High"]
        )

        submit_task = st.form_submit_button("Add Task")

        if submit_task:
            if task_description.strip():
                pet = next(
                    pet for pet in owner.pets
                    if pet.name == selected_pet
                )

                task = Task(
                    description=task_description.strip(),
                    time=task_time.strftime("%H:%M"),
                    frequency=frequency,
                    due_date=task_date,
                    priority=priority
                )

                pet.add_task(task)
                st.success("Task scheduled successfully!")
            else:
                st.warning("Please enter a task description.")
else:
    st.info("Add a pet first to schedule tasks.")

st.divider()

# Display schedule
st.header("📋 Pet Care Schedule")

all_tasks = owner.get_all_tasks()

if all_tasks:
    selected_date = st.date_input(
        "View Schedule For", value=date.today()
    )

    date_tasks = [
        item for item in all_tasks
        if item[1].due_date == selected_date
    ]

    sorted_tasks = scheduler.sort_by_time(date_tasks)

    if sorted_tasks:
        for pet_name, task in sorted_tasks:
            status = "✅ Complete" if task.completed else "⏳ Pending"

            with st.container(border=True):
                st.write(
                    f"**{task.time} — {task.description}**"
                )
                st.write(
                    f"Pet: {pet_name} | "
                    f"Priority: {task.priority} | "
                    f"Frequency: {task.frequency}"
                )
                st.write(f"Status: {status}")

                if not task.completed:
                    if st.button(
                        "Mark Complete",
                        key=f"complete_{id(task)}"
                    ):
                        pet = next(
                            pet for pet in owner.pets
                            if pet.name == pet_name
                        )

                        scheduler.mark_task_complete(pet, task)
                        st.rerun()

        # Check for scheduling conflicts
        conflicts = scheduler.detect_conflicts(sorted_tasks)

        if conflicts:
            st.warning("⚠️ Scheduling Conflicts Detected")
            for conflict in conflicts:
                st.write(conflict)
        else:
            st.success("No scheduling conflicts!")

    else:
        st.info("No tasks scheduled for this date.")

else:
    st.info("No tasks yet. Add a task to get started!")

st.divider()
st.caption("PawPal+ | Smart Pet Care Management")
