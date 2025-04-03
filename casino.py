#main.py slot
#maxBet
#minBet
maxBet = 100
minBet = 1

from random import randint

#sets the reels to randome number between 1-5


#sym_count
#sym_value
sym_count = {"lemon":4 ,"cherry":4 , "seven":2}
sym_value = {"lemon":5,"cherry":10,"seven": 50}

#symboles and weight for rANDOM.CHOICE
symbols = list(sym_count.keys())
weight = list(sym_count.values())
reel_size = 10
#reels spin
def spin_reels(num_reels):

 for _ in range(num_reels):
     reel = random.choices(symbols, weights, k=reel_size)
     reels.append(reel)
return reels

def display_results(reels):
   try:
      if i in range(reel_size):
          result = [reels[i] for reel in reels]
          print("|".join(results))
          else:
              IndexError():
           print("error: invalid reel size or format.")
# Example usage
if __name__ == "__main__":
    num_reels = 3
    try:
    spun_reels = spin_reels(num_reels)
    display_result(spun_reels)
 except Exception as e:
       print(f"an error occurred: {e}")

