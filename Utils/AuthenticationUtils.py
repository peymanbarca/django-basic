from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class AuthenticationUtils:
    def __init__(self, request):
        self.request = request

    def validateAndGetCurrentUserLogin(self):
        token = self.request.headers.get('Authorization').split(' ')[1]
        data = {'token': token}
        try:
            valid_data = VerifyJSONWebTokenSerializer().validate(data)
            user = valid_data['user']
            return user
        except Exception as v:
            print("validation error", v)

