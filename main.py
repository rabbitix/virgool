
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'hello': 'World'}


@app.get('/fake_txt_process')
def read_fake_text_process(txt: str):
    data = {}
    data['title'] = txt.title()
    words = txt.split() # split with  whitespace
    data['word_count'] = len(words)
    data['sentence_count'] = txt.count('.') 
    return data