task = []
done = 'False'
def add_new_task_func():
    new_task = input('Enter a new task: ')
    task.append({'task' : new_task, 'done' : False})
    return f'{new_task} is now added to your to-do list!'
def mark_task_done_func():
    task_found = False
    mark_done = input('Which task would you like to mark as done? ')
    for item in task:
        if item['task'] == mark_done:
            item['done'] = True
            task_found = True
    if task_found == True:
        return f'{mark_done} is now marked as done!'
    else:
        return f'{mark_done} was not found!'
def delete_task_func():
    task_found = False
    delete_task = input('What task would you like to remove?: ')
    for index, item in enumerate(task):
        if item['task'] == delete_task:
            task.pop(index)
            task_found = True
    if task_found == True:
        return f'{delete_task} has now been deleted!'
    else:
        return f'{delete_task} was not found!'
def show_all_task_func():
    if len(task) == 0:
        return 'Your to-do list is empty!'
    counter = 1
    for item in task:
        if item['done'] == True:
            status = 'Completed'
        else:
            status = 'Uncompleted'
        print(f"{counter}. {item['task']} is {status}")
        counter += 1
    return 'All current task have been displayed.'

print('Welcome!')
while True:
    print('What operation would you like to do:')
    operation = ['1. Add a new task', '2. Mark a task as completed', '3. Delete a Task', '4. Show all current tasks']
    for item in operation:
        print(item)
    op = int(input('Input the number next to the wished operation: '))
    if op == 1:
        print(add_new_task_func())
    elif op == 2:
        print(mark_task_done_func())
    elif op == 3:
        print(delete_task_func())
    elif op == 4:
        print(show_all_task_func())
    quit = input('Wanna resume or quit?: ')
    if quit == 'quit':
        break

print('Thanks for using our services!')
