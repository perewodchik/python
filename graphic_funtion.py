from graphics import *
import math as m

window_width = window_height = 800
unit_x = 10
unit_y = 10
division = 0.05 #Разеделение, должно быть меньше 1!!!!!

x_axis = window_height//2 # ось Х
y_axis = window_width//2  # ось Y

for_handle_click = [Line(Point(0,0),Point(0,0))]*8 #КОСТЫЛЬ, убирает линии после рисования
for_surface_area = [] #Тут будут храниться прямоугольники площади


# Уравнение функции 
def equation(x):
	return x**2 - 5*x 
	
def draw_background(unit_x,unit_y):
	""" Рисует задний фон
	"""
	clear = Rectangle(Point(0,0), Point(window_width, window_height))
	clear.setFill("white")
	clear.draw(win)
	win.setBackground(color_rgb(255,255,255))

def draw_axis(unit_x, unit_y):
	""" Рисует оси Х и Y,
		а также размечает отрезки
	"""
	
	#Рисует оси X и Y
	Line(Point(0, window_height//2), Point(window_width, window_height//2)).draw(win)
	Line(Point(window_width//2, 0), Point(window_width//2, window_height)).draw(win)
	
	#Рисует отрезки на оси Х и выводит числа
	for k in range(-unit_x+1, unit_x, 1):
		x_point = (k+unit_x)*window_width//(unit_x*2)
		Line(Point(x_point, x_axis - 10), Point( x_point, x_axis + 10)).draw(win)
		Text(Point(x_point, x_axis + 20), k).draw(win)
	
	#Рисут отрезки на оси Y и выводит числа
	for k in range(-unit_y+1, unit_y, 1):
		y_point = (k+unit_y)*window_height//(unit_y*2)
		Line(Point(y_axis -10, y_point), Point(y_axis +10, y_point)).draw(win)
		Text(Point(y_axis - 20, y_point), -k if k != 0 else "").draw(win)
		
	Line(Point(window_width, x_axis), Point(window_width - 20, x_axis - 10)).draw(win)
	Line(Point(window_width, x_axis), Point(window_width - 20, x_axis + 10)).draw(win)
	Text(Point(window_width - 10, x_axis + 20), "X").draw(win)
	
	Line(Point(y_axis, 0), Point(y_axis - 10, 0 + 20)).draw(win)
	Line(Point(y_axis, 0), Point(y_axis + 10, 0 + 20)).draw(win)
	Text(Point(y_axis - 20, 0 + 10), "Y").draw(win)

def draw_points(equation, unit_x, unit_y):
	""" Рисует значения функции, соответсвующие аргументу
	"""
	
	k = -unit_x 
	while k < unit_x :
		k += division
		x_starting = (k+unit_x)*window_width//(unit_x*2)
		y_starting = x_axis - equation(k)*window_height//(unit_y*2)
		x_ending = (k+division+unit_x)*window_width//(unit_x*2)
		y_ending = x_axis - equation(k+division)*window_height//(unit_y*2)
		Line( Point( x_starting, y_starting ), Point( x_ending , y_ending )).draw(win)
		
def handle_click(coordinate):
	""" Получает координаты мыши, и выводит значение функции при заданном Хъ
		Также выводит площадь функции
	"""

	for_handle_click[0].undraw()
	for_handle_click[1].undraw()
	for_handle_click[2].undraw()
	for_handle_click[3].undraw()
	for_handle_click[4].undraw()
	for_handle_click[5].undraw()
	for_handle_click[6].undraw()
	for_handle_click[7].undraw()
	
	
	x = ((coordinate.getX() - y_axis)/y_axis)*unit_x
	y_point = x_axis - equation(x)*window_height//(unit_y*2)
	for_handle_click[0] = Line( Point(coordinate.getX(), x_axis), Point(coordinate.getX(), y_point))
	for_handle_click[1] = Line( Point(y_axis, y_point), Point(coordinate.getX(), y_point))
	for_handle_click[2] = Text( Point(30, 30), "X = ")
	for_handle_click[3] = Text( Point(60, 30), round(x,2))
	for_handle_click[4] = Text( Point(30, 50), "Y = ")
	for_handle_click[5] = Text( Point(60, 50), round(equation(x),2))
	for_handle_click[6] = Text( Point(80, 70), "Surface from 0 to X: ")
	for_handle_click[7] = Text( Point(170,70), abs(round(surface(x), 2)))

	for_handle_click[0].setWidth(3)
	for_handle_click[1].setWidth(3)
	draw_surface_area(x)
	
	for_handle_click[0].draw(win)
	for_handle_click[1].draw(win)
	for_handle_click[2].draw(win)
	for_handle_click[3].draw(win)
	for_handle_click[4].draw(win)
	for_handle_click[5].draw(win)
	for_handle_click[6].draw(win)
	for_handle_click[7].draw(win)
	
def surface(x):
	""" Находит площадь функции от 0 до Х
	"""
	sum = 0
	while x < 0:
		sum = sum + equation(x)
		x += division
	while x > 0:
		sum = sum + equation(x)
		x -= division
	return sum*division

def draw_surface_area(x):
	""" Рисует площадь функции
	"""

	k = len(for_surface_area)
	while len(for_surface_area) > 0:
		k -= 1
		for_surface_area[k].undraw()
		for_surface_area.pop()
	
	if x < 0:
		while x < 0:
			x_starting = (x+unit_x)*window_width//(unit_x*2)
			y_starting = x_axis - equation(x)*window_height//(unit_y*2)
			x_ending = (x+division+unit_x)*window_width//(unit_x*2)
			y_ending = x_axis - equation(x+division)*window_height//(unit_y*2)
			for_surface_area.append(Rectangle(Point(x_starting, y_starting), Point(x_ending, x_axis)))
			x += division
	else:	
		while x > 0:
			x_starting = (x+division+unit_x)*window_width//(unit_x*2)
			y_starting = x_axis - equation(x)*window_height//(unit_y*2)
			x_ending = (x+unit_x)*window_width//(unit_x*2)
			y_ending = x_axis - equation(x)*window_height//(unit_y*2)
			for_surface_area.append(Rectangle(Point(x_starting, y_starting), Point(x_ending, x_axis)))
			x -= division
		
	
	
	for k  in range(len(for_surface_area)):
		for_surface_area[k].setFill(color_rgb(255,0,0))
		for_surface_area[k].setOutline(color_rgb(255,0,0))
		for_surface_area[k].move(-division/5*window_width//unit_x,0)
		for_surface_area[k].draw(win)

win = GraphWin("Function", window_width, window_height)

while True:
	draw_axis(unit_x,unit_y)
	draw_points(equation, unit_x, unit_y)
	handle_click(win.getMouse())