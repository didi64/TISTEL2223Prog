
import random
import tools 

def print_history(history):
    header = ('Nr.', 'Guess', 'Comment')
    rows = []
    for i, (guess, feedback) in enumerate(history):
        row = (str(i+1), str(guess), feedback) 
        rows.append(row)
        
    tools.print_as_table(header, rows)

def eval_guess(guess, n):
    '''returns a tuple (is_ok, comment)
       is_ok: True, if guess equals n
       comment: 'too big', 'correct' or 'too small'
    '''
    comments = {1: 'too big', 
                0: 'correct', 
                -1:'too small',
               }
    
    is_ok = guess == n
    key = tools.sign(guess - n)
    return is_ok, comments[key]

def play_game(lower, upper):
    '''guess a random Integer between lower and upper,
       lower and upper are included
    '''   
    nbr = random.randint(lower, upper)
    history = []
    
    is_correct = False
    while not is_correct:
        n = int(input('Zahl zwischen {lower} und {upper}? '\
                  .format(lower=lower, upper=upper)))
        
        is_correct, comment = eval_guess(n, nbr)
        
        history.append((n, comment))    
        print(comment)
        
    print('Congrats! You guessed the number {N} in {n} tries.'\
          .format(N=nbr, n=len(history)))
    print()
    print_history(history)
    

if __name__ == '__main__':
    play_game(1, 5)
    
print('__name__:', __name__)    
