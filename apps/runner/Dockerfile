FROM python:3.11-slim
WORKDIR /app
RUN pip install fastapi uvicorn[standard] pydantic
COPY . /app
EXPOSE 8002
CMD ['uvicorn','app.main:app','--host','0.0.0.0','--port','8002']
