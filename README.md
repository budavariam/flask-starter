# flask-starter

Minimal flask app

```bash
python3 -m venv venv
. ./venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# start from Docker
docker build -t flaskstarter .
docker run --rm -p 8084:8084 flaskstarter

curl -XPOST -d @./examples/post.json 127.0.0.1:8084/data
curl 127.0.0.1:8084/version
curl 127.0.0.1:8084/ping
```
