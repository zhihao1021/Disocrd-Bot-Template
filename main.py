import discord

class Client(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)

if __name__ == '__main__':
    client = Client()
    client.run()