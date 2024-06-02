import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import subprocess

class WacomConfigurator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wacom Tablet Configurator")
        self.setGeometry(100, 100, 600, 700)

        self.selected_device = None
        self.selected_screen = None

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.device_label = QLabel("Wacom devices:")
        layout.addWidget(self.device_label)

        self.device_listbox = QListWidget()
        layout.addWidget(self.device_listbox)
        self.load_wacom_devices()

        self.screen_label = QLabel("Connected screens:")
        layout.addWidget(self.screen_label)

        self.screen_listbox = QListWidget()
        layout.addWidget(self.screen_listbox)
        self.load_screens()

        self.map_button = QPushButton("Map Wacom to Screen", self)
        self.map_button.clicked.connect(self.map_wacom_to_screen)
        layout.addWidget(self.map_button)

        self.quit_button = QPushButton("Exit", self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

    def load_wacom_devices(self):
        devices = self.get_wacom_devices()
        for device in devices:
            self.device_listbox.addItem(device)

    def load_screens(self):
        screens = self.get_screens()
        for screen in screens:
            self.screen_listbox.addItem(screen)

    def get_wacom_devices(self):
        try:
            devices = subprocess.check_output("xinput | grep -i Wacom", shell=True).decode().strip().split('\n')
            return [device for device in devices]
        except subprocess.CalledProcessError:
            QMessageBox.warning(self, "Warning", "No Wacom devices found.")
            return []

    def get_screens(self):
        try:
            screens = subprocess.check_output("xrandr | grep ' connected'", shell=True).decode().strip().split('\n')
            return [screen for screen in screens]
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Error", "Failed to get connected screens.")
            return []

    def map_wacom_to_screen(self):
        selected_device_item = self.device_listbox.currentItem()
        selected_screen_item = self.screen_listbox.currentItem()

        if not selected_device_item or not selected_screen_item:
            QMessageBox.warning(self, "Warning", "Please select both a Wacom device and a screen.")
            return

        selected_device = selected_device_item.text()
        selected_screen = selected_screen_item.text()

        device_id = self.extract_device_id(selected_device)
        screen_name = self.extract_screen_name(selected_screen)

        if device_id and screen_name:
            try:
                subprocess.check_call(f"xinput map-to-output {device_id} {screen_name}", shell=True)
                QMessageBox.information(self, "Success", f"Mapped Wacom device to {screen_name}")
            except subprocess.CalledProcessError:
                QMessageBox.critical(self, "Error", "Failed to map Wacom device to screen")
        else:
            QMessageBox.critical(self, "Error", "Failed to extract device ID or screen name.")

    def extract_device_id(self, device_info):
        try:
            return device_info.split("id=")[1].split()[0]
        except IndexError:
            return None

    def extract_screen_name(self, screen_info):
        try:
            return screen_info.split()[0]
        except IndexError:
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WacomConfigurator()
    window.show()
    sys.exit(app.exec_())
