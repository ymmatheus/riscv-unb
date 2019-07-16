#	Heroku deployment docker
## 	 Commands
###	  heroku login  
###	  heroku container:login
###	  heroku container:push web -a warm-stream-61220
###	  heroku container:release web -a warm-stream-61220

FROM python:3.6-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
