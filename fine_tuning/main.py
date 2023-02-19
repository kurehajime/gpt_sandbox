import openai

completion = openai.Completion.create(
    model="davinci",
    prompt="ウミスズメのタイプを教えて？\nタイプ:")
print("普通のdavinciの答え：" + completion.choices[0].text)

completion = openai.Completion.create(
    model="davinci:ft-personal-2023-02-19-11-36-56",
    prompt="ウミスズメのタイプを教えて？\nタイプ:")
print("改良されたdavinciの答え：" + completion.choices[0].text)
