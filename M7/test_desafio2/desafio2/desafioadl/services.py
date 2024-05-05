from .models import Task, SubTask


def recupera_tareas_y_sub_tareas():
    tasks = Task.objects.all()
    tasks_list = []
    for task in tasks:
        subtasks = SubTask.objects.filter(task=task)
        tasks_list.append({
            "task": task,
            "subtasks": subtasks
        })
    return tasks_list

def crear_nueva_tarea(name, description):
    task = Task.objects.create(
        name=name,
        description=description,
    )
    return task

def crear_nueva_subtarea(task, name, description):
    #task can be an id or an object
    if isinstance(task, int):
        task = Task.objects.get(id=task)
    subtask = SubTask.objects.create(
        task=task,
        name=name,
        description=description,
    )
    return subtask

def eliminar_tarea(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

def eliminar_subtarea(subtask_id):
    subtask = SubTask.objects.get(id=subtask_id)
    subtask.delete()

def imprimir_en_pantalla():
    tasks = recupera_tareas_y_sub_tareas()
    task_number = 0
    subtask_number = 0
    print('Tareas y subtareas:')
    for task_iter in tasks:
        task_number+=1
        print(f'[{task_number}] {task_iter["task"].name}')
        for subtask in task_iter["subtasks"]:
            subtask_number+=1
            print(f'.... [{subtask_number}]{subtask.name}')
    return tasks