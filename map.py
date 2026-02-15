class map:
    def __init__(self,environement):
        self.dico_environement={"plaine":{"image":0,0:"desert",1:"neige"},"desert":{"image":1,2:"plaine",3:"volcan"},"neige":{"image":2,3:"plaine"},"volcan":{"image":3,1:"desert"}}
        self.u=0
        self.v=0 
        self.image=self.dico_environement[environement]["image"]
        self.w=160
        self.h=90
        self.x=0
        self.y=12
        self.triger=[Triger((0,self.y),(160,1)),Triger((0,self.y),(1,90)),Triger((0,89),(160,90)),Triger((159,self.y),(160,90))]
        self.environement=environement

    def changer_environement(self,trig):
        if trig in self.dico_environement[self.environement].keys():
            self.environement=self.dico_environement[self.environement][trig]
            self.image=self.dico_environement[self.environement]["image"]
            return True
        return False

class Triger():
    def __init__(self,coordonne,taille):
        self.x=coordonne[0]
        self.y=coordonne[1]
        self.w=taille[0]
        self.h=taille[1]