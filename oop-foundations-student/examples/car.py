class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self._running = False  # underscore to hint at 'internal' use

    def drive(self) -> None:
        if not self._running:
            print("Starting engine...")
            self._running = True
        print(f"{self.make} {self.model} goes: Vroom!")

    def stop(self) -> None:
        if self._running:
            print("Engine off.")
            self._running = False
        else:
            print("Car is already stopped.")


if __name__ == '__main__':
    my_car = Car('Toyota', 'Camry')
    my_car.drive()
    my_car.stop()
