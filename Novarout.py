import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QStackedWidget, QLineEdit, QHBoxLayout, QMessageBox, QGridLayout
)
from PyQt5.QtCore import Qt

class PaginaIniziale(QWidget): 
    def __init__(self, callback_avanti):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl1 = QLabel("NOVAROUT")
        lbl1.setStyleSheet("""
            color: white;
            background-color: rgba(0, 0, 128, 180);
            font-family: 'Times New Roman';
            font-size: 50px;
            font-weight: bold;
            padding: 15px;
            border-radius: 15px;
        """)
        lbl1.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl1)
        
        layout.addSpacing(40)

        bott = QPushButton("INIZIA IL VIAGGIO")
        bott.setFixedSize(220, 60)
        bott.setStyleSheet("""
            background-color: rgba(174, 214, 241, 200);
            color: #000080;
            font-family: 'Times New Roman';
            font-size: 18px;
            font-weight: bold;
            border-radius: 15px;
        """)
        bott.clicked.connect(callback_avanti) 
        layout.addWidget(bott, alignment=Qt.AlignCenter)

        self.setLayout(layout)


class SecondaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl2 = QLabel("BENVENUTO!\n\nCome ti posso chiamare?")
        lbl2.setStyleSheet("""
            color: white;
            background-color: rgba(0, 0, 128, 180);
            font-family: 'Times New Roman';
            font-size: 22px;
            padding: 10px;
            border-radius: 10px;
        """)
        lbl2.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl2)
        
        layout.addSpacing(20)

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Inserisci il tuo nome...")
        self.input_nome.setFixedSize(300, 40)
        self.input_nome.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            padding: 5px;
            font-size: 16px;
        """)
        layout.addWidget(self.input_nome, alignment=Qt.AlignCenter)

        # INVIO = avanti
        self.input_nome.returnPressed.connect(callback_avanti)

        layout.addSpacing(30)

        layout_bottoni = QHBoxLayout()
        
        btn_back = QPushButton("Indietro")
        btn_back.setFixedSize(150, 40)
        btn_back.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
        btn_back.clicked.connect(callback_indietro)
        layout_bottoni.addWidget(btn_back)

        btn_next = QPushButton("Avanti")
        btn_next.setFixedSize(150, 40)
        btn_next.setStyleSheet("background-color: #AED6F1; color: #000080; font-weight: bold; border-radius: 10px;")
        btn_next.clicked.connect(callback_avanti)
        layout_bottoni.addWidget(btn_next)

        layout.addLayout(layout_bottoni)
        self.setLayout(layout)



# --- PAGINA 3 (CONTINENTI) ---
class TerzaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.lbl3 = QLabel("Scegli la tua meta ✈️")
        self.lbl3.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(self.lbl3, alignment=Qt.AlignCenter)

        grid = QGridLayout()
        continenti = ["EUROPA", "ASIA", "OCEANIA", "NORD AMERICA", "SUD AMERICA", "AFRICA"]
        for i, nome in enumerate(continenti):
            btn = QPushButton(nome)
            btn.setFixedSize(160, 50)
            btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
            grid.addWidget(btn, i // 2, i % 2)
        layout.addLayout(grid)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.clicked.connect(callback_avanti)
        layout_nav.addWidget(btn_back); layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

    def aggiorna_nome(self, nome):
        self.lbl3.setText(f"Ciao {nome}! Dove vuoi andare?")

# --- QUARTA PAGINA (PERIODO) ---
class QuartaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("In quale periodo vorresti partire?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)

        grid = QGridLayout()
        periodi = ["PRIMAVERA 🌸", "ESTATE ☀️", "AUTUNNO 🍂", "INVERNO ❄️"]
        for i, stagione in enumerate(periodi):
            btn = QPushButton(stagione)
            btn.setFixedSize(200, 50)
            btn.setStyleSheet("background-color: white; color: #000080; font-weight: bold; border-radius: 10px;")
            grid.addWidget(btn, i // 2, i % 2)
        layout.addLayout(grid)

        layout_nav = QHBoxLayout()
        btn_back = QPushButton("Indietro"); btn_back.clicked.connect(callback_indietro)
        btn_next = QPushButton("Avanti"); btn_next.clicked.connect(callback_avanti)
        layout_nav.addWidget(btn_back); layout_nav.addWidget(btn_next)
        layout.addLayout(layout_nav)
        self.setLayout(layout)

from PyQt5.QtWidgets import QSlider # Aggiungi questo agli import in alto

# --- QUINTA PAGINA (BUDGET CON BARRA A SCORRIMENTO) ---
class QuintaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Qual è il tuo budget massimo?")
        lbl.setStyleSheet("color: white; background-color: rgba(0, 0, 128, 180); font-size: 24px; padding: 15px; border-radius: 10px;")
        layout.addWidget(lbl, alignment=Qt.AlignCenter)

        layout.addSpacing(40)

        # Creazione della Barra (Slider)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)    # Budget minimo
        self.slider.setMaximum(10000)  # Budget massimo
        self.slider.setSingleStep(100)
        self.slider.setFixedWidth(500)
        self.slider.setStyleSheet("""
            QSlider::handle:horizontal {
                background: #AED6F1;
                border: 1px solid #000080;
                width: 20px;
                height: 20px;
                margin: -5px 0;
                border-radius: 10px;
            }
            QSlider::groove:horizontal {
                border: 1px solid #bbb;
                height: 10px;
                background: white;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.slider, alignment=Qt.AlignCenter)

        # Etichetta che mostra il valore corrente
        self.lbl_valore = QLabel("Budget: 500 €")
        self.lbl_valore.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 10px;")
        layout.addWidget(self.lbl_valore, alignment=Qt.AlignCenter)

        # Connette lo spostamento della barra alla funzione di aggiornamento testo
        self.slider.valueChanged.connect(self.aggiorna_etichetta)

        layout.addSpacing(50)

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

    def aggiorna_etichetta(self, valore):
        self.lbl_valore.setText(f"Budget: {valore} €")

from PyQt5.QtGui import QIntValidator # Aggiungi questo in cima al file

# --- SESTA PAGINA (DURATA VIAGGIO) ---
class SestaPagina(QWidget):
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

class FinestraPrincipale(QStackedWidget):
    def __init__(self):
        super().__init__()
        percorso = "D:/INFORMATICA/FOLDER/PYTHON/OOP (program. ad oggetti)/LABORATORIO (Lecci)/LIBRERIE GRAFICHE (PyQt5)/PROGETTO (gruppo2)/sfondo_app.png"
        self.setStyleSheet(f"FinestraPrincipale {{ border-image: url('{percorso}') 0 0 0 0 stretch stretch; }}")

        # Inizializzazione pagine con i callback corretti
        self.pag1 = PaginaIniziale(self.vai_a_pag2)
        self.pag2 = SecondaPagina(self.vai_a_pag1, self.vai_a_pag3)
        self.pag3 = TerzaPagina(self.vai_a_pag2, self.vai_a_pag4)
        self.pag4 = QuartaPagina(self.vai_a_pag3, self.vai_a_pag5)
        self.pag5 = QuintaPagina(self.vai_a_pag4, self.vai_a_pag6)
        self.pag6 = SestaPagina(self.vai_a_pag5, self.vai_a_pag7)
        self.pag7 = QWidget() # Pagina finale placeholder

        # Aggiunta dei widget allo Stack
        self.addWidget(self.pag1) # Index 0
        self.addWidget(self.pag2) # Index 1
        self.addWidget(self.pag3) # Index 2
        self.addWidget(self.pag4) # Index 3
        self.addWidget(self.pag5) # Index 4
        self.addWidget(self.pag6) # Index 5
        self.addWidget(self.pag7) # Index 6

    # Metodi di navigazione
    def vai_a_pag1(self): 
        self.setCurrentIndex(0)

    def vai_a_pag2(self): 
        self.setCurrentIndex(1)

    def vai_a_pag3(self):
        nome = self.pag2.input_nome.text()
        if nome.strip() == "":
            QMessageBox.warning(self, "Errore", "Per continuare inserisci il nome!")
            return
        self.pag3.aggiorna_nome(nome)
        self.setCurrentIndex(2)

    def vai_a_pag4(self): 
        self.setCurrentIndex(3)

    def vai_a_pag5(self): 
        self.setCurrentIndex(4)

    def vai_a_pag6(self): 
        self.setCurrentIndex(5)

    def vai_a_pag7(self):
        # Controllo input giorni della pagina 6
        if self.pag6.input_giorni.text().strip() == "":
            QMessageBox.warning(self, "Errore", "Inserisci il numero di giorni!")
            return
        self.setCurrentIndex(6)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = FinestraPrincipale()
    finestra.showFullScreen()  # FULLSCREEN
    sys.exit(app.exec_())
