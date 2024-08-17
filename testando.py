import sys
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout


class WidgetLindo(QWidget):
  def __init__(self):
    super().__init__()

    self.oi = ["oi mundinho", "hi little world", "hola mundito", "こんにちは、小さな世界"]

    self.botao = QPushButton("me clica pfv nunca te pedi nada")
    self.texto = QLabel("oi mundinho")
    self.texto.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.linlayout = QVBoxLayout(self)
