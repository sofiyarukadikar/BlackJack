import random

class Deck:
    def __init__(self):
        self.cards =[]
        suites=["spade","clubs","hearts","diamonds"]
        ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        rankss=[]
        for rank in ranks:
            dummy={"rank":"dum","value":"dum"}
            value=rank
            if(rank=="A"):
                value=11
                dummy["rank"]=rank
                dummy["value"]=value
                rankss.append(dummy)
            elif rank =="J" or rank=="K" or rank=="Q":
                value=10
                dummy["rank"]=rank
                dummy["value"]=value
                rankss.append(dummy)
            else:
                dummy["rank"]=rank
                dummy["value"]=value
                rankss.append(dummy)
                    
        
        for suite in suites:
            for rank in rankss:
                self.cards.append(Cards(suite,rank))
    def shuffle(self):
            if len(self.cards)>1:            
              random.shuffle(self.cards)  


    def deal(self,number):
            list=[]
            for x in range(number):
                if len(self.cards)!=0:
                  list.append(self.cards.pop())
            return list    
        

class Cards:
    def __init__(self,suites,rank):
        self.suites=suites
        self.rank=rank
        
    def __str__(self):
        return f"{self.rank['rank']} of {self.suites}"


class Hand:
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer
    
    def add_card(self,card_list):
        self.cards.extend(card_list)
    def calculate_value(self):
        self.value=0
        has_ace=False
         
        for card in self.cards:
            card_value=int(card.rank["value"])
            self.value+=card_value
            if card.rank["rank"] == "A":
                has_ace =True

        if has_ace and self.value>21:
            self.value-=10        

    def get_value(self):
        self.calculate_value()
        return self.value        
    

    def is_blackjack(self):
        return self.value == 21
    def display(self,show_all_dealercards=False):
        print(f'''{"Dealer's" if self.dealer else "Your "}Hand: ''')
        for enumerat,card in enumerate(self.cards):
            if enumerate ==0 and self.dealer and not show_all_dealercards and not self.is_blackjack():
                print("hidden")
            else:
                 print(card)
        if not self.dealer:

            print("Value",self.get_value())    
        print()

class Game:
    def play(self):
        self.game_number=0
        self.games_to_play=0
        while(self.games_to_play<=0):
            try:
                self.games_to_play=int(input("How many games would you like to play?"))
            except:
                print("Enter an integer value for number of games")     
        while self.game_number < self.games_to_play:
            self.game_number+=1
            deck=Deck()
            deck.shuffle()
            player_hand=Hand()
            dealer_hand=Hand(dealer=True)
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            print()
            print("*"*30)    
            print(f"game {self.game_number} of {self.games_to_play}")
            print("*"*30)    
            player_hand.display()
            dealer_hand.display()


            if self.check_winner(player_hand,dealer_hand):
                continue


            choice=""
            while( player_hand.get_value()<21) and choice not in ["s","stand"]:
                choice=input("please choose 'Hit' or 'Stand' : ").lower()
                print()
                while choice not in ["h","s","stand","hit"]:
                    choice=input("please choose 'Hit' or 'Stand' : ").lower()
                    print()
                if choice in ["hit","h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()  
            
            if self.check_winner(player_hand,dealer_hand):
                continue       
            player_hand_value=player_hand.get_value()
            dealer_hand_value=dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value=dealer_hand.get_value()

            dealer_hand.display(show_all_dealercards=True) 
            if self.check_winner(player_hand,dealer_hand):
                continue    

 

    def check_winner(self,player_hand,dealer_hand,game_over=False):
            if not game_over:
                if player_hand.get_value()>21:
                    print("You Busted. Dealer wins!")
                    return True
                
                elif player_hand.get_value()>21:
                    print("Dealer Busted. You wins!")

                elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                    print("Both players have blackjack! Tie")    
                    return True
            else:
                if player_hand.get_value()>dealer_hand.get_value():
                    print("You win!")
                elif player_hand.get_value()== dealer_hand.get_value():
                    print('Tieee!!')    
                else:
                    print("Dealer wins!") 
                return True           
            return False

g=Game()
g.play()