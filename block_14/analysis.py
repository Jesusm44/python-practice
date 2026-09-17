import collections
from typing import Any, Counter

def count_ages(patients) -> Counter[Any]:
    age = []
    for patinent in patients:
        grup_age = patinent["age"]
        age.append(grup_age)

    return collections.Counter(age)

def group_age(patients) -> collections.defaultdict[Any, list[Any]]:
    gruoped = collections.defaultdict(list)
    for patient in patients:
        age = patient["age"]
        gruoped[age].append(patient)

    return gruoped

def waiting_queue(pantients):
    waiting = collections.deque()

    for patient in pantients:
        waiting.append(patient)

    return waiting

def next_patient(waiting):
    try:
        patient = waiting.popleft()
        return patient
    except IndexError:
        print("You don't have any patients in the queue.")