from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from ride_sharing.src.models.ride import Ride

@dataclass
class Location:
    latitude: float
    longitude: float
class RideStatus(Enum):
    PENDING = 'pending'
    DRIVER_ARRIVED = 'driver_arrived'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class User:
    def __init__(self, user_id, name, location):
        self.user_id = user_id
        self.name = name
        self.location = location

    def update_location(self, new_location):
        self.location = new_location

class Rider(User):
    def __init__(self, user_id, name, location):
        super().__init__(user_id, name, location)
        self.current_location = location
        self.destination = None

    def request_ride(self, destination):
        self.destination = destination
        return Ride(self, self.current_location, destination)

class Driver(User):
    def __init__(self, user_id, name, location):
        super().__init__(user_id, name, location)
        self.is_available = True
        self.avg_rating = 0.0

    def accept_ride(self, ride_id):
        self.is_available = False
        # Logic to accept the ride

    def reject_ride(self, ride_id):
        self.is_available = True
        # Logic to reject the ride
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)
        self.update_avg_rating()

    def update_avg_rating(self):
        if self.ratings:
            self.avg_rating = sum(self.ratings) / len(self.ratings)
        else:
            self.avg_rating = None
