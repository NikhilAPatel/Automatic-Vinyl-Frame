# Automatic Vinyl Frame
### Love the hassle of physical media with all of the cons of digital? If so, then this is the project for you. This code will read an RFID tag attached to a vinyl record sleeve when it is placed inside a vinyl display frame. Then, it will immediately start to playback the audio, enabling you, dear user, to use your analog media digitally.
 
## Required Dependencies
* RPi.GPIO
* mfrc522
* vlc

## Materials
* Raspberry Pi
* RC522 RFID Module
* 7 Female-Female jumper wires
* RFID Tags
* Vinyl Frame
* Speaker

Here are the [RFID Tags](https://www.amazon.com/gp/product/B01LZYOR7P/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) and [Vinyl Frame](https://www.amazon.com/gp/product/B078J63BFH/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) used in this project

Optional Materials:
* USB bluetooth adapter if you wish to have bluetooth if your Raspberri Pi does not have it built in and you want bluetooth audio, else, get a 3.5mm audio cable
* Battery bank if you do not wish to have your Raspberry Pi constantly plugged into the wall

## Usage

1. Create a base directory where you will store your music files and record its path
    1. Place each album's music in a separate directory within this directory
1. Update the **MUSIC_PATH** variable in *main.py* with your base directory's path
1. Run *read.py* and *write.py* to set up your RFID tags
    1. Write to each RFID tag the name of the folder where it's album's music is stored
1. Run *main.py* and enjoy

Optional: Create an RFID tag with the value "PAUSE" to be able to pause and unpause your music

## RC522 Wiring Schematic
![schem-1](https://user-images.githubusercontent.com/25623305/82866207-72007f00-9ef6-11ea-9db1-63add4a4418a.png)

## Pictures
### View of frame open with no vinyl
![IMG_0946](https://user-images.githubusercontent.com/25623305/82865549-feaa3d80-9ef4-11ea-9ded-df1981d53510.jpg)

### Vinyl being inserted into the frame
![IMG_0947](https://user-images.githubusercontent.com/25623305/82865631-2ef1dc00-9ef5-11ea-8ddd-b01c9a0b19f0.jpg)

### Back when closed
![IMG_0949](https://user-images.githubusercontent.com/25623305/82865654-37e2ad80-9ef5-11ea-9b9f-d2cc2982218d.jpg)

### Front when closed
![IMG_0948](https://user-images.githubusercontent.com/25623305/82865649-35805380-9ef5-11ea-8535-36635bda464d.jpg)
