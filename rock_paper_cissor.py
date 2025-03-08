def rps(p1, p2):
    #your code here
    if p1=="scissors": #case scissors
        if p2=="scissors":
            return "Draw!"
        elif p2=="paper":
            return "Player 1 won!"
        elif p2=="rock":
            return "Player 2 won!"
        else :
            return "Wrong input."
        
    if p1=="paper": # case paper
        if p2=="paper":
            return "Draw!"
        elif p2=="rock":
            return "Player 1 won!"
        elif p2=="scissors":
            return "Player 2 won!"
        else :
            return "Wrong input."
        
    if p1=="rock": # case rock
        if p2=="rock":
            return "Draw!"
        elif p2=="scissors":
            return "Player 1 won!"
        elif p2=="paper":
            return "Player 2 won!"
        else :
            return "Wrong input."