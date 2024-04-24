import requests


ALIGNMENT_ASPECTS = ["Heroism", "Villainy"]
STYLE_ASPECTS = ["Vigilance", "Cunning", "Aggression", "Command"]
ALL_ASPECTS = ["Vigilance", "Cunning", "Aggression", "Command", "Heroism", "Villainy"]
CURRENT_ASPECTS = [STYLE_ASPECTS[3], ALIGNMENT_ASPECTS[1]]
ANTI_ASPECTS = [ALIGNMENT_ASPECTS[0]]


def get_card_data(card_aspects):
   url = 'https://api.swu-db.com/cards/sor'


   try:
       response = requests.get(url)
       response.raise_for_status()  # Raise an exception for bad status codes


       # Parse JSON response
       data = response.json()


       # Extract relevant information from the JSON response
       total_cards = data['total_cards']
       cards = data['data']


       display_cards = []


       for card in cards:
           aspects = card.get('Aspects', [])
           variants = card.get('VariantType', [])
           card_type = card.get('Type')
           if card_type != 'Leader' and card_type != 'Base' and variants == "Normal" and aspects:
               if all(aspect in aspects for aspect in card_aspects.get("currentAspects")) and all(aspect not in aspects for aspect in card_aspects.get("antiAspects")):
                   display_cards.append(card)


       return display_cards, cards


   except requests.exceptions.RequestException as e:
       print('Error connecting to API:', e)
       return None, None


def custom_sort_key(card):
           aspects = card.get('Aspects', [])
           style_aspect_count = aspects.count(CURRENT_ASPECTS[0])
           return (style_aspect_count, int(card.get('Cost', 0)))


def show_card_data(display_cards):
   sorted_cards = sorted(display_cards, key=custom_sort_key)
   page_length = 3
   page_count = 1
   count_of_cards = len(sorted_cards)
   extra_front_lines = 0
   extra_end_lines = 0


   if count_of_cards % page_length == 0:
       pass
   elif (count_of_cards + 1) % page_length == 0:
       extra_front_lines = 1
   elif (count_of_cards + 2) % page_length == 0:
       extra_front_lines = 1
       extra_end_lines = 1


   for index, card in enumerate(sorted_cards):
       if index == 0:
           print(f"\nPage {page_count}")
           if extra_front_lines > 0:
               bonus_card_lines = 0
               while bonus_card_lines < extra_front_lines:
                   print("!!!Bonus Cards!!!")
                   bonus_card_lines += 1
       elif (index + extra_front_lines) % page_length == 0:
           page_count += 1
           print(f"\nPage {page_count}")
       aspects = card.get('Aspects', [])
       style_aspect_count = aspects.count(CURRENT_ASPECTS[0])
      
       if style_aspect_count > 1:
           displayed_count = f'| x{style_aspect_count}'
       else:
           displayed_count = ""
       name = card.get('Name')
       cost = card.get('Cost')
       type = card.get('Type')
       print(f'{type} | {name} | Cost: {cost}{displayed_count}')
   if extra_end_lines > 0:
       bonus_card_lines = 0
       while bonus_card_lines < extra_end_lines:
           print("!!!Bonus Cards!!!")
           bonus_card_lines += 1
   print(f'Total Cards: {count_of_cards}')


if __name__ == "__main__":
   display_cards, cards = get_card_data({"currentAspects": CURRENT_ASPECTS, "antiAspects": ANTI_ASPECTS})
   if display_cards is not None and cards is not None:
       show_card_data(display_cards)

