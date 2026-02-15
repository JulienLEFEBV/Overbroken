import pyxel
from player import Player
from map import map
from enemy import enemy
from item import item
from random import randint

dico_round={"round1":{"plaine":{"Slime":[i for i in range(50)],"Pierre":[i for i in range(50,90)],"Pierre_vie":[i for i in range(90,100)]},"desert":{"Slime_desert":[i for i in range(80)],"Cactusus":[i for i in range(80,100)]},"neige":{"Slime_givre":[i for i in range(80)],"Glacounet":[i for i in range(80,100)]},"volcan":{"Slime_rouge":[i for i in range(80)],"Cochon":[i for i in range(80,100)]},"apparition":50},
            "round2":{"plaine":{"Slime":[i for i in range(25)],"Slime_rose":[i for i in range(25,50)],"Pierre":[i for i in range(50,90)],"Pierre_vie":[i for i in range(90,100)]},"desert":{"Slime_desert":[i for i in range(80)],"Cactusus":[i for i in range(80,100)]},"neige":{"Slime_givre":[i for i in range(80)],"Glacounet":[i for i in range(80,100)]},"volcan":{"Slime_rouge":[i for i in range(80)],"Cochon":[i for i in range(80,100)]},"apparition":46},
            "round3":{"plaine":{"Slime":[i for i in range(25)],"Slime_rose":[i for i in range(25,50)],"Pierre":[i for i in range(50,90)],"Pierre_vie":[i for i in range(90,100)]},"desert":{"Slime_desert":[i for i in range(80)],"Cactusus":[i for i in range(80,100)]},"neige":{"Slime_givre":[i for i in range(40)],"Flaque":[i for i in range(40,80)],"Glacounet":[i for i in range(80,100)]},"volcan":{"Slime_rouge":[i for i in range(80)],"Cochon":[i for i in range(80,100)]},"apparition":44},
            "round4":{"plaine":{"Slime":[i for i in range(25)],"Slime_rose":[i for i in range(25,50)],"Pierre":[i for i in range(50,90)],"Pierre_vie":[i for i in range(90,100)]},"desert":{"Slime_desert":[i for i in range(40)],"Pyramidus":[i for i in range(40,80)],"Cactusus":[i for i in range(80,100)]},"neige":{"Slime_givre":[i for i in range(40)],"Flaque":[i for i in range(40,80)],"Glacounet":[i for i in range(80,100)]},"volcan":{"Slime_rouge":[i for i in range(80)],"Cochon":[i for i in range(80,100)]},"apparition":42},
            "round5":{"plaine":{"Slime":[i for i in range(25)],"Slime_rose":[i for i in range(25,50)],"Pierre":[i for i in range(50,90)],"Pierre_vie":[i for i in range(90,100)]},"desert":{"Slime_desert":[i for i in range(40)],"Pyramidus":[i for i in range(40,80)],"Cactusus":[i for i in range(80,100)]},"neige":{"Slime_givre":[i for i in range(40)],"Flaque":[i for i in range(40,80)],"Glacounet":[i for i in range(80,100)]},"volcan":{"Slime_rouge":[i for i in range(40)],"Pommus":[i for i in range(40,80)],"Cochon":[i for i in range(80,100)]},"apparition":40},
            "round6":{"plaine":{"Slime":[i for i in range(25)],"Slime_rose":[i for i in range(25,50)],"Pierre":[i for i in range(50,90)],"Pierre_vie":[i for i in range(90,100)]},"desert":{"Slime_desert":[i for i in range(40)],"Pyramidus":[i for i in range(40,80)],"Cactusus":[i for i in range(80,100)]},"neige":{"Slime_givre":[i for i in range(40)],"Flaque":[i for i in range(40,80)],"Glacounet":[i for i in range(80,100)]},"volcan":{"Slime_rouge":[i for i in range(40)],"Pommus":[i for i in range(40,80)],"Cochon":[i for i in range(80,100)]},"apparition":1}}

dico_round_item={"Epee_slime":"round2","Epee_grosse":"round3","Epee_magique":"round4","Epee_mecanique":"round5","Epee_sus":"round6"}

dico_craft={item("Epee_pierre",1):[item("Pierre",15),item("Fer",5)],
            item("Potion",1):[item("Gel_bleu",33),item("Pierre",33)],
            item("Epee_givre",1):[item("Gel_givre",33),item("Epee_pierre",1)],
            item("Epee_slime_rose",1):[item("Epee_slime",1),item("Gel_rose",30)],
            item("Grosse_epee_slime",1):[item("Epee_slime_rose",1),item("Epee_grosse",1)],
            item("Veritable_epee_magique",1):[item("Epee_magique",1),item("Pyramide",30)],
            item("Epee_mecasus",1):[item("Epee_mecanique",1),item("Epee_sus",1)],
            item("Fragment_epee",1):[item("Veritable_epee_magique",1),item("Epee_mecasus",1)],
            item("Epee_ultime",1):[item("Fragment_epee",1),item("Grosse_epee_slime",1)],
            item("Oeil_slime",1):[item("Gel_bleu",99),item("Fer",33)],
            item("Glace_choco",1):[item("Gel_givre",99),item("Glace",33)],
            item("Catapeche",1):[item("Gel_desert",99),item("Cactus",33)],
            item("Porc_de_lave",1):[item("Porc",66),item("Pierre_de_lave",33)],
            item("Sus",1):[item("Pomme",66),item("Porc",1)],
            item("Pierre_de_lave",1):[item("Eau",1),item("Gel_rouge",1)]}

class App:
    def __init__(self):
        self.dim_x=160
        self.dim_y=90
        pyxel.init(self.dim_x,self.dim_y,"Overbroken")
        pyxel.load("resource.pyxres")
        self.player=Player(self.dim_x//2-4,self.dim_y//2-4,0.8,3,3,0.1,5,1,"Epee_bois",pyxel.frame_count)
        self.menu=True
        self.main_menu=True
        self.menu_inventaire=False
        self.select_epee=False
        self.map=map("plaine")
        self.round="round1"
        self.enemy=[]
        self.item=[]
        self.select_craft_1=False
        self.select_craft_2=False
        self.craft_act=[item("None",1),item("None",1),item("None",1)]
        self.select_invoc=False
        self.select_delet=False
        self.frame_cool_invoc=0
        self.frame_cool_delet=0
        self.frame_invoc=0
        self.frame_delet=0
        """
        self.inventaire=[None for i in range(4)]
        for i in range(len(self.inventaire)):
            self.inventaire[i]=[item("Pierre",99) for i in range(11)]
        """
        self.inventaire=[item("None",1) for i in range(52)]
        self.inventaire[0]=item("Epee_bois",1)
        self.inventaire[5]=item("Potion",5)
        """
        it=item("None",1)
        en=enemy(0,0,"Slime",0)
        i=0
        for k in it.dico_item.keys():
            if it.dico_item[k]["type"]=="materiaux":
                self.inventaire[i]=item(k,99)
            else:
                self.inventaire[i]=item(k,1)
            i=i+1
        i=0
        self.inventaire[50]=item("Fragment_epee",1)
        self.inventaire[51]=item("Porc",1)
        
        
        for k in en.dico_enemy.keys():
            for j in range(1):
                self.enemy.append(enemy(0+8*i,12+2*i,k,0))
            i=i+1
        """
        self.frame_clignote=0
        self.degat=0
        self.frame_degat=0
        self.game_over=False
        self.frame_cool_change_epee=pyxel.frame_count
        self.frame_select_craft2=pyxel.frame_count
        self.frame_select_craft1=pyxel.frame_count
        self.frame_craft=pyxel.frame_count
        self.ranger_inventaire()
        pyxel.run(self.update, self.draw)
        
    
        

    def update(self):
        if not(self.menu):
            if pyxel.btnp(pyxel.KEY_SPACE,1,4) and (self.player.epee.type=="Epee_mecanique" or self.player.epee.type=="Epee_mecasus" or self.player.epee.type=="Epee_ultime"):
                pass
            elif pyxel.btn(pyxel.KEY_SPACE):
                self.player.attaquer()
                self.frame_degat=pyxel.frame_count
            if not(self.player.attaque):
                self.player.frame_attaque=pyxel.frame_count
                if pyxel.btn(pyxel.KEY_Z):
                    self.player.deplacer("Haut",pyxel.frame_count)
                elif pyxel.btn(pyxel.KEY_S):
                    self.player.deplacer("Bas",pyxel.frame_count)
                elif pyxel.btn(pyxel.KEY_D):
                    self.player.deplacer("Droite",pyxel.frame_count)
                elif pyxel.btn(pyxel.KEY_Q):
                    self.player.deplacer("Gauche",pyxel.frame_count)
                else:
                    self.player.v=0
            else:
                if pyxel.frame_count-self.player.frame_attaque>=self.player.epee.cooldown:
                    self.player.attaque=False
                    self.player.nouv_anime(self.player.direction_act,0)
            place_popo=-1
            for i in range(len(self.inventaire)):
                if self.inventaire[i].type=="potion":
                    place_popo=i
                    break
            if pyxel.btnp(pyxel.KEY_H,15,1) and place_popo>-1:
                self.player.vie=self.player.vie_max
                self.inventaire[i].quantite-=1
                self.ranger_inventaire()
            """
            if pyxel.btn(pyxel.KEY_N):
                self.player.nouvelle_vie()
            
            if pyxel.btn(pyxel.KEY_K):
                self.player.kb()
                if self.player.attaque:
                    self.player.epee.update(self.player.x,self.player.y,self.player.direction_act)
            
            if pyxel.btn(pyxel.KEY_N):
                print(self.round)
            """
            self.player.regenerer(pyxel.frame_count)
            self.player.barre_de_vie()
            for i,ele in enumerate(self.map.triger):
                if self.colision(self.player,ele):
                    changer=self.map.changer_environement(i)
                    if changer:
                        self.enemy=[]
                        self.item=[]
                        if i==0:
                            self.player.y=80
                        elif i==1:
                            self.player.x=150
                        elif i==2:
                            self.player.y=22
                        elif i==3:
                            self.player.x=10
                        break
            if self.player.x+abs(self.player.w)>self.dim_x:
                self.player.x=self.dim_x-abs(self.player.w)
            if self.player.x<0:
                self.player.x=0
            if self.player.y+abs(self.player.h)>self.dim_y:
                self.player.y=self.dim_y-abs(self.player.h)
            if self.player.y<12:
                self.player.y=12
            if randint(0,dico_round[self.round]["apparition"]*len(self.enemy))==0:
                self.generer_enemy()
            for ele in self.enemy:
                if ele.vie<=0 and not(ele.est_mort):
                    drop=ele.mort(pyxel.frame_count)
                    if drop[0] in dico_round_item.keys():
                        if int(dico_round_item[drop[0]][5])>int(self.round[5]):
                            self.round=dico_round_item[drop[0]]
                    if drop[0]!="None":
                        self.item.append(item(drop[0],drop[1]))
                        self.item[-1].x=ele.x
                        self.item[-1].y=ele.y
                if not(ele.est_mort):
                    if (self.colision(self.player,ele) or self.colision(ele,self.player)):
                        self.player.degat(ele.attaque,pyxel.frame_count)
                        self.player.kb()
                        if self.player.attaque:
                            self.player.epee.update(self.player.x,self.player.y,self.player.direction_act)
                    if self.player.attaque and (self.colision(self.player.epee,ele) or self.colision(ele,self.player.epee)):
                        self.degat+=ele.degat(self.player.epee.degat,pyxel.frame_count)
                        ele.kb(self.player.epee.direction)
        
                    if self.player.attaque and self.player.epee.type=="Epee_magique" and pyxel.sqrt((self.player.x+4-ele.x)**2+(self.player.y+3-ele.y)**2)<=17:
                        self.degat+=ele.degat(self.player.epee.degat,pyxel.frame_count)
                    if self.player.attaque and self.player.epee.type=="Veritable_epee_magique" and pyxel.sqrt((self.player.x+4-ele.x)**2+(self.player.y+3-ele.y)**2)<=27:
                        self.degat+=ele.degat(self.player.epee.degat,pyxel.frame_count)
                    if self.player.attaque and self.player.epee.type=="Epee_ultime" and pyxel.sqrt((self.player.x+4-ele.x)**2+(self.player.y+3-ele.y)**2)<=100:
                        self.degat+=ele.degat(self.player.epee.degat,pyxel.frame_count)
                    ele.action(pyxel.frame_count) 
                if ele.x+abs(ele.w)>self.dim_x:
                    ele.x=self.dim_x-abs(ele.w)
                if ele.x<0:
                    ele.x=0
                if ele.y+abs(ele.h)>self.dim_y:
                    ele.y=self.dim_y-abs(self.player.h)
                if ele.y<12:
                    ele.y=12
            for i in range(len(self.item)):
                if i>=len(self.item):
                    i=len(self.item)-1
                ele=self.item[i]
                if self.colision(self.player,ele) or self.colision(ele,self.player):
                    if ele.type=="coeur":
                        if self.player.vie_max<22:
                            self.player.nouvelle_vie()
                        else:
                            self.player.vie=22
                        self.item.pop(i)
                        i-=1
                    else:
                        for ele2 in self.inventaire:
                            if ele.item==ele2.item and ele2.quantite<ele2.quantite_max:
                                nbinv=ele.quantite+ele2.quantite
                                if nbinv>ele2.quantite_max:
                                    ele2.quantite=ele2.quantite_max
                                    ele.quantite=nbinv-ele2.quantite
                                else:
                                    ele2.quantite=nbinv
                                    ele.quantite=0
                            if ele.quantite==0:
                                break
                            if ele2.item=="None":
                                ele2.item=ele.item
                                ele2.quantite=ele.quantite
                                ele2.quantite_max=ele.quantite_max
                                ele2.type=ele.type
                                ele2.u=ele.u
                                ele2.v=ele.v
                                ele2.image=ele.image
                                self.item.pop(i)
                                i-=1
                                break
                    if ele.quantite<=0:
                        self.item.pop(i)
                        i-=1
            self.ranger_inventaire()        
                                
            if self.player.vie<=0:
                self.game_over=True
                self.menu=True
        if pyxel.btnp(pyxel.KEY_P,15,1):
            if self.menu and not(self.main_menu) and not(self.game_over) and not(self.menu_inventaire):
                self.menu=False
            else:
                self.menu=True
        if pyxel.frame_count-self.frame_degat>=30:
            self.degat=0
            self.frame_degat=pyxel.frame_count
        if not(self.main_menu) and not(self.game_over) and  pyxel.btnp(pyxel.KEY_I,15,1):
            if not(self.menu_inventaire):
                self.menu_inventaire=True
                self.menu=True
            else:
                self.menu_inventaire=False
                self.menu=False
                self.select_epee=False
                self.select_craft_1=False
                self.select_craft_2=False
                self.select_invoc=False
                self.select_delet=False
                self.craft_act[0],self.craft_act[1],self.craft_act[2]=item("None",1),item("None",1),item("None",1)
                pyxel.mouse(False)

        if self.menu_inventaire:
            self.ranger_inventaire()
            if self.est_cliquer(45, 75, 10, 12):
                if pyxel.frame_count-self.frame_select_craft1>=15:
                    self.frame_select_craft1=pyxel.frame_count
                    if self.select_craft_1:
                        self.select_craft_1=False
                        self.craft_act[0]=item("None",1)
                        self.craft_act[2]=item("None",1)
                    else:
                        self.select_craft_1=True
                        self.select_craft_2=False
                
            if self.est_cliquer(70, 75, 10, 12):
                 if pyxel.frame_count-self.frame_select_craft2>=15:
                    self.frame_select_craft2=pyxel.frame_count
                    if self.select_craft_2:
                        self.select_craft_2=False
                        self.craft_act[1]=item("None",1)
                        self.craft_act[2]=item("None",1)
                    else:
                        self.select_craft_2=True
                        self.select_craft_1=False
            if self.est_cliquer(145, 0, 10, 12):
                if pyxel.frame_count-self.frame_cool_change_epee>=15:
                    self.frame_cool_change_epee=pyxel.frame_count
                    if self.select_epee:
                        self.select_epee=False
                    else:
                        self.select_epee=True
            if self.est_cliquer(119,79,33,8):
                 if pyxel.frame_count-self.frame_cool_invoc>=15:
                    self.frame_cool_invoc=pyxel.frame_count
                    if self.select_invoc:
                        self.select_invoc=False
                    else:
                        self.select_invoc=True
                        
            if self.est_cliquer(2, 79, 37, 8):
                 if pyxel.frame_count-self.frame_cool_delet>=15:
                    self.frame_cool_delet=pyxel.frame_count
                    if self.select_delet:
                        self.select_delet=False
                    else:
                        self.select_delet=True
            for k,ele in dico_craft.items():
                if ((self.craft_act[0].item == ele[0].item and self.craft_act[0].quantite>=ele[0].quantite) or (self.craft_act[0].item == ele[1].item and self.craft_act[0].quantite>=ele[1].quantite)) and ((self.craft_act[1].item == ele[0].item and self.craft_act[1].quantite>=ele[0].quantite) or (self.craft_act[1].item == ele[1].item and self.craft_act[1].quantite>=ele[1].quantite) ):
                    self.craft_act[2]=k
            if self.est_cliquer(100, 75, 10, 12) and self.craft_act[2].item!="None" and pyxel.frame_count-self.frame_craft>15:
                ele=self.craft_act[2]
                placer=False
                for ele2 in self.inventaire:
                        if ele.item==ele2.item and ele2.quantite<ele2.quantite_max:
                            nbinv=1+ele2.quantite
                            if nbinv<ele2.quantite_max:
                                ele2.quantite=nbinv
                                placer=True
                                break
                        if ele2.item=="None":
                            placer=True
                            ele2.item=ele.item
                            ele2.quantite=1
                            ele2.quantite_max=ele.quantite_max
                            ele2.type=ele.type
                            ele2.u=ele.u
                            ele2.v=ele.v
                            ele2.image=ele.image
                            break
                if placer and pyxel.frame_count-self.frame_craft>15:
                    self.frame_craft=pyxel.frame_count
                    materiaux=dico_craft[self.craft_act[2]]
                    if materiaux[0].item==self.craft_act[0].item:
                        self.craft_act[0].quantite-=materiaux[0].quantite
                        self.craft_act[1].quantite-=materiaux[1].quantite
                        if self.craft_act[1].quantite<materiaux[1].quantite or self.craft_act[0].quantite<materiaux[0].quantite:
                            self.craft_act[2]=item("None",1)
                    elif materiaux[1].item==self.craft_act[0].item:
                        self.craft_act[0].quantite-=materiaux[1].quantite
                        self.craft_act[1].quantite-=materiaux[0].quantite
                        if self.craft_act[0].quantite<materiaux[1].quantite or self.craft_act[1].quantite<materiaux[0].quantite:
                            self.craft_act[2]=item("None",1)
                
            
            
          
        
                

    def draw(self):
        pyxel.cls(4)
        pyxel.bltm(self.map.x,self.map.y,self.map.image,self.map.u,self.map.v,self.map.w,self.map.h)
        for ele in self.item:
            pyxel.blt(ele.x,ele.y,ele.image,ele.u,ele.v,ele.w,ele.h,colkey=0)
            pyxel.text(ele.x, ele.y,str(ele.quantite),4)
        pyxel.text(70,0,"DEGATS:",0)
        if self.degat<10:
            pyxel.text(70,6,str(self.degat),0)
        elif 10<=self.degat<100:
            pyxel.text(70,6,str(self.degat),1)
        elif 100<=self.degat<1000:
            pyxel.text(70,6,str(self.degat),11)
        elif 1000<=self.degat<10000:
            pyxel.text(70,6,str(self.degat),10)
        elif 10000<=self.degat<100000:
            pyxel.text(70,6,str(self.degat),9)
        elif 10000<=self.degat<1000000:
            pyxel.text(70,6,str(self.degat),8)
        elif 1000000<=self.degat<10000000000000000000:
            pyxel.text(70,6,str(self.degat),pyxel.frame_count%10+5)
        else:
            pyxel.text(70,6,str(randint(1000000000000000000,10000000000000000000-1)),pyxel.frame_count%10+5)
            pyxel.text(70,6,str(randint(1000000000000000000,10000000000000000000-1)),pyxel.frame_count%10+5)
            pyxel.text(100,0,"OverFlow",pyxel.frame_count%10+5)
        if self.player.attaque and self.player.epee.type=="Epee_magique" and pyxel.frame_count%2!=0:
            pyxel.circ(self.player.x+4,self.player.y+3, 17, 1)
        if self.player.attaque and self.player.epee.type=="Veritable_epee_magique" and pyxel.frame_count%2!=0:
            pyxel.circ(self.player.x+4,self.player.y+3, 27, 1)
        if self.player.attaque and self.player.epee.type=="Epee_ultime" and pyxel.frame_count%2!=0:
            pyxel.circ(self.player.x+4,self.player.y+3, 100, 1)
        if self.player.attaque and self.player.epee.direction!="Bas":
            pyxel.blt(self.player.epee.x,self.player.epee.y,0,self.player.epee.resource[self.player.epee.direction][0],self.player.epee.resource[self.player.epee.direction][1],self.player.epee.resource[self.player.epee.direction][3],self.player.epee.resource[self.player.epee.direction][2],colkey=self.player.epee.transparant)
        pyxel.blt(self.player.x,self.player.y,0,self.player.u,self.player.v,self.player.w,self.player.h,colkey=0)
        if self.player.clignote(pyxel.frame_count):
            pyxel.rect(self.player.x, self.player.y, abs(self.player.w), abs(self.player.h), 8)
        if self.player.attaque and self.player.epee.direction=="Bas":
            pyxel.blt(self.player.epee.x,self.player.epee.y,0,self.player.epee.resource[self.player.epee.direction][0],self.player.epee.resource[self.player.epee.direction][1],self.player.epee.resource[self.player.epee.direction][3],self.player.epee.resource[self.player.epee.direction][2],colkey=self.player.epee.transparant)
        for i,ele in enumerate(self.enemy):
            pyxel.blt(ele.x,ele.y,0,ele.u,ele.v,ele.w,ele.h,colkey=ele.transparant)
            if ele.clignote(pyxel.frame_count) and not(ele.est_mort):
                pyxel.rect(ele.x, ele.y, ele.w, ele.h, 8)
            if ele.est_mort and pyxel.frame_count-ele.frame_mort>=10:
                self.enemy.pop(i)
                i-=1
        if self.menu_inventaire:
            pyxel.mouse(True)
            pyxel.cls(4)
            pyxel.text(70,4,"INVENTAIRE:",0)
            pyxel.line(0,13,160,13,0)
            """
            for i in range(len(self.inventaire)):
                for j,ele in enumerate(self.inventaire[i]):
                   pyxel.rect(2*(j+1)+10*j, 15+2*i+12*i, 10, 12, 0)
                   if ele!=None:
                       pyxel.blt(2*(j+1)+10*j+1,15+2*i+12*i+1,ele.image,ele.u,ele.v,ele.w,ele.h,colkey=0)
                       pyxel.text(2*(j+1)+10*j, 15+2*i+12*i,str(ele.quantite),15)
            """
            place_item=[2,15]
            for ele in self.inventaire:
                pyxel.rect(place_item[0], place_item[1], 10, 12, 0)
                if ele.item!="None":
                    pyxel.blt(place_item[0]+1,place_item[1]+1,ele.image,ele.u,ele.v,ele.w,ele.h,colkey=0)
                    pyxel.text(place_item[0], place_item[1],str(ele.quantite),15)
                    if self.est_cliquer(place_item[0],place_item[1],ele.w+2,ele.h+2) and self.select_craft_1 and ele.item!=self.craft_act[1].item:
                        self.craft_act[0]=ele
                        self.craft_act[2]=item("None",1)
                    if self.est_cliquer(place_item[0],place_item[1],ele.w+2,ele.h+2) and self.select_craft_2 and ele.item!=self.craft_act[0].item:
                        self.craft_act[1]=ele
                        self.craft_act[2]=item("None",1)
                    if self.est_cliquer(place_item[0],place_item[1],ele.w+2,ele.h+2) and self.select_epee and ele.type=="epee":
                        self.player.nouv_epee(ele.item)
                    if self.est_cliquer(place_item[0],place_item[1],ele.w+2,ele.h+2) and self.select_invoc and ele.type=="invocation" and pyxel.frame_count-self.frame_invoc>=30:
                        self.frame_invoc=pyxel.frame_count
                        inv=self.invoc(ele.item)
                        if inv:
                            ele.quantite-=1
                    if self.est_cliquer(place_item[0],place_item[1],ele.w+2,ele.h+2) and self.select_delet and pyxel.frame_count-self.frame_delet>=30:
                        self.frame_delet=pyxel.frame_count
                        if ele.item!=self.player.epee.type:
                            ele.item="None"
                            ele.type="None"
                            ele.quantite=1
                            ele.quantite_max=1
                        
                if place_item[0]<140:
                    place_item[0]+=12
                else:
                    place_item[1]+=13
                    place_item[0]=2
            pyxel.rect(45, 75, 10, 12, 0)
            ele=self.craft_act[0]
            if ele.item!="None":
                pyxel.blt(46, 76,ele.image,ele.u,ele.v,ele.w,ele.h,colkey=0)
                pyxel.text(45, 75,str(ele.quantite),15)
            if self.select_craft_1:
                pyxel.rectb(44, 74, 12, 14, 8)
            pyxel.rect(70, 75, 10, 12, 0)
            ele=self.craft_act[1]
            if ele.item!="None":
                pyxel.blt(71, 76,ele.image,ele.u,ele.v,ele.w,ele.h,colkey=0)
                pyxel.text(70, 75,str(ele.quantite),15)
            if self.select_craft_2:
                pyxel.rectb(69, 74, 12, 14, 8)
            pyxel.rect(100, 75, 10, 12, 0)
            ele=self.craft_act[2]
            if ele.item!="None":
                pyxel.blt(101, 76,ele.image,ele.u,ele.v,ele.w,ele.h,colkey=0)
                pyxel.text(100, 75,str(ele.quantite),15)
            pyxel.text(120,80,"Invoquer",0)
            if self.select_invoc:
                pyxel.rectb(119, 79, 33, 8, 8)
            pyxel.text(3,80,"Supprimer",0)
            if self.select_delet:
                pyxel.rectb(2, 79, 37, 8, 8)
            pyxel.line(57,81,67,81,0)
            pyxel.line(62,76,62,86,0)
            pyxel.line(85,81,95,81,0)
            pyxel.tri(90,76,90,86,95,81,0)
                
        pyxel.rect(145, 0, 10, 12, 0)
        if self.select_epee:
                pyxel.rectb(145, 0, 10, 12, 8)
        pyxel.blt(145, 1, 0,self.player.epee.icon[0],self.player.epee.icon[1],10, 10, colkey=0)
        place_coeur=[0,0]
        for ele in self.player.liste_coeur:
            if ele==1:
                pyxel.blt(place_coeur[0],place_coeur[1],2,0,0,5,5,colkey=7)
            elif 0.75<=ele<1:
                pyxel.blt(place_coeur[0],place_coeur[1],2,0,5,5,5,colkey=7)
            elif 0.5<=ele<0.75:
                pyxel.blt(place_coeur[0],place_coeur[1],2,0,10,5,5,colkey=7)
            elif 0<ele<0.5:
                pyxel.blt(place_coeur[0],place_coeur[1],2,0,15,5,5,colkey=7)
            else:
                pyxel.blt(place_coeur[0],place_coeur[1],2,0,20,5,5,colkey=7)
            if place_coeur[0]<60:
                place_coeur[0]+=6
            else:
                place_coeur[1]+=7
                place_coeur[0]=0
        #affichage triger
        """
        for ele in self.map.triger:
            pyxel.rect(ele.x, ele.y, ele.w, ele.h, 8)
        """
        if self.main_menu:
            pyxel.cls(0)
            pyxel.text(33,5,"/ \------------------, ",pyxel.frame_count%14+1)
            pyxel.text(33,15,"\_,|                 | ", pyxel.frame_count%14+1)
            pyxel.text(33,25,"   |    OverBroken   | ",pyxel.frame_count%14+1)
            pyxel.text(33,35,"   |  ,----------------",pyxel.frame_count%14+1)
            pyxel.text(33,45,"   \_/_______________/",pyxel.frame_count%14+1)
            if pyxel.frame_count-self.frame_clignote<=15:
                pyxel.text(50,70,"Press A to start",7)
            elif pyxel.frame_count-self.frame_clignote>=30:
                self.frame_clignote=pyxel.frame_count
            if pyxel.btn(pyxel.KEY_A):
                self.menu=False
                self.main_menu=False
        if self.game_over:
            pyxel.cls(0)
            pyxel.mouse(True)
            pyxel.text(33,5,"/ \------------------, ",8)
            pyxel.text(33,15,"\_,|                 | ",8)
            pyxel.text(33,25,"   |    Game Over    | ",8)
            pyxel.text(33,35,"   |  ,----------------",8)
            pyxel.text(33,45,"   \_/_______________/",8)
            pyxel.rect(25,65,45,15,8)
            pyxel.rect(95,65,42,15,5)
            pyxel.text(30,70,"Main Menu",7)
            pyxel.text(100,70,"Continue",7)
            if self.est_cliquer(25,65,45,15):
                self.game_over=False
                self.main_menu=True
                self.reinit()
            if self.est_cliquer(95,65,42,15):
                self.game_over=False
                pyxel.mouse(False)
                self.menu=False
                self.player.vie=3
        


    def est_cliquer(self,x,y,w,h):
        if x<=pyxel.mouse_x<=x+w and y<=pyxel.mouse_y<=y+h and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            return True
        return False

    def colision(self,objet1,objet2):
        return (objet2.x<=objet1.x<=objet2.x+abs(objet2.w) or objet2.x<=objet1.x+abs(objet1.w)<=objet2.x+abs(objet2.w)) and (objet2.y<=objet1.y<=objet2.y+abs(objet2.h) or objet2.y<=objet1.y+abs(objet1.h)<=objet2.y+abs(objet2.h))


    def generer_enemy(self):
        mob=randint(0,99)
        for k,ele in dico_round[self.round][self.map.environement].items():
            if mob in ele:
                mob=k
                break
        if randint(0,1)==0:
            x=randint(0,160)
            y=randint(0,1)*(90-self.map.y)+self.map.y
        else:
            y=randint(self.map.y,90)
            x=randint(0,1)*160
        self.enemy.append(enemy(x,y,mob,pyxel.frame_count))
    
    def ranger_inventaire(self):
        """
        for i in range(len(self.inventaire)):
            for j in range(len(self.inventaire[0])):
                if self.inventaire[i][j].quantite<self.inventaire[i][j].quantite_max:
        """
        for i in range(len(self.inventaire)-1):
            ele=self.inventaire[i]
            for j in range(i+1,len(self.inventaire)):
                if ele.item!="None":
                    if ele.item==self.inventaire[j].item:
                        self.deplacer(self.inventaire,j,i+1)
            if ele.item!="None": 
                if ele.item==self.inventaire[i+1].item and ele.quantite<ele.quantite_max:
                    nb_remplir=ele.quantite_max-ele.quantite
                    if nb_remplir<=self.inventaire[i+1].quantite:
                        ele.quantite=ele.quantite_max
                        self.inventaire[i+1].quantite-=nb_remplir
                    else:
                        ele.quantite+=self.inventaire[i+1].quantite
                        self.inventaire[i+1].quantite=0
        
        for i in range(len(self.inventaire)):
            ele=self.inventaire[i]
            if ele.item!="None":
                if ele.quantite<=0:
                    ele.item="None"
                    ele.quantite=1
                    ele.type="None"
            if ele.item=="None":
                for j in range(i,len(self.inventaire)-1):
                    self.permuter(self.inventaire,j,j+1)
        
            
            
                    
                        

    def deplacer(self,tableau,i_source,i_destination):
        valeur = tableau[i_source]
        if i_source<i_destination:
            pas=1
        else:
            pas=-1
        for i in range(i_source,i_destination,pas):
            self.permuter(tableau,i,i+pas)
        tableau[i_destination] = valeur

    def permuter(self,tableau,i,j):
        tableau[i],tableau[j]=tableau[j],tableau[i]
        
    def invoc(self,inv):
        if inv=="Oeil_slime" and self.map.environement=="plaine":
            self.enemy.append(enemy(80,13,"Big_slime",pyxel.frame_count))
            return True
        if inv=="Glace_choco" and self.map.environement=="neige":
            self.enemy.append(enemy(80,13,"Pingu",pyxel.frame_count))
            return True
        if inv=="Catapeche" and self.map.environement=="desert":
            self.enemy.append(enemy(80,13,"Chatchat",pyxel.frame_count))
            return True
        if inv=="Porc_de_lave" and self.map.environement=="volcan":
            self.enemy.append(enemy(80,13,"Demon",pyxel.frame_count))
            return True
        if inv=="Sus":
            self.enemy.append(enemy(80,13,"Amogus",pyxel.frame_count))
            return True
        return False

    def reinit(self):
        self.player=Player(self.dim_x//2-4,self.dim_y//2-4,0.8,3,3,0.1,5,1,"Epee_bois",pyxel.frame_count)
        self.map=map("plaine")
        self.round="round1"
        self.enemy=[]
        self.item=[]
        self.inventaire=[item("None",1) for i in range(44)]



App()