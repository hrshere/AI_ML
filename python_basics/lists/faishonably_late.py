'''
We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.

Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.
'''

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name,
      return whether the guest was fashi late
    """
    order = arrivals.index(name)

    return order >= len(arrivals)/2 and order != len(arrivals) - 1

def main():
    arrival_list = ["hrs","hrs1","hrs2","hrs3","hrs4","hrs5"]
    name = input('Enter name: ')
    if name in arrival_list:
        print(fashionably_late(arrival_list,name))
    else:
        print("name not present")

if __name__ == "__main__":
    main()