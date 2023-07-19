import random

class VacuumEnvironment:
    def __init__(self):
        self.status = {
            'loc_a':random.choice(['Clean','Dirty']),
            'loc_b':random.choice(['Clean','Dirty'])
        }


class Agent:
    def __init__(self):
        self.agent_status = 'active'
        self.location = random.choice(['loc_a','loc_b'])
        self.env = VacuumEnvironment()
        self.cost = 0

    def action_suck(self):
        self.percept('suck')
        self.env.status[self.location] = 'Clean'
        self.cost = self.cost + 1

    def action_move(self,direction):
        self.percept(direction)
        if(direction == 'left'):
            self.location = 'loc_a'
        else:
            self.location = 'loc_b'

        self.cost = self.cost + 1

    def percept(self,action):
        print("Percept: ",tuple([self.location,action]))

    def take_action(self):
        if(self.location == 'loc_a'):
            if self.env.status['loc_a'] == 'Dirty':
                print("Environement A is dirty.")
                self.action_suck()
                print("Environment A is clean")
                print("After suck:",self.cost)
                self.action_move('right')
                print("After moving\\ right",self.cost)
                print("-------------------------")

            else:
                print("Environment A is clean")
                self.action_move('right')
                print("After movig right",self.cost)
                print("--------------------------")

        elif(self.location == 'loc_b'):
            if self.env.status['loc_b'] == 'Dirty':
                print("Environment B is dirty.")
                self.action_suck()
                print("Environment B is clean")
                print("After suck:",self.cost)
                self.action_move('left')
                print("After moving left",self.cost)
                print("---------------------------")
            else:
                print("Environment B is clean")
                self.action_move('left')
                print("After moving left",self.cost)
                print("--------------------------")
        else:
            print("Agent is lost")

agent = Agent()
iterations = 10
for i in range(iterations):
    #agent.take_action()
    if agent.env.status['loc_a'] == 'Clean' and agent.env.status['loc_b'] == 'Clean':
        print("Since both rooms are clean, agent goes inactive")
        agent.agent_status = 'inactive'
        break
    agent.take_action()