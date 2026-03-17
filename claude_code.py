import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QStackedWidget, QSlider, QCheckBox,
    QComboBox, QSpinBox, QButtonGroup, QRadioButton, QFrame,
    QScrollArea, QGraphicsDropShadowEffect, QProgressBar
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, pyqtSignal, QRect
from PyQt5.QtGui import (
    QFont, QColor, QPalette, QLinearGradient, QPainter,
    QBrush, QPen, QPixmap, QIcon, QRadialGradient
)


# ─────────────────────────────────────────────
#  DATI DESTINAZIONI
# ─────────────────────────────────────────────

DESTINATIONS = [
    {
        "name": "Giappone – Tokyo & Kyoto",
        "emoji": "🗾",
        "flag": "🇯🇵",
        "country": "Giappone",
        "continent": "Asia",
        "climate": ["temperato", "quattro_stagioni"],
        "travel_types": ["cultura", "gastronomia", "avventura", "relax"],
        "budget": "medio_alto",  # medio, medio_alto, alto
        "best_months": [3, 4, 10, 11],
        "min_age": 0,
        "group_types": ["coppia", "famiglia", "amici", "solo"],
        "geopolitical_safety": 5,  # 1-5, 5 = sicurissimo
        "description": "Il contrasto perfetto tra tradizione millenaria e futuro ipertecnologico. Templi zen, sushi di qualità ineguagliabile, boschi di bambù e neon accecanti.",
        "highlights": ["Fushimi Inari", "Shibuya Crossing", "Monte Fuji", "Arashiyama"],
        "tips": "Primavera (sakura) e autunno (koyo) sono le stagioni più belle. Acquista un JR Pass prima di partire.",
    },
    {
        "name": "Islanda – Terra di fuoco e ghiaccio",
        "emoji": "🏔️",
        "flag": "🇮🇸",
        "country": "Islanda",
        "continent": "Europa",
        "climate": ["freddo", "artico"],
        "travel_types": ["avventura", "natura", "fotografia"],
        "budget": "alto",
        "best_months": [6, 7, 8, 12, 1, 2],
        "min_age": 10,
        "group_types": ["coppia", "amici", "solo"],
        "geopolitical_safety": 5,
        "description": "Geyser, aurore boreali, vulcani attivi e lagune glaciali. Un pianeta alieno accessibile in aereo.",
        "highlights": ["Aurora Boreale", "Golden Circle", "Laguna Glaciale Jökulsárlón", "Geyser Strokkur"],
        "tips": "In inverno cerca le aurore. In estate goditi il sole di mezzanotte e le strade aperte. Noleggia un'auto 4x4.",
    },
    {
        "name": "Marocco – Marrakech & Sahara",
        "emoji": "🏜️",
        "flag": "🇲🇦",
        "country": "Marocco",
        "continent": "Africa",
        "climate": ["caldo", "desertico"],
        "travel_types": ["cultura", "avventura", "gastronomia", "relax"],
        "budget": "basso",
        "best_months": [3, 4, 5, 10, 11],
        "min_age": 0,
        "group_types": ["coppia", "famiglia", "amici", "solo"],
        "geopolitical_safety": 3,
        "description": "Medine labirintiche, dune infinite nel Sahara, riad lussuosi nascosti dietro porte in legno intagliato.",
        "highlights": ["Jemaa el-Fna", "Dune di Erg Chebbi", "Chefchaouen", "Souk di Fes"],
        "tips": "Evita luglio e agosto per il caldo estremo. Contratta sempre al souk ed esplora il deserto in cammello.",
    },
    {
        "name": "Nuova Zelanda – Il Signore degli Anelli",
        "emoji": "🌿",
        "flag": "🇳🇿",
        "country": "Nuova Zelanda",
        "continent": "Oceania",
        "climate": ["temperato", "oceano"],
        "travel_types": ["avventura", "natura", "sport_estremi"],
        "budget": "alto",
        "best_months": [12, 1, 2, 3],
        "min_age": 5,
        "group_types": ["coppia", "amici", "solo"],
        "geopolitical_safety": 5,
        "description": "Fiordi mozzafiato, vulcani attivi, bungy jumping, paesaggi tolkieniani. La meta perfetta per chi ama l'avventura pura.",
        "highlights": ["Milford Sound", "Rotorua", "Queenstown", "Abel Tasman NP"],
        "tips": "Noleggia un camper e percorri la Great Ocean Road. Prenota i tour d'avventura a Queenstown con anticipo.",
    },
    {
        "name": "Portogallo – Lisbona & Algarve",
        "emoji": "🌊",
        "flag": "🇵🇹",
        "country": "Portogallo",
        "continent": "Europa",
        "climate": ["mediterraneo", "temperato"],
        "travel_types": ["cultura", "relax", "gastronomia", "mare"],
        "budget": "basso",
        "best_months": [4, 5, 6, 9, 10],
        "min_age": 0,
        "group_types": ["coppia", "famiglia", "amici", "solo", "anziani"],
        "geopolitical_safety": 5,
        "description": "Tramonto dorati sul Tago, pastel de nata, scogliere dell'Algarve e il Fado nell'aria. L'anima latina più autentica d'Europa.",
        "highlights": ["Belém Tower", "Sintra", "Praia da Marinha", "Porto e il Douro"],
        "tips": "Maggio e settembre sono perfetti: meno folla e prezzi più bassi. Usa il tram 28 a Lisbona.",
    },
    {
        "name": "Costa Rica – Biodiversità pura",
        "emoji": "🦜",
        "flag": "🇨🇷",
        "country": "Costa Rica",
        "continent": "America",
        "climate": ["tropicale", "caldo"],
        "travel_types": ["natura", "avventura", "relax", "sport_estremi"],
        "budget": "medio",
        "best_months": [12, 1, 2, 3, 4],
        "min_age": 3,
        "group_types": ["coppia", "famiglia", "amici"],
        "geopolitical_safety": 4,
        "description": "Vulcani attivi, foreste pluviali, tartarughe marine, surf e zip-line sopra la giungla. Pura Vida!",
        "highlights": ["Arenal Volcano", "Manuel Antonio", "Monteverde Cloud Forest", "Tortuguero"],
        "tips": "La stagione secca (dic-apr) è ideale. Noleggia un SUV per le strade sterrate. 'Pura vida' è sia saluto che filosofia di vita.",
    },
    {
        "name": "Georgia – Il Caucaso nascosto",
        "emoji": "⛪",
        "flag": "🇬🇪",
        "country": "Georgia",
        "continent": "Asia/Europa",
        "climate": ["temperato", "montagna"],
        "travel_types": ["cultura", "avventura", "gastronomia", "natura"],
        "budget": "basso",
        "best_months": [4, 5, 6, 9, 10],
        "min_age": 0,
        "group_types": ["coppia", "amici", "solo"],
        "geopolitical_safety": 3,
        "description": "Chiese millenarie sulle vette del Caucaso, vino naturale nelle anfore di terracotta, ospitalità disarmante e prezzi incredibili.",
        "highlights": ["Tbilisi old town", "Kazbegi", "Vardzia", "Signagi"],
        "tips": "La regione di Svaneti in estate è spettacolare per il trekking. Evita zone vicino al confine con Russia/Ossezia.",
    },
    {
        "name": "Vietnam – Da Nord a Sud",
        "emoji": "🛶",
        "flag": "🇻🇳",
        "country": "Vietnam",
        "continent": "Asia",
        "climate": ["tropicale", "umido"],
        "travel_types": ["cultura", "gastronomia", "avventura", "relax"],
        "budget": "basso",
        "best_months": [11, 12, 1, 2, 3],
        "min_age": 5,
        "group_types": ["coppia", "amici", "solo", "famiglia"],
        "geopolitical_safety": 4,
        "description": "Dalla baia di Halong alle risaie di Mu Cang Chai, passando per Hoi An e i suoi lanternini. Street food leggendario.",
        "highlights": ["Halong Bay", "Hoi An", "Mu Cang Chai", "Phong Nha Caves"],
        "tips": "Il paese è lungo 1650 km: usa i voli interni. I migliori mesi dipendono dalla regione. Il pho a Hanoi al mattino è rituale.",
    },
    {
        "name": "Norvegia – Fiordi & Artico",
        "emoji": "🌌",
        "flag": "🇳🇴",
        "country": "Norvegia",
        "continent": "Europa",
        "climate": ["freddo", "artico", "montagna"],
        "travel_types": ["natura", "avventura", "fotografia"],
        "budget": "alto",
        "best_months": [6, 7, 8, 1, 2],
        "min_age": 5,
        "group_types": ["coppia", "amici", "solo", "famiglia"],
        "geopolitical_safety": 5,
        "description": "Fiordi scolpiti dai ghiacciai, balene, orsi polari nelle Svalbard, aurora boreale e l'estate del sole di mezzanotte.",
        "highlights": ["Geirangerfjord", "Trolltunga", "Lofoten", "Preikestolen"],
        "tips": "In estate goditi i fiordi e il midnight sun. In inverno a Tromsø per le aurore. Molto caro: prenota in anticipo.",
    },
    {
        "name": "Peru – Civiltà Inca",
        "emoji": "🦙",
        "flag": "🇵🇪",
        "country": "Peru",
        "continent": "America",
        "climate": ["montagna", "tropicale"],
        "travel_types": ["cultura", "avventura", "natura", "storia"],
        "budget": "medio",
        "best_months": [5, 6, 7, 8, 9],
        "min_age": 10,
        "group_types": ["coppia", "amici", "solo"],
        "geopolitical_safety": 3,
        "description": "Machu Picchu all'alba nella nebbia, le linee di Nazca, il lago Titicaca e Lima capitale gastronomica del Sud America.",
        "highlights": ["Machu Picchu", "Cusco", "Lago Titicaca", "Amazon Jungle Lodge"],
        "tips": "Acclimatati gradualmente all'altitudine di Cusco (3400m). Il Camino Inca va prenotato mesi prima.",
    },
    {
        "name": "Maldive – Paradiso sull'oceano",
        "emoji": "🏝️",
        "flag": "🇲🇻",
        "country": "Maldive",
        "continent": "Asia",
        "climate": ["tropicale", "caldo"],
        "travel_types": ["relax", "mare", "snorkeling", "lusso"],
        "budget": "alto",
        "best_months": [11, 12, 1, 2, 3, 4],
        "min_age": 0,
        "group_types": ["coppia", "famiglia"],
        "geopolitical_safety": 4,
        "description": "Bungalow sull'acqua turchese, barriera corallina spettacolare, mante e squali balena. Il relax nella sua forma più pura.",
        "highlights": ["Overwater Bungalow", "Snorkeling con mante", "Sunset cruise", "Bioluminescenza"],
        "tips": "Scegli isole locali per risparmiare. La stagione secca (nov-apr) garantisce acque cristalline. Ottimo per la luna di miele.",
    },
    {
        "name": "Colombia – Medellín & Cartagena",
        "emoji": "🌺",
        "flag": "🇨🇴",
        "country": "Colombia",
        "continent": "America",
        "climate": ["tropicale", "caldo"],
        "travel_types": ["cultura", "avventura", "gastronomia", "natura"],
        "budget": "basso",
        "best_months": [12, 1, 2, 3, 7, 8],
        "min_age": 16,
        "group_types": ["coppia", "amici", "solo"],
        "geopolitical_safety": 3,
        "description": "Da città più pericolosa del mondo a meta trendy: Medellín ti stupirà. Cartagena coloniale, caffè nelle montagne, danza ovunque.",
        "highlights": ["Cartagena old town", "Valle del Cocora", "Ciudad Perdida", "Coffee Region"],
        "tips": "Evita zone remote di notte. Medellín è sicura nei quartieri turistici. Il caffè colombiano è il migliore al mondo.",
    },
]

MONTH_NAMES = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu",
               "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]

# ─────────────────────────────────────────────
#  STILE GLOBALE
# ─────────────────────────────────────────────

STYLE = """
QWidget {
    background-color: #0d1117;
    color: #e6edf3;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QLabel {
    background: transparent;
}
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #238636, stop:1 #1a7f37);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 28px;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 0.5px;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #2ea043, stop:1 #238636);
}
QPushButton:pressed {
    background: #1a7f37;
}
QPushButton#btnBack {
    background: #21262d;
    color: #8b949e;
    border: 1px solid #30363d;
}
QPushButton#btnBack:hover {
    background: #30363d;
    color: #e6edf3;
}
QPushButton#btnRestart {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #1f6feb, stop:1 #388bfd);
    color: white;
}
QPushButton#btnRestart:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #388bfd, stop:1 #58a6ff);
}
QSlider::groove:horizontal {
    height: 6px;
    background: #21262d;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #238636;
    border: 2px solid #2ea043;
    width: 20px;
    height: 20px;
    border-radius: 10px;
    margin: -7px 0;
}
QSlider::sub-page:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1f6feb, stop:1 #238636);
    border-radius: 3px;
}
QCheckBox {
    spacing: 10px;
    font-size: 13px;
    color: #c9d1d9;
    padding: 4px;
}
QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border-radius: 6px;
    border: 2px solid #30363d;
    background: #21262d;
}
QCheckBox::indicator:checked {
    background: #238636;
    border-color: #2ea043;
    image: none;
}
QCheckBox::indicator:hover {
    border-color: #58a6ff;
}
QRadioButton {
    spacing: 10px;
    font-size: 13px;
    color: #c9d1d9;
    padding: 4px;
}
QRadioButton::indicator {
    width: 20px;
    height: 20px;
    border-radius: 10px;
    border: 2px solid #30363d;
    background: #21262d;
}
QRadioButton::indicator:checked {
    background: #1f6feb;
    border-color: #388bfd;
}
QComboBox {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 13px;
    color: #c9d1d9;
    min-width: 200px;
}
QComboBox:hover {
    border-color: #58a6ff;
}
QComboBox::drop-down {
    border: none;
    width: 30px;
}
QComboBox QAbstractItemView {
    background: #161b22;
    border: 1px solid #30363d;
    selection-background-color: #1f6feb;
    color: #c9d1d9;
}
QSpinBox {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 13px;
    color: #c9d1d9;
    min-width: 80px;
}
QSpinBox:hover {
    border-color: #58a6ff;
}
QScrollArea {
    border: none;
    background: transparent;
}
QScrollBar:vertical {
    background: #0d1117;
    width: 8px;
    border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #30363d;
    border-radius: 4px;
    min-height: 30px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QProgressBar {
    background: #21262d;
    border-radius: 4px;
    height: 6px;
    text-align: center;
    font-size: 0px;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1f6feb, stop:1 #238636);
    border-radius: 4px;
}
"""


def card_style(radius=16, bg="#161b22", border="#30363d"):
    return f"""
        background: {bg};
        border: 1px solid {border};
        border-radius: {radius}px;
        padding: 20px;
    """


# ─────────────────────────────────────────────
#  WIDGET HELPERS
# ─────────────────────────────────────────────

class SectionTitle(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.setStyleSheet("color: #58a6ff; letter-spacing: 1px; margin-bottom: 4px;")


class QuestionLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.setWordWrap(True)
        self.setStyleSheet("color: #e6edf3; margin-bottom: 8px;")


class HintLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Segoe UI", 11))
        self.setWordWrap(True)
        self.setStyleSheet("color: #8b949e; margin-bottom: 16px;")


class Divider(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setStyleSheet("color: #21262d; background: #21262d; border: none; max-height: 1px;")


class OptionCard(QWidget):
    """Clickable card per opzioni tipo 'tipo viaggio'."""
    clicked = pyqtSignal(str)

    def __init__(self, value, emoji, label, parent=None):
        super().__init__(parent)
        self.value = value
        self.selected = False
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(130, 90)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(4)

        emoji_lbl = QLabel(emoji)
        emoji_lbl.setFont(QFont("Segoe UI", 24))
        emoji_lbl.setAlignment(Qt.AlignCenter)
        emoji_lbl.setStyleSheet("background: transparent;")

        text_lbl = QLabel(label)
        text_lbl.setFont(QFont("Segoe UI", 10, QFont.Bold))
        text_lbl.setAlignment(Qt.AlignCenter)
        text_lbl.setWordWrap(True)
        text_lbl.setStyleSheet("background: transparent; color: #c9d1d9;")

        layout.addWidget(emoji_lbl)
        layout.addWidget(text_lbl)
        self._update_style()

    def _update_style(self):
        if self.selected:
            self.setStyleSheet("""
                background: #1f3a5f;
                border: 2px solid #388bfd;
                border-radius: 12px;
            """)
        else:
            self.setStyleSheet("""
                background: #161b22;
                border: 2px solid #30363d;
                border-radius: 12px;
            """)

    def mousePressEvent(self, event):
        self.selected = not self.selected
        self._update_style()
        self.clicked.emit(self.value)


# ─────────────────────────────────────────────
#  PAGINE WIZARD
# ─────────────────────────────────────────────

class WelcomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(60, 40, 60, 40)

        globe = QLabel("🌍")
        globe.setFont(QFont("Segoe UI", 80))
        globe.setAlignment(Qt.AlignCenter)
        globe.setStyleSheet("background: transparent;")

        title = QLabel("Dove vuoi andare?")
        title.setFont(QFont("Segoe UI", 32, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #e6edf3; background: transparent;")

        subtitle = QLabel(
            "Rispondi ad alcune domande e ti troveremo\n"
            "la destinazione perfetta nel mondo 🗺️"
        )
        subtitle.setFont(QFont("Segoe UI", 14))
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color: #8b949e; background: transparent;")

        geopolitical_badge = QLabel("✅  Situazione geopolitica sempre aggiornata")
        geopolitical_badge.setFont(QFont("Segoe UI", 11))
        geopolitical_badge.setAlignment(Qt.AlignCenter)
        geopolitical_badge.setStyleSheet("""
            background: #1a3a2a;
            color: #3fb950;
            border: 1px solid #238636;
            border-radius: 20px;
            padding: 6px 18px;
        """)

        layout.addStretch()
        layout.addWidget(globe)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(10)
        layout.addWidget(geopolitical_badge, 0, Qt.AlignCenter)
        layout.addStretch()


class BudgetPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.answer = "medio"

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(16)

        layout.addWidget(SectionTitle("PASSO 1 DI 6"))
        layout.addWidget(QuestionLabel("Qual è il tuo budget per persona?"))
        layout.addWidget(HintLabel("Considera volo + alloggio + spese per circa 10 giorni."))
        layout.addWidget(Divider())

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(2)
        self.slider.setValue(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self._on_change)

        slider_labels = QHBoxLayout()
        for lbl in ["💰 Economico\n(< 1.000€)", "💳 Medio\n(1-2.500€)", "💎 Premium\n(> 2.500€)"]:
            l = QLabel(lbl)
            l.setAlignment(Qt.AlignCenter)
            l.setFont(QFont("Segoe UI", 10))
            l.setWordWrap(True)
            l.setStyleSheet("color: #8b949e; background: transparent;")
            slider_labels.addWidget(l)

        self.value_label = QLabel("💳  Budget Medio  (1.000 – 2.500€)")
        self.value_label.setFont(QFont("Segoe UI", 15, QFont.Bold))
        self.value_label.setAlignment(Qt.AlignCenter)
        self.value_label.setStyleSheet("""
            background: #1f2d3d;
            color: #58a6ff;
            border: 1px solid #1f6feb;
            border-radius: 12px;
            padding: 14px;
            margin-top: 10px;
        """)

        layout.addWidget(self.slider)
        layout.addLayout(slider_labels)
        layout.addWidget(self.value_label)
        layout.addStretch()

    def _on_change(self, v):
        labels = ["basso", "medio", "medio_alto"]
        descs = [
            "💰  Budget Economico  (< 1.000€)",
            "💳  Budget Medio  (1.000 – 2.500€)",
            "💎  Budget Premium  (> 2.500€)"
        ]
        self.answer = labels[v]
        self.value_label.setText(descs[v])

    def get_answer(self):
        return self.answer


class ClimatePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(12)

        layout.addWidget(SectionTitle("PASSO 2 DI 6"))
        layout.addWidget(QuestionLabel("Che clima preferisci?"))
        layout.addWidget(HintLabel("Puoi selezionare più opzioni."))
        layout.addWidget(Divider())

        options = [
            ("tropicale", "☀️  Tropicale / caldo umido"),
            ("caldo", "🌞  Caldo secco / mediterraneo"),
            ("temperato", "🍂  Temperato / quattro stagioni"),
            ("freddo", "❄️  Freddo / neve"),
            ("artico", "🌌  Artico / aurore boreali"),
            ("montagna", "⛰️  Montagna"),
        ]

        self.checkboxes = {}
        for val, label in options:
            cb = QCheckBox(label)
            cb.setFont(QFont("Segoe UI", 13))
            self.checkboxes[val] = cb
            layout.addWidget(cb)

        layout.addStretch()

    def get_answer(self):
        return [k for k, cb in self.checkboxes.items() if cb.isChecked()]


class TravelTypePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected = set()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(12)

        layout.addWidget(SectionTitle("PASSO 3 DI 6"))
        layout.addWidget(QuestionLabel("Che tipo di viaggio stai cercando?"))
        layout.addWidget(HintLabel("Seleziona tutte le esperienze che desideri."))
        layout.addWidget(Divider())

        options = [
            ("avventura", "🧗", "Avventura"),
            ("relax", "🧘", "Relax"),
            ("cultura", "🏛️", "Cultura"),
            ("natura", "🌿", "Natura"),
            ("gastronomia", "🍜", "Gastronomia"),
            ("mare", "🏖️", "Mare"),
            ("sport_estremi", "🪂", "Sport estremi"),
            ("fotografia", "📷", "Fotografia"),
            ("storia", "📜", "Storia"),
            ("lusso", "✨", "Lusso"),
        ]

        grid = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.cards = []
        for i, (val, emoji, label) in enumerate(options):
            card = OptionCard(val, emoji, label)
            card.clicked.connect(self._toggle)
            self.cards.append(card)
            if i % 2 == 0:
                col1.addWidget(card)
            else:
                col2.addWidget(card)

        grid.addLayout(col1)
        grid.addLayout(col2)
        grid.addStretch()

        scroll_widget = QWidget()
        scroll_widget.setLayout(grid)
        scroll_widget.setStyleSheet("background: transparent;")

        layout.addWidget(scroll_widget)
        layout.addStretch()

    def _toggle(self, value):
        if value in self.selected:
            self.selected.discard(value)
        else:
            self.selected.add(value)

    def get_answer(self):
        return list(self.selected)


class MonthPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(12)

        layout.addWidget(SectionTitle("PASSO 4 DI 6"))
        layout.addWidget(QuestionLabel("Quando vorresti partire?"))
        layout.addWidget(HintLabel("Seleziona il mese o i mesi preferiti."))
        layout.addWidget(Divider())

        months_layout = QHBoxLayout()
        months_layout.setSpacing(8)
        self.month_buttons = {}

        for i, name in enumerate(MONTH_NAMES, start=1):
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.setFixedSize(60, 48)
            btn.setFont(QFont("Segoe UI", 10, QFont.Bold))
            btn.setStyleSheet("""
                QPushButton {
                    background: #21262d;
                    color: #8b949e;
                    border: 1px solid #30363d;
                    border-radius: 8px;
                }
                QPushButton:checked {
                    background: #1f3a5f;
                    color: #58a6ff;
                    border: 2px solid #388bfd;
                }
                QPushButton:hover {
                    border-color: #58a6ff;
                }
            """)
            months_layout.addWidget(btn)
            self.month_buttons[i] = btn

        layout.addLayout(months_layout)
        layout.addStretch()

    def get_answer(self):
        return [m for m, btn in self.month_buttons.items() if btn.isChecked()]


class PeoplePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(16)

        layout.addWidget(SectionTitle("PASSO 5 DI 6"))
        layout.addWidget(QuestionLabel("Chi viaggia con te?"))
        layout.addWidget(Divider())

        # Numero persone
        num_row = QHBoxLayout()
        num_lbl = QLabel("👥  Quante persone?")
        num_lbl.setFont(QFont("Segoe UI", 13))
        num_lbl.setStyleSheet("background: transparent; color: #c9d1d9;")
        self.num_spin = QSpinBox()
        self.num_spin.setMinimum(1)
        self.num_spin.setMaximum(20)
        self.num_spin.setValue(2)
        num_row.addWidget(num_lbl)
        num_row.addWidget(self.num_spin)
        num_row.addStretch()
        layout.addLayout(num_row)

        # Età media
        age_row = QHBoxLayout()
        age_lbl = QLabel("🎂  Età media del gruppo?")
        age_lbl.setFont(QFont("Segoe UI", 13))
        age_lbl.setStyleSheet("background: transparent; color: #c9d1d9;")
        self.age_spin = QSpinBox()
        self.age_spin.setMinimum(1)
        self.age_spin.setMaximum(99)
        self.age_spin.setValue(30)
        self.age_spin.setSuffix(" anni")
        age_row.addWidget(age_lbl)
        age_row.addWidget(self.age_spin)
        age_row.addStretch()
        layout.addLayout(age_row)

        layout.addSpacing(10)
        layout.addWidget(HintLabel("Tipo di gruppo:"))

        group_options = [
            ("coppia", "👫  Coppia"),
            ("famiglia", "👨‍👩‍👧  Famiglia con bambini"),
            ("amici", "🧑‍🤝‍🧑  Gruppo di amici"),
            ("solo", "🧳  Viaggiatore solitario"),
            ("anziani", "👴  Over 65"),
        ]
        self.group_buttons = {}
        for val, label in group_options:
            rb = QRadioButton(label)
            rb.setFont(QFont("Segoe UI", 13))
            self.group_buttons[val] = rb
            layout.addWidget(rb)

        self.group_buttons["coppia"].setChecked(True)
        layout.addStretch()

    def get_answer(self):
        group = next((k for k, rb in self.group_buttons.items() if rb.isChecked()), "coppia")
        return {
            "num_people": self.num_spin.value(),
            "avg_age": self.age_spin.value(),
            "group_type": group,
        }


class PreferencesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(14)

        layout.addWidget(SectionTitle("PASSO 6 DI 6"))
        layout.addWidget(QuestionLabel("Ultime preferenze..."))
        layout.addWidget(HintLabel("Aiutaci a personalizzare al meglio la tua meta."))
        layout.addWidget(Divider())

        # Sicurezza geopolitica
        safe_lbl = QLabel("🛡️  Livello di sicurezza geopolitica richiesto:")
        safe_lbl.setFont(QFont("Segoe UI", 13, QFont.Bold))
        safe_lbl.setStyleSheet("color: #c9d1d9; background: transparent;")
        layout.addWidget(safe_lbl)

        self.safety_slider = QSlider(Qt.Horizontal)
        self.safety_slider.setMinimum(1)
        self.safety_slider.setMaximum(5)
        self.safety_slider.setValue(3)
        self.safety_slider.setTickPosition(QSlider.TicksBelow)
        self.safety_slider.setTickInterval(1)
        self.safety_slider.valueChanged.connect(self._update_safety)

        safety_row = QHBoxLayout()
        for lbl in ["⚠️ Avventuriero", "🟡 Prudente", "🟢 Solo sicuro"]:
            l = QLabel(lbl)
            l.setFont(QFont("Segoe UI", 9))
            l.setAlignment(Qt.AlignCenter)
            l.setStyleSheet("color: #8b949e; background: transparent;")
            safety_row.addWidget(l)

        self.safety_label = QLabel("🟡  Livello medio – evito zone ad alto rischio")
        self.safety_label.setFont(QFont("Segoe UI", 12))
        self.safety_label.setStyleSheet("color: #d29922; background: transparent;")

        layout.addWidget(self.safety_slider)
        layout.addLayout(safety_row)
        layout.addWidget(self.safety_label)

        layout.addSpacing(12)

        # Extra checkbox
        extras = [
            ("no_visto", "📋  Preferisco mete senza visto per italiani"),
            ("accessibile", "♿  Ho bisogno di accessibilità"),
            ("volo_breve", "✈️  Preferisco voli brevi (< 5h da Italia)"),
            ("lingua_facile", "🗣️  Preferisco mete anglofone o con lingue facili"),
        ]
        self.extras = {}
        for val, label in extras:
            cb = QCheckBox(label)
            cb.setFont(QFont("Segoe UI", 12))
            self.extras[val] = cb
            layout.addWidget(cb)

        layout.addStretch()

    def _update_safety(self, v):
        descs = {
            1: "⚠️  Accetto qualsiasi destinazione",
            2: "🟠  Accetto rischi moderati",
            3: "🟡  Evito zone ad alto rischio",
            4: "🟢  Solo mete generalmente sicure",
            5: "✅  Solo mete con massima sicurezza",
        }
        colors = {1: "#f85149", 2: "#d29922", 3: "#d29922", 4: "#3fb950", 5: "#3fb950"}
        self.safety_label.setText(descs[v])
        self.safety_label.setStyleSheet(f"color: {colors[v]}; background: transparent;")

    def get_answer(self):
        return {
            "min_safety": self.safety_slider.value(),
            "extras": [k for k, cb in self.extras.items() if cb.isChecked()],
        }


# ─────────────────────────────────────────────
#  MOTORE DI MATCHING
# ─────────────────────────────────────────────

def compute_score(dest, answers):
    score = 0

    # Budget
    budget_map = {"basso": 0, "medio": 1, "medio_alto": 2, "alto": 2}
    user_budget = {"basso": 0, "medio": 1, "medio_alto": 2}
    dest_budget_num = budget_map.get(dest["budget"], 1)
    user_budget_num = {"basso": 0, "medio": 1, "medio_alto": 2}.get(answers["budget"], 1)
    if dest_budget_num <= user_budget_num:
        score += 20
    elif dest_budget_num == user_budget_num + 1:
        score += 5

    # Clima
    user_climates = answers.get("climate", [])
    if user_climates:
        matches = sum(1 for c in dest["climate"] if c in user_climates)
        score += matches * 15

    # Tipo viaggio
    user_types = answers.get("travel_types", [])
    if user_types:
        matches = sum(1 for t in dest["travel_types"] if t in user_types)
        score += matches * 12

    # Mese
    user_months = answers.get("months", [])
    if user_months:
        matches = sum(1 for m in dest["best_months"] if m in user_months)
        score += matches * 10

    # Sicurezza geopolitica
    min_safety = answers.get("min_safety", 3)
    if dest["geopolitical_safety"] >= min_safety:
        score += 20
    elif dest["geopolitical_safety"] == min_safety - 1:
        score += 5
    else:
        score -= 30  # Penalità forte

    # Gruppo
    group_type = answers.get("group_type", "coppia")
    if group_type in dest["group_types"]:
        score += 10

    # Età
    avg_age = answers.get("avg_age", 30)
    if avg_age >= dest["min_age"]:
        score += 5

    # Extra preferences (bonus semplici)
    extras = answers.get("extras", [])
    eu_countries = ["Portogallo", "Norvegia", "Islanda"]
    if "volo_breve" in extras and dest["country"] in eu_countries:
        score += 10
    if "lingua_facile" in extras and dest["country"] in ["Portogallo", "Costa Rica", "Colombia", "Peru", "Maldive"]:
        score += 8

    return score


def find_best_destinations(answers):
    scored = [(compute_score(d, answers), d) for d in DESTINATIONS]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:3]


# ─────────────────────────────────────────────
#  PAGINA RISULTATI
# ─────────────────────────────────────────────

class ResultPage(QWidget):
    restart_requested = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 20, 40, 20)
        self.layout.setSpacing(0)

    def show_results(self, answers):
        # Pulisci layout precedente
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        results = find_best_destinations(answers)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent; border: none;")

        container = QWidget()
        container.setStyleSheet("background: transparent;")
        vbox = QVBoxLayout(container)
        vbox.setSpacing(20)
        vbox.setContentsMargins(0, 0, 0, 20)

        title = QLabel("🎯  Le tue mete perfette")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setStyleSheet("color: #e6edf3; background: transparent; margin-bottom: 4px;")
        vbox.addWidget(title)

        sub = QLabel("Classificate in base alle tue preferenze e alla situazione geopolitica attuale")
        sub.setFont(QFont("Segoe UI", 11))
        sub.setStyleSheet("color: #8b949e; background: transparent; margin-bottom: 12px;")
        vbox.addWidget(sub)

        medals = ["🥇", "🥈", "🥉"]
        borders = ["#d4af37", "#a8a9ad", "#cd7f32"]
        max_score = results[0][0] if results else 1

        for rank, (score, dest) in enumerate(results):
            pct = int((score / max(max_score, 1)) * 100)

            card = QFrame()
            card.setStyleSheet(f"""
                background: #161b22;
                border: 2px solid {borders[rank]};
                border-radius: 16px;
                padding: 0px;
            """)

            card_layout = QVBoxLayout(card)
            card_layout.setSpacing(8)
            card_layout.setContentsMargins(20, 16, 20, 16)

            # Header
            h_row = QHBoxLayout()
            medal = QLabel(f"{medals[rank]} {dest['flag']}  {dest['name']}")
            medal.setFont(QFont("Segoe UI", 16, QFont.Bold))
            medal.setStyleSheet(f"color: {borders[rank]}; background: transparent;")

            match_lbl = QLabel(f"Match: {pct}%")
            match_lbl.setFont(QFont("Segoe UI", 12, QFont.Bold))
            match_lbl.setStyleSheet("color: #3fb950; background: transparent;")

            h_row.addWidget(medal)
            h_row.addStretch()
            h_row.addWidget(match_lbl)
            card_layout.addLayout(h_row)

            # Progress bar match
            pb = QProgressBar()
            pb.setValue(pct)
            pb.setFixedHeight(6)
            card_layout.addWidget(pb)

            # Descrizione
            desc = QLabel(dest["description"])
            desc.setFont(QFont("Segoe UI", 12))
            desc.setWordWrap(True)
            desc.setStyleSheet("color: #c9d1d9; background: transparent; margin-top: 6px;")
            card_layout.addWidget(desc)

            # Highlights
            h_label = QLabel("📍 " + "  •  ".join(dest["highlights"]))
            h_label.setFont(QFont("Segoe UI", 10))
            h_label.setWordWrap(True)
            h_label.setStyleSheet("color: #58a6ff; background: transparent;")
            card_layout.addWidget(h_label)

            # Safety badge
            safety = dest["geopolitical_safety"]
            safety_colors = {1: "#f85149", 2: "#e3b341", 3: "#d29922", 4: "#3fb950", 5: "#3fb950"}
            safety_texts = {1: "⛔ Alto rischio", 2: "🟠 Rischio moderato",
                            3: "🟡 Attenzione", 4: "🟢 Sicuro", 5: "✅ Molto sicuro"}
            safety_badge = QLabel(f"  {safety_texts[safety]}  ")
            safety_badge.setFont(QFont("Segoe UI", 10, QFont.Bold))
            safety_badge.setStyleSheet(f"""
                background: transparent;
                color: {safety_colors[safety]};
                border: 1px solid {safety_colors[safety]};
                border-radius: 10px;
                padding: 3px 10px;
            """)

            # Budget badge
            budget_texts = {"basso": "💰 Economico", "medio": "💳 Medio",
                            "medio_alto": "💳 Medio-Alto", "alto": "💎 Premium"}
            budget_badge = QLabel(f"  {budget_texts.get(dest['budget'], '💳 Medio')}  ")
            budget_badge.setFont(QFont("Segoe UI", 10, QFont.Bold))
            budget_badge.setStyleSheet("""
                background: transparent;
                color: #58a6ff;
                border: 1px solid #1f6feb;
                border-radius: 10px;
                padding: 3px 10px;
            """)

            badges_row = QHBoxLayout()
            badges_row.addWidget(safety_badge)
            badges_row.addWidget(budget_badge)
            badges_row.addStretch()
            card_layout.addLayout(badges_row)

            # Tip
            tip_box = QFrame()
            tip_box.setStyleSheet("""
                background: #1a2a1a;
                border: 1px solid #238636;
                border-radius: 8px;
                padding: 8px;
            """)
            tip_layout = QVBoxLayout(tip_box)
            tip_layout.setContentsMargins(10, 6, 10, 6)
            tip_label = QLabel(f"💡 {dest['tips']}")
            tip_label.setFont(QFont("Segoe UI", 10))
            tip_label.setWordWrap(True)
            tip_label.setStyleSheet("color: #3fb950; background: transparent;")
            tip_layout.addWidget(tip_label)
            card_layout.addWidget(tip_box)

            vbox.addWidget(card)

        # Bottone ricomincia
        restart_btn = QPushButton("🔄  Ricomincia con nuove preferenze")
        restart_btn.setObjectName("btnRestart")
        restart_btn.setFont(QFont("Segoe UI", 13, QFont.Bold))
        restart_btn.setFixedHeight(50)
        restart_btn.clicked.connect(self.restart_requested.emit)
        vbox.addWidget(restart_btn)

        scroll.setWidget(container)
        self.layout.addWidget(scroll)


# ─────────────────────────────────────────────
#  FINESTRA PRINCIPALE
# ─────────────────────────────────────────────

class TravelWizard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌍 Travel Wizard – Trova la tua meta perfetta")
        self.setMinimumSize(800, 640)
        self.resize(860, 700)
        self.setStyleSheet(STYLE)

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header
        header = QWidget()
        header.setFixedHeight(56)
        header.setStyleSheet("background: #161b22; border-bottom: 1px solid #21262d;")
        h_layout = QHBoxLayout(header)
        h_layout.setContentsMargins(24, 0, 24, 0)

        brand = QLabel("✈️  Travel Wizard")
        brand.setFont(QFont("Segoe UI", 15, QFont.Bold))
        brand.setStyleSheet("color: #e6edf3; background: transparent;")

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedWidth(300)
        self.progress_bar.setFixedHeight(6)
        self.progress_bar.setValue(0)

        self.step_label = QLabel("Benvenuto")
        self.step_label.setFont(QFont("Segoe UI", 10))
        self.step_label.setStyleSheet("color: #8b949e; background: transparent;")

        h_layout.addWidget(brand)
        h_layout.addStretch()
        h_layout.addWidget(self.step_label)
        h_layout.addSpacing(12)
        h_layout.addWidget(self.progress_bar)

        main_layout.addWidget(header)

        # Stack
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background: #0d1117;")
        main_layout.addWidget(self.stack, 1)

        # Pagine
        self.welcome = WelcomePage()
        self.budget_page = BudgetPage()
        self.climate_page = ClimatePage()
        self.travel_type_page = TravelTypePage()
        self.month_page = MonthPage()
        self.people_page = PeoplePage()
        self.prefs_page = PreferencesPage()
        self.result_page = ResultPage()

        for p in [self.welcome, self.budget_page, self.climate_page,
                  self.travel_type_page, self.month_page, self.people_page,
                  self.prefs_page, self.result_page]:
            self.stack.addWidget(p)

        self.result_page.restart_requested.connect(self.restart)

        # Footer navigazione
        footer = QWidget()
        footer.setFixedHeight(72)
        footer.setStyleSheet("background: #161b22; border-top: 1px solid #21262d;")
        f_layout = QHBoxLayout(footer)
        f_layout.setContentsMargins(24, 12, 24, 12)

        self.btn_back = QPushButton("← Indietro")
        self.btn_back.setObjectName("btnBack")
        self.btn_back.setFixedSize(140, 44)
        self.btn_back.clicked.connect(self.go_back)

        self.btn_next = QPushButton("Inizia il viaggio  →")
        self.btn_next.setFixedSize(200, 44)
        self.btn_next.clicked.connect(self.go_next)

        f_layout.addWidget(self.btn_back)
        f_layout.addStretch()
        f_layout.addWidget(self.btn_next)

        main_layout.addWidget(footer)

        self.current = 0
        self.answers = {}
        self._update_nav()

    # ── pagine step map ──
    PAGES = [
        ("welcome", "Benvenuto", 0),
        ("budget", "Budget", 17),
        ("climate", "Clima", 33),
        ("travel_type", "Tipo viaggio", 50),
        ("month", "Periodo", 66),
        ("people", "Gruppo", 83),
        ("prefs", "Preferenze", 100),
    ]

    def _update_nav(self):
        idx = self.current
        is_result = (self.stack.currentWidget() == self.result_page)

        self.btn_back.setVisible(idx > 0 and not is_result)
        self.btn_next.setVisible(not is_result)

        if idx < len(self.PAGES):
            _, name, pct = self.PAGES[idx]
            self.step_label.setText(name)
            self.progress_bar.setValue(pct)

        if idx == 0:
            self.btn_next.setText("Inizia il viaggio  →")
        elif idx == len(self.PAGES) - 1:
            self.btn_next.setText("🎯  Trova la mia meta!")
        else:
            self.btn_next.setText("Avanti  →")

    def go_next(self):
        idx = self.current
        pages = [self.welcome, self.budget_page, self.climate_page,
                 self.travel_type_page, self.month_page, self.people_page, self.prefs_page]

        # Salva risposta corrente
        if idx == 1:
            self.answers["budget"] = self.budget_page.get_answer()
        elif idx == 2:
            self.answers["climate"] = self.climate_page.get_answer()
        elif idx == 3:
            self.answers["travel_types"] = self.travel_type_page.get_answer()
        elif idx == 4:
            self.answers["months"] = self.month_page.get_answer()
        elif idx == 5:
            people = self.people_page.get_answer()
            self.answers.update(people)
        elif idx == 6:
            prefs = self.prefs_page.get_answer()
            self.answers.update(prefs)
            # Mostra risultati
            self.result_page.show_results(self.answers)
            self.stack.setCurrentWidget(self.result_page)
            self.progress_bar.setValue(100)
            self.step_label.setText("Risultati 🎉")
            self._update_nav()
            return

        self.current += 1
        self.stack.setCurrentIndex(self.current)
        self._update_nav()

    def go_back(self):
        if self.current > 0:
            self.current -= 1
            self.stack.setCurrentIndex(self.current)
            self._update_nav()

    def restart(self):
        self.current = 0
        self.answers = {}
        self.stack.setCurrentIndex(0)
        self._update_nav()


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Palette dark base
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#0d1117"))
    palette.setColor(QPalette.WindowText, QColor("#e6edf3"))
    palette.setColor(QPalette.Base, QColor("#161b22"))
    palette.setColor(QPalette.AlternateBase, QColor("#21262d"))
    palette.setColor(QPalette.Text, QColor("#c9d1d9"))
    palette.setColor(QPalette.Button, QColor("#21262d"))
    palette.setColor(QPalette.ButtonText, QColor("#e6edf3"))
    palette.setColor(QPalette.Highlight, QColor("#1f6feb"))
    palette.setColor(QPalette.HighlightedText, QColor("white"))
    app.setPalette(palette)

    window = TravelWizard()
    window.show()
    sys.exit(app.exec_())