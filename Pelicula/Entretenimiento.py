import fresh_tomatoes
import Media


transformers = Media.Movie("Transformers: Age of Extintion",
                           "Transformers: la era de la extincion, o simplemente Transformers 4, es una pelicula de ciencia ficcion estadounidense, basada en la franquicia Transformers.",
                           "https://plus.google.com/u/0/+transformersmovie/videos?pid=6007787439743862162&oid=111401023844217894185",
                           "https://www.youtube.com/watch?v=ragluX5mBzM")

Need_For = Media.Movie("Need For Speed",
                           "Need for Speed es una película de acción, dirigida por Scott Waugh y escrita por John Gatins y George Gatins. Producida y co-distribuida por DreamWorks Pictures, es una adaptación de la popular serie de videojuegos Need for Speed de Electronic Arts.",
                           "https://id.wikipedia.org/wiki/Berkas:PHDi1ujHh9wCGH_2_m.jpeg",
                           "https://www.youtube.com/watch?v=jKkdYXdn8kc")

Juegos_Parte2 = Media.Movie("Los Juegos del Hambre: Sinsajo Parte 2",
                                "Los Juegos del Hambre están de regreso dando continuidad a una historia que nos ha estremecido desde el inicio, Sinsajo Parte 2 nos presenta como siempre, una historia con acción, sorpresas y algo más que solo una continuación de este film. Los enemigos de Katniss Everdeen están tratando a toda costa de destruir todo a su paso, ahora dando un paso más allá de lo predecible. El Capitolio y el presidente Snowden están bajo la mira y se deberán de enfrentar a la chica de una manera final para demostrar quién es el más poderoso. En esta difícil misión Katniss deberá de ser ayudada por sus amigos o de lo contrario podría perder la vida.",
                                "http://www.xn--elseordelanillo-1qb.com/titulos/wp-content/uploads/1414.jpg",
                                "https://www.youtube.com/watch?v=PQwOl15mBNU")
movies = [transformers, Need_For, Juegos_Parte2]
fresh_tomatoes.open_movies_page(movies)