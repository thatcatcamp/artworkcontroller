import json
import os
import random
import subprocess
from os.path import join

import cherrypy
import cherrypy_cors
cherrypy_cors.install()

class Root:
    @cherrypy.expose
    def default(self):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return open("food/puffin.jpg", "rb")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def play(self):
        input_json = cherrypy.request.json
        file = input_json["file"]
        swap = join(f"./wav/{file}")
        if swap is None:
            print("no test data?")
            return
        print("playing...", swap)
        subprocess.check_output(['aplay', swap])

    @cherrypy.expose
    def img(self):
        print('img')
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return open("food/puffin.jpg", "rb")

    @cherrypy.expose
    def stats(self):
        with open("/tmp/stats.json", "rt") as handle:
            spew = handle.readlines()
        cherrypy.response.headers['Content-Type'] = "text/json"
        return spew


def error_page_404(status, message, traceback, version):
    chk = random.randint(0,10)
    annotated = os.path.join("/", "tmp", "annotated.jpg")
    plain = os.path.join("/", "tmp", "swap.jpg")
    print(chk)
    cherrypy.response.headers['Content-Type'] = "image/jpg"
    file = random.choice(os.listdir("food"))
    if chk > 8 or True:
        print("serving notes")
        if os.path.exists(annotated):
            return open(annotated, "rb")
        else:
            return open(plain, "rb")
    print(file)
    return open(os.path.join("food", file), "rb")


current_dir = os.path.dirname(os.path.abspath(__file__))
cherrypy.config.update({
    'server.socket_port': 8888, })
with open("/tmp/stats.json", "wt") as handle:
    handle.write('{"person": 1, "chair": 0, "pottedplant": 0, "tvmonitor": 0}')
conf = {'/images': {'tools.staticdir.on': True,
                    'tools.staticdir.dir': os.path.join(current_dir, 'images')}}
cherrypy.config.update({'error_page.404': error_page_404})
cherrypy.config.update({'/stats': {'cors.expose.on': True,}})
cherrypy.quickstart(Root(), '/', config=conf)
