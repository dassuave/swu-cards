# SW-Cards

SW-Cards is a card organizer for Star Wars Unlimited

## Installation

Use pip to install the contents of the requirements.txt to install the prerequesites into a virtual enrivonment

## Usage
In the main sw-cards.py file, set CURRENT_ASPECTS and ANTI_Aspects to determine what cards to show.  Currently, if any ALIGNMENT_ASPECT is used, the other alignment must be included in the ANTI_ASPECTS.

The following example would show only Villainy Command cards

```
CURRENT_ASPECTS = [STYLE_ASPECTS[3], ALIGNMENT_ASPECTS[1]]
ANTI_ASPECTS = [ALIGNMENT_ASPECTS[0]]
```

One the Aspects you want to show are selected, run the command `python sw_cards.py` in a terminal from the root of this directory to run SW-Cards.  The output will be shown in the terminal.