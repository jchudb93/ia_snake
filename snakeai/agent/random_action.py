import random
import numpy as np
from snakeai.agent import AgentBase
from snakeai.gameplay.entities import ALL_SNAKE_ACTIONS


def direction(head, body):
  x_head = head[1][0]
  y_head = head[0][0]
  x_body = body[1][0]
  y_body = body[1][0]

  if (x_head == x_body and y_head > y_body): return 0 # Mirando verticalmente para abajo
  if (x_head == x_body and y_head < y_body): return 1 # Mirando vericalmente para arriba
  if (y_head == y_body and x_head > x_body): return 2 # Mirando horizontalmente para la derecha
  if (y_head == y_body and x_head < x_body): return 3 # Mirando horizontalmente para la izquierda
  return -1

class RandomActionAgent(AgentBase):
    """ Represents a Snake agent that takes a random action at every step. """

    def __init__(self):
        self.actual_moves = 0
        self.cnt_moves = 0
        self.prev_moves = 0
        self.choice = 0
        pass

    def begin_episode(self):
        pass

    def act(self, observation, reward):
        self.food_coord = np.where(observation == 1)
        self.head_coord = np.where(observation == 2)
        self.body_coord = np.where(observation == 3)

        diff_x = self.head_coord[1][0] - self.food_coord[1][0]
        diff_y = self.head_coord[0][0] - self.food_coord[0][0]
        diff_x_body = self.body_coord[1][0] - self.food_coord[1][0]
        diff_y_body = self.body_coord[0][0] - self.food_coord[0][0]

        if (diff_y == 0 and diff_x != 0):
          # la comida esta a la izquierda o derecha y la serpiente esta mirando en esa direccion
          if ((diff_x > 0 and diff_y_body == 0 and diff_x_body > diff_x) or (diff_x < 0 and diff_y_body == 0 and diff_x_body < diff_x)):
            return ALL_SNAKE_ACTIONS[0]

          # mirando para abajo
          if (diff_x > 0 and diff_y_body < 0) or (diff_x < 0 and diff_y_body > 0):
            return ALL_SNAKE_ACTIONS[2]

          # mirando para arriba
          if (diff_x > 0 and diff_y_body > 0) or (diff_x < 0 and diff_y_body < 0):
            return ALL_SNAKE_ACTIONS[1]

        if (diff_x == 0 and diff_y != 0):
          # la comida esta arriba o abajo y la serpiente esta mirando en esa direccion
          if ((diff_y > 0 and diff_x_body == 0 and diff_y_body > diff_y) or (diff_y < 0 and diff_x_body == 0 and diff_y_body < diff_y)):
            return ALL_SNAKE_ACTIONS[0] # mantiene su direccion

          # mirando para la derecha
          if (diff_y > 0 and diff_x_body < 0) or (diff_y < 0 and diff_x_body > 0):
            return ALL_SNAKE_ACTIONS[1]

          # mirando para la izquierda
          if (diff_y > 0 and diff_x_body > 0) or (diff_y < 0 and diff_x_body < 0):
            return ALL_SNAKE_ACTIONS[2]

        # if (diff_x < 0 and diff_y < 0 and (direction(self.head_coord,self.body_coord) == 0 or direction(self.head_coord,self.body_coord) == 2)):
        #   return ALL_SNAKE_ACTIONS[0]
        # if (diff_x < 0 and diff_y < 0 and direction(self.head_coord,self.body_coord) == 1):
        #   return ALL_SNAKE_ACTIONS[2]
        # if (diff_x < 0 and diff_y < 0 and direction(self.head_coord,self.body_coord) == 3):
        #   return ALL_SNAKE_ACTIONS[1]

        # if (diff_x > 0 and diff_y > 0 and direction(self.head_coord,self.body_coord) == 0):
        #   return ALL_SNAKE_ACTIONS[1]
        # if (diff_x > 0 and diff_y > 0 and direction(self.head_coord,self.body_coord) == 1):
        #   return ALL_SNAKE_ACTIONS[0]



        return np.random.choice(ALL_SNAKE_ACTIONS)

    def end_episode(self):
        print(self.cnt_moves)
        pass

