#importing neccessary modules and the seperately created backend File
import tkinter as tk
from tkinter import messagebox
import soh_registeration
import datetime as dt
from tkinter.font import BOLD

#setting the font styles and formatting
LARGE_FONT= ("TIMES NEW ROMAN", 20, tk.UNDERLINE, BOLD)
SUB_HEADING=("Times New Roman", 14)
TEXT=("Times New Roman",10)



class Scoopsofhappiness(tk.Tk):
   #main frame in which all the other frames will be called one by one
    

    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
         #Welcomepage, PageOne, PageTwo, Menucard, Welcomepage_C, customerdetail, MakeyourChoice -> total frames that are being called, in case you create another frame please include
         #it below
        for F in (Welcomepage, PageOne, PageTwo, Menucard, Welcomepage_C, customerdetail, MakeyourChoice):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Welcomepage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        



   
class Welcomepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.configure(self, bg="#99CCFF")
        
        label = tk.Label(self, text="SCOOPS OF HAPPINESS", font=LARGE_FONT,fg="#fF0000", bg="#99CCFF")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="VENDOR LOG-IN",relief=tk.RAISED,command=lambda: controller.show_frame(PageOne),activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4)
        button.pack(pady=10,padx=10)
        
        button2 = tk.Button(self, text="VENDOR REGISTER",relief=tk.RAISED,command=lambda: controller.show_frame(PageTwo),activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4)
        button2.pack(pady=10,padx=10)



class PageOne(tk.Frame):
   #log-in page
    def check(self):
         #function to authenticate user account
        if(login_un.get().isalpha() and lpd.get().isalnum()):
            c=soh_registeration.search(login_un.get(),lpd.get())
            username.delete(0, tk.END)
            pd.delete(0, tk.END)
            print(login_un.get())
            print(lpd.get())
            if c==1:
                app.show_frame(Menucard)
            else:
                messagebox.showerror("LOG-IN ERROR", "WRONG USERID OR PASSWORD")
        else:
            messagebox.showerror("LOG-IN ERROR", "IMPROPER INPUT")
        
    
    def __init__(self, parent, controller):
        #login frame
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="#99CCFF")
        label = tk.Label(self, text="WELCOME, SET YOUR SHOP", font=LARGE_FONT,fg="#fF0000", bg="#99CCFF")
        label.grid(pady=10,padx=10)
        label2 = tk.Label(self, text="log-in to your shop", font=SUB_HEADING,fg="#663300", bg="#99CCFF")
        label2.grid(pady=10,padx=10)
        global login_un, lpd, username,pd
        label1 = tk.Label(self, text="USERNAME", font=TEXT,fg="#663300", bg="#99CCFF")
        label1.grid(row=3,column=0)
        login_un=tk.StringVar()
        username= tk.Entry(self,textvariable=login_un, bd=5)
        username.grid(row=3,column=1)
        labelp = tk.Label(self, text="PASSWORD", font=TEXT,fg="#663300", bg="#99CCFF")
        labelp.grid(row=4,column=0)
        lpd=tk.StringVar()
        pd= tk.Entry(self,show='*',textvariable=lpd, bd=5)
        pd.grid(row=4,column=1, padx=10, pady=20)
        
        button1 = tk.Button(self, text="LOG-IN",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,command=self.check)
                           
        button1.grid(row=5, column=1)


        button2 = tk.Button(self, text="REGISTER",relief=tk.RAISED,
                             activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=5, column=0)


class PageTwo(tk.Frame):
    #registration page (ice cream vendor) parameters taken as input -> Username, Password, Mobile, Aadhar Card Number, Shop name, Email
    def e_detail(self):
        flag=0
        msg=""
        if(len(u1.get())<8):
            flag=1
            msg=msg+"\n"+"username is below minimum size"
        if(len(p1.get())<8):
            flag=1
            msg=msg+"\n"+"password is below minimum size"
        if(p1.get()!=p2.get()):
            flag=1
            msg=msg+"\n"+"passwords not match"
        if(len(m1.get())!=10):
            flag=1
            msg=msg+"\n"+"wrong mobile no. detected"
        if(len(ad1.get())!=12):
            flag=1
            msg=msg+"\n"+"wrong adhaar entry"
        username.delete(0, tk.END)
        pd.delete(0, tk.END)
        confpd.delete(0, tk.END)
        sn.delete(0, tk.END)
        contact.delete(0, tk.END)
        email.delete(0, tk.END)
        an.delete(0, tk.END)
        if(flag==1):
            messagebox.showerror("WRONG INPUT",msg)    
        else:
            soh_registeration.insert(u1.get(),p1.get(),s1.get(),m1.get(),em1.get(),ad1.get())
            app.show_frame(PageOne)
            
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="#99CCFF")
        label = tk.Label(self, text="REGISTERATION DETAILS", font=LARGE_FONT,fg="#fF0000", bg="#99CCFF")
        label.grid(pady=10,padx=10)
        label1 = tk.Label(self, text="USERNAME", font=TEXT,fg="#663300", bg="#99CCFF")
        label1.grid(row=3,column=0)
        labelp = tk.Label(self, text="PASSWORD", font=TEXT,fg="#663300", bg="#99CCFF")
        labelp.grid(row=4,column=0)
        cpdl = tk.Label(self, text="CONFIRM PASSWORD", font=TEXT,fg="#663300", bg="#99CCFF")
        cpdl.grid(row=5,column=0)
        shopl = tk.Label(self, text="SHOP NAME", font=TEXT,fg="#663300", bg="#99CCFF")
        shopl.grid(row=6,column=0)
        cl= tk.Label(self, text="MOBILE NO.:", font=TEXT,fg="#663300", bg="#99CCFF")
        cl.grid(row=7,column=0)
        el = tk.Label(self, text="E-MAIL ID", font=TEXT,fg="#663300", bg="#99CCFF")
        el.grid(row=8,column=0)
        al = tk.Label(self, text="AADHAR DETAIL", font=TEXT,fg="#663300", bg="#99CCFF")
        al.grid(row=9,column=0)
        
        global u1,p1,p2,s1,m1,em1,ad1,button2,username_reg,pd_reg,confpd,sn,contact,email,an
        u1=tk.StringVar()
        username_reg= tk.Entry(self,textvariable=u1, bd=5)
        username_reg.grid(row=3,column=1)
        
        p1=tk.StringVar()
        pd_reg= tk.Entry(self,show='*',textvariable=p1, bd=5)
        pd_reg.grid(row=4,column=1)
        
        p2=tk.StringVar()
        confpd= tk.Entry(self,show='*',textvariable=p2, bd=5)
        confpd.grid(row=5,column=1)
        
        s1=tk.StringVar()
        sn= tk.Entry(self,textvariable=s1, bd=5)
        sn.grid(row=6,column=1)
       
        m1=tk.StringVar()
        contact= tk.Entry(self,textvariable=m1, bd=5)
        contact.grid(row=7,column=1)
        
        em1=tk.StringVar()
        email= tk.Entry(self,textvariable=em1, bd=5)
        email.grid(row=8,column=1)
        
        ad1=tk.StringVar()
        an= tk.Entry(self,textvariable=ad1, bd=5)
        an.grid(row=9,column=1)
        
        


        button2 = tk.Button(self, text="SUBMIT YOUR DETAILS",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=self.e_detail)
        button2.grid(row=10, column=0, padx=20, pady=20)
        
        button3 = tk.Button(self, text="BACK",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=lambda: controller.show_frame(PageOne))
        button3.grid(row=10, column=1)
        
        
class Menucard(tk.Frame):
    #frame for setting the custom menu card.. here the vendor can add/remove the ice cream flavours based upon the availability
    def get_selected_row(self,event):
        global sel_tuple
        index=list1.curselection()[0]
        sel_tuple=list1.get(index)
        f_name.delete(0,tk.END)
        f_name.insert(tk.END,sel_tuple[0])
        rate_rs.delete(0,tk.END)
        rate_rs.insert(tk.END,sel_tuple[1])
    
    def view_command(self):
        list1.delete(0,tk.END)
        for row in soh_registeration.view():
            list1.insert(tk.END,row)
    
    def delete_command(self):
        soh_registeration.delete(fn.get())
        self.view_command()

    def update_command(self):
        soh_registeration.update(int(rate.get()),sel_tuple[0])
        self.view_command()
   
        
    def flav_entry(self):
        soh_registeration.insert_s(fn.get(),int(rate.get()))
        f_name.delete(0, tk.END)
        rate_rs.delete(0, tk.END)
        self.view_command()

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="#99CCFF")
        label = tk.Label(self, text="customize your menu", font=LARGE_FONT,fg="#fF0000", bg="#99CCFF")
        label.grid(row=0, column=0, pady=10,padx=10)
        label2 = tk.Label(self, text="enter the details of the variety that you offer", font=SUB_HEADING,fg="#663300", bg="#99CCFF")
        label2.grid(row=1, column=0, pady=10, padx=10)
        label3= tk.Label(self, text="NAME OF FLAVOUR", font=TEXT,fg="#663300", bg="#99CCFF")
        label3.grid(row=2,column=0, pady=10, padx=10)
        global fn,rate,f_name,rate_rs,list1
        fn=tk.StringVar()
        f_name= tk.Entry(self,textvariable=fn, bd=5)
        f_name.grid(row=2,column=1)
        label4= tk.Label(self, text="RATE(in rs.)/scoop", font=TEXT,fg="#663300", bg="#99CCFF")
        label4.grid(row=3,column=0, pady=10, padx=10)
        rate=tk.StringVar()
        rate_rs= tk.Entry(self,textvariable=rate, bd=5)
        rate_rs.grid(row=3,column=1)
        list1=tk.Listbox(self, height=6,width=35)
        list1.grid(row=4,column=0,rowspan=6,columnspan=2)
        list1.config(height=10,selectbackground="#cc0066",bg="#990099",fg="white",font=TEXT)
        sb1=tk.Scrollbar(self)
        sb1.grid(row=4,column=2,rowspan=6)
        
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        
        list1.bind('<<ListboxSelect>>',self.get_selected_row)
        
        b3=tk.Button(self,text="Add entry",relief=tk.RAISED, width=12,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,command=self.flav_entry)
        b3.grid(row=4,column=3)
        
        b4=tk.Button(self,text="Update selected",relief=tk.RAISED, width=12,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4, command=self.update_command)
        b4.grid(row=5,column=3)
        
        b5=tk.Button(self,text="Delete selected",relief=tk.RAISED, width=12,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,command=self.delete_command)
        b5.grid(row=6,column=3)
        
        b1=tk.Button(self,text="View all",relief=tk.RAISED, width=12,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4, command=self.view_command)
        b1.grid(row=7,column=3)

        button1 = tk.Button(self, text="SHUTTER UP",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=lambda: controller.show_frame(Welcomepage_C))
        button1.grid(row=12, column=0)
        
class Welcomepage_C(tk.Frame):
    #Welcome Page (Change to Customer Screen or change the vendor)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.configure(self, bg="#99CCFF")
        label = tk.Label(self, text="SCOOPS OF HAPPINESS", font=LARGE_FONT,fg="#fF0000", bg="#99CCFF")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="CUSTOMER ENTER",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=lambda: controller.show_frame(customerdetail))
        button.pack(pady=10,padx=10)

        b2 = tk.Button(self, text="CHANGE VENDOR",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=lambda: controller.show_frame(PageOne))
        b2.pack(pady=10,padx=10)

class customerdetail(tk.Frame):
    #Billing page-1(Enter customer details that are necessary for billing)
    def detailssubmit(self):
        if(cus_mob.get().isalnum() and len(cus_mob.get())==10):
            soh_registeration.insert_c(cus_name.get(),cus_mob.get())
            global billentry1
            billentry1="\nSCOOPS OF HAPPINESS\n\n"+"name of the customer:"+cus_name.get()+"\n"+"mobileno. of the customer"+cus_mob.get()
            name=dt.datetime.now()
            name_s=name.strftime("%Y-%m-%d-%H-%M")+".txt"
            global bill_doc
            bill_doc=open(name_s,"w")
            
            
            cn.delete(0, tk.END)
            ml1.delete(0, tk.END)
            app.show_frame(MakeyourChoice)
        else:
            messagebox.showerror("Wrong Entry", "ENTERED DETAILS SEEM TO BE WRONG PLEASE CHECK IT AGAIN")
        
    
    def __init__(self, parent, controller):
        global cus_name,cus_mob,cn,ml1
        tk.Frame.__init__(self,parent)
        tk.Frame.configure(self, bg="#99CCFF")
        label = tk.Label(self, text="ENTER YOUR DETAILS", font=LARGE_FONT,fg="#fF0000", bg="#99CCFF")
        label.grid(pady=10,padx=10)
        
        cl = tk.Label(self, text="CUSTOMER NAME", font=TEXT,fg="#663300", bg="#99CCFF")
        cl.grid(row=3,column=0)
        cus_name=tk.StringVar()
        cn= tk.Entry(self,textvariable=cus_name, bd=5)
        cn.grid(row=3,column=1)
        ml = tk.Label(self, text="MOBILE NO.", font=TEXT,fg="#663300", bg="#99CCFF")
        ml.grid(row=4,column=0)
        cus_mob=tk.StringVar()
        ml1= tk.Entry(self,textvariable=cus_mob, bd=5)
        ml1.grid(row=4,column=1)

        button = tk.Button(self, text="PROCEED",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=self.detailssubmit)
        button.grid(row=6)
        
        

class MakeyourChoice(tk.Frame):
   #billing page-2 select the flavours that you want to add in your ice-cream and get the bill generated automatically
    total=0
    def get_selected_row(self,event):
        try:
            global selected_tuple
            ind=menu.curselection()[0]
            selected_tuple=menu.get(ind)
            sel_fv.config(state="normal")
            sel_fv.delete(0,tk.END)
            sel_fv.insert(tk.END,selected_tuple[0])
            sel_fv.config(state="readonly")
            rt_sp.config(state='normal')
            rt_sp.delete(0,tk.END)
            rt_sp.insert(tk.END,selected_tuple[1])
            rt_sp.config(state='readonly')
            global s
            s=sfv.get()+" "+r_s.get()
        except:
            pass
        
     
    def get_sel_row(self,event):
        try:
            global s_tuple
            ind=checkingmenu.curselection()[0]
            s_tuple=checkingmenu.get(ind)
            l=s_tuple.split()
            sel_fv.config(state="normal")
            sel_fv.delete(0,tk.END)
            sel_fv.insert(tk.END,l[0])
            sel_fv.config(state="readonly")
            rt_sp.config(state='normal')
            rt_sp.delete(0,tk.END)
            rt_sp.insert(tk.END,l[1])
            rt_sp.config(state='readonly')
            global s
            s=sfv.get()+" "+r_s.get()
        except:
            pass
    
    def add_selected_row(self):
        try:
            checkingmenu.insert(tk.END,s)
            self.total=self.total+int(r_s.get())
            s_t=str(self.total)
            b_total.config(state="normal")
            b_total.delete(0, tk.END)
            b_total.insert(0, s_t)
            b_total.config(state="readonly")
        except:
            pass
    
    def delete(self):
            global s_tuple
            ind=checkingmenu.curselection()
            checkingmenu.delete(ind[0])
            self.total=self.total-int(r_s.get())
            s_t=str(self.total)
            b_total.config(state="normal")
            b_total.delete(0, tk.END)
            b_total.insert(0, s_t)
            b_total.config(state="readonly")
            
    def copy2bill(self):
        s=checkingmenu.get(0, tk.END)
        global billentry2
        billentry2=""
        for items in s:
            stritem1=items.split()
            c_str=stritem1[0]
            c_f_r=stritem1[1]
            billentry2=billentry2+"\nflavour: "+c_str+" price:"+c_f_r+"rs./scoop"
        billentry2=billentry2+"\nTOTAL AMOUNT TO BE PAID:"+str(self.total)+"rs."
        bill_doc.write(billentry1+billentry2)
        app.show_frame(Welcomepage_C)
        bill_doc.close()
        messagebox.showinfo("bill created", "THANK YOU.\n ENJOY YOUR ICE-CREAM")
            
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.configure(self, bg="#99CCFF")
        label = tk.Label(self, text="select your scoops of happiness", font=SUB_HEADING, bg="#99CCFF")
        label.grid(row=0,column=0)
        
        global menu,checkingmenu
        
        label = tk.Label(self, text="MENU", font=SUB_HEADING,fg="#663300", bg="#99CCFF")
        label.grid(row=1,column=0)
        
        label = tk.Label(self, text="YOUR CHOICE", font=SUB_HEADING,fg="#663300", bg="#99CCFF")
        label.grid(row=1,column=3)
        
        
        butadd = tk.Button(self, text="ADD THE SCOOP",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,command=self.add_selected_row
                            )
        butadd.grid(row=2,column=0)
        
        butdel = tk.Button(self, text="DELETE THE SCOOP",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,command=self.delete
                            )
        butdel.grid(row=2,column=3)
        
        global sfv,sel_fv,r_s,rt_sp,b_t,b_total
        sfv=tk.StringVar()
        sel_fv= tk.Entry(self,textvariable=sfv, bd=5)
        sel_fv.grid(row=13,column=1)
        
        r_s=tk.StringVar()
        rt_sp= tk.Entry(self,textvariable=r_s, bd=5)
        rt_sp.grid(row=13,column=3)
        
        b_t=tk.StringVar()
        b_total= tk.Entry(self,textvariable=b_t, bd=5)
        b_total.grid(row=14,column=3)
        
        menu=tk.Listbox(self, height=6,width=35)
        menu.grid(row=3,column=0,rowspan=6,columnspan=2)
        
        for row in soh_registeration.view():
            menu.insert(tk.END,row)
        
        menu.config(height=10,selectbackground="#cc0066",bg="#990099",fg="white",font=TEXT)
        menu.bind('<<ListboxSelect>>',self.get_selected_row)
        sbm=tk.Scrollbar(self)
        sbm.grid(row=3,column=2,rowspan=6)
        
        menu.configure(yscrollcommand=sbm.set)
        sbm.configure(command=menu.yview)
        
        checkingmenu=tk.Listbox(self, height=6,width=35)
        checkingmenu.grid(row=3,column=3,rowspan=6,columnspan=2)
        checkingmenu.bind('<<ListboxSelect>>',self.get_sel_row)
        checkingmenu.config(height=10,selectbackground="#ff3333",bg="#cc6600",fg="white",font=TEXT)
        sbc=tk.Scrollbar(self)
        sbc.grid(row=3,column=6,rowspan=6)
        
        checkingmenu.configure(yscrollcommand=sbm.set)
        sbc.configure(command=checkingmenu.yview)
        
        button1 = tk.Button(self, text="PAY",relief=tk.RAISED,activebackground="#cc0066",bg="#ff66b2",cursor="spraycan",bd=4,
                            command=self.copy2bill)
        button1.grid(row=11,column=0)
        
        cc = tk.Label(self, text="CURRENT CHOICE:", font=TEXT,fg="#663300", bg="#99CCFF")
        cc.grid(row=12,column=0)
        
        selected_flav = tk.Label(self, text="FLAVOUR", font=TEXT,fg="#663300", bg="#99CCFF")
        selected_flav.grid(row=13,column=0)
        
        flav_price = tk.Label(self, text="rate/scoop:", font=TEXT,fg="#663300", bg="#99CCFF")
        flav_price.grid(row=13,column=2)
        
        bill_am = tk.Label(self, text="amount to be charged", font=TEXT,fg="#663300", bg="#99CCFF")
        bill_am.grid(row=14,column=2)
        


app = Scoopsofhappiness()
app.wm_title("SCOOPS OF HAPPINESS")
app.mainloop()
