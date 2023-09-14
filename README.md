# Robot Car simulation [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
This is a simple robot car with differential drive simulator. It is supposed to be used for training tensorflow network. Corently it is in erly development. This repository is also connected to [this repository](https://github.com/mikic202/RobotCar) and neural network trained on this model will be used to steer this real life robot.

## Table of contents:
- [Robot Car simulation ](#robot-car-simulation-)
  - [Table of contents:](#table-of-contents)
  - [Required Packages](#required-packages)
  - [How To Start](#how-to-start)

## Required Packages

Before you clone this repo you would need [pygam](https://www.pygame.org/news) python libray. Of course you would need python compiler to start the project

## How To Start

Before you start the project you need to clone the repository. After you do that you can open the Visualization.py file and click run. You can also run the code from terminal. There are two arguments both with default values. Those args are:
-  --robot - it allows you to specify robot png (or jpg) file that will be shown in the simulation
-  --track - it allows you to specify track that will be used in simulation (you don't need to pass extention because .json is default extension for track file)

You can also create your own track file by starting TrackCreator.py file. It also has one argument that is:
-  --file - it allows you to spocifyname of the file where your track will be saved.

