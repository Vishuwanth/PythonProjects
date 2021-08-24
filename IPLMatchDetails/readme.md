Write a program that reads all the match outcomes and summarizes the information of all the matches.
Points are given to the teams based on the outcome of the match.
A win earns a team 3 points. A draw earns 1. A loss earns 0.
The following information is expected:
MP: Matches Played
W: Matches Won
D: Matches Drawn (Tied)
L: Matches Lost
P: Points

The team information should be displayed in descending order of points.
Input

The first line contains a single integer N, denoting the total no. of matches played.
The following N lines contain outcomes of N matches.
Each of those lines has information on the teams (T1, T2) which played and the outcome (O) in format T1;T2;O.
The outcome (O) is one of 'win', 'loss', 'draw' and refers to the first team listed.
See Sample Input/Output for better understanding.
The team name may contain spaces.
Output

The output should contain summarized information of all the matches in a format similar to 'Team: CSK, Matches Played: 4, Won: 2, Lost: 1, Draw: 1, Points: 7' for each team in a new line.
If there are no teams to print in summary, print "No Output".
Constraints

Names of teams may contain spaces but will be less than 24 characters
100 >= N >= 0
