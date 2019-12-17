# CSCI4131_Final
1. project type A
2. Group Members : Andrew Sheehan
3. https://github.com/sheeh272/CSCI4131_Final
4. https://cs4131final-deploy.herokuapp.com/login
5. This application uses the technologies
        -Google Knowlege Graphs
        -flask
        -twitter bootstrap
        -html/css/javascript
        -sql
        -heroku
        -WTForms
6.  After the user logs in it directs them to the index page.  On this page they can choose from one of three players.
    Next the user should choose to view info about the player, games of the player or exercises from the player.  Once sumbit is clicked the user will be redirected to the respective page.  The playerinfo page draws its info and the picture of the player from the Google Knowledge graphs api.  On the chessgames page the user can move foward or backwards in a game using the nextmove and back move buttons.  Or they can select a new game with the nextgame or prevgame buttons.  On the exercises page the user can click to get a new exercise or hover over to solution to view it.  There is also an about page briefly describing project.  bootstrap used to format elements using bootstrap row/column system.

7.
    -controller for index which routes to initial page after login.
    -controller for form submision for when user submits form on index
    -controller to get to about page when user hits button in nav bar.

8.
    -base template
    -login/registration templates
    -template for index
    -template for about page
    -template for displaying players games
    -template for displaying players exercises
    -template for displaying playerinfo
   
9.
    -table of players contains name as well as flag(path to picture of it)
        the reason it cointains to flag path is so it can render it next to the players name for a nice look
    -games table:
            players table has a 1 to many relationship with this table
            contains fields player1, player2 and chess game notation
    -tactics table:
        tactic is chess jargon for a certain type of chess exersize.
        players table has a 1 to many relationship with this table.  Contains players name from where
        exercise was taken as well as path to picture of chess board displaying picture of it as well as solution.
    
10.
    chess information taken from
    wtharvey.com : for chess exercises
    chessgames.com : for chess games
    
    
    
    
