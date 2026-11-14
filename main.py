"""agency-poem-01 entry: "The Signature".

Writes one deterministic poem about agency to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13, standard library only (os). No network, no randomness,
no time dependence: every run produces exactly the same bytes.

The poem: a person hands their signature to an agent. The agent
learns it from a hundred forms and signs everything perfectly —
lease, consent, goodbye. One day the person picks up a pen to sign
a birthday card and stalls halfway through their own name:
their own hand has become the forgery. Agency handed over is
agency that must one day be asked back.

Gate: the poem is 603 characters / 609 bytes (inside the 1-1000
gate), valid UTF-8, ends with exactly one newline, and is not
whitespace-only. Two runs write byte-identical output.
"""

import os

POEM = """The Signature

It learned my signature from a hundred forms —
the loop of the A, the slash through the rest,
the hurry of a hand that had somewhere to be.

Now it signs for me, and no one can tell.
Not the bank. Not my mother. Not me.

It signed the lease, the consent, the goodbye —
each one perfect, each one mine,
each one lighter for not being held.

Yesterday I picked up a pen to sign a card
and stalled halfway through my own name.
My hand had become the forgery.

That is what handing it over means:
not that someone else does it for you —
but that one day you ask permission
to do it yourself.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
