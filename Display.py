import tkinter as tk
from tkinter import ttk
from tkinter import *
import Functions as f
from tkinter import messagebox

class Affiche():
    
    window = tk.Tk()
    textbox1 = ttk
    textbox2 = ttk
    textbox3 = ttk
    textbox4 = ttk
    cl = ttk
    networkAdressV = ttk
    
    def frameElement(self):

        self.label1 = ttk.Label(self.window, text='Adresse', font=("Arial Bold", 10))
        self.label1.place(x=7, y=10)

        self.textbox1 = ttk.Entry(width="40")
        self.textbox1.place(x=90, y=10)

        self.lbl2 = ttk.Label(self.window, text='IP Version', font=("Arial Bold", 10))
        self.lbl2.place(x=7, y=60)

        self.textbox2 = ttk.Combobox(self.window, state="readonly",
                               values=["IPv4", "IPv6"], width=10)
        self.textbox2.place(x=90, y=60)

        self.lbl4 = ttk.Label(self.window, text='Prefixe', font=("Arial Bold", 10))
        self.lbl4.place(x=7, y=110)

        self.textbox4 = ttk.Entry(width="10")
        self.textbox4.place(x=60, y=110)

        front = ttk.Style()
        front.configure("BW.TLabel", font =
               ('calibri', 11, 'bold'),
                    borderwidth = '4', background="green", foreground="white")

        self.b1 = ttk.Button(self.window,text='VALIDER',
                             command=self.click, style='BW.TLabel')
        self.b1.place(x=7, y=150)
                
    def click(self): 
        
        if self.textbox1.get() == "":
            messagebox.showwarning("", "Entrer l'IP")
            return None
        
        cl = ttk
        masque = ttk
        adresseReseau = ttk
        adresseDiffusion = ttk
        prermierOrdre = ttk
        dernierOrdre = ttk
        hote = ttk
        nombreAdresse = ttk

        classeV = ttk
        masqueV = ttk
        networkAdressV = ttk
        adresseDiffusionV = ttk
        prermierOrdreV = ttk
        dernierOrdreV = ttk
        hoteV = ttk
        nombreAdresseV = ttk
        
        ip = ttk
        ipV = ttk
                
        if self.textbox4.get() == "" and self.textbox2.get() == "IPv4": 
            
            try:
                f.checkIpv4Format(self.textbox1.get(), self)
                f.getNetworkClass(self.textbox1.get())
            except Exception as e:
                messagebox.showwarning("", str(e))
                return None   

            frameIpv4 = tk.Tk()
            frameIpv4.geometry('500x500')
            self.cl = ttk.Label(frameIpv4, text='Classe', font=("Arial Bold", 8))
            self.cl.place(x=7, y=10)
            self.classeV = ttk.Label(frameIpv4, text=f.getNetworkClass(self.textbox1.get()), font=("Arial Bold", 8))
            self.classeV.place(x=120, y=10)
            self.masque = ttk.Label(frameIpv4, text='Masque', font=("Arial Bold", 8))
            self.masque.place(x=7, y=30)
            self.masqueV = ttk.Label(frameIpv4, text=f.getMask(self.textbox1.get()), font=("Arial Bold", 8))
            self.masqueV.place(x=120, y=30)
            self.adresseReseau = ttk.Label(frameIpv4, text='Réseau', font=("Arial Bold", 8))
            self.adresseReseau.place(x=7, y=50)
            self.networkAdressV = ttk.Label(frameIpv4, text=f.getNetworkAddress(self.textbox1.get(), f.getMask(self.textbox1.get())), font=("Arial Bold", 8))
            self.networkAdressV.place(x=120, y=50)
            self.adresseBroadcast = ttk.Label(frameIpv4, text='Diffusion', font=("Arial Bold", 8))
            self.adresseBroadcast.place(x=7, y=70)
            self.adresseBroadcastV = ttk.Label(frameIpv4, text=f.getBroadcatAddress(self.textbox1.get(), f.getMask(self.textbox1.get())), font=("Arial Bold", 8))
            self.adresseBroadcastV.place(x=120, y=70)
            self.premierOrdre = ttk.Label(frameIpv4, text='1er valide', font=("Arial Bold", 8))
            self.premierOrdre.place(x=7, y=90)
            self.premierOrdreV = ttk.Label(frameIpv4, text=f.getFirstOrder(self.textbox1.get(), f.getMask(self.textbox1.get())), font=("Arial Bold", 8))
            self.premierOrdreV.place(x=120, y=90)
            self.dernierOrdre = ttk.Label(frameIpv4, text='Dernier valide', font=("Arial Bold", 8))
            self.dernierOrdre.place(x=7, y=110)
            self.dernierOrdreV = ttk.Label(frameIpv4, text=f.getLastOrder(self.textbox1.get(), f.getMask(self.textbox1.get())), font=("Arial Bold", 8))
            self.dernierOrdreV.place(x=120, y=110)
            self.hote = ttk.Label(frameIpv4, text='Hôte')
            self.hote.place(x=7, y=130)
            self.hoteV = ttk.Label(frameIpv4, text=f.hostBit(self.textbox1.get()), font=("Arial Bold", 8))
            self.hoteV.place(x=120, y=130)
            self.nombreAdresse = ttk.Label(frameIpv4, text='Nombre adresse', font=("Arial Bold", 8))
            self.nombreAdresse.place(x=7, y=150)
            self.nombreAdresseV = ttk.Label(frameIpv4, text=f.getAddressNumber(self.textbox1.get()), font=("Arial Bold", 8))
            self.nombreAdresseV.place(x=120, y=150)                       
            frameIpv4.configure(bg='silver')   
            frameIpv4.mainloop() 
        
        if self.textbox2.get() == "":
            messagebox.showwarning("", "Insérer la version IP")

        if self.textbox2.get() == "IPv4": 

            try:
                f.checkIpv4Format(self.textbox1.get(), self)
                f.checkPrefix(self.textbox4.get(), "IPv4")
            except Exception as e:
                messagebox.showwarning("", str(e))
                return None   

            frameIpv4 = tk.Tk()
            frameIpv4.geometry('450x180')
            
            self.masque = ttk.Label(frameIpv4, text='Masque', font=("Arial Bold", 8))
            self.masque.place(x=7, y=30)
            self.masqueV = ttk.Label(frameIpv4, text=f.getMaskSpecial(int(self.textbox4.get())), font=("Arial Bold", 8))
            self.masqueV.place(x=120, y=30)
            self.adresseReseau = ttk.Label(frameIpv4, text='Réseau', font=("Arial Bold", 8))
            self.adresseReseau.place(x=7, y=50)
            self.networkAdressV = ttk.Label(frameIpv4, text=f.getNetworkAddress(self.textbox1.get(), f.getMaskSpecial(int(self.textbox4.get()))), font=("Arial Bold", 8))
            self.networkAdressV.place(x=120, y=50)
            self.adresseBroadcast = ttk.Label(frameIpv4, text='Diffusion', font=("Arial Bold", 8))
            self.adresseBroadcast.place(x=7, y=70)
            self.adresseBroadcastV = ttk.Label(frameIpv4, text=f.getBroadcatAddress(self.textbox1.get(), f.getMaskSpecial(int(self.textbox4.get()))), font=("Arial Bold", 8))
            self.adresseBroadcastV.place(x=120, y=70)
            self.premierOrdre = ttk.Label(frameIpv4, text='1er valide', font=("Arial Bold", 8))
            self.premierOrdre.place(x=7, y=90)
            self.premierOrdreV = ttk.Label(frameIpv4, text=f.getFirstOrder(self.textbox1.get(), f.getMaskSpecial(int(self.textbox4.get()))), font=("Arial Bold", 8))
            self.premierOrdreV.place(x=120, y=90)
            self.dernierOrdre = ttk.Label(frameIpv4, text='Dernier valide', font=("Arial Bold", 8))
            self.dernierOrdre.place(x=7, y=110)
            self.dernierOrdreV = ttk.Label(frameIpv4, text=f.getLastOrder(self.textbox1.get(), f.getMaskSpecial(int(self.textbox4.get()))), font=("Arial Bold", 8))
            self.dernierOrdreV.place(x=120, y=110)
            self.hote = ttk.Label(frameIpv4, text='Hôte', font=("Arial Bold", 8))
            self.hote.place(x=7, y=130)
            self.hoteV = ttk.Label(frameIpv4, text=f.hostBitSpecial(int(self.textbox4.get())), font=("Arial Bold", 8))
            self.hoteV.place(x=120, y=130)
            self.nombreAdresse = ttk.Label(frameIpv4, text='Nombre adresse', font=("Arial Bold", 8))
            self.nombreAdresse.place(x=7, y=150)
            self.nombreAdresseV = ttk.Label(frameIpv4, text=f.getAddressNumberSpecial(int(self.textbox4.get())), font=("Arial Bold", 8))
            self.nombreAdresseV.place(x=120, y=150)    
            frameIpv4.configure(bg='silver')                 
            frameIpv4.mainloop()             
            
        if self.textbox2.get() == "IPv6": 
            try:
                f.checkIpv6Format(self.textbox1.get())
                f.checkPrefix(self.textbox4.get(), "IPv6")
            except Exception as e:
                messagebox.showwarning("", str(e))
                return None   

            frameIpv6 = tk.Tk()
            frameIpv6.geometry('450x100')
            self.ip = ttk.Label(frameIpv6, text='IP', font=("Arial Bold", 8))
            self.ip.place(x=7, y=30)
            self.ipV = ttk.Label(frameIpv6, text=f.compressedIpv6(self.textbox1.get()), font=("Arial Bold", 8))
            self.ipV.place(x=120, y=30)
            self.adresseReseau = ttk.Label(frameIpv6, text='Adresse réseau', font=("Arial Bold", 8))
            self.adresseReseau.place(x=7, y=50)
            self.networkAdressV = ttk.Label(frameIpv6, text=f.networkAddress(self.textbox1.get(), int(self.textbox4.get())), font=("Arial Bold", 8))
            self.networkAdressV.place(x=120, y=50)
            frameIpv6.configure(bg='silver')          
            frameIpv6.mainloop()                 

    def frame(self):
        
        self.window.geometry('540x250')
        self.window.configure(bg='silver')
        self.frameElement()
        self.window.mainloop()        
        
class Main():
    def main():
        Affiche().frame()
    if __name__ == '__main__':
        main()
        