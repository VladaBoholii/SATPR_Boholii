candidates = [
    ['A', 'C', 'D', 'B'],
    ['C', 'A', 'B', 'D'],
    ['B', 'C', 'D', 'A'],
    ['B', 'A', 'C', 'D']
]

amount_of_votes = [7, 7, 3, 3]

def print_scores(scores):
    for candidate, score in scores.items():
        print(f"{candidate}: {score}")

n = len(amount_of_votes)
m = len(candidates)

borda_weights = [3, 2, 1, 0]

scores = {candidate: 0 for candidate in candidates[0]}

for i in range(len(candidates)):
    for j in range(len(candidates[i])):
        scores[candidates[i][j]] += borda_weights[j] * amount_of_votes[i]

print("Результати:")

while len(scores) > 1:
    winner_borda = max(scores, key=scores.get)
    print(f"{winner_borda}")

    del scores[winner_borda]
    for vote in candidates:
        vote.remove(winner_borda)

    updated_scores = {candidate: 0 for candidate in scores}

    for i in range(len(candidates)):
        for j in range(len(candidates[i])):
            updated_scores[candidates[i][j]] += borda_weights[j] * amount_of_votes[i]


    scores = updated_scores

final_winner = max(scores, key=scores.get)
print(final_winner)
