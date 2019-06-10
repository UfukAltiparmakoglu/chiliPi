# chiliPi
DIY: Watch your chili plant grow.

## Prerequisites

What you'll need:
- Some working-knowledge with linux and python is fine.

- A small flower pot, potting soil and chili seeds.

- Raspberry Pi with preinstalled Image (I am using Raspbian).

- Raspberry Pi Cam (I am using v2.1).

- Python 3 (libraries skimage, numpy).

  > sudo pip3 install scikit-image numpy

- MEncoder <https://wiki.ubuntuusers.de/MEncoder/>

  > sudo apt install mencoder lame

---

## Instructions:
1.  Put some soil into the flower pot and bury a few chili seeds in it. Water the plant!

2.  Build a camera mount.

    ![RPI Camera Mount](/img/chiliPi_camera_mount.jpg)

3.  Make sure to be in your home directory of the raspberry. E.g. /home/pi/

4.  Clone this repository to your raspberry with command:
    > git clone https://github.com/UfukAltiparmakoglu/chiliPi.git

5.  Create a new entry in your crontab:
    > crontab -e

    Insert new line with following contents:
    > 0 0,2,4,6,8,10,12,14,16,18,20,22 * * * /home/pi/chiliPi/cam.py

    This will run the py script every 2 hours infinitely

6.  After a while, you will have collected enough pictures of your plant.

    ![RPI collected images](/img/chiliPi_images.png)

7.  Now let's make a video of it:

    Run the python script **chiliPi_scanner.py** like so:
    > python3 chiliPi_scanner.py

    This script will get rid of pictures which are too dark and produce the final video.

8.  Now there should be a video called **chiliPi.mp4** in your **chiliPi** folder. Congratz, you made it!

