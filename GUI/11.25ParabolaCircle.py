try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import math


def parabola(graph, size):
    for x in range(-size, size):
        y = x * x / size
        plot(graph, x, y)


def circle(graph, radius, g, h, color='green'):
    # for x in range(g*100, (g + radius)*100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g)**2)))
    #     plot(graph, x, y)
    #     plot(graph, x, 2*h - y)
    #     plot(graph, 2*g - x, y)
    #     plot(graph, 2*g - x, 2*h - y)
    graph.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)


def draw_axes(graph):
    graph.update()
    x_origin = graph.winfo_width() / 2
    y_origin = graph.winfo_height() / 2
    graph.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    graph.create_line(-x_origin, 0, x_origin, 0, fill="black")
    graph.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(graph, x, y):
    graph.create_line(x, -y, x + 1, -y + 1, fill="red")


mainwindow = tkinter.Tk()
mainwindow.title("Parabola")
mainwindow.geometry("640x480")
canvas = tkinter.Canvas(mainwindow, width=640, height=480)
canvas.grid(row=0, column=0)

print(repr(canvas))
draw_axes(canvas)
parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)
circle(canvas, 50, 0, 0, "red")
mainwindow.mainloop()
