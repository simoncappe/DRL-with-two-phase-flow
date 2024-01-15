# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:10:32 2024

@author: simon.cappe
"""
def write_circle(radius : float,center: tuple, name : str):
   
       
    texte = """
{Definition"""+name+"""=
    { Type= ModeleDeMouvements }
    { Data=
        { Repere=
            { Dimension= 2 }
            { Nom= Entree"""+name+""" }
            { Origine= """+str(center[0])+' '+ str(center[1])+ """ }   // position du centre pour un cercle ou position du coin inférieur gauche pour une brique
            { Axe= 1 0 0 1 }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
    }
}
   
{ Geo"""+name+"""=
    { Type= ModeleDeGeometres }
    { Data=
        { Geometre=
            { Nom= MUR"""+name+""" }
            { Type= GeometreAnalytique }
            { Data=
                { Forme=
                    { Dimension= 2 }
                    { Type= Boule }  //  Brique  
                    { Data=
                        { Rayon= """+str(radius)+""" }  
                    }
                                                   
                }
                { Repere= Entree"""+name+""" }
            }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
        { Modele= Definition"""+name+""" }
    }
}



{ Distance"""+name+"""=
    { Type= ModeleParticulaire }
    { Data=
        { Champ=
            { Type= P1_Scalaire_Par }
            { Nom= LevelSetEntree"""+name+""" }
            { Data= ValeurItem 1 0.0 }                        // ##
        }
        { Champ=
            { Type= P1_Scalaire_Par }
            { Nom= AppartientEntree"""+name+""" }
            { Data= ValeurItem 1 0.0 }                        // ##
        }
        { ItemSolveur=
            { Type= ISGeometre }
            { NbChampSolution= 2 }
            { ChampSolution= AppartientEntree"""+name+""" LevelSetEntree"""+name+""" }
            { NbChampParametre= 2 }
            { ChampParametre= Coordonnees PrecisionFrontieres }
            { Geometre= MUR"""+name+""" }
            { Distance= 1 }
            { Appartient= 1 }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
        { Champ= Coordonnees }
        { Champ= PrecisionFrontieres }
    }
} """
    with open('circle_'+name+'.txt','w') as f:
        f.write(texte)



def write_border(normal,radius , center,name):
    texte = """
{ Definition"""+name+"""=
    { Type= ModeleDeMouvements }
    { Data=
        { Repere=
            { Dimension= 2 }
            { Nom= Entree"""+name+""" }
            { Origine= """+str(center[0])+' '+str(center[1]) +"""}
            { Normale= """+str(normal[0])+' '+str(normal[1]) +""" }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
    }
}


{ Geo"""+name+"""=
    { Type= ModeleDeGeometres }
    { Data=
        { Geometre=
            { Nom= MUR"""+name+""" }
            { Type= GeometreAnalytique }
            { Data=
                { Forme=
                    { Dimension= 2 }
                    { Type= DemiPlan }
                    { Data=
                        { Rayon= """+str(radius)+""" }
                    }
                                                   
                }
                { Repere= Entree"""+name+""" }
            }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
        { Modele= Definition"""+name+""" }
    }
}

{ Distance"""+name+"""=
    { Type= ModeleParticulaire }
    { Data=
        { Champ=
            { Type= P1_Scalaire_Par }
            { Nom= LevelSetEntree"""+name+""" }
            { Data= ValeurItem 1 0.0 }                        // ##
        }
        { Champ=
            { Type= P1_Scalaire_Par }
            { Nom= AppartientEntree"""+name+""" }
            { Data= ValeurItem 1 0.0 }                        // ##
        }
        { ItemSolveur=
            { Type= ISGeometre }
            { NbChampSolution= 2 }
            { ChampSolution= AppartientEntree"""+name+""" LevelSetEntree"""+name+""" }
            { NbChampParametre= 2 }
            { ChampParametre= Coordonnees PrecisionFrontieres }
            { Geometre= MUR"""+name+""" }
            { Distance= 1 }
            { Appartient= 1 }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
        { Champ= Coordonnees }
        { Champ= PrecisionFrontieres }
    }
}

"""
    with open('border_'+name+'.txt','w') as f:
        f.write(texte)
   


def write_brick(anchor:tuple, dim :tuple, name,axe = (1,1,-1,1)):
   
    texte = """
{ Definition"""+name+"""=
    { Type= ModeleDeMouvements }
    { Data=
        { Repere=
            { Dimension= 2 }
            { Nom= Entree"""+name+""" }
            { Origine= """+str(anchor[0])+' '+str(anchor[1])+""" }
            { Axe= """+str(axe[0])+""" """+str(axe[1])+""" """+str(axe[2])+""" """+str(axe[3])+""" }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
    }
}

{ Geo"""+name+"""=
    { Type= ModeleDeGeometres }
    { Data=
        { Geometre=
            { Nom= MUR"""+name+""" }
            { Type= GeometreAnalytique }
            { Data=
                { Forme=
                    { Dimension= 2 }
                    { Type= Brique }
                    { Data=
                        { Dimension= """+str(dim[0])+""" """+str(dim[1])+""" }
                    }
                                                   
                }
                { Repere= Entree"""+name+""" }
            }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
        { Modele= Definition"""+name+""" }
    }
}

{ Distance"""+name+"""=
    { Type= ModeleParticulaire }
    { Data=
        { Champ=
            { Type= P1_Scalaire_Par }
            { Nom= LevelSetEntree"""+name+""" }
            { Data= ValeurItem 1 0.0 }                        // ##
        }
        { Champ=
            { Type= P1_Scalaire_Par }
            { Nom= AppartientEntree"""+name+""" }
            { Data= ValeurItem 1 0.0 }                        // ##
        }
        { ItemSolveur=
            { Type= ISGeometre }
            { NbChampSolution= 2 }
            { ChampSolution= AppartientEntree"""+name+""" LevelSetEntree"""+name+""" }
            { NbChampParametre= 2 }
            { ChampParametre= Coordonnees PrecisionFrontieres }
            { Geometre= MUR"""+name+""" }
            { Distance= 1 }
            { Appartient= 1 }
        }
    }
    { Dependance=
        { Maillage= MaillagePrincipal }
        { Champ= Coordonnees }
        { Champ= PrecisionFrontieres }
    }
}"""
    with open('brick_'+name+'.txt','w') as f:
        f.write(texte)
   






   


def merge(list_of_names,filename = 'tot'):
   
    with open('tot.txt','w') as fichier:
        for name in list_of_names:
            with open(name+'.txt','r') as f:
                fichier.write(f.read())
            fichier.write('\n\n')
            fichier.write(r'\\#############################')
            fichier.write('\n\n')
    return None
            

            



