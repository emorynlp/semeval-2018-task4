import os
import sys
import argparse
from sets import Set
from collections import Counter

OTHER = -1
MAIN = [59, 183, 248, 292, 306, 335]
TRAIN_ALL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 103, 104, 105, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 246, 247, 248, 249, 250, 251, 252, 254, 256, 257, 258, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 314, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 344, 345, 346, 347, 349, 350, 351, 352, 353, 354, 355, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 370, 372, 373, 374, 375, 376, 377, 378, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400]
ENTITY_LIST = [
'Abby',
'Al',
'Al Kostelic',
'Al Minser',
'Al Pacino',
'Alan',
'Albert Einstein',
'Alex',
'All',
'Amber',
'Amger',
'Andie McDowell',
'Andr',
'Andre',
'Andrea',
'Andrea\'s friend',
'Andrew',
'Angela Delvecchio',
'Annabelle',
'Artelle',
'Ashley',
'Aunt Edna',
'Aunt Iris',
'Aunt Lillian',
'Aunt Phyllis',
'Aunt Syl',
'Aurora',
'Avery',
'Barbara',
'Barry',
'Ben',
'Bernie Spellman',
'Best Man',
'Bethel',
'Betty',
'Big Bully',
'Bill Clinton',
'Bill Dreskin\'s father',
'Billy Dreskin',
'Bing',
'Bishop Tutu',
'Black Bart',
'Bob',
'Bobby Rush',
'Boss Man Bing',
'Brad',
'Braverman',
'Brent Mussberger',
'Brian',
'Brittany',
'Carl',
'Carol Willick',
'Carol and Susan\'s caterer',
'Carol\'s grandmother',
'Caroline',
'Casey',
'Casting Guy',
'Cathy Bates',
'Celia',
'Chandler Bing',
'Chandler\'s date',
'Chandler\'s date\'s husband',
'Chandler\'s date\'s husband\'s secretary',
'Chandler\'s ex-girlfriend',
'Chandler\'s girlfriend',
'Chandler\'s imaginary friend',
'Chandler\'s secretary',
'Charles Bing',
'Chrissy',
'Christine',
'Coma Guy',
'Customer',
'Damone',
'Dan',
'Dana',
'Danielle',
'Danny Arshak',
'Daryl Hannah',
'Dave Thomas',
'David Hasselhof',
'Deb',
'Debbie',
'Debra',
'Dee',
'Demi Moore',
'Denise DeMarco',
'Dick Clark',
'Dillon',
'Director',
'Director\'s Assistant',
'Donna Reid',
'Dorothy',
'Dr. Baldhara',
'Dr. Bazida',
'Dr. Drake Remoray',
'Dr. Flanen',
'Dr. Franzblau',
'Dr. Horton',
'Dr. Mitchell',
'Dr. Oberman',
'Dr. Remore',
'Dr. Rosen',
'Dr. Wong',
'Drew Barrymore',
'Dudley Moore',
'Duncan',
'Ed',
'Ed Begley',
'Eddie',
'Eddie Minowick',
'Eddie Moskowitz',
'Eddie\'s ex-girlfriend',
'Eddie\'s previous roommate',
'Emma',
'Eric Estrada',
'Eric Prower',
'Erica Ford',
'Ernest Borgnine',
'Err',
'Error',
'Estelle',
'Estelle Leonard',
'Esther Livingston',
'Ethan',
'Evelyn Dermer',
'Ewing',
'Fake Monica',
'Fleischman',
'Flench',
'Flight Attendant',
'Florence Henderson',
'Foghorn Leghorn',
'Frank Buffay',
'Frankie',
'Frannie',
'Freud',
'Fun Bobby',
'Gail',
'George',
'George Bailey',
'George Stephanopoulos',
'Girl',
'Girls',
'Gloria Tribbiani',
'Grandmother',
'Gunther',
'Guy',
'Guy 1',
'Guys',
'Hannibal Lecter',
'Helen',
'Henry',
'Hombre Man',
'Howard',
'Huey Lewis',
'Hugh Grant',
'Ingrid Bergman',
'Intercom',
'Interviewer',
'Ive',
'Jack',
'Jack 1',
'Jack 2',
'Jack Geller',
'Jade',
'James Bond',
'Jamie',
'Jane',
'Janice',
'Janitor',
'Jason Costalano',
'Jason Hurley',
'Jay Leno',
'Jeannie',
'Jill',
'Jill Goodacre',
'Jill Green',
'Jill\'s mom',
'Jim Crochee',
'Jimmy Hauser',
'Joan Collins',
'Joanne',
'Joanne\'s father',
'Joey Tribbiani',
'Joey Tribbiani Sr.',
'Joey\'s Co-star',
'Joey\'s cousin',
'Joey\'s date',
'Joey\'s date\'s friend',
'Joey\'s tailor',
'John Savage',
'John Voit',
'Johnny Shapiro',
'Jordie',
'Joseph Stalin',
'Judy Geller',
'Judy Jetson',
'Julie',
'Julie\'s friend',
'Karen',
'Kid',
'Kip',
'Kristin',
'Laurie Schaffer',
'Leon',
'Leonard Green',
'Leroy',
'Leslie',
'Liam Neeson',
'Lifson',
'Lily Buffay',
'Linda',
'Lipson',
'Little Bully',
'Lizzie',
'Lola',
'Lori',
'Lorne Green',
'Lorraine',
'Lowell',
'Luisa',
'Luisa\'s supervisor',
'Lydia',
'Lydia\'s baby',
'Lydia\'s husband',
'Lydia\'s mom',
'Malibu Ken',
'Man',
'Man 1',
'Man 2',
'Marcel',
'Marcel Marceau',
'Mark',
'Marsha',
'Marty',
'Mary Tyler Moore',
'Max',
'Melanie',
'Messier',
'Michael',
'Michelle',
'Milton',
'Mindy',
'Mira',
'Miss Buffay',
'Miss Crankypants',
'Miss Kitty',
'Moncia',
'Monica Geller',
'Monica\'s ex-boyfriend',
'Monica\'s grandmother',
'Morly Safer',
'Mother Theresa',
'Mover',
'Mr. Adelman',
'Mr. Clean',
'Mr. Douglas',
'Mr. Greene',
'Mr. Heckles',
'Mr. Peanut',
'Mr. Ratstatter',
'Mr. Roger',
'Mr. Roper',
'Mr. Salty',
'Mr. Treeger',
'Mr. Tribbiani',
'Mr. Wineburg',
'Mrs. Adelman',
'Mrs. Bing',
'Mrs. Buffay',
'Mrs. Cobb',
'Mrs. Geller',
'Mrs. Green',
'Mrs. Greene',
'Mrs. Tribbiani',
'Mrs. Wallace',
'Mrs. Wallace\'s sister',
'Mrs. Wineburg',
'Ms. Thomas',
'Nathan',
'Nina Bookbinder',
'Norman Mailer',
'Nurse',
'Paolo',
'Paul',
'Paul\'s ex-girlfriend',
'Paula',
'Paulo',
'Person 1',
'Person 2',
'Pete',
'Pete Carney',
'Phoebe Buffay',
'Phoebe and Rachel',
'Phoebe\'s Assistant',
'Phoebe\'s Friends',
'Phoebe\'s boyfriend',
'Phoebe\'s date',
'Phoebe\'s friend',
'Phoebe\'s grandmother',
'Phoebe\'s grandmother\'s boyfriend',
'Phoebe\'s hairdresser',
'Phoebe\'s stepfather',
'Phoebe, Joey, and Ross',
'Pizza Guy',
'Producer',
'Rachel Green',
'Rachel and Phoebe',
'Rachel\'s date',
'Rachel\'s friend',
'Rachel\'s interviewer',
'Rachel\'s interviewer\'s cousin',
'Rachel\'s sister',
'Radio',
'Ramone',
'Randy Brown',
'Receptionist',
'Richard',
'Richard Burke',
'Richard\'s son',
'Rick',
'Rob',
'Rob Dohnen',
'Rob Roy',
'Robbie',
'Robert Pillman',
'Rod Steiger',
'Rodney McDowell',
'Rodrigo',
'Roger',
'Roland',
'Rona',
'Ronni Rappelano',
'Rose',
'Rose Marie',
'Ross Geller',
'Ross\' date',
'Ross\' grandmother',
'Russ',
'Ryan',
'Sandra Green',
'Sandy',
'Scott Alexander',
'Security Guard',
'Shannon Cooper',
'Shelley',
'Shirley',
'Sidney Marks',
'Silvian',
'Soupy Sales',
'Spike Lee',
'Stacy Roth',
'Steffi Graf',
'Stella Niedman',
'Stephanie',
'Steve',
'Store Guy',
'Stranger',
'Susan Bunch',
'Susan Sallidor',
'Susie',
'Tanya',
'Tattoo Artist',
'Teacher',
'Terry',
'The Guys',
'The Whole Party',
'Tilly',
'Tina',
'Tina\'s husband',
'Toby',
'Tommy Rollerson',
'Tony',
'Tony DeMarco',
'Tony Randall',
'Tova Borgnine',
'Tracy',
'Trainer',
'Travis',
'Tso',
'Ugly Naked Guy',
'Uma Thurman',
'Uncle Freddie',
'Uncle Sal',
'Uncle Sal\'s wife',
'Underdog',
'Unknown',
'Ursula',
'Van Damme',
'Vidal Buffay',
'Waiter',
'Waitress',
'Warren Beatty',
'Wedding Planner',
'Wendy',
'Weve',
'Woman',
'Woman 1',
'Yamaguchi',
'Yasmine Blepe',
'Young Ethan'
]

main_entities = Set(MAIN + [OTHER])
all_entities  = Set(TRAIN_ALL + [OTHER])

def parse_key_file(filepath):
    with open(filepath, "rb") as f:
    	keys = []
    	for line in f:
    		line = line.strip()
    		if not line: return keys
    		try:
    			keys.append(int(line))
    		except ValueError:
    			print('Invalid key: "'+line+'" in '+filepath)
    			return None

        return keys
    return None

def measure_macro_f1(entities, correct_counts, auto_counts, gold_counts):
    f1s = dict()
    for entity in entities.intersection(gold_counts.keys()):
        if correct_counts[entity] != 0:
            p = float(correct_counts[entity]) / auto_counts[entity]
            r = float(correct_counts[entity]) / gold_counts[entity]
            f1s[entity] = [p, r, 2.0 * p * r / (p + r)]
        else:
            f1s[entity] = [0.0] * 3;
    return f1s

def main():
    parser = argparse.ArgumentParser(description="SemEval 2018 Task 4: Character Identification Evaluation Script")
    parser.add_argument("ref_out",  type=str, help="Path to the input directory that contains ref/answer.txt and res/answer.txt, that are the gold and the system output files")
    parser.add_argument("sys_out", type=str, help="Path to the output directory where scores.txt will be saved")
    args = parser.parse_args()

    # read key files
    gold_file = os.path.join(args.ref_out)
    auto_file = os.path.join(args.sys_out)
    gold_keys = parse_key_file(gold_file)
    auto_keys = parse_key_file(auto_file)

    if not auto_keys:
    	return

    if len(gold_keys) != len(auto_keys):
    	print('Key mismatch: gold = %d keys, system = %d keys' % (len(gold_keys), len(auto_keys)))
    	return

    # count correct entities
    main_correct     = Counter()
    all_correct      = Counter()
    gold_main_counts = Counter()
    gold_all_counts  = Counter()
    auto_main_counts = Counter()
    auto_all_counts  = Counter()

    for auto_key, gold_key in zip(auto_keys, gold_keys):
        # all entities
        auto_all_key = auto_key if auto_key in all_entities else OTHER
        gold_all_key = gold_key if gold_key in all_entities else OTHER

        auto_all_counts[auto_all_key] += 1
        gold_all_counts[gold_all_key] += 1
        if auto_all_key == gold_all_key: all_correct[auto_all_key] += 1

        # main + other entities
        auto_main_key = auto_key if auto_key in main_entities else OTHER
        gold_main_key = gold_key if gold_key in main_entities else OTHER

        auto_main_counts[auto_main_key] += 1
        gold_main_counts[gold_main_key] += 1
        if auto_main_key == gold_main_key: main_correct[auto_main_key] += 1

    # measure label accuracy
    total_count = len(gold_keys)
    all_accuracy  = float(sum(all_correct.values()))  / total_count
    main_accuracy = float(sum(main_correct.values())) / total_count

    # measure macro F1 scores
    all_f1  = measure_macro_f1(all_entities, all_correct, auto_all_counts, gold_all_counts)
    main_f1 = measure_macro_f1(main_entities, main_correct, auto_main_counts, gold_main_counts)

    all_avg_f1  = float(sum([prf[2] for prf in all_f1.values()]))  / len(all_f1)  if len(all_f1)  > 0 else 0.0
    main_avg_f1 = float(sum([prf[2] for prf in main_f1.values()])) / len(main_f1) if len(main_f1) > 0 else 0.0

    # print evaluation
    eval = [
    	'********** Main + Other Entities **********',
    	'Label Accuracy  : %6.2f (%d/%d)' % (100.0 * main_accuracy, sum(main_correct.values()), total_count),
    	'Average Macro F1: %6.2f' % (100.0 * main_avg_f1),
    	'************** All Entities ***************',
    	'Label Accuracy  : %6.2f (%d/%d)' % (100.0 * all_accuracy, sum(all_correct.values()), total_count),
    	'Average Macro F1: %6.2f' % (100.0 * all_avg_f1)]

    eval.append('***** Main + Other Entities F1 Scores *****')
    for key in sorted(main_f1.keys()):
        prf = main_f1[key]
    	name = ENTITY_LIST[key] if key >= 0 else '##OTHERS##'
        s = '%40s: P = %6.2f (%4d/%4d), R = %6.2f (%4d/%4d), F1 = %6.2f' % (name, prf[0] * 100.0, main_correct[key], auto_main_counts[key], prf[1] * 100.0, main_correct[key], gold_main_counts[key], prf[2] * 100.0)
        eval.append(s)

    eval.append('********* All Entities F1 Scores **********')
    for key in sorted(all_f1.keys()):
        prf = all_f1[key]
    	name = ENTITY_LIST[key] if key >= 0 else '##OTHERS##'
        s = '%40s: P = %6.2f (%4d/%4d), R = %6.2f (%4d/%4d), F1 = %6.2f' % (name, prf[0] * 100.0, all_correct[key], auto_all_counts[key], prf[1] * 100.0, all_correct[key], gold_all_counts[key], prf[2] * 100.0)
        eval.append(s)

    print('\n'.join(eval))
    # fout = open(os.path.join(args.output_dir, 'scores.txt'), 'w')
    # fout.write('accuracy:{0}\n'.format(100.0 * all_avg_f1))
    # fout.close()

    return all_accuracy, main_accuracy, all_avg_f1, main_avg_f1

if __name__ == "__main__":
    main()