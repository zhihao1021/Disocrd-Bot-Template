import discord, time, copy

class Log(discord.Client):
    def log(self, message, channel: int):
        print(message)

    def __date(self, mode=0):
        new_date = []
        for i in range(6):
            temp_time = time.localtime()[i]
            
        if mode == 0:
            return 0