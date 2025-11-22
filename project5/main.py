import copy
import random

class Hat:
    def __init__(self, **balls):
        """Create a hat with balls of different colors.
        balls: keyword arguments where key=color, value=count
        """
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """Draw num_balls randomly from the hat without replacement."""
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Perform a probability experiment drawing balls from a hat.

    Returns the probability of drawing at least the expected balls.
    """
    success_count = 0

    for _ in range(num_experiments):
        # Make a fresh copy of the hat for this experiment
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the number of each color drawn
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check if we have at least the expected number of each color
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    probability = success_count / num_experiments
    return probability