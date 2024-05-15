from fastapi import FastAPI

from blog import write_blog
from ai import Gemini

app = FastAPI()
gen = Gemini()

@app.get("/write")
def read_root():
    title = "Test post"
    content = "<h1>This is a header</h1><p>This is a para text</p>"
    tags = ["test"]
    return write_blog(title, content, tags)



@app.get("/search")
def search():
    return gen.write_article(gen.get_prompt("AI"))

@app.get("/")
def blog_writer():
    topic = "dogs"
    prompt = gen.get_prompt(topic)
    res = gen.write_article(prompt)
    res = write_blog(res["title"], res["content"], res["tags"])
    return {"status": 200, "message": "Blog written successfully!", "res": res}