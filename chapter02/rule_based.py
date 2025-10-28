import re
pattern = r'\w+(?:\'\w+)?|[^\w\s]'

text = ("There's no such thing as survival of the fittest. "
        "Survival of the most adequate, maybe.")

tokens = list(re.findall(pattern, text))
