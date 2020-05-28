

classes = ["banka", "kredi", "vade"]

texts = [
    "geçenlerde bankaya gittim. Bankada sıra vardı.Banka kredi vermiyor.",
    "böyle bir banka olamaz kredi kartında problem var"
]

for text in texts:
    classCounter = {}
    classScore = {}
    for eachclass in classes:
        classCounter.update({eachclass: 0})

    generatedText = ""
    for eachChar in text:
        if eachChar == ".":
            generatedText += " "
        else:
            generatedText += eachChar
    print(generatedText)
    wordCount = len(generatedText.split(' '))
    for eachWord in generatedText.split(' '):
        if eachWord.isspace() or eachWord == "":
            continue
        eachWord = eachWord.strip()
        for eachclass in classes:
            if eachclass in eachWord.lower():
                classCounter.update({eachclass:classCounter[eachclass]+1})
                break
    for eachclass in classes:
        classScore.update({eachclass:float(classCounter[eachclass]/wordCount)})
    print(classCounter)
    print(classScore)

