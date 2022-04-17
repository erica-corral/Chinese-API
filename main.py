from fastapi import FastAPI
import uvicorn
import jieba
from cihai.core import Cihai

#globals for processes
app = FastAPI()
c = Cihai()
if not c.unihan.is_bootstrapped:  # download and install Unihan db for Cihai if not installed already
    c.unihan.bootstrap({})


@app.get("/segment/{input}")
def segment(input):
    print(input)
    seg_result = jieba.cut(input,cut_all=False)
    return " ".join(seg_result)

@app.get("/define/{input}")
def define(input):
    query = c.unihan.lookup_char(input).first()
    return query
