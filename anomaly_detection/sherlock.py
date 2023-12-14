#@dmlab - 2021 - R2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

class Sherlock:
    def __init__(self,secret_solution,investigation_limit=100,keyword="csalás"):
        
        self.secret_solution = secret_solution.copy()
        self.secret_solution=self.secret_solution.set_index("ID")
        self.known_solution = pd.DataFrame({'ID':[],'info':[]})
        assert len(secret_solution['ID'])>0
        assert len(secret_solution['info'])>0
        self.investigation_limit=investigation_limit
        self.keyword="csalás"
    
        
    def stat(self):
        print("Adathalmaz mérete   =",len(self.secret_solution))
        print("Ismert esetek száma =",len(self.known_solution),"\t\tmax:",self.investigation_limit)
        
        if len(self.known_solution)>0:
            
            anom=len(self.known_solution.loc[self.known_solution['info']==self.keyword,:])
            print("  Ismert "+self.keyword+" =",anom)
            print("  Felderítési arány =",str(np.round(anom/len(self.known_solution)*100,1))+"%")
            
    def investigate(self,elements,investigation_time=2):
        if len(self.known_solution)>=self.investigation_limit:
            print("WARNING - Nincs több lehetőség ellenőrizni, elértük a limitet")
            return None
        if type(elements) is int:
            res=self.secret_solution.loc[elements,'info']
            new_sol=pd.DataFrame({'ID':[elements],'info':[res]})
            self.known_solution=self.known_solution.append(new_sol)
            self.known_solution = self.known_solution.drop_duplicates()
            return res
        elements=list(elements)
        if self.investigation_limit<len(elements)+len(self.known_solution):
            maxnum=self.investigation_limit-len(self.known_solution)
            if maxnum==0:
                print("WARNING - Nincs több lehetőség ellenőrizni, elértük a limitet")
                return None
            elements=elements[:maxnum]
        res=list(self.secret_solution.loc[elements,'info'])
        updated_res=[]
        for r in res:
            if r=='anomalia':
                updated_res.append(self.keyword)
            else:
                updated_res.append(r)
        new_sol=pd.DataFrame({'ID':elements,'info':updated_res})
        if investigation_time>0:
            for i,r in new_sol.iterrows():
                sleep(investigation_time)
                cres = r['info']
                if cres == 'anomalia':
                    cres=self.keyword
                print("\tNyomozás eredménye\t{}\t->\t{}".format(r['ID'],cres))
        self.known_solution=self.known_solution.append(new_sol)
        self.known_solution = self.known_solution.drop_duplicates()
    def add_label(self,indf,newname):
        pub=self.known_solution.copy()
        if newname in list(indf.columns):
            del indf[newname]
        pub.columns=['ID',newname]
        outdf=indf.merge(pub,on="ID",how="left")
        outdf[newname]=outdf[newname].fillna("no_info")
        return outdf
        
    
