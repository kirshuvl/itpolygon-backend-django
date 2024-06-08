import epicbox

from core.config.settings.celery import app


@app.task
def run_user_code(code):
    data = []
    for i in range(20):
        epicbox.configure(profiles=[epicbox.Profile("python", "stepik/epicbox-python:3.12.3-1")])
        files = [{"name": "main.py", "content": bytes(code, encoding="UTF-8")}]
        limits = {"cputime": 2, "memory": 64}
        result = epicbox.run("python", "python3 main.py", files=files, limits=limits)
        data.append(result)
    # print(result)
    return data
