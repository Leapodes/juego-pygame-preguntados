'''
LEANDRO PODESTÁ
DIV 212
PROGRAMACIÓN I
'''

'''
Desafío Preguntados

Preguntados es una franquicia de entretenimiento de plataformas y una de las
marcas más exitosas de la división de Gaming de Etermax.
Preguntados es principalmente un juego de preguntas y respuestas de Cultura
General tipo trivia. Digamos que este es el apartado en el que cabrían cuestiones de
todo tipo. Si sabés datos históricos, orígenes de comidas, literatura y curiosidades
de todo tipo, lograrás una buena puntuación.
Recientemente Etermax ha decidido desarrollar el juego en Python, y para acceder a
las entrevistas es necesario completar el siguiente desafío.
La empresa compartió con todos los participantes información que está compuesta
por un grupo de preguntas y respuestas. Semana a semana enviará una lista con los
nuevos requerimientos. Quienes superen todas éstas etapas podrán acceder a una
entrevista con el director de la compañía.
Set de datos
La información a ser analizada se encuentra en el archivo datos.py, por tratarse de
una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:

from datos import lista

Formato de los datos recibidos
lista =
[
{
"pregunta": "¿Cuál es la moneda de México? ",
"a": "Peso",
"b": "Dolar",
"c": "Euro",
"correcta": "a"
},
{
"pregunta": "¿De qué color es la bandera de Japón? ",
"a": "Azul y Amarilla",
"b": "Blanca y Roja",
"c": "Celeste y Blanca",
"correcta": "b"
}
]
Desafío:
A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).

B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.

C. Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”

D. Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.

E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.

F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.

G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.

H. Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada click pasa a la siguiente pregunta.
También debe reiniciar el puntaje.

I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.

J. Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.

NOTAS:
- Tienen total libertad para utilizar los sonidos, imágenes, y animaciones
(opcional) alusivas, donde corresponda.
- El formato del archivo que se debe crear para guardar los puntajes
debe ser TXT, CSV o JSON.
- Se deben definir y utilizar funciones, y las mismas deben estar
documentadas e importadas desde otro archivo (biblioteca).
'''
#IMPORTAR ARCHIVOS

import json
import pygame
from datos_preguntas import lista as lista_preguntas

#INICIO DE PYGAME

pygame.init()

#CONFIGURACION DE LA PANTALLA

screen = pygame.display.set_mode([700, 500]) #tamaño de pantalla
pygame.display.set_caption("Preguntados") #nombre del titulo en ventana

#DEFINICION DE BOTONES

#pantalla 1
#boton_titulo = pygame.Rect(240, 10, 200, 50) #[posicion de botones] | [tamaño de botones]
boton_jugar = pygame.Rect(70, 340, 180, 50) #[de izquierda a derecha y de arriba a abajo / de menor a mayor] | [de angosto a ancho y de chico a grande]
boton_score = pygame.Rect(450, 340, 180, 50)
boton_exit = pygame.Rect(255, 440, 180, 50)
#pantalla 2

boton_pregunta = pygame.Rect(20, 20, 180, 50) #[posicion de botones] | [tamaño de botones]
boton_reiniciar = pygame.Rect(500, 20, 180, 50)#[de izquierda a derecha y de arriba a abajo / de menor a mayor] | [de angosto a ancho y de chico a grande]
#boton_score_actual = pygame.Rect(2, 440, 90, 50)
    
boton_opcion_a = pygame.Rect(217, 285, 310, 50)
boton_opcion_b = pygame.Rect(217, 355, 310, 50)
boton_opcion_c = pygame.Rect(217, 425, 310, 50)

#pantalla 3
boton_volver = pygame.Rect(10, 10, 150, 50)
#boton_mensaje_final = pygame.Rect(140, 110, 400, 350)

#COLOR DE LETRA

#pantalla 1
font_titulo = pygame.font.SysFont("Arial Narrow", 55) #tipo y tamaño de letra

text_titulo = font_titulo.render("PREGUNTADOS", True, (180, 31, 31)) #color de letra

font = pygame.font.SysFont("Arial Narrow", 35) #tipo y tamaño de letra

font_pregunta = pygame.font.SysFont("Arial Narrow", 30)

text_start = font.render("Jugar", True, (255, 255, 255))
text_score = font.render("Ver Puntajes", True, (255, 255, 255))
text_exit = font.render("Salir", True, (255, 255, 255))

#pantalla 2

text_pregunta = font.render("Pregunta", True, (255, 255, 255)) #color de letra
text_reiniciar = font.render("Reiniciar", True, (255, 255, 255))
text_score_actual = font.render("Score", True, (65, 128, 78))
text_mensaje = font_pregunta.render("La pregunta ?", True, (0, 0, 0))
text_opcion_a = font.render("OPCIÓN A", True, (255, 255, 255))
text_opcion_b = font.render("OPCIÓN B", True, (255, 255, 255))
text_opcion_c = font.render("OPCIÓN C", True, (255, 255, 255))

#pantalla 3

text_volver = font.render("Volver", True, (255, 255, 255)) #color de la letra

font = pygame.font.SysFont("Arial Narrow", 45) #tipo y tamaño de letra

text_mensaje_final = font_titulo.render("RANKING", True, (255, 255, 255))
text_nombre = font.render("NOMBRE:", True, (177, 155, 204))

text_rank_1 = font.render("Leandro: 70", True, (255, 255, 255))
text_rank_2 = font.render("Val: 50", True, (255, 255, 255))
text_rank_3 = font.render("Nin: 30", True, (255, 255, 255))

#INSERTAR IMAGEN

#pantalla 1

imagen_principal = pygame.image.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\preguntados inicio.jpg")
imagen_principal_ajustada = pygame.transform.scale(imagen_principal, (700, 500))

#pantalla 2

imagen_pantalla_2 = pygame.image.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\preguntados preguntas.jpg")
pantalla_2_ajustada = pygame.transform.scale(imagen_pantalla_2, (700, 500))

#pantalla 3

imagen_pantalla_3 = pygame.image.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\brick wall.jpg")
pantalla_3_ajustada = pygame.transform.scale(imagen_pantalla_3, (700, 500))

#pantalla 4
imagen_pantalla_4 = pygame.image.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\game over.webp")
pantalla_4_ajustada = pygame.transform.scale(imagen_pantalla_4, (700, 500))


#SONIDOS

#cancion de menu
cancion_menu = pygame.mixer.music.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\Cuphead.mp3")
pygame.mixer.music.play(-1)

#cancion de jugar
#cancion_jugar = pygame.mixer.music.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\Prismatic Stars.mp3")

#sonido correcto
sonido_correcto = pygame.mixer.Sound(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\respuesta correcta.mp3")

#sonido incorrecto
sonido_incorrecto = pygame.mixer.Sound(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\respuesta incorrecta.mp3")

#VARIABLE DE ESTADO

screen_actual = "Menu"

score = False
pregunta = False
reiniciar = False

pregunta_actual = 0
puntaje = 0

bandera_respuesta = True
intentos_respuesta = 2

nombre = ""

#BUCLE PRINCIPAL DEL JUEGO

def ordenar_puntajes(puntaje: list):
    for i in range(len(puntaje)-1):
        for j in range(i+1, len(puntaje)):
            if puntaje[i]["puntaje"] < puntaje[j]["puntaje"]:
                    puntaje_auxiliar = puntaje[i]
                    puntaje[i] = puntaje[j]
                    puntaje[j] = puntaje_auxiliar
    return puntaje

def leer_puntajes_de_data_json():
    with open("puntajes.json", mode='r', newline='', encoding='utf-8') as archivo_json:
        puntajes_json = json.load(archivo_json)
    return puntajes_json    



def guardar_puntajes_data_json(puntajes_json):
    with open("puntajes.json", mode='w', newline='', encoding='utf-8') as archivo_json:
        json.dump(puntajes_json, archivo_json, ensure_ascii=False, indent=4)
#agregar y sobreescribir

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_actual == "Menu":

                #BOTON PARA JUGAR
                if boton_jugar.collidepoint(event.pos):
                    screen_actual = "Jugar"
                    pregunta_actual = 0
                    text_mensaje = font_pregunta.render(lista_preguntas[pregunta_actual]["pregunta"], True, (0, 0, 0)) #color de letra
                    text_opcion_a = font.render(lista_preguntas[pregunta_actual]["a"], True, (255, 255, 255)) #textos que muestran las respuestas 
                    text_opcion_b = font.render(lista_preguntas[pregunta_actual]["b"], True, (255, 255, 255))
                    text_opcion_c = font.render(lista_preguntas[pregunta_actual]["c"], True, (255, 255, 255))
                    pregunta_actual += 1
                    bandera_respuesta = True
                    puntaje = 0
                    intentos_respuesta = 2
                    text_score_actual = font.render(f"Score: {puntaje}", True, (65, 128, 78)) #muestra el puntaje en stand by
                    pygame.mixer.music.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\Prismatic Stars.mp3")
                    pygame.mixer.music.play(-1)
              
                #BOTON PARA VER LOS PUNTAJES
                if boton_score.collidepoint(event.pos):
                    if boton_score.collidepoint(event.pos):
                        screen_actual = "Score"
                        puntajes_json = leer_puntajes_de_data_json()
                        puntajes_json = ordenar_puntajes(puntajes_json)
                        if len(puntajes_json) > 0: #si hay mas de cero puntajes mostrar el primero 
                            text_rank_1 = font.render(f"{puntajes_json[0]["nombre"]}: {puntajes_json[0]["puntaje"]}", True, (255, 255, 255))
                        if len(puntajes_json) > 1: #si hay mas de uno mostrar el segundo
                            text_rank_2 = font.render(f"{puntajes_json[1]["nombre"]}: {puntajes_json[1]["puntaje"]}", True, (255, 255, 255))
                        if len(puntajes_json) > 2:
                            text_rank_3 = font.render(f"{puntajes_json[2]["nombre"]}: {puntajes_json[2]["puntaje"]}", True, (255, 255, 255))
                #BOTON DE SALIR
                if boton_exit.collidepoint(event.pos): 
                    running = False
            elif screen_actual == "Jugar":
                if boton_pregunta.collidepoint(event.pos):
                    if pregunta_actual >= len(lista_preguntas):
                        screen_actual = "Guardar Score" #cuento las preguntas y si termina guarda score
                    else: #si sigue habiendo preguntas, se muestra y sigue el juego
                        text_mensaje = font_pregunta.render(lista_preguntas[pregunta_actual]["pregunta"], True, (0, 0, 0)) #color de letra
                        text_opcion_a = font.render(lista_preguntas[pregunta_actual]["a"], True, (255, 255, 255))
                        text_opcion_b = font.render(lista_preguntas[pregunta_actual]["b"], True, (255, 255, 255))
                        text_opcion_c = font.render(lista_preguntas[pregunta_actual]["c"], True, (255, 255, 255))
                        pregunta_actual += 1 #mueve el contador a la siguente pregunta
                        bandera_respuesta = True
                        intentos_respuesta = 2 #tenes dos intentos por cada una, empezas con dos
                        boton_opcion_a = pygame.Rect(217, 285, 310, 50)
                        boton_opcion_b = pygame.Rect(217, 355, 310, 50)
                        boton_opcion_c = pygame.Rect(217, 425, 310, 50)          
                #BOTON DE REINICIO
                if boton_reiniciar.collidepoint(event.pos):
                    pregunta_actual = 0 #resetea el contador a la primera de vuelta
                    text_mensaje = font_pregunta.render(lista_preguntas[pregunta_actual]["pregunta"], True, (0, 0, 0)) #color de letra
                    text_opcion_a = font.render(lista_preguntas[pregunta_actual]["a"], True, (255, 255, 255))
                    text_opcion_b = font.render(lista_preguntas[pregunta_actual]["b"], True, (255, 255, 255))
                    text_opcion_c = font.render(lista_preguntas[pregunta_actual]["c"], True, (255, 255, 255))
                    pregunta_actual += 1
                    bandera_respuesta = True
                    puntaje = 0
                    intentos_respuesta = 2
                    text_score_actual = font.render(f"Score: {puntaje}", True, (65, 128, 78)) #actualizacion del puntaje 
                    boton_opcion_a = pygame.Rect(217, 285, 310, 50)
                    boton_opcion_b = pygame.Rect(217, 355, 310, 50)
                    boton_opcion_c = pygame.Rect(217, 425, 310, 50)
                
                #BOTON DE OPCIONES DE BOTONES
                if bandera_respuesta and intentos_respuesta > 0:
                    if boton_opcion_a.collidepoint(event.pos):
                        if lista_preguntas[pregunta_actual - 1]["correcta"] == "a":
                            bandera_respuesta = False
                            puntaje += 10 #si respondiste bien, te suma 10 puntos
                            text_score_actual = font.render(f"Score: {puntaje}", True, (65, 128, 78))
                            boton_opcion_b = pygame.Rect(217, 355, 0, 0)
                            boton_opcion_c = pygame.Rect(217, 425, 0, 0)
                            text_opcion_b = font.render("", True, (255, 255, 255))
                            text_opcion_c = font.render("", True, (255, 255, 255)) #actualiza puntaje y desaparecen los botones
                            sonido_correcto.play() 
                        else:
                            intentos_respuesta -= 1 #si te equivocaste te quita un intento y desaparece el boton
                            boton_opcion_a = pygame.Rect(265, 355, 0, 0)
                            text_opcion_a = font.render("", True, (255, 255, 255))
                            sonido_incorrecto.play()
                    elif boton_opcion_b.collidepoint(event.pos):
                        if lista_preguntas[pregunta_actual - 1]["correcta"] == "b":
                            bandera_respuesta = False
                            puntaje += 10
                            boton_opcion_a = pygame.Rect(217, 285, 0, 0)
                            boton_opcion_c = pygame.Rect(217, 425, 0, 0)
                            text_opcion_a = font.render("", True, (255, 255, 255))
                            text_opcion_c = font.render("", True, (255, 255, 255))
                            text_score_actual = font.render(f"Score: {puntaje}", True, (65, 128, 78))
                            sonido_correcto.play()
                        else:
                            intentos_respuesta -= 1
                            boton_opcion_b = pygame.Rect(217, 355, 0, 0)
                            text_opcion_b = font.render("", True, (255, 255, 255))
                            sonido_incorrecto.play()
                    elif boton_opcion_c.collidepoint(event.pos):
                        if lista_preguntas[pregunta_actual - 1]["correcta"] == "c":
                            bandera_respuesta = False
                            puntaje += 10
                            boton_opcion_b = pygame.Rect(217, 355, 0, 0)
                            boton_opcion_a = pygame.Rect(217, 285, 0, 0)
                            text_opcion_b = font.render("", True, (255, 255, 255))
                            text_opcion_a = font.render("", True, (255, 255, 255))
                            text_score_actual = font.render(f"Score: {puntaje}", True, (65, 128, 78))
                            sonido_correcto.play()
                        else:
                            intentos_respuesta -= 1
                            boton_opcion_c = pygame.Rect(217, 425, 0, 0)
                            text_opcion_c = font.render("", True, (255, 255, 255))
                            sonido_incorrecto.play()
                    if intentos_respuesta == 0: #cuando respondiste mal dos veces te saca los 3 botones (por defecto)
                        boton_opcion_b = pygame.Rect(217, 355, 0, 0) #aca desaparece el boton poniendose en "cero" para que no se vea
                        boton_opcion_a = pygame.Rect(217, 285, 0, 0) 
                        text_opcion_b = font.render("", True, (255, 255, 255)) #borras texto para que desaparezca y no se vea 
                        text_opcion_a = font.render("", True, (255, 255, 255))
                        boton_opcion_c = pygame.Rect(217, 425, 0, 0)
                        text_opcion_c = font.render("", True, (255, 255, 255)) 
            elif screen_actual == "Score":
                if boton_volver.collidepoint(event.pos):
                    screen_actual = "Menu"
                    pygame.mixer.music.load(r"C:\Users\LENOVO\OneDrive\Escritorio\Programación I\Cuphead.mp3")
                    pygame.mixer.music.play(-1)
        
        #BOTON PARA GUARDAR NOMBRE Y PUNTAJE
        if event.type == pygame.KEYDOWN:
            if screen_actual == "Guardar Score":
                if event.key == pygame.K_RETURN:
                    nuevo_record = {
                        "nombre": nombre,
                        "puntaje": puntaje
                    }
                    puntajes_json = leer_puntajes_de_data_json()    
                    puntajes_json.append(nuevo_record)
                    guardar_puntajes_data_json(puntajes_json)
                    nombre = ""
                    screen_actual = "Menu"
                #cuando termino el juego y pide puntaje nuevo, al presionar enter guarda el puntaje nuevo
                #de ahi al entrar en la opcion de ver puntajes se agrega el puntaje nuevo
                #el string vacio corresponde a que se pueda escribir de nuevo en blanco en el nombre del final del juego
                elif event.key in range(pygame.K_a, pygame.K_z + 1):
                    nombre += chr(event.key) #el chr transforma el numero de tecla en una letra (la letra que corresponde)
                    text_nombre = font.render("NOMBRE: " + nombre, True, (177, 155, 204))
                #cuando apreto un tecla se fija si pertence al rango de "a" a la "z" en caso de que no, no hace nada
            
    #DIBUJAR LA PANTALLA

    #pantalla 1
    if screen_actual == "Menu":
        screen.blit(imagen_principal_ajustada, (0, 0)) #imagen de fondo
        # color boton
        #pygame.draw.rect(screen, (222, 220, 227), boton_titulo, border_radius=10) #color de boton
        pygame.draw.rect(screen, (212, 116, 78), boton_jugar, border_radius=10)
        pygame.draw.rect(screen, (212, 116, 78), boton_score, border_radius=10)
        pygame.draw.rect(screen, (212, 116, 78), boton_exit, border_radius=10)
        
        #texto del juego
        screen.blit(text_titulo, (200, 20)) #posicion de la letra de los botones
        screen.blit(text_start, (123, 352))
        screen.blit(text_score, (468, 355))
        screen.blit(text_exit, (315, 452))

        
    #pantalla 2
    elif screen_actual == "Jugar":
        screen.blit(pantalla_2_ajustada, (0, 0)) #imagen de fondo
        #color boton
        pygame.draw.rect(screen, (194, 147, 45), boton_pregunta, border_radius=10) #color de boton
        pygame.draw.rect(screen, (194, 147, 45), boton_reiniciar, border_radius=10)
        #pygame.draw.rect(screen, (212, 116, 78), boton_score_actual, border_radius=10)
        
        pygame.draw.rect(screen, (0, 0, 0), boton_opcion_a, border_radius=15)
        pygame.draw.rect(screen, (0, 0, 0), boton_opcion_b, border_radius=15)
        pygame.draw.rect(screen, (0, 0, 0), boton_opcion_c, border_radius=15)
        
        #texto del juego
        screen.blit(text_pregunta, (52, 35)) #posicion de la letra de los botones
        screen.blit(text_reiniciar, (535, 35))
        screen.blit(text_score_actual, (10, 460))
        screen.blit(text_mensaje, (0, 170))
        screen.blit(text_opcion_a, (247, 294))
        screen.blit(text_opcion_b, (247, 364))
        screen.blit(text_opcion_c, (247, 434))

    elif screen_actual == "Score":
        screen.blit(pantalla_3_ajustada, (0,0))

        #pygame.draw.rect(screen, (212, 116, 78), boton_volver, border_radius=10)
        #pygame.draw.rect(screen, (212, 116, 78), boton_mensaje_final, border_radius=20)
        
        screen.blit(text_volver, (20, 20))
        screen.blit(text_mensaje_final, (245, 115))
        screen.blit(text_rank_1,(210, 180))
        screen.blit(text_rank_2,(210, 230))
        screen.blit(text_rank_3,(210, 280))

    
    elif screen_actual == "Guardar Score":
        screen.blit(pantalla_4_ajustada, (0, 0))
        screen.blit(font.render("Terminó el juego Ingrese su nombre: ", True, (255, 255, 255)), (60, 30))
        screen.blit(text_nombre, (45,150))
         




    pygame.display.flip() # Actualizar la pantalla

pygame.quit() # Fin del juego
