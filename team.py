from datetime import datetime
import threading

class Team:
    def __init__(self, name, token, problem):
        self.token = token
        self.name = name
        self.last_submission = None
        self.last_submission_time = None
        self.last_submission_score = None
        self.count_submission = 0
        self.problem = problem
        self.problem.add_team(name)
        self.lock = threading.Lock()  # this prevents multiple submissions from the same team
        

    def submit(self, d):
        self.lock.acquire()
        self.count_submission += 1
        ret = -1
        if self.count_submission <= 30:
            self.last_submission = d
            self.last_submission_score, self.last_submission_time = self.problem.new_submission(self.name, d)
            ret =  self.last_submission_score
        self.lock.release()
        return ret, self.last_submission_time
        
        
    
