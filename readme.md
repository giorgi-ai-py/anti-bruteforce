# Day 4: Brute Force Defender 

**Part of my journey learning Python for cybersecurity (penetration testing & AI security)**

---

## What This Is

After building a basic login system on Day 3, I realized it had a massive flaw: if you typed the wrong password, the script just... died. No second chances. That's terrible UX, but also terrible security if you just let people try forever.

So on Day 4, I learned about **loops** and built a login system that:
- Gives you 3 attempts (like a real system)
- Locks you out after too many failures
- Actually makes you wait between attempts to slow down brute force attacks

## The Code

It's a simple `for` loop that runs 3 times max. If you get the password right, it breaks out early. If you fail 3 times, boom - account locked.

I also added `time.sleep()` delays because real security systems don't respond instantly - they make you wait. It's annoying when you're testing, but that's literally the point. It slows down attackers.

## What I Learned

**Loops:** `for` vs `while` - I used a `for` loop here because I knew exactly how many attempts I wanted (3). Turns out `while` loops are probably better for this specific case, but I wanted to challenge myself.

**The `break` statement:** This is how you exit a loop early. Super important when you find what you're looking for.

**Indentation matters:** Python crashed on me with `TabError: inconsistent use of tabs and spaces`. Learned the hard way that Python cares if you use tabs vs spaces. Stick to spaces. Always.

**Importing modules:** You can't just use `time.sleep()` without `import time` at the top. Duh, but I forgot at first.

## How to Run It

```bash
cd ~/ai-cyber-lab/day\ 4/
python3 Brute_force_defender.py
