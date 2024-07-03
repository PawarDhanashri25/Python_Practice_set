import requests
import json

response= requests.get('https://jsonplaceholder.typicode.com/todos')

todos_text= json.loads(response.text)

print(type(todos_text))
print("All Task todo\n")

print(todos_text)

print("Task those are completed\n")

for task in todos_text:
    if(task['completed'] == True):
        print(task)




