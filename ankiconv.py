#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import genanki
from google_speech import Speech
from slugify import slugify

# process input lines
with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

# genanki content
model_ja = genanki.Model(
    8800000001,
    'Japanese-to-English Model',
    fields=[
        {'name': 'Japanese'},
        {'name': 'English'},
        {'name': 'MyMedia'},
    ],
    templates=[
        {
          'name': 'Card 1',
          'qfmt': '<div class="base-card">{{Japanese}}<br>{{MyMedia}}</div>',
          'afmt': '<div class="base-card">{{FrontSide}}<hr id="answer">{{English}}</div>',
        },
    ],
    css='.base-card { font-family: MS Mincho, Arial; font-size: 35px; text-align: center; }',
)

model_en = genanki.Model(
    8800000002,
    'English-to-Japanese Model',
    fields=[
        {'name': 'English'},
        {'name': 'Japanese'},
        {'name': 'MyMedia'},
    ],
    templates=[
        {
          'name': 'Card 2',
          'qfmt': '<div class="base-card">{{English}}</div>',
          'afmt': '<div class="base-card">{{FrontSide}}<hr id="answer">{{Japanese}}<br>{{MyMedia}}</div>',
        },
    ],
    css='.base-card { font-family: MS Mincho, Arial; font-size: 35px; text-align: center; }',
)

deck = genanki.Deck(
    9900000001,
    'Japanese Vocab'
)

package = genanki.Package(deck)
package.media_files = list()

# add notes
for line in content:
    line_split = line.split(' - ')
    text_ja = line_split[0]
    text_en = line_split[1]
    speech = Speech(text_ja, 'ja')
    media_file = '{}.mp3'.format(slugify(text_en))
    speech.save(media_file)

    package.media_files.append(media_file)

    note_ja = genanki.Note(
        model=model_ja,
        fields=[text_ja, text_en, '[sound:{}]'.format(media_file)]
    )

    note_en = genanki.Note(
        model=model_en,
        fields=[text_en, text_ja, '[sound:{}]'.format(media_file)]
    )

    deck.add_note(note_ja)
    deck.add_note(note_en)

package.write_to_file('my_deck.apkg')

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_file_list = os.listdir(dir_path)
for item in dir_file_list:
    if item.endswith(".mp3"):
        os.remove(os.path.join(dir_path, item))
