import pygame, sys, time, ctypes, random

# Metodos y Parametros Inciales

pygame.init()
size = [1525, 800]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Nombre del Juego Pendiente")


# Funcion para cargar y actualizar (RESIZE) IMAGENES
def load_images(size):
    
    # Global Variables (Imagenes)
    global logo
    global press_start
    global game_background
    global image_background
    global caesars
    global masas
    global dough_raw
    global dough_cooked
    global dough_overcooked
    global tomato
    global jamonada
    global peperoni
    global queso
    global button_in
    global button_out
    global button_tray
    global layer_tomato
    global layer_cheese
    global layer_ham
    global layer_pepperoni
    global ready_0
    global ready_1
    global ready_2
   
    
    # Boton Masas
    masas = pygame.image.load("dough.png")
    masas = pygame.transform.scale(masas, (int(size[0]*0.30), int(size[1]*0.26))) 

    # Boton tomato
    tomato = pygame.image.load("tomato.png")
    tomato = pygame.transform.scale(tomato, (int(size[0]*0.1), int(size[1]*0.31)))

    # Boton jamonada
    jamonada = pygame.image.load("ham.png")
    jamonada = pygame.transform.scale(jamonada, (int(size[0]*0.18), int(size[1]*0.20)))

    # Boton peperoni
    peperoni = pygame.image.load("pepperoni.png")
    peperoni = pygame.transform.scale(peperoni, (int(size[0]*0.165), int(size[1]*0.19)))

    # Boton Queso
    queso = pygame.image.load("cheese.png")
    queso = pygame.transform.scale(queso, (int(size[0]*0.18), int(size[1]*0.21)))

    #Boton In
    button_in = pygame.image.load("button_in.png")
    button_in = pygame.transform.scale(button_in, (int(size[0]*0.14), int(size[1]*0.15)))

    #Boton Out
    button_out = pygame.image.load("button_out.png")
    button_out = pygame.transform.scale(button_out, (int(size[0]*0.14), int(size[1]*0.15)))

    #Boton Tray
    button_tray = pygame.image.load("button_tray.png")
    button_tray = pygame.transform.scale(button_tray, (int(size[0]*0.30), int(size[1]*0.26)))

    
    
    
    # Logo
    logo = pygame.image.load("logo.png")
    logo = pygame.transform.scale(logo, (int(size[0]*0.429), int(size[1]*0.78)))
    
    # Boton Start Image (Resizable)
    press_start = pygame.image.load("text1.png")   
    press_start = pygame.transform.scale(press_start, (int(size[0]/3), int(size[1]*0.45)))

    # Game Backgorund Image (Resizable)
    game_background = pygame.image.load("game_background.png").convert()
    game_background = pygame.transform.scale(game_background, size)

    # Main Menu Background image (Resizable)
    image_background = pygame.image.load("background.jpg").convert()
    image_background = pygame.transform.scale(image_background, size)

    # Caesars
    caesars = pygame.image.load("caesars.png")
    caesars = pygame.transform.scale(caesars, (int(size[0]*0.28), int(size[1]*0.83)))

    

    
    # Raw Dough
    dough_raw = pygame.image.load("dough_raw.png")
    dough_raw = pygame.transform.scale(dough_raw, (int(size[0]*0.30), int(size[1]*0.26))) 

    # Cooked dough
    dough_cooked = pygame.image.load("dough_cooked.png")
    dough_cooked = pygame.transform.scale(dough_cooked, (int(size[0]*0.30), int(size[1]*0.26)))

    # Overcooked dough
    dough_overcooked = pygame.image.load("dough_overcooked.png")
    dough_overcooked = pygame.transform.scale(dough_overcooked, (int(size[0]*0.30), int(size[1]*0.26)))

    # Tomato Sauce Layer
    layer_tomato = pygame.image.load("layer_tomato.png")
    layer_tomato = pygame.transform.scale(layer_tomato, (int(size[0]*0.35), int(size[1]*0.4)))

    # Cheese Layer
    layer_cheese = pygame.image.load("layer_cheese.png")
    layer_cheese = pygame.transform.scale(layer_cheese, (int(size[0]*0.30), int(size[1]*0.26))) 

    # Ham Layer
    layer_ham = pygame.image.load("layer_ham.png")
    layer_ham = pygame.transform.scale(layer_ham, (int(size[0]*0.30), int(size[1]*0.26)))

    # Pepperoni Layer
    layer_pepperoni = pygame.image.load("layer_pepperoni.png")
    layer_pepperoni = pygame.transform.scale(layer_pepperoni, (int(size[0]*0.30), int(size[1]*0.26))) 
    
    
    #Indicator
    ready_0 = pygame.image.load("ready_0.png")
    ready_0 = pygame.transform.scale(ready_0,(int(size[0]*0.05), int(size[1]*0.05)))

    ready_1 = pygame.image.load("ready_1.png")
    ready_1 = pygame.transform.scale(ready_1, (int(size[0]*0.05), int(size[1]*0.05)))

    ready_2 = pygame.image.load("ready_2.png")
    ready_2 = pygame.transform.scale(ready_2, (int(size[0]*0.05), int(size[1]*0.05)))

    

# BUTTON CLASS
class Button:
    def __init__(self, image, x, y, w, h, txt=''):
        # Coords (x, y)
        self.x = x
        self.y = y

        # Dimention
        self.w = w
        self.h = h

        # Text (Optional)
        self.txt = txt

        # Image object 
        self.image = image
    
    def draw(self):
        # Print Image
        screen.blit(self.image, (self.x, self.y))

        # Print Txt
        if self.txt != '':
            font = pygame.font.SysFont('comicsans', 60)
            txt = font.render(self.txt, 1, (0,0,0))
            win.blit(txt, (self.x + (self.w/2 - txt.get_width()/2), self.y + (self.h/2 - text.get_height()/2)))
    
    def over(self, pos):

        #Pos is a tuple of (x,y) mouse coordinates
        if pos[0] > self.x and pos[0] < self.x + self.w:
            if pos[1] > self.y and pos[1] < self.y + self.h:
                return True
        return False

class Pizza:
    def __init__(self):
        self.masa = False
        self.dough_status = 0 #Cruda xd
        self.ingredients = {"tomato":False, "cheese":False, "ham":False, "pepperoni":False}
        self.start_time = 0
        self.cooking_time = 0

    def dibujar(self):
        #Dibujar masa
        if self.masa:
            if self.cooking_time <= 5:
                screen.blit(dough_raw, (810, 435))
                #Llamar imagen (Cruda)
            elif self.cooking_time > 5 and self.cooking_time <= 10:
                self.dough_status = 1
                screen.blit(dough_cooked, (810, 435))
                #Llamar imagen (Cocinada)      
            else:
                self.dough_status = 2
                screen.blit(dough_overcooked, (810, 435))
                #Llamar imagen Quemada :(


        values_ingredients = self.ingredients.items()
        materials = [layer_tomato, layer_cheese, layer_ham, layer_pepperoni]
        positions = [(750, 375), (810, 420), (810, 430), (810, 430)]
        
        for i, j, ingredient in zip(range(4), positions, values_ingredients):
            if ingredient[1]:
                screen.blit(materials[i], j)

    def add(self, ingredient):
        self.ingredients[ingredient] = True

    def update(self):
        if self.cooking_time <= 3:
            self.dough_status = 0
        elif self.cooking_time > 3 and self.cooking_time <= 6:
            self.dough_status = 1  
        else:
            self.dough_status = 2

class Order:
    def __init__(self):
        self.waiting = True
        self.start_time = 0
        self.wait_time = 0
        self.ingredients = []

    def what(self, n):
        self.ingredients = n      

    def start_counter(self):
        if self.wait_time == 0 and self.waiting: 
            self.start_time = time.time()
            return self.start_time

        self.wait_time = time.time() - self.start_time
        return self.wait_time

    
    def popup(self):
        values_ingredients = ["tomato", "cheese", "ham", "pepperoni"]
        materials = [layer_tomato, layer_cheese, layer_ham, layer_pepperoni]
        positions = [(1000, -50), (1060, -5), (1060, 5), (1060, 5)]
        
        screen.blit(dough_cooked, (1060, 10))
        for i, j, k in zip(values_ingredients, materials, positions):
            if i in self.ingredients:
                screen.blit(j, k)           
    
class Oven():
    def __init__(self):
        self.inside = None
    
    def insert(self, n):
        self.inside = n
        self.inside.start_time = time.time()
        
    def remove(self, n):
        self.inside.cooking_time = time.time() - self.inside.start_time
        self.inside = None

    def update(self):
        self.inside.cooking_time = time.time() - self.inside.start_time
        self.inside.update()

    def draw(self):
        if self.inside.cooking_time <= 3:
            screen.blit(ready_0, (50, 143))
        elif self.inside.cooking_time > 3 and self.inside.cooking_time <= 6:
            screen.blit(ready_1, (50, 143))
        elif self.inside.cooking_time > 6:                
            screen.blit(ready_2, (50, 143))

#Functions
def asign_order():
    supplies = ["tomato", "cheese", "ham", "pepperoni"]
    orden = Order()
    m = []
    n = random.randint(1, 4)
    m = random.sample(supplies, n)
    orden.what(m)
    orden.popup()
    return orden


start_game = False # False -> Main Menu
load_images(size) # Load images 

# start_button = Button for start game
start_button = Button(press_start, 0, 0, int(size[0]/3), int(size[1]*0.45))

# Boton Masa
masas_button = Button(masas, int(size[0]*0.70), int(size[1]*0.80), int(size[0]*0.30), int(size[1]*0.26))

# Boton tomato
tomato_button = Button(tomato, int(size[0]*0.90), int(size[1]*0.30), int(size[0]*0.1), int(size[1]*0.31))

# Boton jamonada
jamonada_button = Button(jamonada, int(size[0]*0.27), int(size[1]*0.66), int(size[0]*0.18), int(size[1]*0.20))

# Boton peperoni
peperoni_button = Button(peperoni, int(size[0]*0.28), int(size[1]*0.52), int(size[0]*0.165), int(size[1]*0.19))

# Boton queso
queso_button = Button(queso, int(size[0]*0.37), int(size[1]*0.42), int(size[0]*0.18), int(size[1]*0.21))

# Boton In
in_button = Button(button_in, int(size[0]*0.001), int(size[1]*0.71), int(size[0]*0.14), int(size[1]*0.15))

# Boton Out
out_button = Button(button_out, int(size[0]*0.125), int(size[1]*0.69), int(size[0]*0.14), int(size[1]*0.15))

#Boton Tray
tray_button = Button(button_tray, 390, 230, int(size[0]*0.30), int(size[1]*0.26))

def entregar(orden, entrega):
    if entrega.dough_status == 0 or entrega.dough_status == 2:
        return -50
    if orden.wait_time > 9:
        return -50

    list_a = []
    for i in entrega.ingredients:
        if entrega.ingredients[i] == True:
            list_a.append(i)
    list_a = sorted(list_a)
    orden.ingredients = sorted(orden.ingredients)
    if list_a == orden.ingredients:
        return 100
    return -50
    
def print_score(score):
    font = pygame.font.Font(None, 120)
    txt = "Score: " + str(score)
    mensaje = font.render(txt, 1, (0, 0, 0))
    screen.blit(mensaje, (10, 10))
    return

def print_entrega(entrega):
    if entrega.dough_status == 0: screen.blit(dough_raw, (390, 230))
    elif entrega.dough_status == 1: screen.blit(dough_cooked, (390, 230))
    else: screen.blit(dough_overcooked, (390, 230))

    values = entrega.ingredients.items()
    positions = [(330, 170), (390, 215), (390, 225), (390, 225)]
    ima = [layer_tomato, layer_cheese, layer_ham, layer_pepperoni]

    for i, j, k in zip(ima, positions, values):
        if k[1]:
            screen.blit(i, j)


def main():

    #Yep.. More globals
    global size
    global button_start
    global start_button

    #for de Eventos
    for event in pygame.event.get():

        mouse_coords = pygame.mouse.get_pos()

        # QUIT
        if event.type == pygame.QUIT:
            sys.exit()
        
        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: return True # Space Key for Start game
            if event.key == pygame.K_ESCAPE: sys.exit() # Esc Key for Exit

        # What if user Resize window?
        if event.type == pygame.RESIZABLE:
            
            size = [event.w, event.h] # Size change parameters
            load_images(size) # Reload and convert images to adjust to the new size

            # New parameters to button calling init()
            # New x and y
            boton_start = (int(size[0] * 0.29), int(size[1]*0.55))
            # New w and h
            start_button = Button(press_start, boton_start[0], boton_start[1], int(size[0]/3), int(size[1]*0.45))

        # If press the button Start Game
        if start_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            return True

    #Impresion de Background
    screen.blit(image_background, (0, 0))

    # Draw metod for Button
    start_button.draw()

    # Logo
    screen.blit(logo, (370, 0))

    # Penguin Image :D
    coords_caesars = (int(size[0] * 0.65), int(size[1]*0.15))
    screen.blit(caesars, coords_caesars)


    # Screen update
    pygame.display.update()
    pygame.display.flip()

    return False

order = None
pizza = None
entrega = None
score = 0
oven = Oven()
txt = ""

while True:

    # Main menu
    if not start_game:
        start_game = main()
        continue

    # Crear
    if pizza == None:
        pizza = Pizza()

    if order == None:
        order = asign_order()
        order.start_time = time.time()

    # Print Game Background
    screen.blit(game_background, (0, 0))
    
    # Test on Table
    #screen.blit(dough_raw, (810, 435))
    #screen.blit(layer_tomato, (750, 375))
    #screen.blit(layer_cheese, (810, 420))
    #screen.blit(layer_ham, (810, 430))
    #screen.blit(layer_pepperoni, (810, 430))

    # Test on Tray
    #screen.blit(dough_cooked, (390, 230))
    #screen.blit(layer_tomato, (330, 170))
    #screen.blit(layer_cheese, (390, 215))
    #screen.blit(layer_ham, (390, 225))
    #screen.blit(layer_pepperoni, (390, 225))

    # Test on Orders
    #screen.blit(dough_cooked, (1060, 10))
    #screen.blit(layer_tomato, (1000, -50))
    #screen.blit(layer_cheese, (1060, -5))
    #screen.blit(layer_ham, (1060, 5))
    #screen.blit(layer_pepperoni, (1060, 5))

    # Test on Indicators
    #screen.blit(ready_0, (50, 143))
    #screen.blit(ready_1, (50, 143))
    #screen.blit(ready_2, (50, 143))

    #Impresion_Botones

    masas_button.draw()
    tomato_button.draw()
    jamonada_button.draw()
    peperoni_button.draw()
    queso_button.draw()

    out_button.draw()
    in_button.draw()
    
    # for de Eventos
    for event in pygame.event.get():

        mouse_coords = pygame.mouse.get_pos()
        # Quit
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.RESIZABLE:
            #print(event.w, event.h)
            back_size = (event.w, event.h)
            load_images(back_size)

        if masas_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if not pizza.masa:
                pizza.masa = True
                     
        if tomato_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if pizza.masa:   
                pizza.add("tomato")

        if queso_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if pizza.masa: 
                pizza.add("cheese")

        if jamonada_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if pizza.masa: 
                pizza.add("ham")

        if peperoni_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if pizza.masa:   
                pizza.add("pepperoni")  

        if in_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if pizza != None and pizza.masa:   
                oven.insert(pizza)
                pizza = None
            
        if out_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if oven.inside != None and entrega == None:   
                entrega = oven.inside
                order.wait_time = time.time() - order.start_time
                oven.inside = None

        if tray_button.over(mouse_coords) and event.type == pygame.MOUSEBUTTONDOWN:
            if entrega != None:
                score += entregar(order, entrega)
                entrega = None
                order = None
   

    # Logic

    if pizza != None:
        pizza.dibujar()

    if oven.inside != None:
       oven.update()
       oven.draw()

    if order != None:
        order.popup()

    print_score(score)

    if entrega != None:
        print_entrega(entrega)

    
    if score< -500 or score > 500:
        start_game = False
        order = None
        pizza = None
        entrega = None
        score = 0
        oven = Oven()

    # Screen
    pygame.display.update()
    pygame.display.flip()

