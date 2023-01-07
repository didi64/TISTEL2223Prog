import random

def get_matches(deck):
    '''gibt Dictionary der Form
       {'A': [<index von 1. A>, <index von 2. A>], ...}
       zurueck
    '''   
    matches = {}
    for idx, card  in enumerate(deck):
        matches.setdefault(card, []).append(idx)
    return matches

def init(deck, nplayers = 2, player_to_move = 0):
    '''setzte Werte des Dictionary 'state' '''
    random.shuffle(deck)
    
    state['nplayers'] = nplayers
    state['player_to_move'] = player_to_move    
    state['matches'] = {i: [] for i in range(nplayers)}
    state['layout'] = {idx: card for idx, card in enumerate(deck)}
    state['face_up'] = ()
    
# Hilfsfunktionen
def _cards_face_up():
    return [(idx, state['layout'][idx]) for idx in state['face_up']]
    
def _remaining_cards():
    return list(state['layout'].keys())   

def _remove_cards(idxs):
    for idx in idxs:
        state['layout'].pop(idx)   
        
def _next_player(match = False):
    if not state['layout']:
        state['player_to_move'] = None
    elif not match:
        state['player_to_move'] = (state['player_to_move'] + 1) % state['nplayers']
        
keys =  ['nplayers',   
         'player_to_move',
         'matches',  
         'layout',        
         'face_up',       
        ]       
state = dict.fromkeys(keys)
   