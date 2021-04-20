from grid_world import *

def Grid1d():
    grid1d = Grid(1, 7, (0, 1))
    rewards = {(0, 6): 1}
    actions = {
        (0, 0): ('R'),
        (0, 1): ('L','R'),
        (0, 2): ('L','R'),
        (0, 3): ('L','R'),
        (0, 4): ('L','R'),
        (0, 5): ('L','R'),
          }

    grid1d.set(rewards, actions)
    print('rewards=',grid1d.rewards)
    print('actions=',grid1d.actions)
    return grid1d

def Grid2d():
    grid = Grid(3, 4, (2, 0))
    rewards = {(0, 3): 1, (1, 3): -1}
    actions = {
        (0, 0): ('D', 'R'),
        (0, 1): ('L', 'R'),
        (0, 2): ('L', 'D', 'R'),
        (1, 0): ('U', 'D'),
        (1, 2): ('U', 'D', 'R'),
        (2, 0): ('U', 'R'),
        (2, 1): ('L', 'R'),
        (2, 2): ('L', 'R', 'U'),
        (2, 3): ('L', 'U'),  }

    grid.set(rewards, actions)
    print('rewards=',grid.rewards)
    print('actions=',grid.actions)    
    return grid

if __name__ == "__main__":
    #print three random actions 
    pass