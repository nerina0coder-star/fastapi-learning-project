from fastapi import FastAPI
from dataclasses import dataclass

@dataclass
class Likes:
    count: int = 0

    def incr(self, no: int) -> None:
        self.count += no

app = FastAPI()
likes = Likes()

@app.get("/")
def index() -> dict[str, str]:
    """
    Returns a hello world.
    """
    return {"message": "Hello World!"}

@app.post("/likes")
def add_to_likes(no: int) -> dict[str, int]:
    likes.incr(no)
    return {"count": likes.count}

@app.get("/likes")
def read_likes() -> dict[str, int]:
    return {"count": likes.count}
