import random

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
        
#################################

def init(deck, nplayers = 2, player_to_move = 0):
    '''shuffles the deck (list of cards) and
       updates the dictionary state
    '''
    random.shuffle(deck)
    
    state['nplayers']       = nplayers
    state['player_to_move'] = player_to_move    
    state['matches']        = {i: [] for i in range(nplayers)}
    state['layout']         = {idx: card for idx, card in enumerate(deck)}
    state['face_up']        = ()
    
    _callback('new_game', len(deck))
    
def face_up(i, j):
    '''markiere die ite und jte Karte als 'face_up', 
       falls diese Karten noch nicht eingesammelt wurden
    '''
    if i in state['layout'] and j in state['layout']:
        state['face_up'] = (i, j)
        _callback('phase_1', _cards_face_up())
        
def face_down():
    '''falls face-up Karten kein Match: drehe sie wieder um, gib Zugrecht an naechsten Spieler
       falls face-up Karten Match: entferne Karten aus Layout und update state['matches']
    '''
    (idx1, card1), (idx2, card2) = _cards_face_up()
    match = card1 == card2
    
    if match:
        player = state['player_to_move']
        state['matches'][player].append(card1) 
        _remove_cards((idx1, idx2))
      
    _next_player(match)   
    state['face_up'] = ()  
    _callback('phase_2', (match, (idx1, idx2)))
    
def set_callback(callback):
    global _callback
    _callback = callback    
    
# initialize the state-dictionary
state = dict.fromkeys([
    'nplayers',   
    'player_to_move',
    'matches',  
    'layout',        
    'face_up',       
])   

# set an initial callback
_callback = print