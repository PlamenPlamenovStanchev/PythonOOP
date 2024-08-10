from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        t: Task = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.completed = Task
            return f"Completed task {t.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_task_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {current_task_len - len(self.tasks)} tasks."

    def view_section(self):
        task_details = '\n'.join(t.details for t in self.tasks)
        return f"Section {self.name}:\n{task_details}"


