import webbrowser
class Movie():
    def __init__(self, nombre_pelicula, datos_pelicula, imagen_pelicula,trailer_youtube_url):
        self.nombre = nombre_pelicula
        self.datos = datos_pelicula
        self.imagen = imagen_pelicula
        self.video = trailer_youtube_url

    def muestra(self):
        webbrowser.open(self.video)