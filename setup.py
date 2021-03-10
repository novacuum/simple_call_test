import shutil, json
from pathlib import Path

from engine.metadata import metadata_db
from engine.helpers import write_file

mdb = metadata_db('audio/simpleCall/metadata.json')
valid_labels = ['B2', 'B3', 'B4', 'VS', 'VSV', 'UPS']
name = 'simple_call_test'

Path('audio').mkdir(parents=True, exist_ok=True)

newMdb = dict()
for stem in mdb.db:
    entry = mdb.db[stem].props
    del entry['audio']
    entry['labels'] = list(filter(lambda label: label['sequence'] in valid_labels, entry['labels']))

    if len(entry['labels']) > 0:
        newMdb[stem] = entry
        shutil.copy(f'../audio/simpleCall/{stem}.wav', f'audio/{stem}.wav')

print(f'file count: {len(newMdb)}')
write_file("metadata.json", json.dumps(newMdb, indent=2))
