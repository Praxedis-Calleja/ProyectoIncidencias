import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Clase principal
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prueba con PyQt6")
        self.setGeometry(100, 100, 300, 200)

        # Botón
        self.boton = QPushButton("Haz clic", self)
        self.boton.move(100, 80)
        self.boton.clicked.connect(self.mostrar_mensaje)

    def mostrar_mensaje(self):
        QMessageBox.information(self, "Mensaje", "¡Has hecho clic!")

# Código para iniciar la app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
