
import random

class Game(): #class game with four methods
    
    def __init__(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        self.winner = self.get_game_result()
        
    @staticmethod
    def get_user_item(): #method to get user input
        
        user_item = input("Choose between (rock/paper/scissors) \n")
        first_choice= ["rock","paper","scissors"]
        
        for i in first_choice: # loop through the list of options
            
            if i == user_item:
                return user_item
            
            while user_item not in first_choice:
                user_item = input("Choose between (rock/paper/scissors) \n") 
    @staticmethod
    def get_computer_item(): #method for computer choice
        
        second_choice = ["rock","paper","scissors"]
        computer = random.choice(second_choice)
        return computer
    
    def get_game_result(self): #method to display winner
        if self.user_item == "rock" and self.computer_item == "paper":
            return "Computer"
        if self.user_item == "rock" and self.computer_item == "scissors":
            return "User "
        if self.user_item == "paper" and self.computer_item == "rock":
            return "User"
        if self.user_item == "scissors" and self.computer_item == "rock":
            return "Computer"
        if self.user_item == "rock" and self.computer_item == "rock":
            return "Draw"
        if self.user_item == "paper" and self.computer_item == "scissors":
            return "Computer"
        if self.user_item == "scissors" and self.computer_item == "paper":
            return "User"
        if self.user_item == "paper" and self.computer_item == "paper":
            return "Draw"
        if self.user_item == "scissors" and self.computer_item == "scissors":
            return "Draw"
    
    def play(self):  
        if self.winner == "Draw":     
           print(f'user 1 selected {self.user_item} and computer selected {self.computer_item} There a tie')
        else:
            print(f'user 1 selected {self.user_item} and computer selected {self.computer_item} The winner is {self.winner}')
                       
test = Game()


test.play()





   
    