from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from helpers.blog import write_blog
from helpers.ai import Gemini

app = FastAPI()
templates = Jinja2Templates(directory="templates")
gen = Gemini()

@app.get("/", response_class=HTMLResponse)
async def read_form():
    return FileResponse('templates/index.html')

@app.post("/submit")
async def submit_form(topic: str = Form(...)):
    prompt = gen.get_prompt(topic)
    res = gen.write_article(prompt)
    res = write_blog(res["title"], res["content"], res["tags"])
    return {"res": res}

@app.get("/write")
def read_root():
    title = "Test post"
    content = "<h1>This is a header</h1><p>This is a para text</p>"
    tags = ["test"]
    return write_blog(title, content, tags)

@app.get("/search")
def search():
    return gen.write_article(gen.get_prompt("AI"))

@app.get("/blog_writer")
def blog_writer():
    topic = "dogs"
    prompt = gen.get_prompt(topic)
    res = gen.write_article(prompt)
    res = write_blog(res["title"], res["content"], res["tags"])
    return {"status": 200, "message": "Blog written successfully!", "res": res}
