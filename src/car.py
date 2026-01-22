class TooMuchFuelError(Exception):
    pass


class NotEnoughFuelError(Exception):
    pass


class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0.0  # ОСТАВЛЯЕМ 0 как было

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float):
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise TooMuchFuelError
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float):
        # Считаем, что расход 8 литров на 100 км
        fuel_burned: int = 8 * (distance_km / 100)
        # TODO: Вася, не забудь расскомментировать! Клиенты могут застрять!!11  # noqa: FIX002
        
        # ДОБАВЛЯЕМ АВТОЗАПРАВКУ если топлива мало
        if self._fuel_in_tank < fuel_burned:
            self.refuel_car(fuel_burned - self._fuel_in_tank)
        
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
