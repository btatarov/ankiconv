# AnkiConv

Simple python script for creating Anki decks with google speech from txt input.

## Requirements
* Python 3.x
* [SoX with MP3 support](http://sox.sourceforge.net/)

## Installation
    git clone https://github.com/btatarov/ankiconv.git
    cd ankiconv
    python3 -m venv ankienv
    source ankienv/bin/activate
    pip install -r requirements.txt

## input.txt Format
[target language string] - [english translation]

## Running
    python ankiconv.py
