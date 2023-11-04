# ArtNetSounds

**_This project was written at short notice for a project and is not stable. Use at your own risk. Please report all bugs without annoying me:)_**

Play sounds using ArtNet

## Setup

* install requirements `pip install -r requirements.txt`
* start the script `./main.py`
* stop the script
* move your audio files in the new created folder `sounds`
* if VLC not installed
  * Install VLC media player
  * or edit the variable `VLC_COMMAND` in `audioplayer.py`
* execute `./main.py -gj` to update the json file

## Usage

* start the script `./main.py`
  * if you don't want to use universe 0 add `-u <universe>`
* now you can use [QLC+](https://qlcplus.org) with ArtNet as output

## About me and this project

My Name is Jakob Felix Rieckers. I am a licensed amateur radio operator, and I like programming. Together with my brother Janfred (Jan-Frederik Rieckers) we sometimes operate some lights.

This script was for the project ["Mondschein-Spiele"](https://www.hacrafu.de/2023/10/27/mondscheinspiele/). I was responsible for the last room of this role-playing game and wanted to create a bit of ambience in addition to the lighting.

My (relevant) social media platforms are:
* Twitter (X): [@DO2JFR](https://twitter.com/DO2JFR)
* Mastodon: [@do2jfr@radiosocial.de ](https://radiosocial.de/@do2jfr)
* Reddit: [u/ham_jaky](https://www.reddit.com/user/ham_jaky/)
* Github: [ham-jaky](github.com/ham-jaky)

## License

MIT License

Copyright (c) 2023 Jakob Felix Rieckers
