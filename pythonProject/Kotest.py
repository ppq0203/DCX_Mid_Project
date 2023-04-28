from konlpy.tag import Kkma, Komoran, Hannanum, Okt
sentence = "[재료] 밥 1+1/2공기| 당근 1/4개| 치자단무지 1/2개| 신김치 1쪽| 무순 약간| 날치알 6스푼| 김가루 약간| 후리가케(또는밥이랑같은류)| 참기름 약간| 통깨 약간| 계란 노른자 2알"
print(Kkma().pos(sentence))
print()
print(Komoran().pos(sentence))
print()
print(Hannanum().pos(sentence))
print()
print(Okt().pos(sentence))