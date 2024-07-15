from tkinter import *
from tkinter import ttk
import random
from Sorting_Algos import bubbleSort

root = Tk()
root.title("DSA Project Soring Algorithm Visualizer")
root.geometry('750x600')
root.config(bg='orange')

selectAlgo = StringVar()
arr = []

def generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(array_size.get())
    arr = []
    
    for i in range(size):
        arr.append(random.randrange(lowest,highest+1))

    drawrectangle(arr , ['red' for i in range (len(arr))])

def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [ i / max(arr) for i in arr]
    for i, height in enumerate (normalized_array): 
        x0 = i * bar_width + border_offset + spacing 
        y0 = canvas_height - height * 340 
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height 
        canvas.create_rectangle(x0,y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2,y0, anchor=SW, text=str(arr[i]))

    root.update_idletasks()

def sorting():
    global arr
    bubbleSort(arr , drawrectangle , sortingSpeed.get())

# GUI Coding Part
option_frame = Frame(root , width=700 , height=300 , bg='green')
option_frame.grid(row=0 , column=0 , padx=10 , pady=10)

canvas = Canvas(root , width=700 , height=350 , bg='grey')
canvas.grid(row=1 , column=0 , padx=10 , pady=5)

Label(option_frame , text='Algorithm Choice : ', ).grid(row=0,column=0,padx=10,pady=10)

algoMenu = ttk.Combobox(option_frame , textvariable=selectAlgo , values=['Bubble Sort' , 'Insertion Sort' , 'Selection Sort','Quick Sort','Merge Sort'] ,width=10)
algoMenu.grid(row=0 ,column=1 ,padx=5 ,pady=5)
algoMenu.current(0)

sortingSpeed = Scale(option_frame , from_= 0.1 , to= 2.0 , length=100 , digits=2 , resolution=0.2 , orient=HORIZONTAL , label="Sorting Speed")
sortingSpeed.grid(row=0, column=2 , padx=10 , pady=10)

Button(option_frame , text='Start Sorting' , command=sorting , bg='red' , height=5).grid(row=0 , column=3 , padx= 5 , pady=5)

lowest_Entry = Scale(option_frame , from_=5 , to=20 , resolution=1 ,orient=HORIZONTAL ,label="Lower Limit" )
lowest_Entry.grid(row=1, column=0 , padx=5, pady=5)

highest_Entry = Scale(option_frame , from_=20 , to=100 , resolution=1 ,orient=HORIZONTAL , label="Upper Limit")
highest_Entry.grid(row=1, column=1 , padx=5, pady=5)

array_size = Scale(option_frame , from_=3 , to=25 , resolution=1 ,orient=HORIZONTAL , label="Array Size")
array_size.grid(row=1, column=2, padx=5, pady=5)

Button(option_frame , text='Generate Array' , command=generate_array , bg='blue' , height=5).grid(row=1,column=3,padx=10,pady=10)

root.mainloop() 