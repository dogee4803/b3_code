from rest_framework import serializers
from .models import CurrentCourse, Course
from .models import Client
from .models import Module
from .models import Block
from .models import Question, Answer
from django.utils import timezone

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title']

class CurrentCourseSerializer(serializers.ModelSerializer):
    # Используем вложенный сериализатор для Course
    id_course = CourseSerializer(read_only=True)

    class Meta:
        model = CurrentCourse
        fields = ['connect_date', 'progress', 'id_course']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['is_admin']  # Указываем только поле is_admin

class CourseListSerializer(serializers.ModelSerializer):
    # Поле для количества участников (вычисляемое)
    participants_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'id_creator', 'make_date', 'participants_count']

    # Метод для вычисления количества участников
    def get_participants_count(self, obj):
        return CurrentCourse.objects.filter(id_course=obj).count()
    
class ClientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'surname', 'name', 'patronymic', 'email', 'is_admin']


 # Добавление курсов Клиенту
class AddCurrentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentCourse
        fields = ['id_client', 'id_course']

    def create(self, validated_data):
        # Устанавливаем connect_date как текущую дату и progress как 0
        validated_data['connect_date'] = timezone.now().date()
        validated_data['progress'] = 0
        return super().create(validated_data)
    
class DelCurrentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentCourse
        fields = ['id_client', 'id_course']



class DelCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'id_creator', 'make_date']


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'id_creator']

    def create(self, validated_data):
        # Устанавливаем make_date как текущую дату
        validated_data['make_date'] = timezone.now().date()
        return super().create(validated_data)

class ModuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['number_of_days', 'id_course']

class BlockCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['text_information', 'images', 'video', 'id_module']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text_of_answer', 'is_true']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)  # Вложенный сериализатор для ответов

    class Meta:
        model = Question
        fields = ['text_of_question', 'answers']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'number_of_days', 'id_course']

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'text_information', 'images', 'video', 'id_module']

class AnswerSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text_of_answer', 'is_true']

class QuestionSerializerOut(serializers.ModelSerializer):
    answers = AnswerSerializerOut(many=True, read_only=True)  # Вложенный сериализатор для ответов

    class Meta:
        model = Question
        fields = ['id', 'text_of_question', 'answers']