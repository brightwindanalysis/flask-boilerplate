from app import app

# TODO blueprint + json

@app.route("/", methods=['GET'])
def index():
  return "hello world"
