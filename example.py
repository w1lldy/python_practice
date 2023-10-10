example = {
    "1": {"рус": "один", "eng": "one", },
    "2": {"рус": "два", "eng": "two", },
    "3": {"рус": "три", "eng": "three", },
}

for count, language in example.items():
    print(f"Ключ № {count}")
    for language, znachenie in language.items():
        print(f"значения этого ключа = {language} и {znachenie}")
