"""Solution to Kattis problem 'Accounting'"""
import sys

def read_input():
    data = sys.stdin.read().strip().splitlines()

    N, Q = map(int, data[0].split())
    events = []

    for line in data[1:]:
        parts = line.split()
        event_type = parts[0]

        if event_type == "SET":
            _, i, x = parts
            events.append(("SET", int(i), int(x)))
        elif event_type == "RESTART":
            _, x = parts
            events.append(("RESTART", int(x)))
        elif event_type == "PRINT":
            _, i = parts
            events.append(("PRINT", int(i)))

    return N, Q, events


def main():
    N, Q, events = read_input()

    global_reset_value = 0
    last_global_reset_at = -1
    hashmap = {i: (0, last_global_reset_at) for i in range(1, N + 1)}

    for t, event in enumerate(events):
        etype = event[0]

        if etype == "SET":
            person, value = event[1], event[2]
            hashmap[person] = (value, t)

        elif etype == "RESTART":  # <-- make sure this is uppercase!
            value = event[1]
            global_reset_value = value
            last_global_reset_at = t

        elif etype == "PRINT":
            person = event[1]
            person_value, person_time = hashmap[person]

            if person_time > last_global_reset_at:
                print(person_value)
            else:
                print(global_reset_value)

if __name__ == "__main__":
    main()
