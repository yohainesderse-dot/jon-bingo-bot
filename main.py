import random
import time

print("Welcome to Jon Bingo Bot!")
print("-----------------------")

# የቢንጎ ቁጥሮችን ከ1 እስከ 75 መፍጠር
numbers = list(range(1, 76))

# ቁጥሮቹን በዘፈቀደ ቅደም ተከተል ማስተካከል (Shuffle)
random.shuffle(numbers)

print("Bot is starting the Bingo game...")
print("Let's play Bingo! The numbers will be called out one by one.")
print("Press Ctrl+C to stop the game.")
print("-----------------------")

# ቁጥሮቹን አንድ በአንድ ማውጣት
for number in numbers:
    print(f"Next number: {number}")
    time.sleep(2) # ለ2 ሰከንድ መጠበቅ (እንዲያነብ ለማመቻቸት)
    
    # ሁሉም ቁጥሮች ሲያልቁ
    if number == numbers[-1]:
        print("-----------------------")
        print("All numbers have been called! Game over.")
        break

