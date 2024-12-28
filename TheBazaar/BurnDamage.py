class Item:
    def __init__(self, name, stack_value, cooldown, increases_burn=False):
        """
        Represents an item that applies fire stacks.
        
        :param name: Name of the item.
        :param stack_value: Number of fire stacks applied by the item.
        :param cooldown: Time in seconds before the item can be used again.
        :param increases_burn: If True, increases all fire stack values by +1.
        """
        self.name = name
        self.stack_value = stack_value
        self.cooldown = cooldown
        self.increases_burn = increases_burn


def simulate_fire_damage(items, duration):
    """
    Simulates fire damage over a given duration based on item effects.

    :param items: List of Item objects representing the items used.
    :param duration: Total simulation duration in seconds.
    :return: Total damage dealt and a breakdown of damage per tick.
    """
    # Initialize variables
    total_damage = 0
    damage_per_tick = []
    fire_stacks = 0
    time_elapsed = 0
    item_timers = {item: 0 for item in items}  # Tracks cooldowns for each item

    # Main simulation loop
    while time_elapsed < duration:
        # Apply item effects
        for item in items:
            if item_timers[item] <= 0:  # Item is off cooldown
                # Add fire stacks
                fire_stacks += item.stack_value
                if item.increases_burn:
                    fire_stacks += 1  # Apply burn increase effect
                # Reset item cooldown
                item_timers[item] = item.cooldown

        # Calculate damage for this tick
        damage_this_tick = max(0, fire_stacks)
        total_damage += damage_this_tick
        damage_per_tick.append((time_elapsed, damage_this_tick))

        # Decrease fire stacks
        fire_stacks = max(0, fire_stacks - 1)

        # Advance time
        time_elapsed += 0.5  # Each tick is 0.5 seconds
        for item in items:
            item_timers[item] = max(0, item_timers[item] - 0.5)

    return total_damage, damage_per_tick


def display_damage_summary(total_damage, damage_per_tick):
    """
    Displays a summary of fire damage simulation.

    :param total_damage: Total damage dealt during the simulation.
    :param damage_per_tick: List of tuples (time, damage_at_time).
    """
    print(f"\nTotal Damage: {total_damage}")
    print(f"{'Time (s)':<10} {'Damage':<10}")
    print("-" * 20)
    for time, damage in damage_per_tick:
        print(f"{time:<10} {damage:<10}")


# Example usage
if __name__ == "__main__":
    # Define items
    flame_item = Item(name="Ray", stack_value=2, cooldown=6)
    burn_augment = Item(name="Core", stack_value=6, cooldown=3.33, increases_burn=True)

    # Input items and simulation time
    items = [flame_item, burn_augment]
    duration = 40  # Simulate for 10 seconds

    # Run simulation
    total_damage, damage_per_tick = simulate_fire_damage(items, duration)

    # Display results
    display_damage_summary(total_damage, damage_per_tick)