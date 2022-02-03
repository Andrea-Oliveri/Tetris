# Tetris, by Andrea Oliveri

## Project Overview

The goal of the project is to implement a Tetris game in Python respecting most of the [Tetris Guidelines](https://tetris.wiki/Tetris_Guideline).

**This project was done for recreational and learning purposes, and is not, nor it was at any time, meant for commercial purposes.**

## Repository Structure

This directory contains the following files and directories:

* [**tetris.py**](tetris.py): Main Python script used to run the game.
* [**src**](src): Directory collecting all additional Python scripts and custom packages needed to run the game.
* [**assets**](assets): Audio and image files used in the game. 
* [**tetris.spec**](tetris.spec): Pyinstaller specification file needed to package the game into a single executable (~19 MB in size).
* [**README.md**](README.md): The Readme file you are currently reading.


## Getting Started

### 0) Python Environment

The Python enviroment used for this project was kept as simple as possible to prevent the size of the executable from increasing too much.

An environment containing the required packages with compatible versions can be created as follows:

```bash
conda create -n tetris python=3.9.7
conda activate tetris
pip install pygame==2.0.1
```

Optionally, to package the game into an executable, Pyinstaller also needs to be installed into the environment:

```bash
conda install -c conda-forge pyinstaller==4.5.1
```

### 1) Run

To run the Python script, simply activate the correct conda environment and, from the same directory as the [**tetris.py**](tetris.py) file run:

```bash
python tetris.py
```


### 2) Generate executable

To generate a single executable containing the whole game and all assets, simply activate the correct conda environment and, from the same directory as the [**tetris.spec**](tetris.spec) file run:

```bash
pyinstaller tetris.spec
```

After running this command, the executable should appear inside a folder named **dist**, and can be moved anywhere freely. Another folder named **build** will also be generated. Feel free to delete both folders after generating the executable. 


## Tetris Guidelines

Here are the Tetris Guidelines (as of 2009) collected from [this](https://tetris.fandom.com/wiki/Tetris_Guideline) page (last visited in August 2021).


| Image | Meaning |
|:-----:|:--------|
|  🟢    | Currently implemented |
|  🔴️  | Pending implementation |
|  ⚫️  | Not going to be implemented |


| Guideline | Status |
|:----- |:-------:|
| Playfield is 10×40, where rows above 20 are hidden or obstructed by the field frame to trick the player into thinking it's 10×20 | 🟢 |
| If hardware permits it, a few pixels of row 21 will be visible | ⚫️ |
| Tetrimino colors are as follows: <ul><li>Cian <i>I</i></li><li>Yellow <i>O</i></li><li>Purple <i>T</i></li><li>Green <i>S</i></li><li>Red <i>Z</i></li><li>Blue <i>J</i></li><li>Orange <i>L</i></li></ul> | 🟢 |
| Tetrimino start locations: <ul><li>The I and O spawn in the middle columns</li><li>The rest spawn in the left-middle columns</li><li>The tetriminoes spawn horizontally with J, L and T spawning flat-side first</li><li>Spawn above playfield, row 21 for I, and 21/22 for all other tetriminoes</li><li>Immediately drop one space if no existing Block is in its path</li></ul> | 🟢 |
| Initial rotation and movement: <ul><li>Super Rotation System/Standard Rotation System (SRS) specifies tetrimino rotation</li></ul> | 🟢 |
| Standard mappings for computer keyboards: <ul><li>Up arrow and X are to rotate 90° clockwise</li><li>Space to hard drop</li><li>Shift and C are to hold</li><li>Ctrl and Z are to rotate 90° counterclockwise</li><li>Esc and F1 are to pause</li><li>Up, Down, Left, Right arrows perform locking hard drop, non-locking soft drop, left shift, and right shift respectively</li></ul> | 🟢 |
| Number pad controls | ⚫️ |
| 7-bag Random Generator | 🟢 |
| Hold piece: The player can press a button to send the falling tetrimino to the hold box, and any tetrimino that had been in the hold box moves to the top of the screen and begins falling. Hold cannot be used again until after the piece locks down | 🟢 |
| Must have sound effects on by default, on rotation, movement, landing on surface, touching a wall, locking, line clear and game over | 🟢 |
| Ghost piece function | 🟢 |
| Terms used in the help section: <ul><li>"Tetriminos" (the capital T is required)</li><li>Letter names</li></ul> | 🟢 |
| Designated soft drop speed  | 🟢 |
| Player may only level up by clearing lines or performing T-Spins | 🟢 |
| May use fixed-goal or variable-goal: <ul><li>Fixed goal is 10 lines</li></ul> | 🟢 |
| The game must use a variant of Roger Dean's Tetris logo: <ul><li>The logo may not have its t-tetrimino split into 4 minoes</li><li>The logo may not be sheared or skewed</li><li>The logo must be 2D</li></ul> | 🟢 |
| Game must include a song called Korobeiniki. This must be the default song | 🟢 |
| Uses half second lock delay | 🟢 |
| The player tops out when a piece is spawned overlapping at least one block (block out), or a piece locks completely above the visible portion of the playfield (lock out) | 🟢 |
| Must have 1 to 6 next pieces | 🟢 |
| Recognition and rewarding of T-spin moves | 🟢 |
| Recognition and rewarding of Mini T-spin moves | ⚫️ |
| Rewarding of Back to Back chains | ⚫️ |
| Multiplayer, Arcade, Marathon, Sprint, Ultra variation | ⚫️ |
| Speed curve must be the same as Tetris Worlds | 🟢 |
| Game must use scoring system described [here](https://tetris.fandom.com/wiki/Scoring#Guideline_scoring_system) | 🟢 |
| Game must count down from 3 after you press start, and after you resume a paused game | 🟢 |
| Game must display a notice when the game starts | ⚫️ |