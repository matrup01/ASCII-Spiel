import random #Alle Namen von https://www.fantasynamegenerators.com/

class Names:
    def __init__(self):
        self.realm = ""

    def realmname(self): # --> self.realm
        realmlist = ["Iohitha","Lessearona", "Iaccorah","Stayitika","Geaglonet","Waebrajan","Eonnialas","Flobadale","Giabola","Kraworial","Keniorona","Klorrurat","Opheven","Kreomemund","Earizan","Lajania","Biwerus","Tiapponia","Zumusos","Reasala","Erilar","Safenica","Icromos","Eokitora","Diafunata","Axerim","Ivirath","Iadiolar","Fiodovar","Eareagoth","Iappimund","Sabrodell","Iakotara","Fiadducia","Astrearia","Otegus","Eorrinor","Iapuriel","Anuzan","Eoridran","Ezirhia","Iahuthas","Naemutria","Igunia","Fladealyn","Dochipia","Jeoforos"]

        rand = random.randrange(len(realmlist))
        self.realm = realmlist[rand]
        return self.realm