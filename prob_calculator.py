import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = list()
    for k, v in kwargs.items():
      for i in range(0, v):
        self.contents.append(k) 
  
  def draw(self, num: int):
    drawn = list()

    for i in range(0, num):
      num_balls = len(self.contents)
      if num_balls == 0:
        break
      ix = random.randint(0, num_balls-1)
      drawn.append(self.contents[ix])

      # pop chosen ball from contents
      self.contents[ix] = self.contents[-1]
      self.contents.pop()
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  num_satisfied_exp = 0
  for exp in range(0, num_experiments):
    hat_copy = copy.deepcopy(hat)
    step_output = hat_copy.draw(num_balls_drawn)
    is_satisfied = True
    
    for color in expected_balls.keys():
      print()
      if step_output.count(color) < expected_balls[color]:
        is_satisfied = False
        break
    if is_satisfied:
      num_satisfied_exp += 1

  return num_satisfied_exp/num_experiments