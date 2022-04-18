from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import jieba
from chinese_english_lookup import Dictionary
from pypinyin import pinyin

#globals for processes
app = FastAPI()
d = Dictionary()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/segment/{input}")
def segment(input):
    print(input)
    seg_result = jieba.cut(input,cut_all=False)
    return " ".join(seg_result)

@app.get("/define/{input}")
def define(input):
    word_entry = d.lookup(input)
    kDefinition = word_entry.definition_entries[0].definitions
    kHanyuPinyin = processpinyin(input)
    kTraditionalVariant = word_entry.trad
    return {"kDefinition": kDefinition,"kHanyuPinyin": kHanyuPinyin, "kTraditionalVariant":kTraditionalVariant }

def processpinyin(input):
    initial_pinyin = pinyin(input)
    final_pinyin = ""
    for word in initial_pinyin:
        final_pinyin = final_pinyin+word[0]
    return final_pinyin

