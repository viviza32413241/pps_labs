from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, race_data):
        pass


class RaceBoard(Observer):
    def __init__(self):
        self.current_position = 0
        self.average_speed = 0
        self.lap_time = 0
        self.last_three_laps = []

    def update(self, race_data):
        self.current_position = race_data['current_position']
        self.average_speed = race_data['average_speed']
        self.lap_time = race_data['lap_time']
        self.last_three_laps = race_data['last_three_laps']
        self.display()

    def display(self):
        print("Current Position:", self.current_position)
        print("Average Speed:", self.average_speed)
        print("Lap Time:", self.lap_time)
        print("Last Three Laps:")
        for i, lap_data in enumerate(self.last_three_laps, start=1):
            print(" Lap", i, "Position:", lap_data['position'], "Speed:", lap_data['speed'], "Time:", lap_data['time'])
        print("")


class StatisticsDisplay(Observer):
    def __init__(self):
        self.last_three_laps_data = []

    def update(self, race_data):
        self.last_three_laps_data = race_data['last_three_laps']
        self.display()

    def display(self):
        print("Statistics for Last Three Laps:")
        for i, lap_data in enumerate(self.last_three_laps_data, start=1):
            print(" Lap", i, "Position:", lap_data['position'], "Speed:", lap_data['speed'], "Time:", lap_data['time'])
        print("")


class RaceDataSubject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, race_data):
        for observer in self.observers:
            observer.update(race_data)

    def set_race_data(self, race_data):
        self.notify_observers(race_data)

if __name__ == "__main__":
    race_data_subject = RaceDataSubject()

    race_board = RaceBoard()
    statistics_display = StatisticsDisplay()

    race_data_subject.register_observer(race_board)
    race_data_subject.register_observer(statistics_display)

    race_data = {
        'current_position': 1,
        'average_speed': 200,
        'lap_time': 60,
        'last_three_laps': [
            {'position': 1, 'speed': 200, 'time': 60},
            {'position': 1, 'speed': 210, 'time': 58},
            {'position': 2, 'speed': 195, 'time': 62}
        ]
    }
    race_data_subject.set_race_data(race_data)