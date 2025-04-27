import json

# Step 1: Open your credentials.json
with open('credentials.json', 'r') as f:
    data = json.load(f)

# Step 2: Dump it into a one-liner JSON string
one_liner = json.dumps(data)

# Step 3: Print it (copy this output and paste into Render env variable)
print(one_liner)
