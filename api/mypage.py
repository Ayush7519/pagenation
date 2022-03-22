from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagfination(PageNumberPagination):
    page_size= 6
    # page_query_param='p' 
    # yesley chai aafno page ko name or page laii indicate garni new word generate garna help garxa
    # page_size_query_param='records' 
    # yesley chai user lai yauta page ma kati ota record herna milni vaney rw setup garni access provide garxa
    # max_page_size=7 
    # yesley cahii maxim 7 ota user vanda display garauna user ley record ma jati value haley ni