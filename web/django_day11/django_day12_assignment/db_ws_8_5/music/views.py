from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Music, Comment
from .serializers import MusicListSerializer, MusicSerializer, CommentSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

# @extend_schema_view(
#     list=extend_schema(
#         tags=['musics']
#     )
# )
@extend_schema(
    tags=['musics']
)
@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MusicListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['musics']
)
@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번 음악이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@extend_schema(
    tags=['comments']
)        
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@extend_schema(
    tags=['comments']
)     
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'delete':f'댓글 {comment_pk}번이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

@extend_schema(
    tags=['comments']
)     
@api_view(['POST'])
def comment_create(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music=music)
        return Response(serializer.data, status=status.HTTP_201_CREATED)