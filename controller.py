import csv


def write_line(filename, line):
    file = open(f'files/{filename}', 'a', newline='')
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(line)
    file.close()


def import_csv(filename):
    file = open(f'files/{filename}', 'r')
    csv_reader = csv.reader(file, delimiter=',')
    ret = []
    next(csv_reader)
    for row in csv_reader:
        print(row)
        ret = ret + [row]
    file.close()
    print(ret)
    return ret


def write_csv(header, filename, data):
    file = open(f'files/{filename}', 'w', newline='')
    file.truncate()
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(header)
    for line in data:
        csv_writer.writerow(line)
    file.close()


def voter_registered(voter_info):
    registered_voters = import_csv('registeredVoters.csv')
    for voter in registered_voters:
        if voter == voter_info:
            return True
    return False


def not_voted(voter_info):
    already_voted = import_csv('alreadyVoted.csv')
    for voter in already_voted:
        if voter == voter_info:
            return False
    return True


def count_vote(voter, vote):
    if voter_registered(voter):
        if not_voted(voter):
            if vote == 0:
                return 'Please select someone to vote for'
            candidates = import_csv('candidates.csv')
            candidate_value = vote - 1
            choice = candidates[candidate_value][0]
            candidates[candidate_value][2] = int(candidates[candidate_value][2]) + 1
            write_csv(['Candidates', 'Party', 'Votes'], 'candidates.csv', candidates)
            write_line('alreadyVoted.csv', voter)
            return f'You voted for {choice}'
        else:
            return 'You already voted!'
    return 'Voter isn\'t registered or voter info is incorrect'


def get_candidates():
    candidates = import_csv('candidates.csv')
    can1_name = candidates[0][0]
    can1_party = candidates[0][1]
    can2_name = candidates[1][0]
    can2_party = candidates[1][1]
    return [f'{can1_name} ({can1_party})', f'{can2_name} ({can2_party})']
