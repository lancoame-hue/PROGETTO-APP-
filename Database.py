class Destinazione:
    def __init__(self, nome, paese, budget, clima, paesaggio, mood, esperienze,
                 sicurezza, stagione, popolarita, famiglia=False, disabilita=False):
        self.nome = nome
        self.paese = paese
        self.budget = budget
        self.clima = clima
        self.paesaggio = paesaggio
        self.mood = mood
        self.esperienze = esperienze
        self.sicurezza = sicurezza  # 1-10
        self.stagione = stagione
        self.popolarita = popolarita  # 1-10
        self.famiglia = famiglia
        self.disabilita = disabilita
        self.punteggio = 0


def crea_database():
    return [

        # 🇮🇹 ITALIA
        Destinazione("Roma","Italia",130,"Mediterraneo",["Città"],["Cultura"],["Musei","Storia"],7,"Primavera",10,True),
        Destinazione("Milano","Italia",150,"Fresco",["Città"],["Lusso"],["Shopping","Eventi"],8,"Autunno",9),
        Destinazione("Napoli","Italia",100,"Mediterraneo",["Mare","Città"],["Gastronomico"],["Cibo","Cultura"],6,"Estate",9),

        # 🇫🇷 FRANCIA
        Destinazione("Parigi","Francia",180,"Fresco",["Città"],["Romantico"],["Musei","Arte"],7,"Primavera",10),
        Destinazione("Nizza","Francia",160,"Mediterraneo",["Mare"],["Relax"],["Spiaggia"],8,"Estate",9),
        Destinazione("Lione","Francia",130,"Fresco",["Città"],["Gastronomico"],["Cibo"],8,"Autunno",8),

        # 🇪🇸 SPAGNA
        Destinazione("Barcellona","Spagna",120,"Mediterraneo",["Mare","Città"],["Cultura"],["Cibo","Spiaggia"],7,"Estate",10),
        Destinazione("Madrid","Spagna",110,"Mediterraneo",["Città"],["Cultura"],["Musei"],8,"Primavera",9),
        Destinazione("Valencia","Spagna",105,"Mediterraneo",["Mare"],["Relax"],["Spiaggia"],8,"Estate",8),

        # 🇩🇪 GERMANIA
        Destinazione("Berlino","Germania",100,"Fresco",["Città"],["Cultura"],["Musei","Storia"],8,"Estate",10,True,True),
        Destinazione("Monaco","Germania",140,"Fresco",["Città"],["Lusso"],["Eventi"],9,"Autunno",9),
        Destinazione("Amburgo","Germania",120,"Fresco",["Città"],["Relax"],["Porto"],8,"Estate",8),

        # 🇦🇹 AUSTRIA
        Destinazione("Vienna","Austria",130,"Fresco",["Città"],["Cultura"],["Musei"],9,"Primavera",9),
        Destinazione("Salzburg","Austria",125,"Montano",["Montagne"],["Relax"],["Natura"],9,"Inverno",8),
        Destinazione("Innsbruck","Austria",130,"Montano",["Montagne"],["Avventura"],["Sci","Escursioni"],9,"Inverno",9),

        # 🇬🇷 GRECIA
        Destinazione("Atene","Grecia",90,"Mediterraneo",["Città"],["Cultura"],["Storia"],7,"Primavera",9),
        Destinazione("Santorini","Grecia",150,"Mediterraneo",["Mare"],["Romantico"],["Relax"],9,"Estate",10),
        Destinazione("Mykonos","Grecia",170,"Mediterraneo",["Mare"],["Lusso"],["Nightlife"],8,"Estate",10),

        # 🇵🇹 PORTOGALLO
        Destinazione("Lisbona","Portogallo",110,"Mediterraneo",["Città"],["Cultura"],["Cibo"],8,"Primavera",9),
        Destinazione("Porto","Portogallo",100,"Mediterraneo",["Città"],["Relax"],["Vino"],8,"Autunno",8),
        Destinazione("Faro","Portogallo",105,"Mediterraneo",["Mare"],["Relax"],["Spiaggia"],8,"Estate",8),

        # 🇳🇱 OLANDA
        Destinazione("Amsterdam","Olanda",150,"Fresco",["Città"],["Cultura"],["Musei"],9,"Primavera",10),
        Destinazione("Rotterdam","Olanda",130,"Fresco",["Città"],["Moderno"],["Architettura"],9,"Estate",8),
        Destinazione("Utrecht","Olanda",120,"Fresco",["Città"],["Relax"],["Canali"],9,"Primavera",8),

        # 🇬🇧 UK
        Destinazione("Londra","UK",180,"Fresco",["Città"],["Cultura"],["Musei"],8,"Estate",10),
        Destinazione("Edimburgo","UK",140,"Freddo",["Città"],["Cultura"],["Festival"],9,"Estate",9),
        Destinazione("Manchester","UK",120,"Fresco",["Città"],["Sport"],["Eventi"],8,"Autunno",8),

        # 🇨🇭 SVIZZERA
        Destinazione("Zurigo","Svizzera",200,"Freddo",["Città"],["Lusso"],["Natura"],10,"Inverno",9),
        Destinazione("Ginevra","Svizzera",190,"Freddo",["Lago"],["Relax"],["Natura"],10,"Estate",9),
        Destinazione("Interlaken","Svizzera",180,"Montano",["Montagne"],["Avventura"],["Sport estremi"],10,"Estate",10),
    ]
