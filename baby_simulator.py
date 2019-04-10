from random import choice
#ask a question:
question = ['Why is the sky blue?: ', "why is there a face on the moon: ?:", "Where are all the dinosaurs?: "]
question = choice(question)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()
print("oh..okay!")
