# Raspberry Pi
To setup the Raspberry Pi for this curriculum follow these instructions.

These instructions are for Raspberry Pi 4B devices running Raspberry Pi OS (Debian Trixie based).

# Information
After finishing students should be able to connect to their Raspberry Pi using the information:

- **Hostname:** `raspberrypi`  
- **Username:** `pi`
- **Password:** `password`

Access:

- Ethernet SSH:
  ```bash
  ssh pi@raspberrypi.local
  ```
- WiFi SSH:
  ```bash
  ssh pi@<ip>
  ```
- Web shell: `<ip>:7681` in your web browser
  - Use the `rz` command to send files from your browser to the Raspberry Pi
  - Use the `sz` command to download files from your Raspberry Pi to your browser

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
  - Install [ttyd](https://github.com/tsl0922/ttyd) (web terminal)
    - Download:
      ```bash
      curl -L https://github.com/tsl0922/ttyd/releases/download/1.7.7/ttyd.aarch64 -o ~/Downloads/ttyd
      sudo mv ~/Downloads/ttyd /usr/local/bin/
      chmod +x /usr/local/bin/ttyd
      ```
    - Add systemd service:  
      ([Source](https://github.com/tsl0922/ttyd/wiki/Systemd-service))
      - Upload the [`config/ttyd.service`](./config/ttyd.service) file via rsync:  
        (On the host machine run)
        ```bash
        rsync ./config/ttyd.service pi@<ip>:/home/pi/Downloads
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
          > Not usable unless accessing ttyd over https
          ```bash
          curl -s 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7074ce75da7cc691c1ae1a7c7e51d1ad956055ca' \
              | sudo gpg --dearmor -o /usr/share/keyrings/trzsz.gpg
          echo 'deb [signed-by=/usr/share/keyrings/trzsz.gpg] https://ppa.launchpadcontent.net/trzsz/ppa/ubuntu jammy main' \
              | sudo tee /etc/apt/sources.list.d/trzsz.list
          sudo apt-get update

          sudo apt install -y trzsz
          ```
    

# Troubleshooting
- On linux if keeps disconnecting set Network Manager
  - IPv4 disabled
  - IPv6 link local
- If internet keeps droppping out on ethernet: Make sure the physical connection is secure (click sound on each side)
