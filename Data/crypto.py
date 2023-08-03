import bcrypt
# passwd = '123456'
#
# bytes_my_password = bytes(passwd, encoding='utf-8')
#
# bytes_my_hashpassword = bcrypt.hashpw(bytes_my_password,bcrypt.gensalt())
# str_my_hashpassword = str(bytes_my_hashpassword,encoding='utf-8')
# print(str_my_hashpassword)
#
# my_password='123456'
# bytes_my_password=bytes(my_password,encoding='utf-8')
# str_my_hashpassword='$2b$12$CL.AaJPyNQCAOGCWu3GuF.gTTAKGILXVzgyNGJAPj/lhn2sBsGCrS'
# bytes_my_hashpassword=bytes(str_my_hashpassword,encoding='utf-8')
# print(bcrypt.checkpw(bytes_my_password,bytes_my_hashpassword))


def passwd_hash(passwd):
    bytes_my_password = bytes(passwd, encoding='utf-8')
    bytes_my_hashpassword = bcrypt.hashpw(bytes_my_password, bcrypt.gensalt())
    str_my_hashpassword = str(bytes_my_hashpassword, encoding='utf-8')
    return str_my_hashpassword


def checkPasswd(passwd, passwd_hash):
    bytes_my_password = bytes(passwd, encoding='utf-8')
    bytes_my_hashpassword = bytes(passwd_hash, encoding='utf-8')
    return bcrypt.checkpw(bytes_my_password, bytes_my_hashpassword)

