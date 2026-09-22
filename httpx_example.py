import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())
print(response.status_code)