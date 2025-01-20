from typing import Dict, Optional
from ..models.city import City
from ..models.user import Driver, Rider
from ..models.ride import Ride

class RideMatchingService:
    def __init__(self):
        self.cities: Dict[str, City] = {}

    def add_city(self, city_name: str) -> None:
        if city_name not in self.cities:
            self.cities[city_name] = City(city_name)

    def add_driver(self, city_name: str, driver: Driver) -> None:
        if city_name in self.cities:
            self.cities[city_name].add_driver(driver)

    def match_ride(self, city_name: str, rider: Rider) -> Optional[Ride]:
        if city_name in self.cities:
            city = self.cities[city_name]
            nearest_driver = city.find_nearest_driver(rider.current_location)
            
            if nearest_driver:
                ride = rider.request_ride(rider.destination)
                ride.driver = nearest_driver
                nearest_driver.accept_ride(ride.ride_id)
                ride.update_status(RideStatus.PENDING)
                return ride
            else:
                city.add_ride(rider)
                return None
        return None