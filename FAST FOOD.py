from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("Pajak")

Tops = Frame (root, width= 1350, height=100, bd=12, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="\t    KEDE SAYA\t\t\t")
lblTitle.grid(row =0, column=0)

BottomMainFrame = Frame (root, width= 1350 , height=650, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)
#===============================================
f1 = Frame (BottomMainFrame, width = 450 , height=650, bd= 12, relief="raise")
f1.pack(side=LEFT)
f2 = Frame (BottomMainFrame, width = 450 , height=650, bd= 12, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame (f2,width = 450 , height=350, bd=4, relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM = Frame (f2,width = 450 , height=300, bd=4, relief="raise")
f2BOTTOM.pack(side=BOTTOM)
#==================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)

#==============Variabel=============
varTuna =StringVar()
varSalmon =StringVar()
varTeri =StringVar()
varKakap =StringVar()
varTongkol =StringVar()
varBendeng =StringVar()
varSarden =StringVar()
varNila =StringVar()
varFillet =StringVar()
varAntar =StringVar()

varHarga=StringVar()
varPajak=StringVar() 
varPaymen=StringVar()
varTotal =StringVar()
varKembali=StringVar()
var11=StringVar()
#===============
varTuna.set("0")
varSalmon.set("0")
varTeri.set("0")
varKakap.set("0")
varTongkol.set("0")
varBendeng.set("0")
varSarden.set("0")
varNila.set("0")
varFillet.set("0")
varAntar.set("0")

varHarga.set("0")
varPajak.set("0")
varPaymen.set("")
varTotal.set("0")
varKembali.set("0")
var11.set("0")

#===================Rumus=================

def iExit():
    qExit= messagebox.askyesno("Gitu Kau Yaa","Yakin Mau Keluar?")
    if (qExit):
       root.destroy()
       return

def Reset():
    varTuna.set("0")
    varSalmon.set("0")
    varTeri.set("0")
    varKakap.set("0")
    varTongkol.set("0")
    varBendeng.set("0")
    varSarden.set("0")
    varNila.set("0")
    varFillet.set("0")
    varAntar.set("0")

    varHarga.set("0")
    varPajak.set("0")
    varTotal.set("0")
    varPaymen.set("")
    varKembali.set("0")
    #=====
    txtTuna.configure(state =DISABLED)
    txtSalmon.configure(state =DISABLED)
    txtKakap.configure(state =DISABLED)
    txtTongkol.configure(state =DISABLED)
    txtBendeng.configure(state =DISABLED)
    txtSarden.configure(state =DISABLED)
    txtNila.configure(state =DISABLED)
    txtFillet.configure(state =DISABLED)
    txtAntar.configure(state =DISABLED)

    txtHarga.configure(state =DISABLED)
    txtPajak.configure(state =DISABLED)
    txtPaymen.configure(state =NORMAL)
    txtTotal.configure(state =DISABLED)
    txtKembali.configure(state =DISABLED)

def chkTuna():
    if (var1.get() == 1):
        txtTuna.configure(state = NORMAL)
        varTuna.set("")
    elif(var1.get() == 0):
        txtTuna.configure(state =DISABLED)
        varTuna.set("0")

def chkSalmon():
    if (var2.get() == 1):
        txtSalmon.configure(state = NORMAL)
        varSalmon.set("")
    elif(var2.get() == 0):
        txtSalmon.configure(state =DISABLED)
        varSalmon.set("0")

def chkTeri():
    if (var3.get() == 1):
        txtTeri.configure(state = NORMAL)
        varTeri.set("")
    elif(var3.get() == 0):
        txtTeri.configure(state =DISABLED)
        varTeri.set("0")

def chkKakap():
    if (var4.get() == 1):
        txtKakap.configure(state = NORMAL)
        varKakap.set("")
    elif(var4.get() == 0):
        txtKakap.configure(state =DISABLED)
        varKakap.set("0")

def chkTongkol():
    if (var5.get() == 1):
        txtTongkol.configure(state = NORMAL)
        varTongkol.set("")
    elif(var5.get() == 0):
        txtTongkol.configure(state =DISABLED)
        varTongkol.set("0")        
       
       
def chkBendeng():
    if (var6.get() == 1):
        txtBendeng.configure(state = NORMAL)
        varBendeng.set("")
    elif(var6.get() == 0):
        txtBendeng.configure(state =DISABLED)
        varBendeng.set("0")


def chkSarden():
    if (var7.get() == 1):
        txtSarden.configure(state = NORMAL)
        varSarden.set("")
    elif(var7.get() == 0):
        txtSarden.configure(state =DISABLED)
        varSarden.set("0")


def chkNila():
    if (var8.get() == 1):
        txtNila.configure(state = NORMAL)
        varNila.set("")
    elif(var8.get() == 0):
        txtNila.configure(state =DISABLED)
        varNila.set("0")

def chkFillet():
    if (var9.get() == 1):
        txtFillet.configure(state = NORMAL)
        varFillet.set("")
    elif(var9.get() == 0):
        txtFillet.configure(state =DISABLED)
        varFillet.set("0")        

def chkAntar():
    if (var10.get() == 1):
        txtAntar.configure(state = NORMAL)
        varAntar.set("")
    elif(var10.get() == 0):
        txtAntar.configure(state =DISABLED)
        varAntar.set("0")

def harga ():
    meal1 = float(varTuna.get())
    meal2 = float(varSalmon.get())
    meal3 = float(varTeri.get())
    meal4 = float(varKakap.get())
    meal5 = float(varTongkol.get())
    meal6 = float(varBendeng.get())
    meal7 = float(varSarden.get())
    meal8 = float(varNila.get())
    meal9 = float(varFillet.get())
    meal10 = float(varAntar.get())

    itotal=((meal1 * 12000) + (meal2 * 50000) + (meal3*8000)+(meal4*30000)+
            (meal5*20000)+(meal6*40000)+(meal7*20000)+(meal8*15000)+(meal9*8000)+
            (meal10*5000))
    if (var11.get() == "Tunai"):
        iChange = float(varPaymen.get())
        iCost = (itotal)
        iTax=(iCost *0)
        iTaxq="Rp",str('%.2f'%(iTax))
        varPajak.set(iTaxq)

        iCostq=str('%.2f'%(iCost))
        varHarga.set(iCost)
        iTotalq=str('%.2f'%((iCost + iTax)))
        varTotal.set(iTotalq)
        cChange = (iChange - (iCost + iTax))
        cChangeq =str('%.2f'%(cChange))
        varKembali.set(cChangeq)

    elif(var11.get() == "Kartu Kredit"):
        iChange = float(varPaymen.get())
        iCost = (itotal)
        iTax=(iCost * 0.1)
        iTaxq=('%.2f'%(iTax))
        varPajak.set(iTaxq)
        
        iCostq=str('%.2f'%(iCost))
        varHarga.set(iCost)
        iTotalq=str('%.2f'%((iCost + iTax)))
        varTotal.set(iTotalq)
        cChange = (iChange - (iCost + iTax))
        cChangeq =str('%.2f'%(cChange))
        varKembali.set(cChangeq)



        
#==============Kotak Pertama=============

lblMeal = Label (f1, font=('arial', 18, 'bold'), text="IKAN SEGAR / Kg\n\n")
lblMeal.grid(row =0, column=0)


Tuna =Checkbutton(f1, text="Tuna\t\tRp.12.000\t", variable=var1, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkTuna).grid(row=1, column=0, sticky=W)
txtTuna = Entry (f1,font=('arial',18,'bold'), textvariable =varTuna, width =6, justify='right', state=DISABLED)
txtTuna.grid(row=1, column=1)

Salmon =Checkbutton(f1, text="Salmon\t\tRp.50.000\t", variable=var2, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkSalmon).grid(row=2, column=0, sticky=W)
txtSalmon = Entry (f1,font=('arial',18,'bold'), textvariable =varSalmon, width =6, justify='right', state=DISABLED)
txtSalmon.grid(row=2, column=1)

Teri =Checkbutton(f1, text="Teri\t\tRp.8.000\t", variable=var3, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkTeri).grid(row=3, column=0, sticky=W)
txtTeri = Entry (f1,font=('arial',18,'bold'), textvariable =varTeri, width =6,justify='right', state=DISABLED)
txtTeri.grid(row=3, column=1)

Kakap =Checkbutton(f1, text="Kakap\t\tRp.30.000\t", variable=var4, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkKakap).grid(row=4, column=0, sticky=W)
txtKakap = Entry (f1,font=('arial',18,'bold'), textvariable =varKakap, width =6, justify='right', state=DISABLED)
txtKakap.grid(row=4, column=1)

Tongkol =Checkbutton(f1, text="Tongkol\t\tRp.20.000\t", variable=var5, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkTongkol).grid(row=5, column=0, sticky=W)
txtTongkol = Entry (f1,font=('arial',18,'bold'), textvariable =varTongkol, width =6, justify='right', state=DISABLED)
txtTongkol.grid(row=5, column=1)

Bendeng =Checkbutton(f1, text="Bendeng\t\tRp.40.000\t", variable=var6, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkBendeng).grid(row=6, column=0, sticky=W)
txtBendeng = Entry (f1,font=('arial',18,'bold'), textvariable =varBendeng, width =6, justify='right', state=DISABLED)
txtBendeng.grid(row=6, column=1)

Sarden =Checkbutton(f1, text="Sarden\t\tRp.20.000\t", variable=var7, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkSarden).grid(row=7, column=0, sticky=W)
txtSarden = Entry (f1,font=('arial',18,'bold'), textvariable =varSarden, width =6, justify='right', state=DISABLED)
txtSarden.grid(row=7, column=1)

Nila =Checkbutton(f1, text="Nila\t\tRp.15.000\t", variable=var8, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkNila).grid(row=8, column=0, sticky=W)
txtNila = Entry (f1,font=('arial',18,'bold'), textvariable =varNila, width =6, justify='right', state=DISABLED)
txtNila.grid(row=8, column=1)

lblspace = Label (f1, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row =9, column=0)

#============Kotak 2 atas=========
lbl = Label (f2TOP, font=('arial', 18, 'bold'), text="Permintaan Lebih\t\t\t\t\t\n\n")
lbl.grid(row =0, column=0)

Fillet =Checkbutton(f2TOP, text="Fillet\t\tRp.8.000\t", variable=var9, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkFillet).grid(row=1, column=0, sticky=W)
txtFillet = Entry (f2TOP,font=('arial',18,'bold'), textvariable =varFillet, width =6, justify='right', state=DISABLED)
txtFillet.grid(row=1, column=1)

Antar =Checkbutton(f2TOP, text="Antar\t\tRp.5.000/Km\t", variable=var10, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command= chkAntar).grid(row=2, column=0, sticky=W)
txtAntar = Entry (f2TOP,font=('arial',18,'bold'), textvariable =varAntar, width =6, justify='right', state=DISABLED)
txtAntar.grid(row=2, column=1)

lbl = Label (f2TOP, text="\n\n")
lbl.grid(row =3, column=0)

#============Kotak 2 Bawah=========
lblMeal = Label (f2BOTTOM, font=('arial', 18, 'bold'), text="Cara Bayar\t\t\t\n\n")
lblMeal.grid(row =0, column=0)

cmbCaraBayar = ttk.Combobox (f2BOTTOM , textvariable = var11, state='readonly', font=('arial',10, 'bold'), width= 20)
cmbCaraBayar['value']=('Tunai','Kartu Kredit')
cmbCaraBayar.current(0)
cmbCaraBayar.grid(row=1,column=0)

txtPaymen = Entry(f2BOTTOM,font=('aria',18,'bold'),textvariable =varPaymen, width =8, justify='left')
txtPaymen.grid(row =2, column =0)

lblHarga = Label (f2BOTTOM , font=('arial', 14, 'bold'), text="Harga", bd=10, anchor='w')
lblHarga.grid(row=0,column=1)
txtHarga = Entry(f2BOTTOM,font=('aria',18,'bold'),textvariable =varHarga, width =8, justify='left', state =DISABLED)
txtHarga.grid(row =0, column =2)

lblPajak = Label (f2BOTTOM , font=('arial', 14, 'bold'), text="Pajak", bd=10, anchor='w')
lblPajak.grid(row=1,column=1)
txtPajak = Entry(f2BOTTOM,font=('aria',18,'bold'),textvariable =varPajak, width =8,justify='left', state =DISABLED)
txtPajak.grid(row =1, column =2)

lblTotal = Label (f2BOTTOM , font=('arial', 14, 'bold'), text="Total", bd=10, anchor='w')
lblTotal.grid(row=2,column=1)
txtTotal = Entry(f2BOTTOM,font=('aria',18,'bold'),textvariable =varTotal, width =8, justify='left', state =DISABLED)
txtTotal.grid(row =2, column =2)

lblKembali = Label (f2BOTTOM , font=('arial', 14, 'bold'), text="Kembali", bd=10,width =6, anchor='w')
lblKembali.grid(row=3,column=1)
txtKembali = Entry (f2BOTTOM,font=('arial', 18, 'bold'), textvariable =varKembali, width =8, justify='left', state =DISABLED)
txtKembali.grid(row=3,column=2)

#======Tombol=============

btnTotal = Button (f2BOTTOM,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'),width=5,
                   text="Total", command=harga).grid(row=4, column=0)

btnReset = Button (f2BOTTOM,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'),width=5,
                   text="Reset", command =Reset).grid(row=4, column=1)

btnExit = Button (f2BOTTOM,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'),width=5,
                   text="Exit",command=lambda: iExit()).grid(row=4, column=2)









root.mainloop()
