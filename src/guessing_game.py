import random
from toolbox import sign, table2str

def history2table(h):
    '''returns a string, representing h as a table 
    
       h: list of tuples, [(guess, comment),...]
    '''
    header = ('Nr.', 'guess', 'comment')
    rows =  [(str(i), str(n), c) for i, (n, c) in enumerate(h)]    
    return table2str(header, rows)

def eval_guess(guess, n):
    '''returns a tuple (is_ok: bool, comment: str)
    
       is_ok: True, if guess equals n
       comment: 'too big', 'correct' or 'too small'
    '''
    comments = {1: 'too big', 
                0: 'correct', 
                -1: 'too small',
               }
    
    is_ok = guess == n
    key = sign(guess - n)
    return is_ok, comments[key]

def play_game(lower = 0, upper = 10):
    '''guess a random Integer between lower and upper,
       lower and upper are included
    '''   
    nbr = random.randint(lower, upper)
    history = []
    
    is_correct = False
    while not is_correct:
        n = input('Zahl zwischen {a} und {b}? '.format(a=lower, b=upper))
        n = int(n)
        is_correct, comment = eval_guess(n, nbr)
        history.append((n, comment))   
        
        print(comment)
        
    table = history2table(history)
    print('Congrats! You guessed the number {N} in {n} tries.\n'.format(N=nbr, n=len(history)))
    print(table)
    
    
if __name__ == '__main__':
    play_game()    
