import sys
import argparse


def main():
    """Main function to process scores."""

    INPUT_TEXT_FILE_NAME = sys.argv[1]

    win = 3
    draw = 1
    lose = 0
    team_and_score = {}

    # Open file
    with open(INPUT_TEXT_FILE_NAME, encoding='utf-8') as input_file:
        count = 0
        line = input_file.readline()
        while line:
            count += 1
            # Extract line, replace newline and split on comma
            split_line = line.replace('\n', '').split(',')
            
            # Split the teams by space (' ') using the rightmost space to prevent team names e.g. FC Awesome from being split
            team_1, team_1_score = split_line[0].rsplit(' ', 1)
            team_2, team_2_score = split_line[1].rsplit(' ', 1)

            # Convert to integer and remove trailing or leading whitespaces
            team_1_score = int(team_1_score)
            team_2_score = int(team_2_score)
            team_1 = team_1.strip()
            team_2 = team_2.strip()

            # Init scoring
            if team_1 not in team_and_score:
                team_and_score[team_1] = 0
            if team_2 not in team_and_score:
                team_and_score[team_2] = 0

            # Do scoring
            if team_1_score > team_2_score:
                team_and_score[team_1] += win
            elif team_1_score == team_2_score:
                team_and_score[team_1] += draw
                team_and_score[team_2] += draw
            else:
                team_and_score[team_2] += win

            # Read next line
            line = input_file.readline()


        team_and_score_sorted = {val[0]: val[1] for val in sorted(team_and_score.items(), key=lambda x: (-x[1], x[0]))}
        count = 0
        # Print the formatted values
        for team, value in team_and_score_sorted.items():
            count += 1
            print(f"{count}. {team}, {value} pts")


if __name__ == "__main__":

    # Get input text file from command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    sys.argv[1] = args.filename

    main()
