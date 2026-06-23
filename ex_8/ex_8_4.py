e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
f2e = {fr: en for en, fr in e2f.items()}
print(f2e['chien'])