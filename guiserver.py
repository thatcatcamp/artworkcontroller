import cherrypy

PATH = "/butts/gui/dist/gui"


class Root(object): pass
    cherrypy.tree.mount(Root(), '/', config={
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': PATH,
            'tools.staticdir.index': 'index.html',
        },
    })

cherrypy.quickstart()
