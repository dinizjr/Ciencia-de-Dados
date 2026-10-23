import csv


def process_file(input_file):

    total_tournament = 0
    total_attendance = 0
    total_matches_played = 0
    total_goals_scored = 0
    country_winner = 0
    brazil_between_winners = 0
    france_in_third = []
    attendance_final_0 = 0
    total_goals_54_90 = 0
    winners = {}

    # csv reader without header
    with open(input_file, 'r',) as f:
        reader = csv.reader(f)
        next(reader)

        # iterate over lines
        for line in reader:
            # total of tournament
            total_tournament += 1

            # total of matches played
            total_matches_played += int(line[8])

            # total of goals scored
            total_goals_scored += int(line[6])

            # total of attendance
            attendance = int(line[9].replace('.', ''))
            total_attendance += attendance

            # when country was winner
            if line[1] == line [2]:
                country_winner += 1

            # public sum of events with year with final 0
            if line[0].endswith('0'):
                attendance_final_0 += attendance

            # goals between 1954 and 1990
            year = int(line[0])
            if 1954 <= year <= 1990:
                total_goals_54_90 += int(line[6])

            # each times Brazil was between the four finalists
            if(line[2] == 'Brazil' or line[3] == 'Brazil' or
               line[4] == 'Brazil' or line[5] == 'Brazil'):
                brazil_between_winners += 1

            # each times France was third
            if line[4] == 'France':
                france_in_third.append(line[0])

            # winners
            if winners.get(line[2]) is None:
                winners[line[2]] = 1
            else:
                winners[line[2]] += 1


    # output results
    with open('/temp/WorldCupsOutput.txt', 'w') as output:
        output.write('Soma de público das copas com final 0: {0}\n'.format(attendance_final_0))
        output.write('Quantidade total de gols entre as copas de 1954 e 1990: {0}\n'.format(total_goals_54_90))
        output.write('Média de público: {0}\n'.format(total_attendance / total_tournament))
        output.write('Média de gols por partida: {0:.2f}\n'.format(total_goals_scored / total_matches_played))
        output.write('Quantidade de vezes em que o país sede foi campeão: {0}\n'.format(country_winner))
        output.write('Quantidade de vezes em que o time do Brasil ficou entre uma das 4 primeiras posições: {0}\n'.format(brazil_between_winners))
        output.write('Ano das edições em que o time da França finalizou em terceiro lugar: {0}\n'.format(','.join(map(str, france_in_third))))
        output.write('Quantidade de vitórias por país, classificada em ordem crescente do número de títulos:\n')
        for win in sorted(winners.items(), key=lambda kv: kv[1]):
            output.write('\t' + '{0}:{1}'.format(win[0], win[1])  + '\n')


process_file('/temp/WorldCups.csv')