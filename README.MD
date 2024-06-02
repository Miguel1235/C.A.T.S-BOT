# :robot: C.A.T.S BOT

## Features

This bot plays the game of C.A.T.S, for now it supports:

1. QuickFights
2. LeagueFights
3. Championship

For now you can only switch modes commenting and descommeting the code, in future versions I will add a menu for this.

## Installation

1. Install [nox](https://www.bignox.com)
2. Set up the resolution of `960x540` in the `systemSettings -> Performance` tab
3. Set up `Fixed window size` in the `settings -> display` tab
4. Install [C.A.T.S game](https://play.google.com/store/apps/details?id=com.zeptolab.cats.google)
5. Install [python](https://www.python.org/downloads)
6. Install requirements for running the bot using the following command

```bash
pip install -r ./requirements.txt --upgrade
```

7. Run the bot

```bash
python ./main.py
```

> [!WARNING]  
> You must set up the nox player to the resolution of `960x540` and not resize the windows. This is because the bot heavily relies on pictures of the game, so if you resize the window, it mess up with the images.
