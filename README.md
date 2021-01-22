TABLE OF CONTENTS:

    General Info
    Prerequisites
    Setup
    Usage


GENERAL INFO

    Game Short info:
    The object of Yahtzee is to obtain the highest score from throwing 5 dice.
    The game consists of 13 rounds. In each round, you roll the dice and then score the roll in one of 13 categories. You must score once in each category. The score is determined by a different rule for each category.
    The game ends once all 13 categories have been scored.

    In my game I added extra game as two pair into lower part of the game. 
    For players who love to test I added extra rules such as 
    
    - When a roll collection is displayed after last (3rd) roll if you don't Press Enter then the code removes your last game from the list (upper or lower list) however it will still consider/evaluate your final collection against the calculation logic

    - If the user does not provide correct input they will be asked to enter correct input

    - If the user tries to choose wrong game from the provided lists twice then last game in the list (dict actually) will be removed. Depending on the case the score either can be evaluated or a zero score is forced for that turn

    - For chance game, if you have Yahtzee I believe user must be rewarded as getting Yahtzee which I did not know about it 
    
    - Game score table at the end is not sorted, I skipped to implement it.. It's reading the key-value pairs from a dict in the order of insertion means order of played games.

    Please feel free to improve the code, in player class a decorater function can be added for logging. Main class looks complicated a bit,  yes because I wanted to add new rules to make it fun but became a bit complicated.So decorators or extra methods can be used to make it look tidy.

    One more thing to improve is score table, I have just tried to use right justify but a better score table could be created


PREREQUISITES
    
    Python 3.6 or newer version is required
    

Setup

    sudo apt-get update
    sudo apt-get install python3.6

    # If you want to create exe for Windows or Mac
    pip install pyinstaller
    pip install pyinstaller --onedir --debug=all yahtzee_main.py


Usage

    python3 yahtzee_main.py
    
