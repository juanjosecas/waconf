#!/bin/bash

# Function to list all connected screens, their number, and if they are primary
list_all_screens() {
    echo "Connected screens:"
    screens=$(xrandr | grep ' connected' | nl)
    echo "$screens"
}

# Function to identify the primary screen
identify_primary_screen() {
    primary_screen=$(xrandr | grep 'primary' | awk '{print $1}')
    echo "Primary screen: $primary_screen"
}

# Function to list Wacom devices
list_wacom_devices() {
    echo "Wacom devices:"
    xinput | grep -i Wacom
}

# Function to map a Wacom device to a selected screen
map_wacom_to_screen() {
    echo "Enter the ID of the Wacom device you want to map:"
    read wacom_id
    echo "Select the screen number to which you want to map the Wacom device:"
    list_all_screens
    read screen_number
    screen=$(xrandr | grep ' connected' | awk 'NR=='"$screen_number"'{print $1}')
    if [ -n "$screen" ]; then
        xinput map-to-output "$wacom_id" "$screen"
        echo "Wacom device mapped to screen $screen."
    else
        echo "Invalid screen number. Please try again."
    fi
}

# Print the list of screens and Wacom devices at startup
list_all_screens
list_wacom_devices

# Main menu
while true; do
    clear
    echo "Wacom Tablet Configuration Menu on Ubuntu Linux"
    echo "1. List Connected Screens"
    echo "2. List Wacom Devices"
    echo "3. Map Wacom Device to a Screen"
    echo "4. Exit (you can also press 'q')"
    echo -n "Select an option: "
    read choice

    case $choice in
        1)
            list_all_screens
            ;;
        2)
            list_wacom_devices
            ;;
        3)
            list_all_screens
            list_wacom_devices
            map_wacom_to_screen
            ;;
        4|q|Q)
            echo "Exiting the script."
            exit 0
            ;;
        *)
            echo "Invalid option. Please select a valid option."
            ;;
    esac

    echo -n "Press Enter to continue..."
    read enter_key
done
