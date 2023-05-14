from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer, Userserializer, ModifyingPutSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from users.models import User


class Userview(APIView):
    def post(self, request):
      serializer = Userserializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({"message":"회원가입완료"}, status=status.HTTP_201_CREATED)
      else:
        return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockview(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response("get 요청")


class followView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("팔로우 취소!", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("팔로우 완료!",status=status.HTTP_200_OK)
        
class profileModifyView(APIView):
    def put(self,request):
        serializer = ModifyingPutSerializer(data=request.data)
        if serializer.is_valid(): #유효하다면
            user = request.user # 요청받은 유저를 본래 유저로 넣고
            user.set_password(serializer.validated_data.get('password')) 
            user.username = serializer.validated_data.get('nickname')
            user.save() # 저장
            return Response({'message': 'User information updated successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)