# narratives-detection


## Team Members

Dasha, Fabio, Fraser, Renu, Andrey, Yasha.

## The Repository

Contains multiple sets of tools to collect, extract, and utilise narratives. Primarily based on the Bellingcat QAnon database. 
## Installation

Move to the tool's directory and install the tool

`cd narratives-detecion`

`mamba env create -f environment.yml`

Activate the environment:

`mamba activate narratives-detection` 

Updates to Python Package 

`mamba env update --file environment.yml --prune`

## Run

Configure the database connection in a `.env` file and run 'source .env'

`python ./src/entry.py`

## Usage

### Matchmaker

```python
import entity_matching.post_matcher
matcher = entity_matching.post_matcher.PostMatcher('path/to/bellingcat/qanon/csv')
post = matcher._matchmaker._posts[0]  # json_object_in_form_of_bellingcat_db
result = matcher.match_post(post)  # list of tuples with the first item being a rank and the second being the matching post
```

Limitations and future additions:
* No disambiguation is performed. This would improve accuracy.
* Generalising accepted input format would make the tool more accessible
* Integrating with Telegram channels for auomatic input rather than manual input
* Integrating with proper DB rather than CSV file usage

 ## Sample Post

```
Unmasking the Dark Secrets of Power! 🔥
BILL GATES: A Mastermind without a Medical Degree? 💉
COVID: The Patented Pandemic?
DEPOPULATION AGENDA: Gates and the Elites' Sinister Plot☠️
BIG PHARMA: The Evil Empire Unveiled💊
THE TRUTH THEY HID FROM US: The Deep State's Brainwashing 🔐
TRUMP: The Unfinished Battle for the Republic ⚖️
THE MILITARY: Guardians of the Constitution 💪
THE MOMENT OF TRUTH: Corruption Exposed, Heroes Unveiled 🌐
ALL YOUR ANSWERS ARE IN THE CHANNEL BELOW.THE WORLD NEEDS TO KNOW THE TRUTH.
```   
