from enum import Enum

class RideStatus(Enum):
    PENDING = 'pending'
    DRIVER_ARRIVED = 'driver_arrived'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'