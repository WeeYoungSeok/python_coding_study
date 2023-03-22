# 로그인 성공?
def solution(id_pw, dbs):
    for db in dbs:
        if db == id_pw:
            return "login"
        else:
            if db[0] == id_pw[0]:
                return "wrong pw"
    return "fail"