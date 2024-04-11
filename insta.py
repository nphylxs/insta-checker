import sys
import csv
import instaloader


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: py insta.py [username]")
    username = sys.argv[1]
    #create an insance of imported class
    L = instaloader.Instaloader()

    #logging in
    try:
        L.login("expe_riment23","devashish2008")
    except:
        sys.exit("Couldn't login to the dummy account.")
    print("Logged in")

    #getting profile
    profile = instaloader.Profile.from_username(L.context, username)
    #getting list of followers
    cfollowers = []
    for follower in profile.get_followers():
        cfollowers.append(follower.username)
    print("Obtained followers list")

    #getting list of following
    cfollowing = []
    for person in profile.get_followees():
        cfollowing.append(person.username)
    print("Obtained following list")

    #followers check
    checker(username, cfollowers, "followers")

    #following check
    checker(username, cfollowing, "followings")
    
def checker(username: str, data: list, category: str):
    try:
        with open(f"{username}_{category}.csv", "r") as file:
            follows = []
            reader = csv.reader(file)
            for row in reader:
                follows.extend(row)
            print(f"Un{category}: ")
            i = 1
            for person in follows:
                if person not in data:
                    print(f"{i}. {person}")
                    i+=1
            if i == 1:
                print("NONE")
            print(f"New {category}: ")
            i = 1
            for person in data:
                if person not in follows:
                    print(f"{i}. {person}")
                    i+=1
            if i == 1:
                print("NONE")     
    except FileNotFoundError:
        print(f"No {category} records for {username}. Saved the current version.")  
    with open(f"{username}_{category}.csv", "w") as file:
        for person in data:
            file.write(person + '\n')

if __name__ == "__main__":
    main()