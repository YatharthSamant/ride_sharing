from typing import List, Optional
from .user import Driver, Rider, Location

class City:
    def __init__(self, name: str):
        self.name = name
        self.available_drivers: List[Driver] = []
        self.pending_rides: List[Rider] = []

    def add_driver(self, driver: Driver) -> None:
        self.available_drivers.append(driver)

    def add_ride(self, ride: Rider) -> None:
        self.pending_rides.append(ride)

    def find_nearest_driver(self, rider_location: Location) -> Optional[Driver]:
        # In production, implement actual nearest driver algorithm
        return next((driver for driver in self.available_drivers if driver.is_available), None)
