"""Solution to Kattis problem 'Accounting'"""
import sys

# ---------- Linear Probing Hash Map ----------
class LinearProbingMap:
    LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(self, capacity=8):
        self.N = capacity
        self.n = 0
        self.A = [None] * self.N

    def _hash(self, key):
        return hash(key) % self.N

    def _find_slot(self, key):
        """Find index of key or first empty slot."""
        i = self._hash(key)
        start = i
        while self.A[i] is not None and self.A[i][0] != key:
            i = (i + 1) % self.N
            if i == start:
                return None  # full map (handled via rehash)
        return i

    def _load_factor(self):
        return self.n / self.N

    def _rehash(self):
        """Double the table size and reinsert all entries."""
        old = self.A
        self.N *= 2
        self.n = 0
        self.A = [None] * self.N
        for entry in old:
            if entry is not None:
                key, value, ts = entry
                self.set(key, value, ts)

    def set(self, key, value, timestamp):
        """Insert or update (key, value, timestamp)."""
        if self._load_factor() >= self.LOAD_FACTOR_THRESHOLD:
            self._rehash()

        i = self._find_slot(key)
        if i is None:
            self._rehash()
            i = self._find_slot(key)

        if self.A[i] is None:
            self.n += 1
        self.A[i] = (key, value, timestamp)

    def get(self, key):
        """Return (value, timestamp) or None if missing."""
        i = self._hash(key)
        start = i
        while self.A[i] is not None:
            k, v, t = self.A[i]
            if k == key:
                return (v, t)
            i = (i + 1) % self.N
            if i == start:
                break
        return None


# ---------- Input Parsing ----------
def read_input():
    data = sys.stdin.read().strip().splitlines()
    N, Q = map(int, data[0].split())
    events = []
    for line in data[1:]:
        parts = line.split()
        if parts[0] == "SET":
            _, i, x = parts
            events.append(("SET", int(i), int(x)))
        elif parts[0] == "RESTART":
            _, x = parts
            events.append(("RESTART", int(x)))
        elif parts[0] == "PRINT":
            _, i = parts
            events.append(("PRINT", int(i)))
    return N, Q, events


# ---------- Main Logic ----------
def main():
    N, Q, events = read_input()

    table = LinearProbingMap(capacity=max(8, 2 * N))
    global_reset_value = 0
    last_reset_time = -1

    for t, event in enumerate(events):
        etype = event[0]

        if etype == "SET":
            person, value = event[1], event[2]
            table.set(person, value, t)

        elif etype == "RESTART":
            value = event[1]
            global_reset_value = value
            last_reset_time = t

        elif etype == "PRINT":
            person = event[1]
            entry = table.get(person)

            if entry is None:
                print(global_reset_value)
            else:
                person_value, person_time = entry
                if person_time > last_reset_time:
                    print(person_value)
                else:
                    print(global_reset_value)


if __name__ == "__main__":
    main()
