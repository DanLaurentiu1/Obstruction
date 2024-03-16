## Project Status
🔴 Closed

## Description
[Obstruction](http://www.papg.com/show?2XMX) is a game where players take turns in marking squares on a grid. The first player unable to move loses. You can choose to play on any size grid

## Visuals
![ObstructionStartScreen](https://github.com/DanLaurentiu1/Obstruction/assets/91523577/8ce4eb84-7a78-4b1d-97ef-8e37223fd281)
![ObstructionGameScreen](https://github.com/DanLaurentiu1/Obstruction/assets/91523577/0e106e5c-a950-4052-8edb-6d0ec4b7988d)

## Features
This project is implemented in Python, using OOP and layered architecture

You can switch between: Graphical User Interface in PySimpleGUI and Text User Interface in ```UserInterface/settings.txt```

Unit-test for file operations, player and computer moves and board rendering

The computer will always win if it can do so in a **single move**. Also, if the board is of size **odd number x odd number** and the computer is going first, it is going to take the guaranteed win by playing in the middle and mirroring the player's moves
