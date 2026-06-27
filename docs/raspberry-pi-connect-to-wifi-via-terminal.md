# Raspberry Pi Connect to Wifi Via Terminal
If you do not see either of these symbols in the top right of your Raspberry Pi's screen:

![The wifi symbol](./public/raspberry-pi-setup/wifi-symbol.png)  
![The ethernet symbol](./public/raspberry-pi-setup/ethernet-symbol.png)

Then follow these instructions:

1. Open the terminal  
   ![Terminal symbol](./public/raspberry-pi-setup/terminal-symbol.png)
2. Type the following then hit enter:
   ```bash
   sudo raspi-config
   ```
   - This will open a menu where you will be able to configure the wifi
   - Use arrow keys to navigate between options
   - Hit enter to select an option
3. Select the "System Options" menu item and hit enter  
   ![raspi-config system options menu](./public/raspberry-pi-setup/raspi-config-system-options.png)
4. Select the "Wireless LAN" menu item and hit enter  
   ![raspi-config wireless lan menu](./public/raspberry-pi-setup/raspi-config-wireless-lan.png)
5. Type in the name of your Wifi network  
   ![raspi-config wireless lan ssid menu](./public/raspberry-pi-setup/raspi-config-wireless-lan-ssid.png)
   - Be careful to type it in exactly correct (capitalization and spaces matter)
   - Double check the name of the Wifi on your phone or computer to make sure you entered the name correctly
   - Hit enter
6. Type in the password to the Wifi then hit enter, if there is no password leave this empty and hit enter  
   ![raspi-config wireless lan password menu](./public/raspberry-pi-setup/raspi-config-wireless-lan-password.png)
7. Once you hit enter the Raspberry Pi should connect to the Wifi, if you see an error then call over an instructor

You can now go back to the other setup guide and continue where you left off.
