from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title='Silicoid Runner')
@app.get('/healthz')
def h(): return {'ok':True}
class Run(BaseModel): workspace_id:str; step:str
@app.post('/run')
def run(r:Run): return {'ok':True,'workspace_id':r.workspace_id,'step':r.step}
