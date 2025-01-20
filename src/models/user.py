from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple

from ride_sharing.src.models.ride import Ride

@dataclass
class Location:
    latitude: float
    longitude: float

class User(ABC):
    def __init__(self, user_id: str, name: str, location: Location):
        self.user_id = user_id
        self.name = name
        self.location = location

    def update_location(self, new_location: Location) -> None:
        self.location = new_location

class Rider(User):
    def __init__(self, user_id: str, name: str, location: Location):
        super().__init__(user_id, name, location)
        self.current_location = location
        self.destination = None

    def request_ride(self, destination: Location) -> 'Ride':
        from .ride import Ride
        self.destination = destination
        return Ride(self, self.current_location, destination)

class Driver(User):
    def __init__(self, user_id: str, name: str, location: Location):
        super().__init__(user_id, name, location)
        self.is_available = True

    def accept_ride(self, ride_id: str) -> None:
        self.is_available = False

    def reject_ride(self, ride_id: str) -> None:
        self.is_available = True
