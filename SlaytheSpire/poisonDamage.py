def calculate_poison_damage(initial_poison, rounds):
    """
    Calculate the total poison damage dealt over a given number of rounds in Slay the Spire.

    :param initial_poison: The initial amount of poison on the target.
    :param rounds: The number of rounds to calculate damage for.
    :return: A list of tuples showing the damage per round and total damage.
    """
    poison = initial_poison
    total_damage = 0
    damage_by_round = []

    for round_num in range(1, rounds + 1):
        if poison <= 0:
            break
        # Poison damage is dealt
        total_damage += poison
        damage_by_round.append((round_num, poison, total_damage))
        # Poison count decreases by 1
        poison -= 1

    return damage_by_round


def display_damage_summary(damage_data):
    """
    Display the damage calculation in a user-friendly way.

    :param damage_data: List of tuples (round, damage_this_round, total_damage)
    """
    print(f"{'Round':<6} {'Damage This Round':<20} {'Total Damage':<12}")
    print("-" * 38)
    for round_num, damage, total in damage_data:
        print(f"{round_num:<6} {damage:<20} {total:<12}")


# User input
try:
    initial_poison = int(input("Enter the initial poison count: "))
    rounds = int(input("Enter the number of rounds to simulate: "))

    damage_data = calculate_poison_damage(initial_poison, rounds)
    display_damage_summary(damage_data)

    if not damage_data:
        print("No poison damage dealt, as the poison count was 0 or negative.")

except ValueError:
    print("Invalid input. Please enter numeric values for poison count and rounds.")