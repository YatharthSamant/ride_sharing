from typing import List, Optional
from .user import Driver, Rider, Location
import time
from geopy.distance import geodesic # type: ignore

class City:
    def __init__(self, name: str):
        self.name = name
        self.available_drivers: List[Driver] = []
        self.pending_rides: List[Rider] = []

    def add_driver(self, driver: Driver) -> None:
        self.available_drivers.append(driver)

    def add_ride(self, ride: Rider) -> None:
        self.pending_rides.append(ride)

    def get_distance(loc1: Location, loc2: Location) -> float:
        """
        Calculate the distance between two locations using their latitude and longitude.

        Args:
            loc1 (Location): The first location.
            loc2 (Location): The second location.

        Returns:
            float: The distance between the two locations in kilometers.
        """
        return geodesic((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).kilometers

    def find_nearest_driver(self, rider_location: Location) -> Optional[Driver]:
        """
        Finds the nearest available driver to the given rider location.

        Args:
            rider_location (Location): The location of the rider.

        Returns:
            Optional[Driver]: The nearest available driver if found, otherwise None.
        """
        available_drivers = [driver for driver in self.available_drivers if driver.is_available]
        if not available_drivers:
            return None

        # Sort drivers by distance to the rider and rating weightage
        available_drivers.sort(key=lambda driver: self.get_distance(driver.location, rider_location) * 0.8 - driver.rating * 0.2)

        # Batch processing
        batch_size = 20
        batch_time = 15  # seconds
        max_wait_time = 5 * 60  # 5 minutes

        for i in range(0, len(available_drivers), batch_size):
            batch = available_drivers[i:i + batch_size]
            for driver in batch:
                # Simulate sending request to driver
                driver.receive_ride_request(rider_location)
            
            time.sleep(batch_time)
            
            # Check if any driver accepted the ride
            for driver in batch:
                if driver.has_accepted_ride():
                    return driver

            # If total wait time exceeds max_wait_time, stop trying
            if (i // batch_size + 1) * batch_time >= max_wait_time:
                break

        return None