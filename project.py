"""
Project Management
Estimate: 15 minutes
Actual: 10 minutes
"""

import datetime


class Project:
  def __init__(self, name, start_date, priority, estimate, completion):
    self.name = name
    self.start_date = start_date
    self.priority = priority
    self.estimate = estimate
    self.completion = completion

  def __str__(self):
    return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
           f"estimate: ${self.estimate}, completion: {self.completion}%"
