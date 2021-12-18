# constants.py
PARAMS_FOR_NEGATIVE_AUTH = [("", "!QAZ2wsx"), ("qa_test@test.ru", ""), ("qa_test.ru", "!QAZ2wsx"),
                            ("my_little_ponny@test.ru", "!QAZ2wsx")]
PARAMS_FOR_POSITIVE_AUTH = {"email": "api_user_6@test.ru",
                            "password": "q6w6e6"}


class Links:
    url = {"prod": "https://qastand.valhalla.pw/",
           "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"
    post_user2 = "blog/author/2/"


SESSION_COOKIE = {'name': 'session',
                  'value': '.eJwlzjsOwjAMANC7ZGaIY8dOepnKvwjWlk6Iu1OJ9U3vU_Z15Pks2_u48lH2V5StyBqQi7ImkPiU5lrRRGSG'
                           '-00tp_TZsEtSzVUTOSYyADF1BZRcbICZLoKkAWwIOmwO6bqATIM8alPjVQ2HsIQ2bL0HO7uUO3Kdefw3vXx_kLUu5w'
                           '.YYp1Jw.w2W5u8wPj9MHmLEEPtXXqAgs3-s'}
