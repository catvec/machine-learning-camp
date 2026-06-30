# Raspberry Pi
To setup the Raspberry Pi for this curriculum follow these instructions.

These instructions are for Raspberry Pi 4B devices running Raspberry Pi OS (Debian Trixie based).

# Information
After finishing students should be able to connect to their Raspberry Pi using the information:

- **Hostname:** `raspberrypi`  
- **Username:** `pi`
- **Password:** `password`

Services:

- Ethernet (port `22`)
- TTYD HTTP terminal (port `7681`)
  - Use the `rz` command to send files from your browser to the Raspberry Pi
  - Use the `sz` command to download files from your Raspberry Pi to your browser
- VNC (port `5900`)
- Jupyter Lab (port `8999`)

Access methods:

- Direct connect (Ethernet) on the `raspberrypi.local` domain
- Over the device's IP on Wifi

# Setup ISO
- In RPI imager
  - Set hostname to `raspberrypi`
  - Set username to `pi`
  - Set password to `password`
  - No Wifi setup
  - Enable SSH
- Initial network and access setup  
  Access shell via ssh.
  - Enable wifi
    ```bash
    sudo nmcli radio wifi on
    ```
  - Configure via `raspi-config`
    ```bash
    sudo raspi-config
    ```
    - Configure WiFi  
      System Options > Wireless LAN: then enter SID and password
    - Enable VNC  
      Interface Options > VNC > Yes
- Development environment setup  
  Access via VNC.
  - Update and upgrade:
    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade -y
    ```
  - Install uv:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
  - Install Avahi service configuration files
    - Copy the files to the Raspberry Pi  
      (Run on your computer)
      ```bash
      rsync -r ./files/avahi-services pi@$PI_IP:/home/pi/Downloads
      ```
    - Install the files  
      (Run on the Raspberry Pi)  
      ```bash
      sudo mv ~/Downloads/avahi-services/*.service /etc/avahi/services/
      sudo systemctl restart avahi-daemon
      rm -rf ~/Downloads/avahi-services
      ```
  - Install [ttyd](https://github.com/tsl0922/ttyd) (web terminal)
    - Download:
      ```bash
      curl -L https://github.com/tsl0922/ttyd/releases/download/1.7.7/ttyd.aarch64 -o ~/Downloads/ttyd
      sudo mv ~/Downloads/ttyd /usr/local/bin/
      chmod +x /usr/local/bin/ttyd
      ```
    - Add systemd service:  
      ([Source](https://github.com/tsl0922/ttyd/wiki/Systemd-service))
      - Upload the [`files/ttyd.service`](./files/ttyd.service) file via rsync:  
        (On the host machine run)
        ```bash
        rsync ./files/ttyd.service pi@$PI_IP:/home/pi/Downloads
        ```
      - Move the service to the correct place:  
        (On the Raspberry Pi run)
        ```bash
        sudo mv ~/Downloads/ttyd.service /etc/systemd/system/
        ```
      - Enable and start:  
        (On the Raspberry Pi run)
        ```bash
        sudo systemctl enable --now ttyd
        ```
      - Note: ttyd does not work with the `login` command on newer versions of Debian
        - This is due to `login` now not allowing recursive logins
        - [GitHub Issue](https://github.com/tsl0922/ttyd/issues/1489)
      - Install file transfer tools:  
        (On the Raspberry Pi run)
        - Based on the zmodem protocol (serial)
          ```bash
          sudo apt-get install -y lrzsz
          ```
        - trzsz (modern):
          > Not usable unless accessing ttyd over https or localhost
          > ```bash
          > ssh -L 7681:localhost:7681 pi@$PI_IP
          > ```
          ```bash
          curl -s 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7074ce75da7cc691c1ae1a7c7e51d1ad956055ca' \
              | sudo gpg --dearmor -o /usr/share/keyrings/trzsz.gpg
          echo 'deb [signed-by=/usr/share/keyrings/trzsz.gpg] https://ppa.launchpadcontent.net/trzsz/ppa/ubuntu jammy main' \
              | sudo tee /etc/apt/sources.list.d/trzsz.list
          sudo apt-get update

          sudo apt install -y trzsz
          ```
  - Setup Jupyter Lab
    - Copy [`files/notebooks/`](./files/notebooks/) to `~/Documents/notebooks` on the Raspberry Pi:  
      (Run on your computer)
      ```bash
      rsync -r ./files/notebooks/ pi@$PI_IP:/home/pi/Documents/notebooks
      ```
    - Setup the Python virtual environment:  
      (Run on the Raspberry Pi)
      ```bash
      cd ~/Documents/notebooks
      sudo apt-get install -y libcap-dev libcamera-dev
      uv venv --python /usr/bin/python3 --system-site-packages
      uv sync
      ```      
    - Install the Systemd service:  
      (Run on the Raspberry Pi)
      ```bash
      sudo mv ~/Documents/notebooks/jupyterlab.service /etc/systemd/system/
      chmod +x ~/Documents/notebooks/notebook-server.sh
      sudo systemctl enable --now jupyterlab
      ```
  - Install Braincraft HAT display driver:
    - Copy the files to the Raspberry Pi
      (Run on your computer)
      ```bash
      rsync -r ./files/display-driver-install/ pi@$PI_IP:/home/pi/Downloads/display-driver-install
      ```
    - Install the driver and cleanup
      (Run on the Raspberry Pi)
      ```bash
      sudo mv ~/Downloads/display-driver-install /opt/display-driver
      sudo chown -R pi:pi /opt/display-driver
      cd /opt/display-driver
      uv sync
      chmod +x ./install.sh
      ./install.sh
      ```
      When the script asks you if you want to reboot answer `y`
  - Configure a headless display so VNC resolution isn't the resolution of the Braincraft HAT display
    - Copy the files to the Raspberry Pi
      (Run on your computer)
      ```bash
      rsync ./files/labwc-* pi@raspberrypi.local:/home/pi/Downloads
      ```
    - Move the file to the correct location
      (Run on the Raspberry Pi)
      ```bash
      mv ~/Downloads/labwc-environment ~/.config/labwc/environment
      mv ~/Downloads/labwc-rx.xml ~/.config/labwc/rc.xml
      ```
  
# Troubleshooting
- On linux if keeps disconnecting set Network Manager
  - IPv4 disabled
  - IPv6 link local
- If internet keeps droppping out on ethernet: Make sure the physical connection is secure (click sound on each side)
- If Avahi services aren't being discovered run `avahi-discover` on your computer then try again
