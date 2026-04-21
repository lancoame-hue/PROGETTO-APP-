import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QStackedWidget, QLineEdit, QHBoxLayout, QMessageBox, QGridLayout,
    QSlider, QSpinBox, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

# ====================== CLASSE DESTINAZIONE + DATABASE ======================
class Destinazione:
    def __init__(self, nome, paese, budget_medio_giorno, clima, paesaggio, mood, esperienze,
                 adatto_famiglia=False, adatto_disabilita=False):
        self.nome = nome
        self.paese = paese
        self.budget_medio_giorno = budget_medio_giorno
        self.clima = clima
        self.paesaggio = paesaggio
        self.mood = mood
        self.esperienze = esperienze
        self.adatto_famiglia = adatto_famiglia
        self.adatto_disabilita = adatto_disabilita
        self.punteggio = 0   # verrà calcolato dall'algoritmo

def crea_database_destinazioni():
    return [
        Destinazione("Barcellona", "Spagna", 120, "Mediterraneo", ["Mare", "Città"], ["Cultura", "Gastronomico"],
                     ["Visite culturali", "Esperienze enogastronomiche"], True, False),
        Destinazione("Santorini", "Grecia", 150, "Mediterraneo", ["Mare"], ["Relax", "Romantico"],
                     ["Relax in spa", "Tour in barca"], False, False),
        Destinazione("Lisbona", "Portogallo", 110, "Mediterraneo", ["Mare", "Città"], ["Cultura", "Gastronomico"],
                     ["Visite culturali", "Esperienze enogastronomiche"], True, False),
        Destinazione("Parigi", "Francia", 180, "Fresco", ["Città"], ["Cultura", "Romantico"],
                     ["Visite culturali"], False, True),
        Destinazione("Costiera Amalfitana", "Italia", 140, "Mediterraneo", ["Mare"], ["Relax", "Romantico"],
                     ["Relax in spa", "Tour in barca"], False, False),
        Destinazione("Innsbruck", "Austria", 130, "Montano", ["Montagne"], ["Avventura", "Relax"],
                     ["Escursioni"], True, False),
        Destinazione("Berlino", "Germania", 100, "Fresco", ["Città"], ["Cultura"],
                     ["Visite culturali"], True, True),
        Destinazione("Atene", "Grecia", 90, "Mediterraneo", ["Città", "Mare"], ["Cultura"],
                     ["Visite culturali"], True, False),
        Destinazione("Madrid", "Spagna", 110, "Mediterraneo", ["Città"], ["Cultura", "Gastronomico"],
                     ["Visite culturali", "Esperienze enogastronomiche"], True, False),
        Destinazione("Salzburg", "Austria", 125, "Montano", ["Montagne"], ["Cultura", "Relax"],
                     ["Visite culturali"], True, False),
    ]


# ====================== PAGINA 1: SCHERMATA INIZIALE ======================
class PaginaIniziale(QWidget):
    def __init__(self, callback_avanti):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl1 = QLabel("NOVAROUT")
        lbl1.setStyleSheet("""
            color: white; background-color: rgba(0, 0, 128, 180);
            font-family: 'Times New Roman'; font-size: 50px; font-weight: bold;
            padding: 15px; border-radius: 15px;
        """)
        lbl1.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl1)

        layout.addSpacing(40)

        bott = QPushButton("INIZIA IL VIAGGIO")
        bott.setFixedSize(220, 60)
        bott.setStyleSheet("""
            background-color: rgba(174, 214, 241, 200); color: #000080;
            font-family: 'Times New Roman'; font-size: 18px; font-weight: bold; border-radius: 15px;
        """)
        bott.clicked.connect(callback_avanti)
        layout.addWidget(bott, alignment=Qt.AlignCenter)
        self.setLayout(layout)


# ====================== PAGINA 2: NOME ======================
class SecondaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl2 = QLabel("BENVENUTO!\n\nCome ti posso chiamare?")
        lbl2.setStyleSheet("""
            color: white; background-color: rgba(0, 0, 128, 180);
            font-family: 'Times New Roman'; font-size: 22px; padding: 10px; border-radius: 10px;
        """)
        lbl2.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl2)

        layout.addSpacing(20)
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Inserisci il tuo nome...")
        self.input_nome.setFixedSize(300, 40)
        self.input_nome.setStyleSheet("background-color: white; border-radius: 10px; padding: 5px; font-size: 16px;")
        layout.addWidget(self.input_nome, alignment=Qt.AlignCenter)
        self.input_nome.returnPressed.connect(callback_avanti)

        layout.addSpacing(30)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro")
        btn_back.setFixedSize(150, 40)
        btn_back.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
        btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.setFixedSize(150, 40)
        btn_next.setStyleSheet("background-color: #AED6F1; color: #000080; font-weight: bold; border-radius: 10px;")
        btn_next.clicked.connect(callback_avanti)
        layout_nav.addWidget(btn_back); layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)


# ====================== PAGINA 3: BENVENUTO ======================
class TerzaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.lbl3 = QLabel("")
        self.lbl3.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 26px; padding: 20px; border-radius: 15px; text-align: center;")
        layout.addWidget(self.lbl3, alignment=Qt.AlignCenter)

        layout.addSpacing(30)
        info = QLabel("Rispondi alle prossime domande e il nostro algoritmo troverà\nla destinazione perfetta per te!")
        info.setStyleSheet("color: white; font-size: 18px; font-style: italic;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro")
        btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti")
        btn_next.clicked.connect(callback_avanti)

        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40)
            b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        
        layout_nav.addWidget(btn_back)
        layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

    def aggiorna_nome(self, nome):
        self.lbl3.setText(f"Ciao {nome}! ✨\nTi aiuteremo a trovare la tua meta perfetta")


# ====================== PAGINE 4 ======================
class QuartaPagina(QWidget):   # Budget
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Qual è il tuo budget massimo?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)

        layout.addSpacing(40)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10000)
        self.slider.setSingleStep(100)
        self.slider.setFixedWidth(500)
        self.slider.setStyleSheet("""QSlider::handle:horizontal {background: #AED6F1; border: 1px solid #000080; width: 20px; height: 20px; margin: -5px 0; border-radius: 10px;}
                                     QSlider::groove:horizontal {border: 1px solid #bbb; height: 10px; background: white; border-radius: 5px;}""")
        layout.addWidget(self.slider, alignment=Qt.AlignCenter)

        self.lbl_valore = QLabel("Budget: 0 €")
        self.lbl_valore.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 10px;")
        layout.addWidget(self.lbl_valore, alignment=Qt.AlignCenter)
        self.slider.valueChanged.connect(self.aggiorna_etichetta)

        layout.addSpacing(50)
        
        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro")
        btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti")
        btn_next.clicked.connect(callback_avanti)
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40)
            b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        layout_nav.addWidget(btn_back)
        layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

    def aggiorna_etichetta(self, valore):
        self.lbl_valore.setText(f"Budget: {valore} €")

# ---  QUINTA PAGINA (DURATA VIAGGIO) ---
class QuintaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Per quanti giorni vorresti stare via?")
        lbl.setStyleSheet("""
            color: white; 
            background-color: rgba(0, 0, 128, 180); 
            font-size: 24px; 
            padding: 15px; 
            border-radius: 10px;
        """)
        layout.addWidget(lbl, alignment=Qt.AlignCenter)

        layout.addSpacing(30)

        # Campo di input per i giorni
        self.input_giorni = QLineEdit()
        self.input_giorni.setPlaceholderText("Es: 7")
        self.input_giorni.setFixedSize(150, 50)
        # Accetta solo numeri interi tra 1 e 365
        self.input_giorni.setValidator(QIntValidator(1, 365)) 
        self.input_giorni.setStyleSheet("""
            background-color: white; 
            border-radius: 10px; 
            font-size: 20px; 
            text-align: center;
            padding: 5px;
        """)
        layout.addWidget(self.input_giorni, alignment=Qt.AlignCenter)

        lbl_info = QLabel("Inserisci un numero di giorni (es. 1-365)")
        lbl_info.setStyleSheet("color: white; font-size: 14px; margin-top: 5px;")
        layout.addWidget(lbl_info, alignment=Qt.AlignCenter)

        layout.addSpacing(40)

        # Navigazione
        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.clicked.connect(callback_avanti)
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40)
            b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        
        layout_nav.addWidget(btn_back)
        layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

class SestaPagina(QWidget):   # Persone + bambini + disabilità
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Quante persone partecipano al viaggio?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)
        layout.addSpacing(30)

        # Totale
        tot_layout = QHBoxLayout()
        tot_layout.addWidget(QLabel("Totale persone:"))
        self.spin_total = QSpinBox()
        self.spin_total.setRange(1,30)
        self.spin_total.setValue(2)
        self.spin_total.setFixedWidth(120)
        tot_layout.addWidget(self.spin_total)
        layout.addLayout(tot_layout)
        
        # Bambini
        bam_layout = QHBoxLayout()
        bam_layout.addWidget(QLabel("Di cui bambini (0-14 anni):"))
        self.spin_bambini = QSpinBox()
        self.spin_bambini.setRange(0,15)
        self.spin_bambini.setValue(0)
        self.spin_bambini.setFixedWidth(120)
        bam_layout.addWidget(self.spin_bambini)
        layout.addLayout(bam_layout)

        layout.addSpacing(10)
        
        # Età bambini
        self.lbl_eta = QLabel("Età dei bambini (separate da virgola, es. 5,8,12):")
        self.lbl_eta.setStyleSheet("color: white; font-size: 16px;")
        layout.addWidget(self.lbl_eta, alignment=Qt.AlignCenter)
        self.input_eta = QLineEdit(); self.input_eta.setPlaceholderText("es. 5,8,12"); self.input_eta.setFixedSize(300,40)
        self.input_eta.setStyleSheet("background-color: white; border-radius: 10px; padding: 5px; font-size: 16px;")
        layout.addWidget(self.input_eta, alignment=Qt.AlignCenter)

        layout.addSpacing(20)

        # Disabilità
        self.check_disabilita = QCheckBox("Ci sono persone con disabilità?")
        self.check_disabilita.setStyleSheet("color: white; font-size: 18px;")
        layout.addWidget(self.check_disabilita, alignment=Qt.AlignCenter)

        layout.addSpacing(40)

        # Navigazione
        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.clicked.connect(callback_avanti)
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40); b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        layout_nav.addWidget(btn_back); layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)


# ====================== PAGINA 7: CLIMA (con salvataggio scelta) ======================
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class SettimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_clima = ""                     

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Che tipo di clima preferisci?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)
        layout.addSpacing(30)

        grid = QGridLayout()
        climi = ["Tropicale ☀️", "Mediterraneo 🌊", "Fresco 🍂", "Freddo ❄️", "Montano ⛰️"]
        self.bottoni_clima = []
        
        for i, testo in enumerate(climi):
            btn = QPushButton(testo)
            btn.setFixedSize(200, 60)
            btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px; font-size: 18px;")
            
            # Colleghiamo direttamente al metodo seleziona senza lambda
            btn.clicked.connect(self.seleziona)
            
            grid.addWidget(btn, i // 2, i % 2)
            self.bottoni_clima.append(btn)

        layout.addLayout(grid)
        layout.addSpacing(30)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro")
        btn_back.clicked.connect(callback_indietro)
        
        btn_next = QPushButton("Avanti")
        btn_next.clicked.connect(callback_avanti)
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40)
            b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
            
        layout_nav.addWidget(btn_back)
        layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        
        self.setLayout(layout)

    def seleziona(self):
        # Usiamo sender() per capire quale bottone è stato premuto
        bottone_cliccato = self.sender()
        self.scelta_clima = bottone_cliccato.text()

        # Ciclo sui bottoni clima per aggiornare l'evidenziazione
        for btn in self.bottoni_clima:
            if btn == bottone_cliccato:
                # Stile per il bottone selezionato (Azzurro)
                btn.setStyleSheet("background-color: #AED6F1; color: #000080; font-weight: bold; border-radius: 10px; font-size: 18px;")
            else:
                # Stile per gli altri bottoni (Bianco)
                btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px; font-size: 18px;")

# ====================== PAGINE 8-9-10  (con salvataggio scelta) ======================

class OttavaPagina(QWidget):   # Regione / Stato
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_regione = ""
        self.bottoni_stato = []  # Lista per gestire lo stile dei bottoni

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        lbl = QLabel("In quale regione geografica / stato europeo vuoi andare?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)
        layout.addSpacing(20)

        grid = QGridLayout()
        stati = ["Italia 🇮🇹", "Francia 🇫🇷", "Spagna 🇪🇸", "Grecia 🇬🇷", "Portogallo 🇵🇹", 
                 "Germania 🇩🇪", "Svizzera 🇨🇭", "Austria 🇦🇹", "Regno Unito 🇬🇧", "Altri"]
        
        for i, testo in enumerate(stati):
            btn = QPushButton(testo)
            btn.setFixedSize(160, 55)
            btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
            
            # Colleghiamo direttamente al metodo seleziona senza lambda
            btn.clicked.connect(self.seleziona)
            
            grid.addWidget(btn, i // 2, i % 2)
            self.bottoni_stato.append(btn)
            
        layout.addLayout(grid)

        # Navigazione
        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro")
        btn_back.clicked.connect(callback_indietro)
        
        btn_next = QPushButton("Avanti")
        btn_next.clicked.connect(callback_avanti)
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40)
            b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
            
        layout_nav.addWidget(btn_back)
        layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        
        self.setLayout(layout)

    def seleziona(self):
        # Recuperiamo quale bottone è stato premuto
        bottone_cliccato = self.sender()
        self.scelta_regione = bottone_cliccato.text()

        # Ciclo sui bottoni salvati per cambiare lo stato visivo
        for btn in self.bottoni_stato:
            if btn == bottone_cliccato:
                # Colore azzurro per il selezionato
                btn.setStyleSheet("background-color: #AED6F1; color: #000080; font-weight: bold; border-radius: 10px;")
            else:
                # Bianco per gli altri
                btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")

class NonaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_paesaggio = ""
        self.bottoni_paesaggio = []

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        lbl = QLabel("Che tipo di paesaggio preferisci?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)
        layout.addSpacing(20)

        grid = QGridLayout()
        paesaggi = ["Mare 🏖️", "Montagne ⛰️", "Città 🏙️", "Foresta 🌲", "Lago 🏞️", "Deserto 🏜️", "Campagna 🌾"]
        
        for i, testo in enumerate(paesaggi):
            btn = QPushButton(testo)
            btn.setFixedSize(160, 55)
            btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
            # Collegamento diretto
            btn.clicked.connect(self.seleziona)
            grid.addWidget(btn, i // 2, i % 2)
            self.bottoni_paesaggio.append(btn)
        
        layout.addLayout(grid)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.clicked.connect(callback_avanti)
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40); b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        layout_nav.addWidget(btn_back); layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

    def seleziona(self):
        bottone_cliccato = self.sender()
        self.scelta_paesaggio = bottone_cliccato.text()
        for btn in self.bottoni_paesaggio:
            if btn == bottone_cliccato:
                btn.setStyleSheet("background-color: #AED6F1; color: #000080; font-weight: bold; border-radius: 10px;")
            else:
                btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")


class DecimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_mood = ""
        self.bottoni_mood = []

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        lbl = QLabel("Che mood di viaggio cerchi?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)
        layout.addSpacing(20)

        grid = QGridLayout()
        mood_list = ["Relax 🧘", "Avventura 🏔️", "Sport Estremi 🪂", "Lusso 💎", "Cultura 🏛️", "Famiglia 👨‍👧‍👦", "Romantico ❤️", "Gastronomico 🍷"]
        
        for i, testo in enumerate(mood_list):
            btn = QPushButton(testo)
            btn.setFixedSize(180, 55)
            btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
            # Collegamento diretto
            btn.clicked.connect(self.seleziona)
            grid.addWidget(btn, i // 2, i % 2)
            self.bottoni_mood.append(btn)
            
        layout.addLayout(grid)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro")
        btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti")
        btn_next.clicked.connect(callback_avanti)
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40)
            b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        layout_nav.addWidget(btn_back)
        layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

    def seleziona(self):
        bottone_cliccato = self.sender()
        self.scelta_mood = bottone_cliccato.text()
        for btn in self.bottoni_mood:
            if btn == bottone_cliccato:
                btn.setStyleSheet("background-color: #AED6F1; color: #000080; font-weight: bold; border-radius: 10px;")
            else:
                btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")

# ====================== PAGINA 11: ESPERIENZE (checkbox) ======================
class UndicesimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Quali esperienze vuoi vivere?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)
        layout.addSpacing(20)

        esperienze_layout = QVBoxLayout()
        self.checks = []
        esperienze = ["Escursioni e trekking", "Visite culturali / musei", "Sport acquatici o estremi",
                      "Esperienze enogastronomiche", "Relax in spa / wellness", "Tour in barca o crociera",
                      "Attività con animali (safari, ecc.)", "Festival e eventi"]
        for exp in esperienze:
            cb = QCheckBox(exp)
            cb.setStyleSheet("color: white; font-size: 18px;")
            esperienze_layout.addWidget(cb)
            self.checks.append(cb)
        layout.addLayout(esperienze_layout)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.clicked.connect(callback_avanti)
        for b in [btn_back, btn_next]:
            b.setFixedSize(150, 40); b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold;")
        layout_nav.addWidget(btn_back); layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)


# ====================== PAGINA RISULTATI (nuova pagina finale) ======================
class PaginaRisultati(QWidget):
    def __init__(self, callback_indietro, callback_ricomincia):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.lbl_titolo = QLabel("LA TUA META PERFETTA È...")
        self.lbl_titolo.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")
        self.layout.addWidget(self.lbl_titolo)

        self.lbl_meta = QLabel("")
        self.lbl_meta.setStyleSheet("color: #AED6F1; font-size: 42px; font-weight: bold; margin: 20px;")
        self.layout.addWidget(self.lbl_meta)

        self.lbl_motivazione = QLabel("")
        self.lbl_motivazione.setStyleSheet("color: white; font-size: 20px; text-align: center; margin: 15px;")
        self.lbl_motivazione.setWordWrap(True)
        self.layout.addWidget(self.lbl_motivazione)

        nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_restart = QPushButton("Ricomincia"); btn_restart.clicked.connect(callback_ricomincia)
        for b in [btn_back, btn_restart]:
            b.setFixedSize(160, 50); b.setStyleSheet("background-color: white; border-radius: 10px; font-weight: bold; font-size: 16px;")
        nav.addWidget(btn_back); nav.addWidget(btn_restart)
        self.layout.addLayout(nav)

    def mostra_risultato(self, top3, nome_utente):
        if not top3:
            self.lbl_meta.setText("Nessuna meta trovata 😢")
            return
        migliore = top3[0]
        self.lbl_meta.setText(f"{migliore.nome} ({migliore.paese})")
        motiv = f"Perché è perfetta per te:\n• Budget compatibile\n• Clima {migliore.clima}\n• {len(migliore.esperienze)} esperienze che ti piacciono\nPunteggio: {migliore.punteggio}/100"
        self.lbl_motivazione.setText(motiv)


# ====================== FINESTRA PRINCIPALE ======================
import os

class FinestraPrincipale(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Path assoluto automatico – funziona sempre, su qualsiasi PC
        BASE = os.path.dirname(os.path.abspath(__file__))
        percorso = os.path.join(BASE, "sfondo_app.png").replace("\\", "/")

        self.setStyleSheet(f"""
            FinestraPrincipale {{
                border-image: url('{percorso}') 0 0 0 0 stretch stretch;
            }}
        """)
        # Creazione pagine
        self.pag1 = PaginaIniziale(self.vai_a_pag2)
        self.pag2 = SecondaPagina(self.vai_a_pag1, self.vai_a_pag3)
        self.pag3 = TerzaPagina(self.vai_a_pag2, self.vai_a_pag4)
        self.pag4 = QuartaPagina(self.vai_a_pag3, self.vai_a_pag5)
        self.pag5 = QuintaPagina(self.vai_a_pag4, self.vai_a_pag6)
        self.pag6 = SestaPagina(self.vai_a_pag5, self.vai_a_pag7)
        self.pag7 = SettimaPagina(self.vai_a_pag6, self.vai_a_pag8)
        self.pag8 = OttavaPagina(self.vai_a_pag7, self.vai_a_pag9)
        self.pag9 = NonaPagina(self.vai_a_pag8, self.vai_a_pag10)
        self.pag10 = DecimaPagina(self.vai_a_pag9, self.vai_a_pag11)
        self.pag11 = UndicesimaPagina(self.vai_a_pag10, self.vai_a_pag12)
        self.pag12 = PaginaRisultati(self.vai_a_pag11, self.vai_a_pag1)

        # AGGIUNTE TUTTE LE PAGINE (Inclusa la 12!)
        pagine = [self.pag1, self.pag2, self.pag3, self.pag4, self.pag5, self.pag6, 
                  self.pag7, self.pag8, self.pag9, self.pag10, self.pag11, self.pag12]
        for p in pagine:
            self.addWidget(p)

    # ====================== NAVIGAZIONE CORRETTA ======================
    def vai_a_pag1(self): 
        self.setCurrentIndex(0)
    def vai_a_pag2(self): 
        self.setCurrentIndex(1)

    def vai_a_pag3(self):
        nome = self.pag2.input_nome.text().strip()
        if not nome:
            QMessageBox.warning(self, "Errore", "Inserisci il nome!")
            return
        self.pag3.aggiorna_nome(nome)
        self.setCurrentIndex(2)

    def vai_a_pag4(self): 
        self.setCurrentIndex(3)
    def vai_a_pag5(self): 
        self.setCurrentIndex(4)

    def vai_a_pag6(self):
        if self.pag5.input_giorni.text().strip() == "":
            QMessageBox.warning(self, "Errore", "Inserisci il numero di giorni!")
            return
        self.setCurrentIndex(5)

    def vai_a_pag7(self): 
        self.setCurrentIndex(6)
    def vai_a_pag8(self): 
        self.setCurrentIndex(7)
    def vai_a_pag9(self): 
        self.setCurrentIndex(8)
    def vai_a_pag10(self): 
        self.setCurrentIndex(9)

    def vai_a_pag11(self):
        # Controllo solo l'ultima scelta fatta (il mood) per non bloccare
        if not self.pag10.scelta_mood:
            QMessageBox.warning(self, "Attenzione", "Seleziona un mood per continuare!")
            return
        self.setCurrentIndex(10)

    def vai_a_pag12(self):
        # Qui calcoliamo i risultati finali
        top3 = self.calcola_meta_perfecta()
        self.pag12.mostra_risultato(top3, self.pag2.input_nome.text())
        self.setCurrentIndex(11) 

    # ====================== ALGORITMO ======================
    def raccogli_risposte_utente(self):
        return {
            'nome': self.pag2.input_nome.text().strip(),
            'giorni': int(self.pag5.input_giorni.text() or 7),
            'budget_max': self.pag4.slider.value(),
            'num_persone': self.pag6.spin_total.value(),
            'num_bambini': self.pag6.spin_bambini.value(),
            'disabilita': self.pag6.check_disabilita.isChecked(),
            'clima': self.pag7.scelta_clima,
            'regione': self.pag8.scelta_regione, # Aggiunto riferimento regione
            'paesaggio': self.pag9.scelta_paesaggio,
            'mood': self.pag10.scelta_mood,
            'esperienze': [cb.text() for cb in self.pag11.checks if cb.isChecked()],
        }
    
    # ... resto del codice calcola_meta_perfecta ...


    def calcola_meta_perfecta(self):
        dati = self.raccogli_risposte_utente()
        destinazioni = crea_database_destinazioni()

        for dest in destinazioni:
            punteggio = 0

            # Budget
            costo_stimato = dest.budget_medio_giorno * dati['num_persone'] * 7   # 7 giorni di esempio
            if dati['budget_max'] >= costo_stimato:
                punteggio += 30
            elif dati['budget_max'] >= costo_stimato * 0.6:
                punteggio += 15

            # Clima
            if dati['clima'] == dest.clima:
                punteggio += 25

            # Paesaggio
            if dati['paesaggio'] in dest.paesaggio:
                punteggio += 20

            # Mood
            if dati['mood'] in dest.mood:
                punteggio += 20

            # Esperienze
            match = len(set(dati['esperienze']) & set(dest.esperienze))
            punteggio += match * 8

            # Famiglia
            if dati['num_bambini'] > 0 and dest.adatto_famiglia:
                punteggio += 15

            # Disabilità
            if dati['disabilita'] and dest.adatto_disabilita:
                punteggio += 10

            dest.punteggio = punteggio

        destinazioni.sort(key=lambda d: d.punteggio, reverse=True)
        return destinazioni[:3]   # top 3

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.showNormal()


# ====================== AVVIO ======================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = FinestraPrincipale()
    finestra.showFullScreen()
    sys.exit(app.exec_())
