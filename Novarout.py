import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QStackedWidget, QLineEdit, QHBoxLayout, QMessageBox
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


class TerzaPagina(QWidget):
    def __init__(self, callback_indietro):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.lbl3 = QLabel("PAGINA 3")
        self.lbl3.setStyleSheet("""
            color: white;
            background-color: rgba(0, 0, 128, 180);
            font-size: 25px;
            font-family: 'Times New Roman';
            padding: 10px;
            border-radius: 10px;
        """)
        layout.addWidget(self.lbl3, alignment=Qt.AlignCenter)

        layout.addSpacing(30)

        btn_back = QPushButton("Torna indietro")
        btn_back.setFixedSize(200, 40)
        btn_back.setStyleSheet("background-color: white; border-radius: 10px;")
        btn_back.clicked.connect(callback_indietro)
        layout.addWidget(btn_back, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def aggiorna_nome(self, nome):
        self.lbl3.setText(f"Ciao {nome}! Scegli la tua meta ✈️")


class FinestraPrincipale(QStackedWidget):
    def __init__(self):
        super().__init__()

        # SFONDO GLOBALE FULLSCREEN
        self.setStyleSheet("""
            QStackedWidget {
                border-image: url("D:\\INFORMATICA\\FOLDER\\PYTHON\\OOP (program. ad oggetti)\\LABORATORIO (Lecci)\\LIBRERIE GRAFICHE (PyQt5)\\PROGETTO (gruppo2)\\sfondo_app.png") 0 0 0 0 stretch stretch;
            }
        """)

        self.pag1 = PaginaIniziale(self.vai_a_pag2)
        self.pag2 = SecondaPagina(self.vai_a_pag1, self.vai_a_pag3)
        self.pag3 = TerzaPagina(self.vai_a_pag2)

        self.addWidget(self.pag1)
        self.addWidget(self.pag2)
        self.addWidget(self.pag3)

        self.setWindowTitle("App Viaggio")

    def vai_a_pag1(self):
        self.setCurrentIndex(0)

    def vai_a_pag2(self):
        self.setCurrentIndex(1)
    
    def vai_a_pag3(self):
        nome = self.pag2.input_nome.text()

        if nome.strip() == "":
            QMessageBox.warning(self, "Errore", "Inserisci il nome prima di continuare!")
            return

        self.pag3.aggiorna_nome(nome)
        self.setCurrentIndex(2)

    # ESC per uscire dal fullscreen
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = FinestraPrincipale()
    finestra.showFullScreen()  # FULLSCREEN
    sys.exit(app.exec_())
