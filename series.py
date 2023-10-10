import math

series_name = input("Enter series name: ")
season_num = int(input("How many seasons does it have: "))
episode_num = int(input("How many episodes per season does it have: "))
episode_lenght = int(input("How long is one episode: "))

total_time = season_num * (episode_num - 1) * episode_lenght

ads = total_time * 0.25

special = season_num * (episode_lenght + 12) + 0.25 * (episode_lenght + 12)

total_time += ads + special

print(f"I needed {math.floor(total_time)} minutes to watch {series_name}.")
