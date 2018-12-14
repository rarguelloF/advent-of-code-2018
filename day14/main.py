#!/usr/bin/env/python

import sys


class RecipiesState:
    def __init__(self, sequence):
        self.elf1_pos = 0
        self.elf2_pos = 1
        self.recipies = [3, 7]
        self.seq_matching = []
        self.matched = False
        self._check_sequence = sequence

        if self._check_sequence:
            for idx, rec in enumerate(self.recipies):
                if rec == sequence[idx]:
                    self.seq_matching.append(rec)


    def _get_new_pos(self, current, movements):
        return (current + movements) % len(self.recipies)


    def create_new(self):
        elf1_rec = self.recipies[self.elf1_pos]
        elf2_rec = self.recipies[self.elf2_pos]

        result = str(elf1_rec + elf2_rec)
        for num in result:
            self.recipies.append(int(num))

            if self._check_sequence and not self.matched:
                new_match = self.seq_matching + [int(num)]
                if new_match == self._check_sequence[:len(new_match)]:
                    self.seq_matching = new_match

                    if self.seq_matching == self._check_sequence:
                        self.matched = True
                else:
                    self.seq_matching = []


        self.elf1_pos = self._get_new_pos(self.elf1_pos, 1 + elf1_rec)
        self.elf2_pos = self._get_new_pos(self.elf2_pos, 1 + elf2_rec)


def p1(num_recipies):
    print("Number of recipies ->", num_recipies)

    state = RecipiesState([])

    while len(state.recipies) < (num_recipies + 10):
        state.create_new()

    return ''.join(str(x) for x in state.recipies[num_recipies:num_recipies+10])


def p2(sequence):
    print("Checking sequence ->", sequence)

    state = RecipiesState(sequence)

    while not state.matched:
        state.create_new()

    check_str = ''.join(str(x) for x in sequence)
    return ''.join(str(x) for x in state.recipies).index(check_str)


if __name__ == '__main__':
    try:
        num_recipies = int(sys.argv[1])
        sequence = [int(x) for x in sys.argv[2]]
    except Exception:
        print(f"Usage: {sys.argv[0]} <num_recipies (int)> <sequence (int)>")
        sys.exit(1)

    print("Part1 solution ->", p1(num_recipies))
    print("Part2 solution ->", p2(sequence))
