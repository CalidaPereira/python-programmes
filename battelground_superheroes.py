#Libraries 
import random
import time

#Variables to keep track of cards 
player1_card_no = 0 
player2_card_no = 0 

#Player names 
player1_name=''
player2_name=''

#Indicator variable for computer
comp = "|\/|$%&*()+1234567890.,454545gsdfsi5445667uteenb777jkknndssdf///"

#Functions 
class battleground_superheroes():
    def __init__(self):
        self.characters = [{'character':"Superman",'strength':10,'agility':9,'intelligence':"5"},{'character':"Batman",'strength':3,'agility':6,'intelligence':9},{'character':"Black Panther",'strength':4,'agility':5,'intelligence':6},{'character':"Aquaman",'strength':6,'agility':3,'intelligence':"1"},{'character':"Ironman",'strength':5,'agility':4,'intelligence':10},{'character':"Thor",'strength':9,'agility':7,'intelligence':2},{'character':"Wonder Woman",'strength':8,'agility':8,'intelligence':3},{'character':"Hulk",'strength':7,'agility':2,'intelligence':8},{'character':"Dr. Strange",'strength':1,'agility':1,'intelligence':7},{'character':"Flash",'strength':2,'agility':10,'intelligence':4}]
        
    def chooseMode(self):
        while True:
            mode = input("\n Do you want to play single player(S) or multi player(M) ? ")
            if (mode.lower() != 's' and mode.lower() != 'm'):
                print("\n Invalid input")
                print("\n Enter a valid input!! Single player (S) or Multi player (M) ?")  
            else: 
                break
        return mode
        
    def introduction(self):
        print("\n Welcome to Battleground Superheroes!!!") 
        print("\n A game in which, to the victor belong the spoils")
        
        self.mode = self.chooseMode()
        self.player1_name = input ("\n Please enter your name Player 1 ")
        
        if self.mode=='m':
            self.player2_name = input ("\n Please enter your name Player 2 ")
            print("\n Hey {} and {}, hope you'll are doing well ".format(self.player1_name,self.player2_name))
        else:
            print("\n Hey {}, hope you're doing well".format(self.player1_name))
            self.player2_name="Computer"
            print("\n Your opponent is the worthy {}".format(self.player2_name))
        time.sleep(2)
       
        while True:
            require_instruction = input("\n Do you want to know the rules of the game? yes/y or no/n ")
            if require_instruction.lower() =='y' or require_instruction.lower() =='yes':
                time.sleep(0.5)
                print("\n Well the rules of the game are pretty simple.....each player has equal no. of superheroes with same characteristices but different strengths which are not known to them prior")
                time.sleep(3)
                print("\n Players are required to first roll the dice to decide who will begin the game.The player that rolls the highest value begins")
                time.sleep(3)
                print("\n A card from the first players deck is displayed to him with the superheroes characteristices. He gets to choose the characteristic with which he wishes to challenge his opponent")
                print("\n The player with the highest value for the chosen characteristic wins and gets to select the next characteristic to challenge on")
                time.sleep(3)
                print("\n This continues until the cards in the players decks are exhausted")
                time.sleep(3)
                print("\n The player with the highest points wins")
                time.sleep(3)
                print("\n Sounds pretty simple right ?")
                time.sleep(3)
                print("\n right..........?")
                time.sleep(1)
                print("\n right........?")
                time.sleep(1)
                print("\n Well let's make it interesting")
                time.sleep(2)
                print("\n Introducing the GOD & RESSURECT Spells")
                time.sleep(3)
                print("\n Did you win the dice throw and are beginning the round OR did you win the previous round ? Then you can use an a powerful weapon, the GOD spell !!!")
                time.sleep(3)
                print("\n Once you choose the characteristic on which you wish to challenge your opponent, you can cast the GOD spell that let's you pick a card from the opponents deck")
                time.sleep(3)
                print("\n The player with the highest value for the chosen characteristic wins")
                time.sleep(3)
                print("\n To play the GOD spell, enter G/God after you've chosen the characteristic to challenge your opponent")
                time.sleep(3)
                print("\n If one player casts the GOD spell, the other player cannot cast the GOD spell too in the same round")
                time.sleep(3)
                print("\n The next one is the RESSURECT Spell")
                time.sleep(3)
                print("\n With this spell you can bring back a superhero back from the dead!")
                time.sleep(3)
                print("\n A card that was already played either by you or your opponent will be picked at random and placed on the top of your deck")
                time.sleep(3)
                print("\n It will then be used to fight the battle")
                time.sleep(3)
                print("\n As always, the player with the highest value for the chosen characteristic wins the round")
                time.sleep(3)
                print("\n Note: The resurrect spell can only be played before choosing the next card & characteristic")
                time.sleep(3)
                print("\n To play the RESSURECT spell, enter r/ressurect after you've chosen the characteristic to challenge your opponent")
                time.sleep(3)
                print("\n Lastly, each player gets only one GOD & RESSURECT spell each")
                time.sleep(3)
                print("\n So use them wisely")
                print("\n All the best!!")
                time.sleep(5)
                print("\n Let the battle begin")
                break
            elif require_instruction.lower() =='n' or require_instruction.lower() =='no':
                print("\n All the best!!! Let the battle begin ;)")
                break
            else:
                print("\n Enter valid input dummy!")
     
    def playerRollDice(self,player):
        if player.lower() != comp:
            print("\n {} press ENTER to roll the dice".format(player))
            input()
        else:
            print("\n Computer has rolled the dice")
            
        value = random.randint(1, 6)
        print("\n No. rolled is {}".format(value))
        return value
        
    def diceThrowWinner(self):
        if self.p1dice > self.p2dice:
            print("\n {} has won the dice throw!".format(self.player1_name))
            time.sleep(0.5)
            print("You begin first....")
            self.starting_player = 1
        elif self.p1dice < self.p2dice:
            if self.mode =='s':
                print("\n The Computer has won the dice throw!")
                time.sleep(0.5)
                print("\n It begins first....")
            else:
                print("\n {} has won the dice throw!".format(self.player2_name))
                time.sleep(0.5)
                print("\n You begin first....")
            self.starting_player = 2
        else:
            self.starting_player = 0
        
        
    def decideStartPlayer_Beginning(self):
        while True:          
           self.p1dice = self.playerRollDice(self.player1_name)
           if self.mode=='s':
            self.p2dice = self.playerRollDice(comp)
           else:
            self.p2dice = self.playerRollDice(self.player2_name)
                
           self.diceThrowWinner()
           if self.starting_player!=0:
               break
           
           print("\n It's a tie :/ ...Players roll the dice again !!")
                 
    def shuffleDeck(self,value):
        if value == 'c':
            random.shuffle(self.characters)
        else:
            random.shuffle(self.outdated)
        
    def splitDeck(self):
        self.player1 = self.characters[0:5]
        self.player2 = self.characters[5:10]
      
    def pickCharacteristicToChallenge(self):
       print("Pick a characteristics to challenge your opponent")
       while True:
           characteristic = input("Strength(s/strength) | Agility (a/agility) | Intelligence (i/intelligence)? ")
           if characteristic.lower()== 's' or characteristic.lower()== 'strength':
                characteristic='strength'
                break
           elif characteristic.lower()== 'a' or characteristic.lower()== 'agility':
                characteristic='agility'
                break
           elif characteristic.lower()== 'i' or characteristic.lower()== 'intelligence':
                characteristic='intelligence'
                break
           else:
               print("Pick a valid characteristic to challenge!!!")
       return characteristic
            
    def playFirstCardOfDeck(self):
        if self.current_winner == 1:
            temp = self.player1[0]
            print("Picking a card from {}'s deck".format(self.player1_name))
            print("Character: ",self.player1[0]['character'])
            print("Characteristics")
            print("Strength: {}, Agility: {}, Intelligence: {}".format(self.player1[0]['strength'],self.player1[0]['agility'],self.player1[0]['intelligence']))
            self.player1.pop(0)
        else:
            temp = self.player2[0]
            print("Picking a card from {}'s deck".format(self.player2_name))
            print("Character: ",self.player2[0]['character'])
            print("Characteristics")
            print("Strength: {}, Agility: {}, Intelligence: {}".format(self.player2[0]['strength'],self.player2[0]['agility'],self.player2[0]['intelligence']))
            self.player2.pop(0)
        return temp
                  
    def resurrect(self):
          self.shuffleDeck('o')
          print("The resurrect spell has been cast and {} has risen from the dead".format(self.outdated[0]['character']))
          res = self.outdated.pop(0)
          return res
        
    
    def finalWinner(self):
        print("---------Scores-----------")
        print("{}: {}".format(self.player1_name,self.player1Pts))
        print("{}: {}".format(self.player2_name,self.player2Pts))
        if (self.player1Pts > self.player2Pts):
            print("Winner is {}".format(self.player1_name))
        elif (self.player1Pts < self.player2Pts):
            print("Winner is {}".format(self.player2_name))
        elif (self.player1Pts == self.player2Pts):
            print("Damn you both are good!!, It's a tie !!")
        
    def playOpponentCard(self):
        if self.current_winner != 1:
            ltemp = self.player1[0]
            print("Picking a card from {}'s deck".format(self.player1_name))
            print("Character: ",self.player1[0]['character'])
            print("Characteristics")
            print("Strength: {}, Agility: {}, Intelligence: {}".format(self.player1[0]['strength'],self.player1[0]['agility'],self.player1[0]['intelligence']))
            self.player1.pop(0)
            
        else:
            ltemp = self.player2[0]
            print("Picking a card from {}'s deck".format(self.player2_name))
            print("Character: ",self.player2[0]['character'])
            print("Characteristics")
            print("Strength: {}, Agility: {}, Intelligence: {}".format(self.player2[0]['strength'],self.player2[0]['agility'],self.player2[0]['intelligence']))
            self.player2.pop(0)
        return ltemp
        
    def computeRoundWinner(self, p1_char, p2_char):
        if int(p1_char) > int(p2_char):
            self.player1Pts = self.player1Pts + 1
            print("\n Score is ---- Player 1 : {} , Player 2 : {} ----".format(self.player1Pts,self.player2Pts))
            print("\n Winner of this round is {}".format(self.player1_name))
            self.current_winner = 1
        else:
            self.player2Pts = self.player2Pts + 1
            print("\n Score is ---- Player 1 : {} , Player 2 : {} ----".format(self.player1Pts,self.player2Pts))
            print("\n Winner of this round is {}".format(self.player2_name))
            self.current_winner = 2
                   
    def multiPlayerGame(self):
        self.outdated=[]
        self.player1Pts=0
        self.player2Pts=0
        self.player1_resurrect = 0 
        self.player2_resurrect = 0
        self.player1_god = 0 
        self.player2_god = 0
        self.rounds=1
        self.current_winner = self.starting_player
        while True:
            print(self.player1,self.player2)
            print("\n ROUND ",self.rounds)
            #Both players have played resurrect and deck is empty
            if not self.player1 and not self.player2 and self.player1_resurrect==1 and self.player2_resurrect==1:  
                self.finalWinner()
                break
            #Player 1 deck is empty and has not played resurrect 
            elif not self.player1 and self.player1_resurrect == 0:
                if self.current_winner == 1:
                    print(" You have to cast the RESURRECT spell")
                    p1 = self.resurrect()
                    print("Character: ",p1['character'])
                    print("Characteristics")
                    print("Strength: {}, Agility: {}, Intelligence: {}".format(p1['strength'],p1['agility'],p1['intelligence']))          
                    ch = self.pickCharacteristicToChallenge()
                    self.player1_resurrect = 1
                    if not self.player2 and self.player2_resurrect == 0:
                        print(" You have to cast the RESURRECT spell")
                        p2 = self.resurrect()
                        print("Character: ",p2['character'])
                        print("Characteristics")
                        print("Strength: {}, Agility: {}, Intelligence: {}".format(p2['strength'],p2['agility'],p2['intelligence']))
                           
                        self.player2_resurrect == 1
                    elif self.player2_resurrect == 1:
                        p2 = self.playOpponentCard()
                    print(p1,p2)
                    self.computeRoundWinner(p1[ch],p2[ch])
                    self.finalWinner()
                    break
                else:
                    if not self.player2 and self.player2_resurrect == 0:
                        print(" You have to cast the RESURRECT spell")
                        p2 = self.resurrect()
                        print("Character: ",p2['character'])
                        print("Characteristics")
                        print("Strength: {}, Agility: {}, Intelligence: {}".format(p2['strength'],p2['agility'],p2['intelligence']))
                        self.player2_resurrect == 1
                    elif self.player2_resurrect == 1:
                        p2 = self.playFirstCardOfDeck()
                    ch = self.pickCharacteristicToChallenge()
                    print("{} turn".format(self.player1_name))
                    print(" You have to cast the RESURRECT spell {}".format(self.player1_name))
                    p1 = self.resurrect()
                    print("Character: ",p1['character'])
                    print("Characteristics")
                    print("Strength: {}, Agility: {}, Intelligence: {}".format(p1['strength'],p1['agility'],p1['intelligence']))
                    self.player1_resurrect = 1    
                    print(p1,p2)
                    self.computeRoundWinner(p1[ch],p2[ch])
                    self.finalWinner()
                    break
            #Player 2 deck is empty and has not played resurrect
            elif not self.player2 and self.player2_resurrect == 0:
                if self.current_winner == 2:
                    print(" You have to cast the RESURRECT spell")
                    p2 = self.resurrect()
                    print("Character: ",p2['character'])
                    print("Characteristics")
                    print("Strength: {}, Agility: {}, Intelligence: {}".format(p2['strength'],p2['agility'],p2['intelligence']))  
                    print(p2)
                    self.player2_resurrect = 1
                    ch = self.pickCharacteristicToChallenge()
                    if not self.player1 and player1_resurrect == 0:
                        print(" You have to cast the RESURRECT spell")
                        p1 = self.resurrect()
                        print("Character: ",p1['character'])
                        print("Characteristics")
                        print("Strength: {}, Agility: {}, Intelligence: {}".format(p1['strength'],p1['agility'],p1['intelligence']))
                        self.player1_resurrect == 1
                    elif self.player1_resurrect == 1:
                        p1 = self.playOpponentCard()
                    print(p1,p2)
                    self.computeRoundWinner(p1[ch],p2[ch])
                    self.finalWinner()
                    break   
                else:
                    if not self.player1 and player1_resurrect == 0:
                        print(" You have to cast the RESURRECT spell")
                        p1 = self.resurrect()
                        print("Character: ",p1['character'])
                        print("Characteristics")
                        print("Strength: {}, Agility: {}, Intelligence: {}".format(p1['strength'],p1['agility'],p1['intelligence']))
                        self.player1_resurrect == 1
                    elif self.player1_resurrect == 1:
                        p1 = self.playFirstCardOfDeck()
                    ch = self.pickCharacteristicToChallenge()
                    ("{} turn".format(self.player2_name))
                    print(" You have to cast the RESURRECT spell")
                    p2 = self.resurrect()
                    print("Character: ",p2['character'])
                    print("Characteristics")
                    print("Strength: {}, Agility: {}, Intelligence: {}".format(p2['strength'],p2['agility'],p2['intelligence']))
                    self.player2_resurrect = 1
                    print(p1,p2)
                    self.computeRoundWinner(p1[ch],p2[ch])
                    self.finalWinner()
                    #rounds = rounds + 1
                    break   
            
            #Both decks are not empty 
            else:
                    #Player 1 is the round winner and has not resurrected any card
                    print("current winner",self.current_winner)
                    if self.current_winner == 1 and self.player1_resurrect ==0:
                            print("{}'s turn".format(self.player1_name))
                            if self.rounds != 1:
                                p1 = self.wantToResurrect(1)
                                ch = self.pickCharacteristicToChallenge()
                                if self.player1_god == 0:
                                    p2 = self.wantToUseGodSpell(1)
                                    
                                    self.computeRoundWinner(p1[ch],p2[ch])
                                    self.rounds = self.rounds + 1
                                    
                                elif self.player1_god == 1:
                                    print("{}'s turn".format(self.player2_name))
                                    if self.player2_resurrect ==0:
                                        p2 = self.wantToResurrect(2)
                                    else:
                                        p2 =self.playOpponentCard()
                                    
                                    self.computeRoundWinner(p1[ch],p2[ch])
                                    self.rounds = self.rounds + 1
                                    
                            else:
                                print("{}'s turn".format(self.player1_name))
                                p1 = self.playFirstCardOfDeck()
                                ch = self.pickCharacteristicToChallenge()
                                p2 = self.wantToUseGodSpell(1)      
                                
                                self.computeRoundWinner(p1[ch],p2[ch])
                                self.rounds = self.rounds + 1
                                
                            self.outdated.append(p1)
                            self.outdated.append(p2)
                    elif self.current_winner == 2 and self.player2_resurrect ==0:
                        print("{}'s turn".format(self.player2_name))
                        if self.rounds != 1:
                                p2 = self.wantToResurrect(2)
                                ch = self.pickCharacteristicToChallenge()
                                if self.player2_god == 0:
                                    p2 = self.wantToUseGodSpell(2)
                                    
                                    self.computeRoundWinner(p1[ch],p2[ch])
                                    self.rounds = self.rounds + 1
                                    
                                elif self.player2_god == 1:
                                    print("{}'s turn".format(self.player1_name))
                                    if self.player1_resurrect ==0:
                                        p1 = self.wantToResurrect(1)
                                    else:
                                        p1 =self.playOpponentCard()
                                    
                                    self.computeRoundWinner(p1[ch],p2[ch])
                                    self.rounds = self.rounds + 1
                                     
                        else:
                            print("{}'s turn".format(self.player2_name))
                            p2 = self.playFirstCardOfDeck()
                            ch = self.pickCharacteristicToChallenge()
                            p1 = self.wantToUseGodSpell(2)      
                            
                            self.computeRoundWinner(p1[ch],p2[ch])
                            self.rounds = self.rounds + 1
                             
                        self.outdated.append(p1)
                        self.outdated.append(p2)
                    elif self.current_winner == 1 and self.player1_resurrect ==1:
                            print("{}'s turn".format(self.player1_name))
                            p1 = self.playFirstCardOfDeck()
                            ch = self.pickCharacteristicToChallenge()
                            if self.player1_god == 0:
                                p2 = self.wantToUseGodSpell(1)
                                
                                self.computeRoundWinner(p1[ch],p2[ch])
                                self.rounds = self.rounds + 1
                                
                            elif self.player1_god == 1:
                                print("{}'s turn".format(self.player2_name))
                                if self.player2_resurrect ==0:
                                    p2 = self.wantToResurrect(2)
                                else:
                                    p2 = self.playOpponentCard()
                                
                                self.computeRoundWinner(p1[ch],p2[ch])
                                self.rounds = self.rounds + 1
                                  
                            self.outdated.append(p1)
                            self.outdated.append(p2)
                    elif self.current_winner == 2 and self.player2_resurrect ==1:
                                print("{}'s turn".format(self.player2_name))
                                p2 = self.playFirstCardOfDeck()
                                ch = self.pickCharacteristicToChallenge()
                                if self.player2_god == 0:
                                        p1 = self.wantToUseGodSpell(2)
                                        
                                        self.computeRoundWinner(p1[ch],p2[ch])
                                        self.rounds = self.rounds + 1
                                        
                                elif self.player2_god == 1:
                                        print("{}'s turn".format(self.player1_name))
                                        if self.player1_resurrect==0:
                                            p1 = self.wantToResurrect(1)
                                        else:
                                            p1 = self.playOpponentCard()
                                        
                                        self.computeRoundWinner(p1[ch],p2[ch])
                                        self.rounds = self.rounds + 1
                                       
                                self.outdated.append(p1)
                                self.outdated.append(p2)
                            
                        
                    
                                     
    def wantToResurrect(self,v):
            while True:
                ans_resurrect = input("Do you want to resurrect a superhero? yes/y or no/n" )
                if ans_resurrect.lower() == 'y' or ans_resurrect == 'yes':
                    card = self.resurrect()
                    print("Character: ",card['character'])
                    print("Characteristics")
                    print("Strength: {}, Agility: {}, Intelligence: {}".format(card['strength'],card['agility'],card['intelligence']))
                    if v == 1:
                       self.player1_resurrect = 1
                    elif v == 2:
                       self.player2_resurrect = 1
                    return card
                    break
                elif ans_resurrect.lower() == 'n' or ans_resurrect == 'no':
                    if v ==1 and self.current_winner ==1:
                        card = self.playFirstCardOfDeck()
                    elif v ==2 and self.current_winner ==2:
                        card = self.playFirstCardOfDeck()
                    elif v ==1 and self.current_winner !=1:
                        card = self.playOpponentCard()
                    elif v ==2 and self.current_winner !=2:
                        card = self.playOpponentCard()
                    return card
                    break
                else: 
                    print("Enter valid input !!!")
                
    def wantToUseGodSpell(self,v):
            while True:
                ans_godspell = input("Do you want to cast the God spell? yes/y or no/n" )
                if ans_godspell.lower() == 'y' or ans_godspell.lower() == 'yes':
                    card = self.godSpell(v)
                    print("Character: ",card['character'])
                    print("Characteristics")
                    print("Strength: {}, Agility: {}, Intelligence: {}".format(card['strength'],card['agility'],card['intelligence']))
                   
                    if v == 1:
                        print("{}'s card".format(self.player2_name))
                        self.player1_god = 1
                    elif v == 2:
                        print("{}'s card".format(self.player1_name))
                        self.player2_god = 1
                    return card
                    break
                elif ans_godspell.lower() == 'n' or ans_godspell.lower() == 'no':
                    if self.rounds!=1:
                        if v ==1: 
                            if self.player1_resurrect == 0:
                                print("{}'s turn".format(self.player1_name))
                                card = self.wantToResurrect(1)
                            else:
                                card = self.playFirstCardOfDeck()
                        elif v ==2:
                            if self.player2_resurrect == 0:
                                print("{}'s turn".format(self.player2_name))
                                card = self.wantToResurrect(2)
                            else:
                                card = self.playFirstCardOfDeck()
                    else:
                        card = p2 = self.playOpponentCard()  
                        
                    return card
                    break
                else: 
                    print("Enter valid input !!!")
        
    def godSpell(self,v):
            print("Showing Opponents cards")
            if v ==1:
                p2_showDeck =[]
                for i in self.player2: 
                    p2_showDeck.append(i['character'])
                print("Superhero in Opponents deck are {}".format(p2_showDeck))
                while True:
                    try:
                        val = int(input("Choose card that the opponent must play from 1 to {}".format(len(self.player2))))
                        if val<1 or val > len(self.player2):
                            print("Enter valid input")
                        else:
                            break
                    except:
                        print("Invalid input")
                    
                card = self.player2[val -1] 
                self.player2.pop(val-1)
               
            elif v ==2:
                p1_showDeck =[]
                for i in self.player1: 
                    p1_showDeck.append(i['character'])
                print("Superhero in Opponents deck are {}".format(p1_showDeck))
                while True:
                    val = int(input("Choose card that the opponent must play from 1 to {}".format(len(self.player1))))
                    if (val <1 or val > len(self.player1)):
                        print("Enter valid input")
                    else:
                        break
                card = self.player1[val -1] 
                self.player1.pop(val-1)
                
            return card 
        
#Main program 
play = battleground_superheroes()
play.introduction()
play.decideStartPlayer_Beginning()
play.shuffleDeck('c')
play.splitDeck()
play.multiPlayerGame()


     