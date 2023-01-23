'''Uh-huh'''


def main(score):
    '''Yeet'''
    score_a, score_b, match_set, winner = 0, 0, 1, None
    a_win, b_win, new_set = 0, 0, False
    for i in score:
        if i == 'A':
            score_a += 1
        elif i == 'B':
            score_b += 1
        if abs(score_a - score_b) >= 2:
            req_score = 25 if match_set < 5 else 15
            if score_a >= req_score and score_a > score_b:
                a_win += 1
                new_set = True
            elif score_b >= req_score and score_b > score_a:
                b_win += 1
                new_set = True
        if new_set:
            print("Set %d: A (%d) | B (%d)" % (match_set, score_a, score_b))
            match_set += 1
            score_a, score_b, new_set = 0, 0, False
            if a_win >= 3 or b_win >= 3:
                print("%s won %d:%d set" % (
                    "A" if a_win > b_win else "B" if a_win < b_win else '',
                    a_win if a_win > b_win else b_win if a_win < b_win else '',
                    b_win if a_win > b_win else a_win if a_win < b_win else '',
                ))
                winner = True
                break
    if not winner:
        print("Set %d: A (%d) | B (%d)" % (match_set, score_a, score_b))
        print('The game has not finished yet.')


main(input())
