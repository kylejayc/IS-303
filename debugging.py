scores = [88, 45, 92, 67, 73]
total = 0

for score in scores:
    print(f"DEBUG: score={score}, total_before={total}")    # <-- add this
    total = total + score
    print(f"DEBUG: total_after={total}")                     # <-- and this

print(f"Final total: {total}")

for i, score in enumerate(scores):
    if i < 3:    # Only print debug for first 3 iterations
        print(f"DEBUG [{i}]: score = {score}, total = {total}")
    total = total + score

for team in teams:
    print(f"DEBUG: Outer loop - team={team}")
    for member in members:
        print(f"DEBUG:   Inner loop - member={member}")