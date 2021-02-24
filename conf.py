from tkinter import*

def change_color():
    global color, label_im, price_color
    if color.get()=='red':
        label_im['image']=im_red
        price_color=20000
        
    if color.get()=='gray':
        label_im['image']=im_gray
        price_color=0
        
    if color.get()=='violet':
        label_im['image']=im_violet
        price_color=50000
        
    if color.get()=='chocolate':
        label_im['image']=im_chocolate
        price_color=30000
        
    if color.get()=='green':
        label_im['image']=im_green
        price_color=20000
        
    if color.get()=='blue':
        label_im['image']=im_blue
        price_color=20000

def submit():
    global inter1, inter2, inter3, exter1, exter2, exter3
    global trans, price_base, price_color, price_interior, price, label_price
    global price_exterior, price_transmission

    i1=0
    i2=0
    i3=0
    e1=0
    e2=0
    e3=0
    
    if inter1.get()==1:
        i1=10000
    if inter2.get()==2:
        i2=15000
    if inter3.get()==3:
        i3=12000
    price_interior=i1+i2+i3
        
    if exter1.get()==1:
        e1=10000
    if exter2.get()==2:
        e2=10000
    if exter3.get()==3:
        e3=10000
    price_exterior=e1+e2+e3

    if trans.get()==1:
        price_transmission=0
    if trans.get()==2:
        price_transmission=5000
        
    price=price_base+price_color+price_interior+price_exterior+price_transmission
    label_price.config(text=f'{price} рублей')
    
a=Tk()
a.title('Конфигуратор автомобиля')
a.iconbitmap('images/icon_black.ico')
a.config(bg='white')
a.geometry('700x420+460+150')
a.resizable(width=False, height=False)

price_base=700000
price_color=0
price_interior=0
price_transmission=0
price_exterior=0
price=price_base+price_color+price_interior+price_exterior+price_transmission

submit_btn=Button(text='Рассчитать',fg='white',bg='orange',command=submit,
                  font=('Arial',13,'bold'),bd=5)
submit_btn.pack(side=BOTTOM)

label_price=Label(text=f'{price} рублей',font=('Arial',18,'bold'),bg='palegreen',width=700)
label_price.pack(side=TOP,fill=X)

im_red=PhotoImage(file='images/red.gif')
im_blue=PhotoImage(file='images/blue.gif')
im_gray=PhotoImage(file='images/gray.gif')
im_green=PhotoImage(file='images/green.gif')
im_chocolate=PhotoImage(file='images/chocolate.gif')
im_violet=PhotoImage(file='images/violet.gif')

label_im=Label(image=im_gray,bg='white')
label_im.pack(side=TOP,pady=12)

frame=Frame(a,bg='lightgray',height=30)
frame.pack(fill=X)

#frame
frame1=Frame(a,bg='blueviolet',height=300)
frame1.pack(fill=X,pady=8)

i_frame=LabelFrame(frame1,text='Интерьер',height=250,bg='khaki',width=150)
i_frame.pack(side=LEFT,padx=25,pady=10)

e_frame=LabelFrame(frame1,text='Экстерьер',height=250,bg='yellowgreen',width=150)
e_frame.pack(side=LEFT,padx=35,pady=10)

t_frame=LabelFrame(frame1,text='Коробка передач',height=70,bg='ivory',width=250)
t_frame.pack(side=LEFT,padx=25,pady=3)

#interior
inter1=IntVar()
i1=Checkbutton(i_frame,text='Подогрев руля',bg='khaki',font=('Arial',11,'bold'),
               variable=inter1,onvalue=1,offvalue=0)
i1.pack(anchor=W)

inter2=IntVar()
i2=Checkbutton(i_frame,text='Подогрев сидений',bg='khaki',font=('Arial',11,'bold'),
               variable=inter2,onvalue=2,offvalue=0)
i2.pack(anchor=W)

inter3=IntVar()
i3=Checkbutton(i_frame,text='Подлокотник',bg='khaki',font=('Arial',11,'bold'),
               variable=inter3,onvalue=3,offvalue=0)
i3.pack(anchor=W)

#exterior
exter1=IntVar()
e1=Checkbutton(e_frame,text='Подкрылки',bg='yellowgreen',font=('Arial',11,'bold'),
               variable=exter1,onvalue=1,offvalue=0)
e1.pack(anchor=W)

exter2=IntVar()
e2=Checkbutton(e_frame,text='Защита радиатора',bg='yellowgreen',font=('Arial',11,'bold'),
               variable=exter2,onvalue=2,offvalue=0)
e2.pack(anchor=W)

exter3=IntVar()
e3=Checkbutton(e_frame,text='Зеркала хром',bg='yellowgreen',font=('Arial',11,'bold'),
               variable=exter3,onvalue=3,offvalue=0)
e3.pack(anchor=W)

#transmission
trans=IntVar()
trans.set(2)
t1=Radiobutton(t_frame,text='механическая',bg='ivory',font=('Arial',11,'bold'),
               variable=trans, value=1)
t1.pack(anchor=W)
t2=Radiobutton(t_frame,text='автоматическая',bg='ivory',font=('Arial',11,'bold'),
               variable=trans, value=2)
t2.pack(anchor=W)

#colors
color=StringVar()
color.set('gray')
gray=Radiobutton(frame,text='серый',variable=color, value='gray',
                 font=('Arial',10,'bold'),bg='silver',
                 width=11,command=change_color)
gray.pack(side=LEFT,expand=1)

blue=Radiobutton(frame,text='голубой',variable=color, value='blue',
                 font=('Arial',10,'bold'),bg='aqua',
                 width=11,command=change_color)
blue.pack(side=LEFT,expand=1)

red=Radiobutton(frame,text='красный',variable=color, value='red',
                font=('Arial',10,'bold'),bg='crimson',
                width=11,fg='bisque',command=change_color)
red.pack(side=LEFT,expand=1)

green=Radiobutton(frame,text='зеленый',variable=color, value='green',
                  font=('Arial',10,'bold'),bg='yellowgreen',
                  width=11,command=change_color)
green.pack(side=LEFT,expand=1)

chocolate=Radiobutton(frame,text='шоколад',variable=color, value='chocolate',
                      font=('Arial',10,'bold'),bg='sienna',
                      width=11,fg='bisque',command=change_color)
chocolate.pack(side=LEFT,expand=1)

violet=Radiobutton(frame,text='сиреневый',variable=color, value='violet',
                   font=('Arial',10,'bold'),bg='mediumorchid',
                   width=11,fg='bisque',command=change_color)
violet.pack(side=LEFT,expand=1)

a.mainloop()
