# Raspberry Pi Setup

This guide will help you set up your Raspberry Pi by:

1. [Initial Raspberry Pi Setup](#initial-raspberry-pi-setup)
1. [Connecting to the WiFi](#connect-to-the-wifi)
2. [Install the Camera on the Raspberry Pi](#install-the-camera-on-the-raspberry-pi)
3. [Install the BrainCraft Hat on the Raspberry Pi](#install-the-braincraft-hat-on-the-raspberry-pi)
4. Running your machine learning model on the Raspberry Pi

# Materials
You should have been given 1 of each by instructors:

- [Raspberry Pi 4 B ](https://www.adafruit.com/product/4296) (minimum 4gb RAM)
- [Raspberry Pi Camera Board](https://www.adafruit.com/product/3099)
- [BrainCraft Hat](https://www.adafruit.com/product/4374)
- [2 x 20 Socket Riser Header](https://www.amazon.com/dp/B07PPD25MK?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- 2x 18mm spacers 
- [Power supply compatible with Raspberry Pi 4](https://www.adafruit.com/product/4298)
- [microSD card with adapter 16 GB](https://www.adafruit.com/product/2693)
- [Micro SD Card Reader](https://www.adafruit.com/product/939) (optional)
- [USB C to USB A Adapter](https://www.adafruit.com/product/5030) (optional)

# Initial Raspberry Pi Setup
Before we begin you need to get your Raspberry Pi ready and turn it on:

1. Put the SD card in to the Raspberry Pi's SD card port
   ![Image of Raspberry Pi SD card port](./public/raspberry-pi-setup/insert-sd-card.jpg)  
   _([Image credits](https://researchparent.com/raspberry-pi-computer-building-for-kids/))_
  - Flip your Raspberry Pi over so it is upside-down
  - There should be a metal rectangle on the edge of the board, this is the SD card port
  - Pick up your SD card (being careful to avoid touching the gold parts on the end)
  - Flip it so the gold contacts are facing the Raspberry Pi 
  - Insert the SD card into the SD card port
  - Gently nudge the SD card into the port to make sure it is secure
2. Plug the Raspberry Pi in to power  
  ![Image of Raspberry Pi power port](./public/raspberry-pi-setup/power-port.jpg)  
  - Plug the USB C power cable you have in to the power port indicated by the red arrow in the photo above
  - The red and green LEDs next to the port should turn on and flash every once and a while

# Connect to the Wifi
The first thing we need to do is connect to the Wifi. To do this we need to talk to the Raspberry Pi directly.

1. Install a remote desktop viewer program on your computer:
  - If you are on Windows, Mac, or Linux install [TigerVNC](https://tigervnc.org/)
    - Go to the releases page of the website
    - Find the latest release
    - Follow the link to the "latest binaries"
    - If you are on Windows download the file ending in `.exe`, if you are on Mac download the `.dmg` file
  - If you are on Android or iOS install [MultiVNC](https://github.com/bk138/multivnc)
    - Scroll down to the "How to get it" section on the website
    - Click the button for your platforms app store 
    - Install the app
2. Make sure your Raspberry Pi is turned on
3. Take an Ethernet cord and plug it into your Raspberry Pi and your computer  
   - Be sure the cord is firmly plugged in to both devices!
     - You should hear a click when you plug it in
     - Lights on the Ethernet port of the Raspberry Pi should turn on when the cord is plugged in
4. Wait 2 minutes. The Raspberry Pi has to turn on and get ready
5. Open your remote desktop viewer program (either TigerVNC or MultiVNC)
  - Enter `raspberrypi.local` as the address of the device you wish to connect to
  - The username is `pi`
  - The password is `password`
  - You should now see a desktop with a few icons:
    ![Screenshot of what the Raspberry Pi will look like when you connect](./public/raspberry-pi-setup/vnc-success-login.png)
  - In the top right of your screen there should be one of these symbols:  
    ![The wifi symbol](./public/raspberry-pi-setup/wifi-symbol.png)  
    ![The ethernet symbol](./public/raspberry-pi-setup/ethernet-symbol.png)
    - Click the symbol
      - If you do not see this symbol then follow these [Raspberry Pi Connect to Wifi Via Terminal](./raspberry-pi-connect-to-wifi-via-terminal.md) instructions  
        **Only follow these if you do not see the indicated symbol**
    - Then connect to the Wifi
    - Click the browser icon in the top left of the screen  
      ![Browser icon](./public/raspberry-pi-setup/browser-symbol.png)
    - Ensure you have internet access by going to a website in the browser
6. Get the IP of your raspberry pi
  - Open a terminal  
    ![Terminal symbol](./public/raspberry-pi-setup/terminal-symbol.png)
  - Type the following then hit enter:
    ```bash
    hostname -I
    ```
  - You should see an IP address (a series of numbers separated by dots)  
    ![Image of terminal with IP address](./public/raspberry-pi-setup/hostname-i.png)
  - Write this IP address down somewhere, share it with your teammates as well
  - Any time you see the text: `<IP>` in instructions replace that text with your Raspberry Pi's IP address
7. Disconnect from the Raspberry Pi in your remote desktop viewer program
8. Disconnect the ethernet cable from your computer and the Raspberry Pi
9. Make sure your computer is connected to the same Wifi network that you connected your Raspberry Pi to (Make sure your computer has internet acess on this Wifi network)
10. Reconnect to your Raspberry Pi but this time use the `<IP>` you found
  - It should work the same as before
  - Now that both your computer and the Raspberry Pi are on the same Wifi you can access it using the `<IP>` instead of needing an Ethernet cable 

# Install the Camera on the Raspberry Pi
Before plugging in or unplugging anything always ensure your Raspberry Pi is off and disconnected from power.

## Connect the Fan
Some kits come with the fan already assembled, while some do not have a fan attached yet.

If the fan is attached to your Braincraft HAT then skip this section.

1. Carefully position your Braincraft HAT screen side down
2. Take off the orange hole protector stickers from the board
3. Take your fan from its packaging and connect the wires into the small connector that says FAN: P4
4. The Red wire should face the large black plastic connector
4. Once this is connected position your fan on the middle of the board aligning the holes
5. Position the wire so it is not pinched under the fan, and carefully attach the screws firmly, but not too tight
6. You should be using the screws that _do not_ come with the small nuts (don’t use the nuts)
7. Now your fan should be installed and look like this:  
   ![Image of Braincraft HAT with fan installed](./public/raspberry-pi-setup/braincraft-hat-with-fan.jpg)

## Joystick Cover
Some Braincraft HAT kits come with a plastic joystick cover, check if it is already installed:

If the joystick is installed the front of your Braincraft HAT will look like this:

![Braincraft HAT with joystick cover](./public/raspberry-pi-setup/braincraft-with-joystick-cover.jpg)

If the joystick is not installed the front of your Braincraft HAT will look like this:

![Braincraft HAT no joystick cover](./public/raspberry-pi-setup/braincraft-no-joystick-cover.jpg)

To install the joystick cover simply take the part:

![Braincraft HAT joystick cover](./public/raspberry-pi-setup/braincraft-joystick-cover-alone.jpg)

And press it on to the joystick.

## Spacers
None of these steps should require that much strength or force to complete. If you feel yourself trying really hard to screw something in, then unscrew the item and try again. Encountering a lot of force while screwing in means the part is not aligned properly.

1. Locate the two holes on the Raspberry Pi circuit board on the side opposite from the pins:  
   ![Raspberry pi spacer locations](./public/raspberry-pi-setup/spacers-locations.jpg)
2. Put one spacer in each hole, the pointy side of the spacer that looks like a screw should go through the hole  
   ![Raspberry pi with spacer through hole](./public/raspberry-pi-setup/spacers-hand-position.jpg)
3. Thread a nut on the bottom side of the spacer under the Raspberry Pi board. Tighten it until the nut is touching the circuit board. Do not tighten it too much, you should be able to wiggle and rotate the spacer around  
   ![Raspberry Pi with spacers on bottom](./public/raspberry-pi-setup/spacers-complete-bottom.jpg)
4. Once complete your Raspberry Pi should look like this:  
   ![Raspberry Pi spacers on top](./public/raspberry-pi-setup/spacers-complete-top.jpg)

## Connect the Camera

1. Orient both your Raspberry Pi and Braincraft HAT as shown in this photo:  
   ![Orientation of devices](./public/raspberry-pi-setup/raspberry-pi-and-braincraft-orientation.jpg)
   - The row of pins on the Raspberry Pi should be on the bottom, the USB and Ethernet ports on the left, and the spacers you should put on should be on the top
   - The joystick on the Braincraft HAT should be on the left and the row of ports should be on the top
2. Locate the Camera Module port on the Raspberry Pi  
   ![Diagram showing where camera should be connected to the Raspberry Pi](./public/raspberry-pi-setup/camera-module-port.png)
3. Connect the camera cable  
   ![Animation showing how to connect camera cable](./public/raspberry-pi-setup/connect-camera.gif)
  - Gently pull up on the edges of the port’s plastic clip
  - Insert the Camera Module ribbon cable through the Braincraft HAT camera cable slot:
    ![Image of braincraft hat camera cable slot](./public/raspberry-pi-setup/braincraft-camera-cable-slot.jpg)  
  - Make sure the blue side of the cable is facing the Ethernet ports on the Raspberry Pi (The blue side should face **left**)
  - Insert the cable into the camera slot on the Raspberry Pi
  - Push the black plastic clip back into place firmly, but make sure you’re pressing it down vertically. This part is tricky so be careful!
4. After completing these steps your Raspberry Pi, Braincraft HAT, and camera should look like this:
   ![Image of Raspberry Pi camera attached](./public/raspberry-pi-setup/raspberry-pi-with-camera-and-braincraft-before-attach.jpg)
   
## Attach the Braincraft HAT
Your camera should be attached to the Raspberry Pi, and its cable should be going through the hole in your Braincraft HAT.

1. Carefully align the Braincraft HAT's plastic connector over the pins on your board so the hat is covering the majority of the Raspberry Pi
   ![Pins aligned top down](./public/raspberry-pi-setup/pins-aligned-top-down.jpg)
   ![Pins aligned side](./public/raspberry-pi-setup/pins-aligned-side.jpg)
2. Firmly press down to make sure the components are connected 
  - Be careful to only push straight down, we don't want to bend any pins

Congratulations, your Braincraft board, camera, and fan are installed!
Your hardware should look something like this now:

![Raspberry Pi pin side](./public/raspberry-pi-setup/post-attach-pin-side.jpg)  
![Raspberry Pi spacer side](./public/raspberry-pi-setup/post-attach-spacer-side.jpg)  
![Raspberry Pi top down](./public/raspberry-pi-setup/post-attach-top-down.jpg)

## 4. Connecting and Configuring Braincraft HAT
**IMPORTANT: Please make sure all installation in this section is done so the Python Virtual environment created previously!!!**

### Introduction

_Most of this section is sourced [from this page](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/overview). Visit this tutorial for more info and additional direction._

The idea behind the Adafruit BrainCraft HAT is that you’d be able to “craft brains” for Machine Learning on the EDGE (Edge is a way to refer to small computers like phones or other smaller hardware), with Microcontrollers & Microcomputers. This HAT will let you build a wide range of audio/video AI projects while also allowing easy plug-in of sensors and robotics!

As a part of this section we will also connect the controllable mini fan to the bottom of the hat to keep your Pi cool while doing intense AI inference calculations. Most importantly, there’s an On/Off switch that will completely disable the audio codec, so that when it's off, there’s no way it's listening to you.

We’re not going to go in depth on each component, [but if you want to learn more about the board and its pinouts, check this out.](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/pinouts) The basic features are as follows:

- 1.54" IPS TFT display with 240x240 resolution that can show text or video
- Stereo speaker ports for audio playback - either text-to-speech, alerts or for creating a voice assistant.
- Stereo headphone out for audio playback through a stereo system, headphones, or powered speakers.
- Stereo microphone input - perfect for making your very own smart home assistants
- Two 3-pin JST STEMMA connectors that can be used to connect more buttons, a relay, or even some NeoPixels!
- STEMMA QT plug-and-play I2C port, can be used with any I2C STEMMA QT boards, or can be used to connect to Grove I2C devices with an adapter cable.
- 5-Way Joystick + Button for user interface and control.
- Three RGB DotStar LEDs for colorful LED feedback.


### Blinka Setup

Blinka is a CircuitPython (python meant to be run on microcontrollers) library compatibility layer. It allows many of the libraries that were written for CircuitPython to run on CPython for Linux. To learn more about Blinka, you can check out the [CircuitPython on Linux and Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux) guide. We will need to install it to get the Braincraft Components up and running.

SSH into your Raspberry Pi or access via VNC viewer and open a terminal. Activate your Python virtual environment. Execute the following series of commands. Note these are several commands that will run one after another. When it asks you if you want to reboot, choose yes.

```bash
cd ~
pip3 install --upgrade adafruit-python-shell
cd /home/<**YOUR USERNAME**>/env/lib/python3.11/site-packages
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```

Once it reboots, there are a couple CircuitPython libraries to install for the BrainCraft HAT.

The DotStar library is for controlling the 3 on-board DotStar LEDs and the Motor library is for testing out the GPIO pins. Install it using pip using the command below.

```bash
pip3 install --upgrade adafruit-circuitpython-dotstar adafruit-circuitpython-motor adafruit-circuitpython-bmp280
```

If you get stuck on any of the steps, double check with these [instructions](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/blinka-setup).

### Fan Service Setup

There is a really simple fan service that will control the onboard fan you just installed. The reason we have it set up as a service instead of keeping the fan on all the time is so that it doesn't drain too much power from the Pi during the initial power on.

The fan service basically controls turning GPIO 4 on at startup, which is what the fan is connected to. Installing the fan service is really simple and we have a script for doing that.

To install, ssh in or access using VNC Viewer and open a terminal window. Activate your Python virtual environment. Input the following command:

```bash
sudo raspi-config
```

Select Performance Options

![alt_text](images/image7.png)

Select Fan

![alt_text](images/image5.png "image_tooltip")

Select Yes

![alt_text](images/image3.png "image_tooltip")

And make sure you put down GPIO pin 4 for the fan

![alt_text](images/image17.png "image_tooltip")

You can customize the fan temperature setting. **For testing, put it on 60.**

![alt_text](images/image4.png "image_tooltip")

To see if it’s connected correctly, run a stress test. The following command will stress test the CPU causing the Pi to heat up. The fan should turn on at 60 degrees C.

```bash
sudo apt-get install stress
while true; do vcgencmd measure_clock arm; vcgencmd measure_temp; sleep 10; done& stress -c 4 -t 900s
```

If the fan works as expected, press control-C (^C) and reboot your pi using `sudo reboot` to end the stress test. When it is rebooted follow the instructions above and switch the temperature to 80 degrees.

If the fan does not switch on as expected, try reconnecting the wire (make sure the wire is securely attached).

If you get stuck on any of the steps, double check with these [instructions](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/fan-service-setup).

### Display Module Setup

For some purposes you can setup the display using pure Python, which is probably easier, but for our purposes we will need to install using a kernel module. [You can learn more about kernel modules here if you want.](https://en.wikipedia.org/wiki/Loadable_kernel_module)

To setup run the following script while you are ssh’d in or on a terminal opened through VNC Viewer. Make sure you activate your Python virtual environment.

```bash
cd ~
pip3 install --upgrade adafruit-python-shell click
sudo apt-get install -y git
git clone https://github.com/adafruit/Raspberry-Pi-Installer-Scripts.git
cd Raspberry-Pi-Installer-Scripts
sudo -E env PATH=$PATH python3 adafruit-pitft.py --display=st7789v_bonnet_240x240 --rotation=0 --install-type=mirror
```

When you are asked to reboot, reboot.

If your display module has a bunch of lines running through it, [check out this page to troubleshoot. ](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/kernel-module-troubleshooting)

If you get stuck on any of the steps, double check with these [instructions](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/display-kernel-module-install).

### Camera Test

If you are running the command from SSH, test out your camera by running::

```bash
DISPLAY=:0 libcamera-hello -t 0
```

Else, if you are running the command through VNC and Raspi Terminal:
```bash
libcamera-hello -t 0
```

If it is working you should see what the camera is viewing on your display.

![alt_text](images/image18.jpg)

Don't worry if things aren't working! To trouble shoot, shutdown your Raspberry Pi, unplug the camera, and reconnect. Ensure it is facing the right direction, it is seated at the bottom of the connective housing, it is not crooked, and the black clip is pushed all the way down.

Also double check on the camera board that the small ribbon cable below the lens is connected to the board evenly. Do not attempt to unplug if it is already connected. This is a very delicate connector and should be treated with the utmost care.

After following these troubleshooting steps, plug in your Raspberry Pi and try to run the command again. The camera connection can be finicky, it may take a couple tries to get it connected the right way. _[You can also checkout this guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)_

### Interacting with BrainCraft HAT using Python

At this point, you should have just about everything already set up.

Besides the display, audio, and fan, this board has quite a few other useful features on it that can be controlled through Python. We'll go through those and how to control them in Python.

#### Joystick and Button test

The 5-way Joystick and button uses digitalio and each uses a separate GPIO, so they're really simple to control. Here's a script that will setup the GPIOs, Create Internal Pullups, and then print out the value to the terminal.

What you want to do is create a new python file and paste this script into the file. To do this we use nano, which is a simple text editor that you can access through your terminal. To create a new file you input `nano filename` which will then pull up an empty file with the name you chose. In a terminal access your Pi via ssh, and input the following:

```bash
nano button_test.py
```

Paste the following script into the file and save and exit using the commands listed in the terminal.

```python
import time
import board
from digitalio import DigitalInOut, Direction, Pull

BUTTON_PIN = board.D17
JOYDOWN_PIN = board.D27
JOYLEFT_PIN = board.D22
JOYUP_PIN = board.D23
JOYRIGHT_PIN = board.D24
JOYSELECT_PIN = board.D16

buttons = [BUTTON_PIN, JOYUP_PIN, JOYDOWN_PIN,
           JOYLEFT_PIN, JOYRIGHT_PIN, JOYSELECT_PIN]
for i,pin in enumerate(buttons):
  buttons[i] = DigitalInOut(pin)
  buttons[i].direction = Direction.INPUT
  buttons[i].pull = Pull.UP
button, joyup, joydown, joyleft, joyright, joyselect = buttons

while True:
  if not button.value:
    print("Button pressed")
  if not joyup.value:
    print("Joystick up")
  if not joydown.value:
    print("Joystick down")
  if not joyleft.value:
    print("Joystick left")
  if not joyright.value:
    print("Joystick right")
  if not joyselect.value:
    print("Joystick select")

  time.sleep(0.01)
```

Once you have done this run this Python file using

```bash
python3 button_test.py
```

Now try moving the joystick and press the button and you should see it print out what you're pressing.

#### DotStar LEDs Test

Using the same method explained above, save this script as `dotstar_test.py`

```python
import time
import board
import adafruit_dotstar

DOTSTAR_DATA = board.D5
DOTSTAR_CLOCK = board.D6

dots = adafruit_dotstar.DotStar(DOTSTAR_CLOCK, DOTSTAR_DATA, 3, brightness=0.2)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

while True:
    for j in range(255):
        for i in range(3):
            rc_index = (i * 256 // 3) + j * 5
            dots[i] = wheel(rc_index & 255)
        dots.show()
        time.sleep(0.01)
```

Run by entering

```bash
python3 dotstar_test.py
```

The DotStar LEDs should start color-cycling in a rainbow.

## 5. Deploying a Computer Vision Machine Learning Model to Raspberry Pi through TensorFlow Lite and OpenCV

## 5.1. Setup TensorFlow Lite and OpenCV

1. Install Picamera2:

```bash
sudo apt install -y python3-picamera2
```

2. Then, clone the Picamera2 repository:

```bash
git clone https://github.com/raspberrypi/picamera2.git
```

3. (If you used SSH, skip this step if you didn't) Run this command to set display:

```bash
export DISPLAY=:0
```

4. Install model dependencies:

```bash
sudo apt install build-essential
sudo apt install libatlas-base-dev
pip3 install tflite-runtime
pip3 install opencv-python-headless
```
5. Add code to display labels in console

```bash
cd picamera2/examples/tensorflow
nano yolo_v5_real_time_with_labels.py
```
The `yolo_v5_real_time_with_labels.py` script should now open in your terminal. Scroll down to the end and add `print(labels[classes[i]])` to [line 149](https://github.com/raspberrypi/picamera2/blob/a89eb1dc39578fb764d792d83ba34095a9597f80/examples/tensorflow/yolo_v5_real_time_with_labels.py#L149). Your script should now look something like this:

![alt_text](images/updated_script.png)

Then exit by typing ctrl-X (^X). When prompted to whether you want to save your changes, type `Y` and press enter.


6. Test the default object detection model:

```bash
python3 yolo_v5_real_time_with_labels.py --model=yolov5s-fp16.tflite --label=coco_labels_yolov5.txt
```

You should see a bunch of text scrolling in your SSH window.
![alt_text](images/example_code.png)

Now start holding up various items in front of the camera and it should display what it thinks it sees, which isn't actually what the item may be. For example, it should detect a person, a phone, or a cup. See the full list of objects it can detect [here](https://github.com/raspberrypi/picamera2/blob/main/examples/tensorflow/coco_labels_yolov5.txt).

![alt_text](images/image6.png "image_tooltip")

## 5.2. Create and add your own machine learning model to your raspberry PI to use in your conservation technology projects.

**Useful Links:**

[Google TeachableMachine](https://teachablemachine.withgoogle.com/train)

We’re going to use Teachable Machine to train and use a machine learning model for conservation technology projects. Teachable machine is a web-based tool that makes creating machine learning models fast, easy and accessible to everyone. It’s for educators, artists, students, innovators, makers of all kinds. **No prerequisite machine learning knowledge or experience is required. **

First we’re going to train our ML model. To do so, visit [TeachableMachine](https://teachablemachine.withgoogle.com/train)

Choose:

- Image project → Standard Image model

You can either use your webcam or upload pictures to train your ML model. Our suggestion is to start with an easy model first so that you can get a feel for it. Our suggestion is to begin by creating three classes. In the example below:

- Class 1: I grabbed about 10 water bottles that I had at home and I took over 300 samples (just clicking and holding the button), Class 2: I grabbed other things that were not water bottles and took pictures of them, and Class 3: I took pictures of empty backgrounds. Having 3 classes allows the ML to “train” using bottles, other objects and empty backgrounds. You can pass many more classes to be more specific. The more specific you are with the photos (data) you’re passing, the more specific your ML model will be as well.
- Hints: \* As you take (or choose) pictures make sure you do so with different backgrounds. Changes in light and changes in background -while maintaining the focus on the object that you’re labeling fixed - will allow us to have better training data.
  ![alt_text](images/image11.png)
  After you’ve created your classes, click on “Training”. It’ll take a little bit for the model to train. After that’s completed, click on “Export Mode” and follow [the instructions here.](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

The first step is to export your shiny new model. This makes it easy to transfer all of the files needed to the Pi, since it comes in a zip file.
![alt_text](images/image13.png)
In the dialog that appears, choose **TensorFlow Lite** and choose either the **Quantized** or **Floating point** model conversion type, as shown below. Then, click **Download my model**. After a minute or two, your browser will save a `converted_savedmodel.zip` file.
![alt_text](images/image15.png)
Now we’re running the model on the Pi. When you clicked the **Download my model** button in the last step, your browser should have saved a file called `converted_tflite.zip`. Now you need to place this on your Raspberry Pi.

You can transfer the model to the Raspberry Pi using scp. Feel free to unzip the file and change the name of the model and label file to desired. Afterwards, open a new terminal on your mac and run:

```bash
# if zip file
$ scp <PATH_TO_DOWNLOADS>/converted_tflite.zip <PI USERNAME>@<YOUR IP NETWORK>:/<PATH_TO_MODEL_FOLDER>
# for example
$ scp ~/Downloads/converted_tflite.zip tymho@192.168.0.138:/home/tymho/picamera2/examples/tensorflow

# otherwise if unzipped
$ scp -r <PATH_TO_DOWNLOADS>/converted_tflite <PI USERNAME>@<YOUR IP NETWORK>:/<PATH_TO_MODEL_FOLDER>
```

Now, go back to the other terminal SSH'ed into your Pi and run:

```bash
python3 yolo_v5_real_time_with_labels.py --model=<PATH_TO_YOUR_CUSTOM_MODEL> --label=<PATH_TO_YOUR_CUSTOM_LABELS>

# for example
cp ~/picamera2/examples/tensorflow/converted_tflite/custom_model.tflite
cp ~/picamera2/examples/tensorflow/converted_tflite/custom_labels.txt
python3 yolo_v5_real_time_with_labels.py --model=custom_model.tflite --label=custom_labels.txt
# or
python3 yolo_v5_real_time_with_labels.py --model=~/picamera2/examples/tensorflow/converted_tflite/custom_model.tflite --label=~/picamera2/examples/tensorflow/converted_tflite/custom_labels.txt
```

Congratulations! You have now completed an end-to-end project building hardware, creating a machine learning model, and deploying the model on the hardware.

**Two Bonus Challenge!!!!!**

**Challenge 1:** [Train your model to recognize audio](https://learn.adafruit.com/adafruit-braincraft-hat-easy-machine-learning-for-raspberry-pi/audio-setup)

**Challenge 2:** Go back to Teachable Machines and recreate your machine learning model using the **Embedded image model** instead of the **standard image model**. In the world of machine learning, we are always looking for ways to scale down the size of our models to improve performance, compute speed, and deploy-ability. Try to integrate this embedded image model into your hardware.

**Hint:** The embedded image model utilizes greyscale images instead of colored images, so you might see an error like:

```bash
  File "/home/tymho/picamera2/examples/tensorflow/yolo_v5_real_time_with_labels.py", line 135, in main
    interpreter.set_tensor(input_details[0]['index'], input_data)
  File "/home/tymho/env/lib/python3.11/site-packages/tflite_runtime/interpreter.py", line 720, in set_tensor
    self._interpreter.SetTensor(tensor_index, value)
ValueError: Cannot set tensor: Dimension mismatch. Got 3 but expected 1 for dimension 3 of input 1.
```

Can you fix it? It might have something to do with how `img` is currently being created on line 121 of the `yolo_v5_real_time_with_labels.py` file. This [conversion](https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html) should come in handy.

## 6. (Optional) Running with Lobe.ai
If you cannot get Tensorflow Lite and OpenCV to work **no matter how hard** you debug, try this tutorial. However, I ask that you give the previous section one last attempt :)

Note that Lobe.ai does not currently work on M1 macs so if you're working on an M1 Mac, you may need to use teachable machine.

Most of this section was copied from [this tutorial](https://learn.adafruit.com/machine-learning-101-lobe-braincraft/get-predictions-on-the-pi). Check it out for more info.

Follow instructions to download and set up Lobe.ai on your computer [here](https://www.lobe.ai/)

SSH into your Raspberry Pi and run the following code to install the necessary packages:

```bash
cd ~
git clone https://github.com/lobe/lobe-adafruit-kit.git
```

Once this is installed, create a new folder in the home directly called `model` by running:

```bash
cd ~
mkdir model
```
copy your saved `tflite model` and `signature.json` from the folder on your computer where they were exported to your raspberry pi by running the following for each file you want to transfer:

```bash
scp username@ip-address:/model/ path/on/local/machine
```

In terminal on the Pi, run the following script to install Lobe and all it's dependencies:

```bash
cd ~
wget https://raw.githubusercontent.com/lobe/lobe-python/master/scripts/lobe-rpi-install.sh
sudo bash lobe-rpi-install.sh
```

While SSH'd into your pi run the `lobe-basic-prediction.py` program by running the following:
  
```bash
cd ~
cd lobe-adafruit-kit
python3 lobe-basic-prediction.py
```
