# Wacom Tablet Configurator

## Motivation

In the field of graphic design and digital illustration, Wacom tablets are an essential tool for many artists and creative professionals. However, configuring and managing these devices on Linux systems can be challenging, especially when mapping the tablet to different screens. This project was born out of the need to simplify and automate this process, providing an easy-to-use graphical interface for configuring Wacom devices on Linux environments.

The primary goal is to make Wacom tablet configuration accessible and efficient, allowing users to focus on their creativity without worrying about technical issues.

## Description

`Wacom Tablet Configurator` is available in two versions: a graphical application developed in Python using the `PyQt5` library, and a command-line script written in Bash. Both tools allow users to list and select connected Wacom devices, as well as map these devices to any screen connected to the system. Additionally, the Python version offers options to configure pressure sensitivity, pen buttons, and tablet orientation.

## Features

- **List Wacom Devices**: Displays all Wacom devices connected to the system.
- **List Connected Screens**: Displays all connected screens, indicating which is the primary screen.
- **Map Wacom Devices to Screens**: Allows mapping any Wacom device to any selected screen.
- **Configure Pressure Sensitivity**: (Python version only) Adjusts the pen's pressure sensitivity.
- **Configure Pen Buttons**: (Python version only) Assigns specific functions to the pen buttons.
- **Configure Tablet Orientation**: (Python version only) Defines the tablet's orientation (normal, left, right, inverted).
- **Intuitive Graphical Interface**: (Python version only) Developed with `PyQt5` for a simple and effective user experience.

## Requirements

- Python 3.6 or higher (for the Python version)
- PyQt5 (for the Python version)
- xinput
- xrandr
- xsetwacom

## Installation

### Python Version

1. **Clone the repository**

   ```sh
   git clone https://github.com/your_username/wacom-tablet-configurator.git
   cd wacom-tablet-configurator
   ```

2. **Install the dependencies**

   Ensure you have `pip` installed. Then run:

   ```sh
   pip install PyQt5
   ```

3. **Run the script**

   ```sh
   python wacom_configurator.py
   ```

### Bash Version

1. **Clone the repository**

   ```sh
   git clone https://github.com/your_username/wacom-tablet-configurator.git
   cd wacom-tablet-configurator
   ```

2. **Make the script executable**

   ```sh
   chmod +x wacom_config.sh
   ```

3. **Run the script**

   ```sh
   ./wacom_config.sh
   ```

## Usage

### Python Version

1. **Launch the application**

   Running the script will open a window displaying connected Wacom devices and screens.

2. **Select devices and screens**

   - Select a Wacom device from the list.
   - Select a screen from the list.

3. **Map the device to the screen**

   - Click the "Map Wacom to Screen" button to map the selected device to the selected screen.

4. **Additional configurations**

   - Use the buttons in the interface to configure pressure sensitivity, pen buttons, and tablet orientation.

5. **Exit**

   - You can close the application by clicking the "Exit" button or pressing the `q` key.

### Bash Version

1. **List screens and devices**

   The script will automatically list all connected screens and Wacom devices when started.

2. **Menu options**

   - **1. List Connected Screens**: Displays all connected screens with their numbers and primary status.
   - **2. List Wacom Devices**: Displays all Wacom devices connected to the system.
   - **3. Map Wacom Device to a Screen**: Prompts to select a Wacom device ID and a screen number to map the device to the screen.
   - **4. Exit**: Exits the script. You can also press `q` to exit.

## Contribution

If you wish to contribute to this project, please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thanks to all the developers and the Linux user community who have made tools like `xinput`, `xrandr`, and `xsetwacom` possible. Their tireless work is the foundation upon which projects like this are built.

---

This project was inspired by the need to facilitate the use of Wacom tablets on Linux environments, making technology accessible and functional for all creatives and professionals who rely on these tools.
