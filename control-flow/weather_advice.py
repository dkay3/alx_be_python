def get_clothing_advice():
  """
  Asks the user about the weather and provides clothing recommendations.
  """
  # Get user input for weather conditions
  weather = input("What is the weather like today (sunny, rainy, windy, cold, hot)? ").lower()

  # Use if-elif-else statements to provide clothing advice
  if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
  elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
  elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
  else:
    print("Sorry, I don't have recommendations for this weather.")

# Call the function to get clothing advice
get_clothing_advice()
