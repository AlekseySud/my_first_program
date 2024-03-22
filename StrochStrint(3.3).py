string = "аоыгСпДЕыйччЛавывсАаЛ ДвыотЕпотоЛмучфО - ГпайУтонЛвеселЯЙ СыйМявапкЕиудывЛО"
result = ''
for i in string:
    if not i.islower():
        result = result + i
print(result)
    