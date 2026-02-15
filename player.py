dico_contraire={"Gauche":"Droite","Droite":"Gauche","Haut":"Bas","Bas":"Haut"}

class Player:
    def __init__(self,x,y,vitesse,vie_max,vie,regen,temps_regen,defense,epee,frame):
        self.x=x
        self.y=y
        self.vitesse=vitesse
        self.u=0
        self.v=0
        self.h=8
        self.w=8
        self.vie_max=vie_max
        self.vie=vie
        self.liste_coeur= [0 for i in range(vie_max)]
        self.barre_de_vie()
        self.regen=regen
        self.temps_regen=temps_regen*30
        self.defense=defense
        self.direction_act="Haut"
        self.dico_direction={"Haut":(0,-1),"Bas":(0,1),"Gauche":(-1,0),"Droite":(1,0)}
        self.dico_anime={"Haut":(0,1),"Bas":(8,1),"Gauche":(16,-1),"Droite":(16,1),"Haut_at":(24,1,0),"Bas_at":(24,1,8),"Gauche_at":(24,-1,16),"Droite_at":(24,1,16)}
        self.attaque=False
        self.frame_anime=frame
        self.frame_invinsibilite=0
        self.frame_regen=frame
        self.frame_attaque=0
        self.val_kb=5
        self.epee=Epee(epee)
        self.est_touche=False

    def attaquer(self):
        self.attaque=True
        self.nouv_anime(self.direction_act+"_at",self.dico_anime[self.direction_act+"_at"][2])
        self.epee.attaque(self.x,self.y,self.direction_act)

    def deplacer(self, direction,frame):
        self.x += self.dico_direction[direction][0]*self.vitesse
        self.y += self.dico_direction[direction][1]*self.vitesse
        if self.direction_act==direction:
            if frame-self.frame_anime>=4:
                self.frame_anime=frame
                self.anime_suivante(4)
        else:
            self.frame_anime=frame
            self.direction_act=direction
            self.nouv_anime(direction,0)

    
    def anime_suivante(self,nb_anime):
        self.v=(self.v+8)%(8*nb_anime)
    
    def nouv_anime(self,anime,v):
        self.v=v
        self.u=self.dico_anime[anime][0]
        self.w=8*self.dico_anime[anime][1]

    def barre_de_vie(self):
        vie = self.vie
        for i in range(self.vie_max):
            if vie>=1:
                self.liste_coeur[i]=1
                vie-=1
            elif 0<vie<1:
                self.liste_coeur[i]=vie
                vie=0
            else:
                self.liste_coeur[i]=0

    def nouvelle_vie(self):
        self.vie_max+=1
        self.liste_coeur.append(0)
    
    def degat(self, degat,frame):
        if frame-self.frame_invinsibilite>8:
            self.vie-=degat/self.defense
            self.frame_invinsibilite=frame
            self.est_touche=True
        """    
        A reprendre si on veut un clignotement ...
        else:
            if round(((frame-self.frame_invinsibilite)*100))%2==0:
                print(round(((frame-self.frame_invinsibilite)*100)))
                self.u=24
            else:
                self.u=self.dico_anime[self.direction_act][0]
        """
    def regenerer(self,frame):
        if frame-self.frame_regen>self.temps_regen:
            if self.vie<self.vie_max:
                nouv=self.vie+self.regen
                self.vie=min(self.vie_max,nouv)
            self.frame_regen=frame

    def kb(self):
        self.x += self.dico_direction[dico_contraire[self.direction_act]][0]*self.val_kb
        self.y += self.dico_direction[dico_contraire[self.direction_act]][1]*self.val_kb
    
    """
    def colision_mur(self):
        self.x += self.dico_direction[dico_contraire[self.direction_act]][0]*self.vitesse
        self.y += self.dico_direction[dico_contraire[self.direction_act]][1]*self.vitesse
    """

    def clignote(self,frame):
        if frame-self.frame_invinsibilite>8:
            self.est_touche=False
        if self.est_touche:
            if 0<=frame-self.frame_invinsibilite<=2 or 4<=frame-self.frame_invinsibilite<=6:
                return True
        return False
    def nouv_epee(self,epee):
        self.epee=Epee(epee)

class Epee():
    def __init__(self,epee):
        self.dico_epee={"Epee_bois":{"degat":1,"cooldown":10,"kb":5,"resource":{"Haut":(0,252,4,3,3,-3),"Bas":(0,252,-4,3,2,6),"Droite":(3,253,3,4,7,3),"Gauche":(3,253,3,-4,-3,3)},"transparant":0,"icon":(0,242)},
                        "Epee_pierre":{"degat":10,"cooldown":9,"kb":5,"resource":{"Haut":(9,250,6,3,3,-5),"Bas":(9,250,-6,3,2,6),"Droite":(12,253,3,6,7,3),"Gauche":(12,253,3,-6,-5,3)},"transparant":0,"icon":(0,232)},
                        "Epee_givre":{"degat":25,"cooldown":5,"kb":3,"resource":{"Haut":(18,248,8,3,3,-7),"Bas":(18,248,-8,3,2,6),"Droite":(21,253,3,8,7,3),"Gauche":(21,253,3,-8,-7,3)},"transparant":0,"icon":(0,222)},
                        "Epee_slime":{"degat":100,"cooldown":8,"kb":10,"resource":{"Haut":(29,244,12,5,2,-10),"Bas":(29,244,-12,5,1,6),"Droite":(34,251,5,12,7,2),"Gauche":(34,251,5,-12,-10,2)},"transparant":0,"icon":(0,212)},
                        "Epee_grosse":{"degat":500,"cooldown":15,"kb":4,"resource":{"Haut":(46,235,21,7,1,-20),"Bas":(46,235,-21,7,0,6),"Droite":(53,249,7,21,7,1),"Gauche":(53,249,7,-21,-20,1)},"transparant":0,"icon":(16,202)},
                        "Epee_slime_rose":{"degat":1000,"cooldown":5,"kb":10,"resource":{"Haut":(78,239,12,5,2,-10),"Bas":(78,239,-12,5,1,6),"Droite":(78,251,5,12,7,2),"Gauche":(78,251,5,-12,-10,2)},"transparant":0,"icon":(0,201)},
                        "Grosse_epee_slime":{"degat":5000,"cooldown":10,"kb":14,"resource":{"Haut":(90,235,21,7,1,-20),"Bas":(90,235,-21,7,0,6),"Droite":(97,249,7,21,7,1),"Gauche":(97,249,7,-21,-20,1)},"transparant":0,"icon":(0,188)},
                        "Epee_magique":{"degat":10000,"cooldown":10,"kb":10,"resource":{"Haut":(118,241,15,4,2,-14),"Bas":(118,241,-15,4,1,6),"Droite":(123,251,4,15,7,2),"Gauche":(123,251,4,-15,-14,2)},"transparant":0,"icon":(0,175)},
                        "Veritable_epee_magique":{"degat":100000,"cooldown":10,"kb":10,"resource":{"Haut":(139,241,15,4,2,-14),"Bas":(139,241,-15,4,1,6),"Droite":(144,251,4,15,7,2),"Gauche":(144,251,4,-15,-14,2)},"transparant":0,"icon":(0,165)},
                        "Epee_mecanique":{"degat":1000000,"cooldown":2,"kb":1,"resource":{"Haut":(161,241,15,6,2,-14),"Bas":(161,241,-15,6,1,6),"Droite":(167,251,4,15,7,2),"Gauche":(167,251,4,-15,-14,2)},"transparant":0,"icon":(0,155)},
                        "Epee_mecasus":{"degat":10000000,"cooldown":2,"kb":1,"resource":{"Haut":(161,225,15,6,2,-14),"Bas":(161,225,-15,6,1,6),"Droite":(167,234,4,15,7,2),"Gauche":(167,234,4,-15,-14,2)},"transparant":0,"icon":(0,145)},
                        "Epee_sus":{"degat":1000000000,"cooldown":10,"kb":100,"resource":{"Haut":(182,243,13,8,0,-12),"Bas":(182,243,-13,8,0,6),"Droite":(190,248,8,13,7,0),"Gauche":(190,248,8,-13,-12,0)},"transparant":0,"icon":(0,135)},
                        "Epee_ultime":{"degat":1000000000000000000,"cooldown":3,"kb":100,"resource":{"Haut":(203,220,35,9,0,-33),"Bas":(203,220,-35,9,0,6),"Droite":(212,246,9,35,7,0),"Gauche":(212,246,9,-35,-34,0)},"transparant":0,"icon":(0,125)}}
        self.degat=self.dico_epee[epee]["degat"]
        self.cooldown=self.dico_epee[epee]["cooldown"]
        self.kb=self.dico_epee[epee]["kb"]
        self.resource=self.dico_epee[epee]["resource"]
        self.transparant=self.dico_epee[epee]["transparant"]
        self.direction="Haut"
        self.type=epee
        self.x=0
        self.y=0
        self.h=0
        self.w=0
        self.icon=self.dico_epee[epee]["icon"]
    
    def attaque(self,x,y,direction):
        self.x=x+self.resource[direction][4]
        self.y=y+self.resource[direction][5]
        self.w=self.resource[direction][3]
        self.h=self.resource[direction][2]
        self.direction=direction
    
    def update(self,x,y,direction):
        self.x=x+self.resource[direction][4]
        self.y=y+self.resource[direction][5]
        self.w=self.resource[direction][3]
        self.h=self.resource[direction][2]
        self.direction=direction

