import random

rules = [
    ((), 0),
    ((1,), 100),
    ((1, 1), 200),
    ((1, 1, 1), 1000),
    ((1, 1, 1, 1), 2000),
    ((1, 1, 1, 1, 1), 3000),
    ((1, 1, 1, 1, 1, 1), 4000),
    ((2,), 0),
    ((2, 2), 0),
    ((2, 2, 2), 200),
    ((2, 2, 2, 2), 400),
    ((2, 2, 2, 2, 2), 600),
    ((2, 2, 2, 2, 2, 2), 800),
    ((3,), 0),
    ((3, 3), 0),
    ((3, 3, 3), 300),
    ((3, 3, 3, 3), 600),
    ((3, 3, 3, 3, 3), 900),
    ((3, 3, 3, 3, 3, 3), 1200),
    ((4,), 0),
    ((4, 4), 0),
    ((4, 4, 4), 400),
    ((4, 4, 4, 4), 800),
    ((4, 4, 4, 4, 4), 1200),
    ((4, 4, 4, 4, 4, 4), 1600),
    ((5,), 50),
    ((5, 5), 100),
    ((5, 5, 5), 500),
    ((5, 5, 5, 5), 1000),
    ((5, 5, 5, 5, 5), 1500),
    ((5, 5, 5, 5, 5, 5), 2000),
    ((6,), 0),
    ((6, 6), 0),
    ((6, 6, 6), 600),
    ((6, 6, 6, 6), 1200),
    ((6, 6, 6, 6, 6), 1800),
    ((6, 6, 6, 6, 6, 6), 2400),
    ((1, 2, 3, 4, 5, 6), 1500),
    ((2, 2, 3, 3, 4, 6), 0),
    ((2, 2, 3, 3, 6, 6), 1500),
    ((1, 1, 1, 2, 2, 2), 1200),
]

recorded = []
scored_points = []
new_tuple = []
last_rolled = []
def random_num():
    return random.randint(1, 6)


class Dice:
    def __init__(self, value):
        self.sides = 6,
        self.occurences = 0,
        self.value = value


def calculate_score(input):
    # Dictionary to track die value
    tracked_dice = {}
    tracked_vals = {}
    tracker_id = 0

    input = sorted(input)
    straight_dice = [input]
    #print(straight_dice)
    for x in input:
        die = Dice(x)
        if x not in tracked_dice.keys():
            tracked_dice.update({x: 1})
        else:
            update_count = tracked_dice[x] + 1
            tracked_dice[x] = update_count


    aggregate(tracked_dice)


    #print(score)


def aggregate(tracked_dice):
    print("dice 1:",tracked_dice)
    all_results=[]
    straight_dice = []

    # Calculate and store repetitive die rolls (i.e. 3 5s)
    for die in tracked_dice:
        times_rolled = tracked_dice.get(die)
        #print(f'{die} was rolled {times_rolled}')

        straight_dice.append(die)

        die_result = []

        for result in range(times_rolled):
            die_result.append(die)
        all_results.append(die_result)

    all_results.append(straight_dice)
    check_for_points(all_results)

def check_for_points(all_results):
    # for die in tracked_dice:
    #     num_of_occurences =tracked_dice[die]
    #         #print(die,num_of_occurences)
    #     recorded.append(die)
    #     format_values(die, num_of_occurences)
    x = 1
    #For each result check against the rules
    for result in all_results:
        #print(all_results)
        # Check against each rule
        for index, value in enumerate(rules):
            rule = rules[index][0]
            score = value[1]
            print(result, list(rule), score)

            if result == list(rule):
                scored_points.append(int(score))
            x = x + 1
    return sum(scored_points)


            #Check if the result is in the ruleset
        #     if result == rule:
        #         scored_points.__add__(score)





    # Calculate values for the last four rules


    # Check die results against the rules and store points





    # def format_values(die, num_of_occurences):
    #     #print(f"ff + {die}, {num_of_occurences}")
    #
    #     x = 0
    # print(str(die))
    #
    # for x in range(num_of_occurences):
    #     if die in last_rolled:
    # #             new_tuple.append(die)
    # #
    # #
    #         # initialize list
    #     # test_list = [(4, (5, 'Gfg')), (7, (8, 6))]
    #
    #         # printing original list
    #         #print("The original list is : " + str(test_list))
    #
    #         # Unpacking nested tuples
    #         # using list comprehension + * operator
    #     rule_list = [(z, str(b)) for z, b in rules]
    #
    #     for rule in rule_list:
    #            # print(ress)
    #             try:
    #                 #print(rule[0])
    #                 point_value = rule[1]
    #                 criteria = rule[0]
    #                 #print(str(point_value))
    #                # print(new_tuple)
    #                 if point_value > 0 and criteria == tuple(new_tuple):
    #                    print(f"Criteria: {criteria} | Point-Value: {point_value}----------------- {new_tuple}")
    #
    #             except:
    #                 return 'not found'
    #
    # def check_for_points(tracked_dice):
    #
    #     #print(tracked_dice)
    #
    #     for die in tracked_dice:
    #         num_of_occurences =tracked_dice[die]
    #         #print(die,num_of_occurences)
    #         recorded.append(die)
    #
    #         format_values(die, num_of_occurences)

    #Check for points
# Loop through list and print
# if key is 1 thru 6 check for succession and award [points]

# last_4_rules = ((1, 2, 3, 4, 5, 6), 1500),

# check ((2, 2, 3, 3, 4, 6), 0),
# check ((2, 2, 3, 3, 6, 6), 1500),
# check ((1, 1, 1, 2, 2, 2), 1200),


# Loop through the rules and accumulate points

calculate_score((1,5,5,1,2,2))

print(sum(scored_points))