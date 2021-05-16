from typing import List

number = ["", "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

twelve_days = ["twelve Drummers Drumming", "eleven Pipers Piping", "ten Lords-a-Leaping",
         "nine Ladies Dancing", "eight Maids-a-Milking", "seven Swans-a-Swimming",
         "six Geese-a-Laying", "five Gold Rings", "four Calling Birds",
         "three French Hens", "two Turtle Doves", "a Partridge in a Pear Tree."]


def line(n: int) -> str:
    template = f"On the {number[n]} day of Christmas my true love gave to me: "
    insertion = "" if n == 1 else ", and "
    return template + ", ".join(twelve_days[-n:-1]) + insertion + twelve_days[-1]


def recite(start_verse: int, end_verse: int) -> List[str]:
    """Return the verses of the Twelve Days of Christmas based on the day."""
    return [line(n) for n in range(start_verse, end_verse + 1)]
