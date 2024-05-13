from Test import Basketball
from Test import Bored

def main():
    api_token = "354ae034a6mshfba4ca44ab43425p1da669jsn9d7187c4078f"
    basketball_leagues = Basketball(api_token)
    print("Что связанное с баскетболлом:")
    print(basketball_leagues)
    
    random_activity = Bored()
    print("\Какая то активность:")
    print(random_activity)

if __name__ == "__main__":
    main()
