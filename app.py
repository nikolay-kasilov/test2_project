from utils import (
write_tasks,
read_tasks,
filter_task
)
from fastapi import  (
     FastAPI,
     Request,
     Response

)

@app.get('/')
def get(r: Request) -> Response:
     priority = r.query_params.get('priority')
     data = read_tasks()
     if priority:
          data = filter_tasks(data,int(priority))
          return Response(content =data, status_code=200)

@app.post('/')
async def post(r:Request) -> Response:
     data = await  r.json()
     erors =[]
     for item in ('title','description','priority'):
          if data.get(item):
               errors.append(f"нет поля{item}")
     if not data.get('priority').isdigit():
               errors.append('Поле priority должно быть числом')
     if errors:
          return Response(content=errors, status_code=400)
     task = {
            'title': data.get("title"),
"description": data.get('description'),
'priority' : int(data.get('priority')),
'date' : datetime.now().strftime('%Y



@app.delite('/')
def delite (r:Request) -> Response:
    title = r.query_params.get('title')
    return Response(content=['Нет поля title'],status_code=400)
    task = read