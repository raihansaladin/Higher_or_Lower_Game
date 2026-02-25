import art, random
from game_data import data

print(art.logo)

def modify_a():
    """Memodifikasi/memindahkan data B ke data A"""
    global rand_data_name, rand_data_desc, rand_data_country, rand_data_follower
    rand_data_name = rand_data_name_B
    rand_data_desc = rand_data_name_B
    rand_data_country = rand_data_country_B
    rand_data_follower = rand_data_follower_B

def randomize_data_B():
    global data_B
    data_B = random.choice(data)

    return (
        data_B['name'], data_B['description'], data_B['country'], data_B['follower_count']
    )

def randomize_data():
    # call data for B random data
    data_A = random.choice(data)
    data_B = random.choice(data)

    while data_A == data_B:
        data_B = random.choice(data)

    return (
        data_A['name'], data_A['description'], data_A['country'], data_A['follower_count'],
        data_B['name'], data_B['description'], data_B['country'], data_B['follower_count']
    )

(rand_data_name, rand_data_desc, rand_data_country, rand_data_follower,
 rand_data_name_B, rand_data_desc_B, rand_data_country_B, rand_data_follower_B) = randomize_data()

score = 0
# running the game using while loops
running = True
while running:
    print(f"Compare A: {rand_data_name}, a {rand_data_desc}, from {rand_data_country}, {rand_data_follower}")
    print(art.vs)
    print(f"Compare B: {rand_data_name_B}, a {rand_data_desc_B}, from {rand_data_country_B}, {rand_data_follower_B}")
    compare = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Comparison
    if compare == "a":
        if rand_data_follower > rand_data_follower_B:
            score += 1
            print("\n"*25)
            print(art.logo)
            print(f"You're' right! Current score : {score}")
            modify_a()
            (rand_data_name_B, rand_data_desc_B, rand_data_country_B, rand_data_follower_B) = randomize_data_B()
        else :
            print(f"Sorry, that's wrong. Final score: {score}")
            running = False
            break
    elif compare == "b":
        if rand_data_follower_B > rand_data_follower:
            score += 1
            print("\n" * 25)
            print(art.logo)
            print(f"You're' right! Current score : {score}")
            modify_a()
            (rand_data_name_B, rand_data_desc_B, rand_data_country_B, rand_data_follower_B) = randomize_data_B()
        else :
            print(f"Sorry, that's wrong. Final score: {score}")
            running = False
            break
    else :
        print(f"Sorry, that's wrong. Final score: {score}")
        running = False
        break