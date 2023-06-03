import os
import random

import cherrypy


class Root:
    @cherrypy.expose
    def default(self):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return open("food/puffin.jpg", "rb")

    @cherrypy.expose
    def img(self):
        print('img')
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return open("food/puffin.jpg", "rb")


def error_page_404(status, message, traceback, version):
    print('404')
    cherrypy.response.headers['Content-Type'] = "image/jpg"
    file = random.choice(os.listdir("food"))
    print(file)
    return open(os.path.join("food", file), "rb")


current_dir = os.path.dirname(os.path.abspath(__file__))
cherrypy.config.update({
    'server.socket_port': 8888, })
conf = {'/images': {'tools.staticdir.on': True,
                    'tools.staticdir.dir': os.path.join(current_dir, 'images')}}
cherrypy.config.update({'error_page.404': error_page_404})
cherrypy.quickstart(Root(), '/', config=conf)
