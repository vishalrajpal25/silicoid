from fastapi import FastAPI
app = FastAPI(title='Silicoid Control Plane')
@app.get('/healthz')
def h(): return {'ok':True}
@app.get('/api/auth/github/callback')
def cb(code:str=''): return {'ok': bool(code)}
