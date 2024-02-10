'''python dictionary with keys having multiple inputs'''
def main():
    places()

dict = {}

x, y, z = 10, 20, 30
dict[x, y, z] = z + y - z

x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z

print(dict)

def places():
    places = {("19.01", "72.54"): "Mumbai",
              ("28.33", "77.06"): "Delhi"}
    print(places)
    print('\n')
    lat = []
    long = []
    plc = []
    for i in places:
        lat.append(i[0])
        long.append(i[1])
        plc.append(places[i[0],i[1]])
    
    print(lat)
    print(long)
    print(plc)

if __name__ == "__main__":
    main()