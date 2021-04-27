
def tournamenet_winner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam : 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        print(idx, competition)
        homeTeam, awayTeam = competition
        print(homeTeam, awayTeam)

        winningTeam = homeTeam if result == 1 else awayTeam

        if winningTeam not in scores:
            scores[winningTeam] = 0

        scores[winningTeam] += 3
        
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam

if __name__ == '__main__':
    competitions = [
        ["HTML","C#"],
        ["C#","Python"],
        ["Python","HTML"]
    ]
    results = [0,0,1]
    bestTeam = tournamenet_winner(competitions, results)
    print("Best Team is ", bestTeam)
