import json, os

clear = lambda: os.system("cls")

file = "chatGPT_python.json"

with open(file, "r") as f:
    data = json.load(f)

for key in data:
    try:
        entry = data[key]
        if entry["type"] == "question":
            clear()
            print("\n--------------------------------\n")
            print("Question Asked:\n" + entry["content"] + "\n")
            input()
            print(f"Answer Given:\n  {data[entry['answer']]['content']}")
            # print("\n--------------------------------\n\n")
            input()
    except KeyError:
        print("No more entries")
        break
