#############
#############
#Make Sure to include sympy library
#Make Sure to include tkinter library
#############
#############
from sympy import *
from tkinter import *

app = Tk()
app.title('Traffixo')
app.minsize(600,550)
app.config(bg="#1b1464")
code = -9878888

canvas = Canvas(app, width=250, height=230)
img = PhotoImage(file="42.png")

def first():
    Label(bg='#1b1464').pack()
    welcome.pack()
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=img)
    Label(bg='#1b1464').pack()
    first_btn.pack()
    end.pack()


canvas2 = Canvas(app, width=180, height=170)
img2 = PhotoImage(file="4.png")

def second():
    first_btn.destroy()
    welcome.destroy()
    canvas.destroy()
    end.destroy()

    canvas2.pack()
    canvas2.create_image(0, 0, anchor=NW, image=img2)

    Lx.pack()
    x1.pack()
    x2.pack()

    Ly.pack()
    y1.pack()
    y2.pack()


    Lz.pack()
    z1.pack()
    z2.pack()

    Lw.pack()
    w1.pack()
    w2.pack()

    Label(bg='#1b1464').pack()
    buttonCalc.pack()


def third():

    Lxyzw = making_mat()
    print(Lxyzw)
    Lx.destroy()
    x1.destroy()
    x2.destroy()
    Ly.destroy()
    y1.destroy()
    y2.destroy()
    Lz.destroy()
    z1.destroy()
    z2.destroy()
    Lw.destroy()
    w1.destroy()
    w2.destroy()

    buttonCalc.destroy()
    canvas2.destroy()
##########################
    resultL.pack()


    dic ={
        Lxyzw[0]: "x",
        Lxyzw[1]:"y",
        Lxyzw[2]:"z",
        Lxyzw[3]:"w"
    }
    best = dic[min(dic.keys())]

    if( Lxyzw[0]==code):
        text1="values are manipulated can't be like that"
    else:
        text1 = f'''street X = {Lxyzw[0]}
street Y = {Lxyzw[1]}
street Z = {Lxyzw[2]}
street W = {Lxyzw[3]}
\nbest street to go through is Street {best}'''
    result2.config(text=text1)
    result2.pack()


def getValueStreet(M,r):
    return M[0].row(r).col(4).det()

def making_mat():
    M = Matrix([
        [1, -1, 0, 0, int(x2.get()) - int(y1.get()) ],
        [-1, 0, 0, 1, int(y2.get()) - int(x1.get()) ],
        [0, 0, 1, -1, int(z2.get()) - int(w1.get()) ],
        [0, 1, -1, 1, int(y2.get()) - int(z1.get()) ]
    ])

    M2 = M.rref()

    print(M2)
    print(getValueStreet(M2,0))
    print(getValueStreet(M2,1))
    print(getValueStreet(M2,2))
    print(getValueStreet(M2,3))


    if(getValueStreet(M2,0)<0 or getValueStreet(M2,1)<0 or getValueStreet(M2,2)<0 or getValueStreet(M2,3)<0):
        return [code, getValueStreet(M2, 1), getValueStreet(M2, 2), getValueStreet(M2, 3)]

    return [getValueStreet(M2,0),getValueStreet(M2,1),getValueStreet(M2,2),getValueStreet(M2,3)]



welcome = Label(app, text="Welcome in Traffixo program\n",font='Arial 20 bold',bg='#1b1464',fg='#00ffc5')
end = Label(app, text="\n\n\n\nProgram by\n\nMoustafa Ashmawy - Phelopater Ramsis - Hassan Ahmed",font='Arial 12',bg='#1b1464',fg='#00ffc5')

first_btn= Button(text='start simulating',command=second,height=2,width=20,font='Arial 12',bg='#00ffc5')
first()

Lx = Label(text='Street X',bg='#1b1464',fg='#00ffc5')
Ly =Label(text='Street Y',bg='#1b1464',fg='#00ffc5')
Lw = Label(text='Street W',bg='#1b1464',fg='#00ffc5')
Lz = Label(text='Street Z',bg='#1b1464',fg='#00ffc5')
x1 = Entry(bg='#1b1464',fg='#ec008c')
x2= Entry(bg='#1b1464',fg='#ec008c')
y1= Entry(bg='#1b1464',fg='#ec008c')
y2= Entry(bg='#1b1464',fg='#ec008c')
z1= Entry(bg='#1b1464',fg='#ec008c')
z2= Entry(bg='#1b1464',fg='#ec008c')
w1= Entry(bg='#1b1464',fg='#ec008c')
w2= Entry(bg='#1b1464',fg='#ec008c')

buttonCalc = Button(text='Calculating',command=third,height=2,width=20,font='Arial 12',bg='#00ffc5')


resultL = Label(text='Results of the traffic system',font='Arial 18 bold',bg='#1b1464',fg='#00ffc5')
result2 = Label(text='Results of the traffic system',font='Arial 14 bold',bg='#1b1464',fg='#00ffc5')


app.mainloop()
