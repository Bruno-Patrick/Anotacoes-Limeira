# def teste(professorId,semestre: int = None, ano=None):
#     query = f"""SELECT * FROM disciplinas WHERE 
#             `professor` = '{professorId}'
#             {"".join([x for x in f"AND `semestre`= '{semestre}'" if semestre])}
#             {"".join([x for x in f"AND `ano`= '{ano}'" if ano])}"""
#     return(print(query))

# teste(1, ano=2022, semestre=2)

print('12345'.encode('utf-8'))