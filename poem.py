import random
nouns=["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs=["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives=["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions=["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs=["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
adj_1 = random.choice(adjectives) # прилагательные
adj_2 = random.choice(adjectives)
adj_3 = random.choice(adjectives)
pre_1 = random.choice(prepositions) # предлоги
pre_2 = random.choice(prepositions)
nouns_1 = random.choice(nouns) # существительные
nouns_2 = random.choice(nouns)
nouns_3 = random.choice(nouns)
adv_1 = random.choice(adverbs) # наречия
verbs_1 = random.choice(verbs) # глаголы
verbs_2 = random.choice(verbs)
verbs_3 = random.choice(verbs)
if adj_1.startswith(("a", "e", "i", "o", "u")): Aan = "An"
else: Aan = "A"
print(f"{Aan} {adj_1} {nouns_1} \n\n{Aan} {adj_1} {nouns_1} {verbs_1} {pre_1} the {adj_2} {nouns_2} \n{adv_1}, the {nouns_1} {verbs_2} \nthe {nouns_2} {verbs_3} {pre_2} a {adj_3} {nouns_3}")
