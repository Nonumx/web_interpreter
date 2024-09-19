from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/algorithm-info")
def read_root():
    return {
        "title": "标题名称",
        "filename": "文件名称",
        "description": "文件描述",
        "arguments": [
            {
                "name": "123",
                "type": "double",
                "value": 123.0,
            },
            {
                "key": "123",
                "type": "str",
                "value": "123.8",
            },
        ],
    }
