from django.test import TestCase

from .models import Task, SubTask
from .services import *

class TaskTestCase(TestCase):
    def setUp(self):
        task1 = Task.objects.create(name="Task 1", description="Description 1")
        task2 = Task.objects.create(name="Task 2", description="Description 2")
        task3 = Task.objects.create(name="Task 3", description="Description 3")

        SubTask.objects.create(task=task1, name="SubTask 1.1", description="Description 1.1")
        SubTask.objects.create(task=task1, name="SubTask 1.2", description="Description 1.2")

        SubTask.objects.create(task=task2, name="SubTask 2.1", description="Description 2.1")
        SubTask.objects.create(task=task2, name="SubTask 2.2", description="Description 2.2")

        SubTask.objects.create(task=task3, name="SubTask 3.1", description="Description 3.1")
        SubTask.objects.create(task=task3, name="SubTask 3.2", description="Description 3.2")

    def test_create_task(self):
        task = crear_nueva_tarea(name="Task 4", description="Description 4.1")
        self.assertEqual(task.name, "Task 4")
        self.assertEqual(task.description, "Description 4.1")

    def test_create_subtask(self):
        task = Task.objects.get(name="Task 1")
        subtask = crear_nueva_subtarea(task=task, name="SubTask 1.3", description="Description 1.3")
        self.assertEqual(subtask.name, "SubTask 1.3")
        self.assertEqual(subtask.description, "Description 1.3")

    def test_delete_subtask(self):
        subtask = SubTask.objects.get(name="SubTask 3.1")
        eliminar_subtarea(subtask.id)
        self.assertRaises(SubTask.DoesNotExist, SubTask.objects.get, name="SubTask 3.1")

    def test_delete_task(self):
        task = Task.objects.get(name="Task 3")
        eliminar_tarea(task.id)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, name="Task 3")

    def test_print_tasks(self):
        imprimir_en_pantalla()