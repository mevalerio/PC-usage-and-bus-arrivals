# Conky Widget for monitoring PC and bus arrivals

This repository contains a custom Conky widget designed for Linux desktops, providing real-time system information and live bus arrival data for Transport for London (TfL) bus stops.

## Features

*   **System Information:**
    *   Overall CPU Usage
    *   Individual CPU Core Usage (up to 4 cores)
    *   RAM Usage
    *   Disk Usage (for root partition)
    *   Network Download Speed
    *   Network Upload Speed
*   **Live TfL Bus Arrivals:**
    *   Displays upcoming bus arrivals for specified TfL bus stops.
    *   Color-coded arrival times:
        *   **Green:** Less than 5 minutes
        *   **Orange:** Less than 3 minutes
        *   **Red:** Less than 1 minute

## Prerequisites

*   **Conky:** A free, light-weight system monitor for X.
*   **Python 3:** The scripting language used for fetching bus data.
*   **`requests` library:** A Python library for making HTTP requests. Install with `pip install requests`.
*   **TfL API Keys (Optional but Recommended):** For higher request limits, register on the [TfL API Portal](https://api-portal.tfl.gov.uk/) to obtain an `app_id` and `app_key`. The widget currently uses anonymous access, which is limited to 50 requests per minute.

## Installation

1.  **Clone this repository:**
    ```bash
    git clone <repository_url> ~/.config/conky_custom
    ```
    *(Note: It's recommended to clone into a new directory like `conky_custom` to avoid conflicts with existing Conky files. You will then copy the files from here.)*

2.  **Copy Conky files:**
    Copy `conky.conf` and `bus_arrivals.py` to your Conky configuration directory (usually `~/.config/conky/`):
    ```bash
    cp ~/.config/conky_custom/conky.conf ~/.config/conky/
    cp ~/.config/conky_custom/bus_arrivals.py ~/.config/conky/
    ```

3.  **Make the Python script executable:**
    ```bash
    chmod +x ~/.config/conky/bus_arrivals.py
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install requests
    ```

5.  **Update Python executable path (if necessary):**
    The `conky.conf` file currently assumes your Python executable is at `/home/valerio/anaconda3/bin/python`. If yours is different (e.g., `/usr/bin/python3`), you'll need to edit `~/.config/conky/conky.conf` and update the paths for the `execpi` commands:
    ```
    ${execpi 15 /path/to/your/python /home/valerio/.config/conky/bus_arrivals.py 490008927J}
    ${execpi 15 /path/to/your/python /home/valerio/.config/conky/bus_arrivals.py 490008927K}
    ```
    You can find your Python path using `which python` or `which python3`.

## Usage

To start Conky with this configuration, run:
```bash
conky
```
It's often recommended to add Conky to your desktop environment's startup applications for it to launch automatically on login.

## Customization

### Bus Stops
To change or add bus stops, edit `~/.config/conky/conky.conf`.
*   Find the lines starting with `${execpi 15 /home/valerio/anaconda3/bin/python /home/valerio/.config/conky/bus_arrivals.py ...}`.
*   Replace `490008927J` or `490008927K` with your desired TfL StopPoint ID.
*   You can find StopPoint IDs using the TfL API documentation or by searching online for "TfL Naptan ID lookup".
*   Remember to update the display name above the `execpi` line (e.g., `BUS ARRIVALS (My New Stop)`).

### Refresh Rate
The bus arrival data refreshes every 15 seconds. You can change this by modifying the `15` in `${execpi 15 ...}` to your desired interval (in seconds). Be mindful of the TfL API rate limits.

### Colors
The colors for bus arrival times are defined within `bus_arrivals.py`. You can modify the `color_start` assignments to use different Conky color tags (e.g., `${color #RRGGBB}`).

### Font and Size
Edit `~/.config/conky/conky.conf` to change the `font` and `default_color` settings, as well as `minimum_width`, `gap_x`, and `gap_y` to adjust the widget's appearance and position.

## Credits

*   **Conky:** [https://conky.cc/](https://conky.cc/)
*   **Transport for London (TfL) API:** [https://api.tfl.gov.uk/](https://api.tfl.gov.uk/)
