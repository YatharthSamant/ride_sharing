from typing import Optional
import random
from .enums import RideStatus
from .user import Rider, Driver, Location

class Ride:
    def __init__(self, rider: Rider, pickup_location: Location, destination: Location):
        self.ride_id = str(id(self))  # In production, use UUID
        self.rider = rider
        self.driver: Optional[Driver] = None
        self.pickup_location = pickup_location
        self.destination = destination
        self.status = RideStatus.PENDING

    def update_status(self, new_status: RideStatus) -> None:
        self.status = new_status
        self.notify_parties()

    def notify_parties(self) -> None:
        # In production, use proper logging and notification service
        if self.driver:
            print(f"Driver {self.driver.name} notified: Ride status updated to {self.status.value}")
        print(f"Rider {self.rider.name} notified: Ride status updated to {self.status.value}")

    def driver_arrived(self) -> None:
        self.update_status(RideStatus.DRIVER_ARRIVED)

    def start_ride(self) -> None:
        self.update_status(RideStatus.IN_PROGRESS)

    def complete_ride(self) -> None:
        self.update_status(RideStatus.COMPLETED)

    def show_estimated_arrival_time(self) -> int:
        # In production, implement actual ETA calculation
        return random.randint(5, 15)

    def show_estimated_fare(self) -> float:
        # In production, implement actual fare calculation
        distance = random.uniform(1.0, 10.0)
        return round(distance * 1.5, 2)