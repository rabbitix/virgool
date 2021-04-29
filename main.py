
from fastapi import FastAPI,Request

app = FastAPI()


@app.get('/')
def read_root(request:Request):
    return {'docs': str(request.client.host) + '/docs' }


@app.get('/fake_txt_process')
def read_fake_text_process(txt: str):
    data = {}
    data['title'] = txt.title()
    words = txt.split() # split with  whitespace
    data['word_count'] = len(words)
    data['sentence_count'] = txt.count('.') 
    return data