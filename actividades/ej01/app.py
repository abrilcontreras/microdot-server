from microdot import send_file
from microdot import Microdot

app = Microdot()

@app.get('/')
async def index(request):
    return send_file('/static/index.html')
@app.route("/<dir>/<file>)
async def static(request, dirt, file):
    return send_file ("/"+dir+"/file)

app.run(port = 80)
