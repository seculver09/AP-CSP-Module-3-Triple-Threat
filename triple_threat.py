"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""

import random

def main() -> None:
    cost_to_play: int = 1
base_prize: int =10
mega_number: int =6    
mega_multiplier: int =10

    # roll three dice
   player, roll_1: int = random.randomint(1, 6)  
   player, roll_2: int = random.randomint(1, 6)  
   player, roll_3: int = random.randomint(1, 6) 
     # i they are, calculate the prize
    print(f"Casino collects:   ${cost_to_play}")
    print(f"Player rolls {roll_1}---{roll_2}---{roll_3}")
__name__ == "__main__": main()