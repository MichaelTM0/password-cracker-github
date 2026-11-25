# Password Cracker

A command-line Python tool that demonstrates a brute-force attack. You type in a password, and the program tries every possible character combination until it finds a match, reporting how many attempts it took and how long it ran. It's a hands-on way to see why password length and character variety matter so much.

> **Note:** This is an educational tool. It brute-forces a password you enter yourself, on your own machine, to show how the guessing space grows. It does not target accounts, systems, or anyone else's data.

## ⚠️ Disclaimer — Educational Use Only

This project was built for **learning purposes** as part of my journey studying
Python and cybersecurity fundamentals. It runs entirely **locally** on a password
the user enters themselves, and it does **not** target, access, or attempt to
compromise any real account, system, or network.

It is intended to demonstrate core programming concepts (loops, `itertools`,
input validation, efficiency) and to illustrate *why* password length and
complexity matter. Please do not use it for anything other than education on
systems you own.

## Features

- Brute-forces a password by trying every combination of a 50-character set (lowercase letters, digits, and common symbols)
- Tries combinations one length at a time, from 1 character up to the password's length
- Reports whether the password was cracked, the number of attempts, and the runtime
- Checks upfront for characters outside the test set, so it doesn't waste time on an impossible search

## Requirements

- Python 3.6 or newer
- No external packages; it uses only the built-in `itertools` and `time` modules

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/MichaelTM0/password-cracker.git
   cd password-cracker
   ```

2. Run the program:

   ```bash
   python passwordcracker.py
   ```

3. Enter a short password when prompted. Start with 2-3 lowercase characters; longer passwords take dramatically longer.

## Example

```
Enter your password: cat
Password cracked: 'cat'
Attempts: 7,570
Runtime: 0.0017 seconds
```

## The Point of the Project

Every character you add multiplies the number of possible passwords by the size of the character set (50 here):

| Length | Combinations to try |
|---|---|
| 1 | 50 |
| 2 | 2,500 |
| 3 | 125,000 |
| 4 | 6,250,000 |
| 5 | 312,500,000 |

A 3-character password cracks instantly. A longer one, or one using characters outside the set (like uppercase letters or symbols), becomes impractical to brute-force. That jump is exactly why strong passwords work.

## How It Works

- `itertools.product(chars, repeat=length)` generates every combination of a given length, one at a time.
- Each guess is checked and discarded immediately, so only one combination is ever held in memory. This is what keeps the program from running out of memory on larger searches.
- The outer loop steps the length from 1 up to the length of the password, since the answer can't be longer than the password itself.

## Warning

Do not enter a real password you use anywhere. This is a demonstration tool; type in a throwaway test value.

## Future Improvements

- Add uppercase letters and more symbols to the character set
- Estimate crack time for a password without actually running the full search
- Compare a password against a list of common passwords first (a dictionary attack)
- Show progress as the search runs

## What I Learned

- Generating combinations with `itertools.product` instead of building them by hand
- Why generators matter: generate, check, and discard instead of storing everything in memory
- How a search space grows exponentially with length
- Guarding against impossible inputs before starting an expensive loop

## Author

**Michael Murchie**

- GitHub: [@MichaelTM0](https://github.com/MichaelTM0)
- LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
