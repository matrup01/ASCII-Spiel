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
        namelist = ["Hugolinus","Tetbald","Gwychardus","Siegbert","Heribert","Gwyn","Daymiosus","Balian","Thyon","Otho","Simkin","Hieronymus","Skaat","Reinoldus","Abel","Godfrey","Melcher","Urianus","Guilhelm","Imbart","Dederic","Ernisius","Merek","Anselm","Ranulfo","Berogrim","Ingraham","Melmidoc","Arthurius","Umfried","Bregormir","Gorm","Urobe","Reynfred","Aegidius","Albrecht","Balduin","Blancheflor","Bosomil","Bredelin","Feist","Gallus","Gerlach","Halmann","Helfrich","Herburgar","Hilging","Marquard","Rainald","Saladin","Zolner","Ingward","Lautrec","Oswald","Kindred","Havel","Tarkus","Atreus","Ibor","Evarin","Olurgo","Thorbjörn","Rimort","Aethor","Axor","Jeofor","Izar","Barromir","Olimar","Rambroch","Iorith","Ironar","Immerich","Peregrinus","Gothowick","Utherich","Mariannus","Dagomar","Bebor","Vexolith","Horomar","Leogrith","Aethelsthaed","Arkadius","Sirius","Severus"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def femalepersonname(self):
        namelist = ["Fulke","Aethelswith","Gorra",]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def swordname(self):
        namelist = ["Ashrune","Omega","Sturmbringer","Dunkelklinge","Inferno","Tyrhung","Donnerkeil","Chaosklinge"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def shieldname(self):
        namelist = ["Gwychardus' Bollwerk","Letzte Hoffnung","Drachenstopper","Schleier der Ahnen","Unheilsfänger","Klingenbrecher"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def axename(self):
        namelist = ["Feindspalter","Vollender","Urukuzûl","Abgrundsbeil","Wellenbrecher","Ragnarök"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def daggername(self):
        namelist = ["Seelenschnitter","Sturmflut","Schicksalsdorn","Todeszahn","Oswalds Ende"]

        rand = random.randrange(len(namelist))
        name = namelist[rand]
        return name

    def mtitles(self):
        titlelist = ["der Schöne","der Starke","der Dicke","der Wilde","der Grausame","der Gerechte","der Feige","der Mutige","der Drachentöter","Bärenbruder","Löwenreiter","der Fels","der Mächtige","der Schwache","der Giftmischer","der Riese","der Kurze","der Brudermörder","der Säufer","der Aufrichtige","der Tugendhafte","der Rachsüchtige","Eisenhaupt","Goldhand","Zwergenfreund","der Fuchs","der Kühne","der Wahnsinnige","der Berserker","der Weise","der Dumme","der Strenge"]

        rand = random.randrange(len(titlelist))
        title = titlelist[rand]
        return title

    def wtitles(self):
        titlelist = ["die Schöne","die Starke","die Dicke","die Wilde","die Grausame","die Gerechte","die Feige","die Mutige","die Drachentöterin","Wolfskind","Löwenreiterin","die Zarte","die Mächtige","die Schmächtige","die Giftmischerin","die Riesin","die Säuferin","die Aufrichtige","die Tugendhafte","die Rachsüchtige","Goldlocke","Elfenschwester","die Elster","die Kühne","die Wahnsinnige","die Wikingerin","die Weise","die Dümmliche","die Strenge"]

        rand = random.randrange(len(titlelist))
        title = titlelist[rand]
        return title