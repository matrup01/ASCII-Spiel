import random #Alle Namen von https://www.fantasynamegenerators.com/

class Names:
    def __init__(self):
        self.realm = ""

    def realmname(self): # --> self.realm
        realmlist = ["Iohitha","Lessearona", "Iaccorah","Stayitika","Geaglonet","Waebrajan","Eonnialas","Flobadale","Giabola","Kraworial","Keniorona","Klorrurat","Opheven","Kreomemund","Earizan","Lajania","Biwerus","Tiapponia","Zumusos","Reasala","Erilar","Safenica","Icromos","Eokitora","Diafunata","Axerim","Ivirath","Iadiolar","Fiodovar","Eareagoth","Iappimund","Sabrodell","Iakotara","Fiadducia","Astrearia","Otegus","Eorrinor","Iapuriel","Anuzan","Eoridran","Ezirhia","Iahuthas","Naemutria","Igunia","Fladealyn","Dochipia","Jeoforos","Iatezan","Vaxeorea","Leakadolon","Ibethan","Irunol","Ianotika","Onniroth","Harogrim","Utemond","Fittemor","Eabilas","Aetinor","Arramar","Ioshisos","Fuhidin","Taepition"]

        rand = random.randrange(len(realmlist))
        self.realm = realmlist[rand]
        return self.realm

    def malepersonname(self):
        namelist = ["Hugolinus","Tetbald","Gwychardus","Siegbert","Heribert","Gwyn","Daymiosus","Balian","Thyon","Otho","Simkin","Hieronymus","Skaat","Reinoldus","Abel","Godfrey","Melcher","Urianus","Guilhelm","Imbart","Dederic","Ernisius","Merek","Anselm","Ranulfo","Berogrim","Ingraham","Melmidoc","Arthurius","Umfried","Bregormir","Gorm","Urobe","Reynfred","Aegidius","Albrecht","Balduin","Blancheflor","Bosomil","Bredelin","Feist","Gallus","Gerlach","Halmann","Helfrich","Herburgar","Hilging","Marquard","Rainald","Saladin","Zolner","Ingward","Lautrec","Oswald","Kindred","Havel","Tarkus","Atreus","Ibor","Evarin","Olurgo","Thorbjörn","Rimort","Aethor","Axor","Jeofor","Izar","Barromir","Olimar","Rambroch","Iorith","Ironar","Immerich","Peregrinus","Gothowick","Utherich","Mariannus","Dagomar","Bebor","Vexolith","Horomar","Leogrith"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def femalepersonname(self):
        namelist = ["Fulke"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def swordname(self):
        namelist = ["Ashrune","Omega","Sturmbringer","Dunkelklinge","Inferno"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def shieldname(self):
        namelist = ["Platzhalter1","Platzhalter2"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def mtitles(self):
        titlelist = ["der Schöne","der Starke","der Dicke","der Wilde","der Grausame","der Gerechte","der Feige","der Mutige","der Drachentöter","Bärenbruder","Löwenreiter"]

        rand = random.randrange(len(titlelist))
        title = titlelist[rand]
        return title