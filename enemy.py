from random import randint

dico_contraire={"Gauche":"Droite","Droite":"Gauche","Haut":"Bas","Bas":"Haut"}

class enemy:
    def __init__(self,x,y,enemy,frame):
        self.x=x
        self.y=y
        self.dico_enemy={"Slime":{"u":248,"v":0,"h":6,"w":8,"vitesse":5,"type_deplacement":"slime","vie_max":5,"regen":0,"temps_regen":0,"attaque":0.13,"defense":0.8,"transparant":7,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Gel_bleu":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Gel_bleu":6,"None":1}},
                         "Slime_givre":{"u":216,"v":0,"h":6,"w":8,"vitesse":8,"type_deplacement":"slime","vie_max":10,"regen":0,"temps_regen":0,"attaque":0.5,"defense":0.8,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Gel_givre":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Gel_givre":6,"None":1}},
                         "Slime_desert":{"u":208,"v":0,"h":6,"w":8,"vitesse":10,"type_deplacement":"slime","vie_max":50000,"regen":1000,"temps_regen":120,"attaque":1,"defense":0.8,"transparant":7,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Gel_desert":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Gel_desert":6,"None":1}},
                         "Slime_rose":{"u":200,"v":0,"h":6,"w":8,"vitesse":9,"type_deplacement":"slime","vie_max":5000,"regen":50,"temps_regen":250,"attaque":1,"defense":0.8,"transparant":7,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Gel_rose":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Gel_rose":6,"None":1}},
                         "Slime_rouge":{"u":192,"v":0,"h":6,"w":8,"vitesse":12,"type_deplacement":"slime","vie_max":1000000,"regen":10000,"temps_regen":120,"attaque":10,"defense":0.8,"transparant":7,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Gel_rouge":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Gel_rouge":6,"None":1}},
                         "Pierre":{"u":232,"v":0,"h":8,"w":8,"vitesse":0.09,"type_deplacement":"aléatoire","vie_max":6,"regen":0,"temps_regen":0,"attaque":0.25,"defense":2,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":3,"dico_drop":{"Pierre":[i for i in range(40)],"Fer":[i for i in range(80,100)],"None":[i for i in range(40,80)]},"dico_nbmax":{"Pierre":5,"Fer":3,"None":1}},
                         "Pierre_vie":{"u":224,"v":0,"h":8,"w":8,"vitesse":0.09,"type_deplacement":"aléatoire","vie_max":6,"regen":0,"temps_regen":0,"attaque":0.25,"defense":2,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":3,"dico_drop":{"Coeur":[i for i in range(100)]},"dico_nbmax":{"Coeur":1}},
                         "Glacounet":{"u":184,"v":0,"h":8,"w":8,"vitesse":0.9,"type_deplacement":"aléatoire","vie_max":1000,"regen":0,"temps_regen":0,"attaque":2,"defense":0.5,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":10,"dico_drop":{"Glace":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Glace":6,"None":1}},
                         "Cactusus":{"u":176,"v":0,"h":8,"w":8,"vitesse":0.8,"type_deplacement":"aléatoire","vie_max":80000,"regen":1000,"temps_regen":120,"attaque":2,"defense":1,"transparant":8,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Cactus":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Cactus":6,"None":1}},
                         "Cochon":{"u":160,"v":0,"h":8,"w":16,"vitesse":0.3,"type_deplacement":"aléatoire","vie_max":1000000,"regen":1000,"temps_regen":120,"attaque":10,"defense":3,"transparant":8,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":5,"dico_drop":{"Porc":[i for i in range(90)],"None":[i for i in range(90,100)]},"dico_nbmax":{"Porc":1,"None":1}},
                         "Flaque":{"u":152,"v":0,"h":8,"w":8,"vitesse":0.5,"type_deplacement":"aléatoire","vie_max":10000000,"regen":1000000,"temps_regen":150,"attaque":15,"defense":5,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":3,"dico_drop":{"Eau":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Eau":4,"None":1}},
                         "Pyramidus":{"u":144,"v":0,"h":8,"w":8,"vitesse":0.5,"type_deplacement":"aléatoire","vie_max":50000,"regen":100,"temps_regen":150,"attaque":3,"defense":2,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":1,"dico_drop":{"Pyramide":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Pyramide":4,"None":1}},
                         "Pommus":{"u":136,"v":0,"h":8,"w":8,"vitesse":0.5,"type_deplacement":"aléatoire","vie_max":10000000,"regen":100000,"temps_regen":90,"attaque":3,"defense":5,"transparant":7,"dico_anime":{"Dep":(240,1),"Mort":(240,1)},"kb":1,"dico_drop":{"Pomme":[i for i in range(40)],"None":[i for i in range(40,100)]},"dico_nbmax":{"Pomme":5,"None":1}},
                         "Big_slime":{"u":120,"v":0,"h":13,"w":16,"vitesse":30,"type_deplacement":"big_slime","vie_max":250,"regen":0,"temps_regen":0,"attaque":2,"defense":2,"transparant":8,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":0,"dico_drop":{"Epee_slime":[i for i in range(100)]},"dico_nbmax":{"Epee_slime":1}},
                         "Pingu":{"u":104,"v":0,"h":16,"w":16,"vitesse":0.5,"type_deplacement":"aléatoire","vie_max":750,"regen":10,"temps_regen":1000,"attaque":4,"defense":2,"transparant":8,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":0,"dico_drop":{"Epee_grosse":[i for i in range(100)]},"dico_nbmax":{"Epee_grosse":1}},
                         "Chatchat":{"u":88,"v":0,"h":16,"w":16,"vitesse":1,"type_deplacement":"chatchat","vie_max":10000,"regen":100,"temps_regen":1000,"attaque":6,"defense":5,"transparant":8,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":0,"dico_drop":{"Epee_magique":[i for i in range(100)]},"dico_nbmax":{"Epee_magique":1}},
                         "Demon":{"u":72,"v":0,"h":16,"w":16,"vitesse":0.3,"type_deplacement":"aléatoire","vie_max":750000,"regen":10000,"temps_regen":600,"attaque":8,"defense":2,"transparant":7,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":0,"dico_drop":{"Epee_mecanique":[i for i in range(100)]},"dico_nbmax":{"Epee_mecanique":1}},
                         "Amogus":{"u":56,"v":0,"h":16,"w":16,"vitesse":0.1,"type_deplacement":"aléatoire","vie_max":75000000,"regen":100000,"temps_regen":600,"attaque":10,"defense":2,"transparant":4,"dico_anime":{"Dep":(248,1),"Mort":(240,1)},"kb":0,"dico_drop":{"Epee_sus":[i for i in range(100)]},"dico_nbmax":{"Epee_sus":1}}}
        self.vitesse=self.dico_enemy[enemy]["vitesse"]
        self.u=self.dico_enemy[enemy]["u"]
        self.v=self.dico_enemy[enemy]["v"]
        self.h=self.dico_enemy[enemy]["h"]
        self.w=self.dico_enemy[enemy]["w"]
        self.vie_max=self.dico_enemy[enemy]["vie_max"]
        self.vie=self.dico_enemy[enemy]["vie_max"]
        self.regen=self.dico_enemy[enemy]["regen"]
        self.temps_regen=self.dico_enemy[enemy]["temps_regen"]*30
        self.defense=self.dico_enemy[enemy]["defense"]
        self.attaque=self.dico_enemy[enemy]["attaque"]
        self.type_deplacement=self.dico_enemy[enemy]["type_deplacement"]
        self.direction_act="Haut"
        self.dico_direction={"Haut":(0,-1),"Bas":(0,1),"Gauche":(-1,0),"Droite":(1,0)};
        self.dico_anime=self.dico_enemy[enemy]["dico_anime"]
        self.transparant=self.dico_enemy[enemy]["transparant"]
        self.frame_anime=frame
        self.frame_invinsibilite=0
        self.frame_regen=frame
        self.val_kb=self.dico_enemy[enemy]["kb"]
        self.est_touche=False
        self.est_mort=False
        self.frame_mort=0
        self.frame_dir=frame
        self.dico_drop=self.dico_enemy[enemy]["dico_drop"]
        self.dico_nbmax=self.dico_enemy[enemy]["dico_nbmax"]

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
            self.nouv_anime(direction)

    def deplacer_slime(self, direction,frame):
        if frame-self.frame_anime>=10:
            if self.v==0:
                self.x += self.dico_direction[direction][0]*self.vitesse
                self.y += self.dico_direction[direction][1]*self.vitesse
            self.frame_anime=frame
            self.anime_suivante(4)
    
    def deplacer_big_slime(self, direction,frame):
        if frame-self.frame_anime>=60:
            if self.v==39:
                self.x += self.dico_direction[direction][0]*self.vitesse
                self.y += self.dico_direction[direction][1]*self.vitesse
            self.frame_anime=frame
            self.anime_suivante(4)
    
    def deplacer_aleatoire(self,frame,tps_anime):
        if frame-self.frame_dir>=30:
            dico={0:"Haut",1:"Bas",2:"Gauche",3:"Droite"}
            direction=dico[randint(0,3)]
            self.direction_act=direction
            self.frame_dir=frame
        else:
            direction=self.direction_act 
        if self.x+abs(self.w)>=160 or self.x<=0 or self.y+abs(self.h)>=90 or self.y<=12:  
            self.direction_act=dico_contraire[direction]
            direction=self.direction_act
        self.x += self.dico_direction[direction][0]*self.vitesse
        self.y += self.dico_direction[direction][1]*self.vitesse
        if frame-self.frame_anime>=tps_anime:
            self.frame_anime=frame
            self.anime_suivante(4)

    def deplacer_chatchat(self):
        if self.direction_act=="Haut":
            self.direction_act=="Gauche"
            direction="Gauche"
        else:
            direction=self.direction_act 
        if self.x+abs(self.w)>=160 or self.x<=0:  
            self.direction_act=dico_contraire[direction]
            direction=self.direction_act
        self.x += self.dico_direction[direction][0]*self.vitesse
        self.y += self.dico_direction[direction][1]*self.vitesse


    def action(self,frame):
        if self.type_deplacement=="slime":
            dico={0:"Haut",1:"Bas",2:"Gauche",3:"Droite"}
            direction=randint(0,3)
            self.deplacer_slime(dico[direction],frame)
        if self.type_deplacement=="big_slime":
            dico={0:"Haut",1:"Bas",2:"Gauche",3:"Droite"}
            direction=randint(0,3)
            self.deplacer_big_slime(dico[direction],frame)
        if self.type_deplacement=="aléatoire":
            self.deplacer_aleatoire(frame,10)
        if self.type_deplacement=="chatchat":
            self.deplacer_chatchat()
        self.regenerer(frame)

        
    def anime_suivante(self,nb_anime):
        self.v=(self.v+self.h)%(self.h*nb_anime)
    
    def nouv_anime(self,anime):
        self.v=0
        self.u=self.dico_anime[anime][0]
        self.w=abs(self.w)*self.dico_anime[anime][1]
    
    def degat(self, degat,frame):
        if frame-self.frame_invinsibilite>8:
            self.est_touche=True
            self.vie-=degat/self.defense
            self.frame_invinsibilite=frame
            return degat/self.defense
        return 0
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

    def kb(self,direction):
        self.x += self.dico_direction[direction][0]*self.val_kb
        self.y += self.dico_direction[direction][1]*self.val_kb

    def clignote(self,frame):
        if frame-self.frame_invinsibilite>8:
            self.est_touche=False
        if self.est_touche:
            if 0<=frame-self.frame_invinsibilite<=2 or 4<=frame-self.frame_invinsibilite<=6:
                return True
        return False
    
    def mort(self,frame):
        self.est_mort=True
        if self.w>8:
            self.x=self.x+self.w//2
        if self.h>8:
            self.y=self.y+self.h//2
        self.w=8
        self.h=8
        self.nouv_anime("Mort")
        self.frame_mort=frame
        return self.drop()

    def drop(self):
        item=randint(0,99)
        for k,ele in self.dico_drop.items():
            if item in ele:
                item=k
                break
        nbitem=randint(1,self.dico_nbmax[item])
        return (item,nbitem)


    """
    def colision_mur(self):
        self.x += self.dico_direction[dico_contraire[self.direction_act]][0]*self.vitesse
        self.y += self.dico_direction[dico_contraire[self.direction_act]][1]*self.vitesse
    """