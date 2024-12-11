def main():



 time =  input("what time is it: ")
 time_code = convert(time)
 if 7<=time_code<=8:
        print("breakfast time")
 elif 12<=time_code<=13:
        print("lunch time")
 elif 18<=time_code<=19:
        print("dinner time")

def convert(time):
    time_parts = time.split(":")
    minute = float(time_parts[1])
    hour = float(time_parts[0])
    minutes = minute/60
    time_code = hour+minutes
    return time_code
if __name__ == "__main__":
    main()

