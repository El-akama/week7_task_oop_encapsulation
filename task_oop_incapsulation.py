# task1
# class Car:

#     def __init__(self, make, model, year, odometer=0, fuel=70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel

#     def __add_distance(self, km):
#         self.odometer += km

#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel

#     def drive(self, km):
#         if self.fuel * 10 >= km:
#             self.__add_distance(km)
#             kml = km // 10
#             self.__subtract_fuel(kml)
#             print('Let’s drive!')
#         else:
#             print('Need more fuel!')

# a = Car('japan', 'toyota', 2020, 70)
# a.drive(100)
# print(a.odometer)
# print(a.fuel)

# task2 
# class Mobile:

#     __imeil = "samsung"
#     __battery = 100
#     __info = 'ssd'
#     __os = 'charity'

#     def listen_music(self):
#         self.__battery -= 5
#         print(f'играет музыка, заряд батареи {self.__battery} %')

#     def watch_video(self):
#         self.__battery -=7
#         print(f"смотрим видео, заряд батареи {self.__battery} %")
#         if self.__battery <= 10:
#             print(f"не смотрим видео, заряд батареии {self.__battery} %")
        
#     def battery_charging(self):
#         self.__battery = 100
#         print('батарея заряжена')

#     def info_battery(self):
#         if self.__battery == 0:
#             raise Exception ("батарея разряжена, нужно подзарядить")
#         else:
#             print(self.__battery)

# m = Mobile()
# m.listen_music()
# m.listen_music()
# m.listen_music()
# m.listen_music()
# m.listen_music()
# m.listen_music()
# m.watch_video()
# m.watch_video()
# m.watch_video()
# m.watch_video()
# m.watch_video()
# m.watch_video()
# m.watch_video()
# m.watch_video()
# # m.watch_video()
# # m.watch_video()       # чтобы вызвать ошибку
# m.info_battery()
# m.battery_charging()
# m.info_battery()


# task3
# делаю