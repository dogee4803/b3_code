from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CurrentCourse
from .serializers import CurrentCourseSerializer
from .models import Client
from .serializers import ClientSerializer
from .serializers import  CourseListSerializer
from .models import Course

class ClientCourseProgressView(APIView):
    def get(self, request, client_id):
        try:
            # Получаем все записи из CurrentCourse для данного клиента
            current_courses = CurrentCourse.objects.filter(id_client=client_id)
            
            # Сериализуем данные
            serializer = CurrentCourseSerializer(current_courses, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ClientIsAdminView(APIView):
    def get(self, request, client_id):
        try:
            # Получаем клиента по id
            client = Client.objects.get(id=client_id)
            
            # Сериализуем данные
            serializer = ClientSerializer(client)
            
            # Возвращаем сериализованные данные
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Client.DoesNotExist:
            # Если клиент не найден, возвращаем ошибку 404
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Обработка других ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class CourseListView(APIView):
    def get(self, request):
        try:
            # Получаем все курсы
            courses = Course.objects.all()
            
            # Сериализуем данные
            serializer = CourseListSerializer(courses, many=True)
            
            # Возвращаем сериализованные данные
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

from .serializers import ClientDataSerializer

class ClientListView(APIView):
    def get(self, request):
        try:
            # Получаем всех клиентов
            clients = Client.objects.all()
            
            # Сериализуем данные
            serializer = ClientDataSerializer(clients, many=True)
            
            # Возвращаем сериализованные данные
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


 # Добавление курсов Клиенту
from .serializers import AddCurrentCourseSerializer
class CurrentCourseCreateView(APIView):
    def post(self, request):
        try:
            # Получаем параметры из query string
            id_client = request.query_params.get('id_client')
            id_course = request.query_params.get('id_course')

            # Проверяем, что параметры переданы
            if not id_client or not id_course:
                return Response(
                    {'error': 'Both id_client and id_course are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Подготавливаем данные для сериализатора
            data = {
                'id_client': id_client,
                'id_course': id_course
            }

            # Сериализуем данные
            serializer = AddCurrentCourseSerializer(data=data)
            if serializer.is_valid():
                # Сохраняем запись в БД
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            # Если данные невалидны, возвращаем ошибку
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


from .serializers import DelCurrentCourseSerializer
class CurrentCourseDeleteView(APIView):
    def delete(self, request):
        try:
            # Получаем параметры из query string
            id_client = request.query_params.get('id_client')
            id_course = request.query_params.get('id_course')

            # Проверяем, что параметры переданы
            if not id_client or not id_course:
                return Response(
                    {'error': 'Both id_client and id_course are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Подготавливаем данные для сериализатора
            data = {
                'id_client': id_client,
                'id_course': id_course
            }

            # Валидируем данные с помощью сериализатора
            serializer = DelCurrentCourseSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Ищем запись в таблице CurrentCourse
            current_course = CurrentCourse.objects.filter(
                id_client_id=id_client,
                id_course_id=id_course
            ).first()

            # Если запись не найдена, возвращаем ошибку
            if not current_course:
                return Response(
                    {'error': 'Record not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Удаляем запись
            current_course.delete()

            # Возвращаем успешный ответ
            return Response(
                {'message': 'Record deleted successfully.'},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
from .serializers import DelCourseSerializer
class CourseDeleteView(APIView):
    def delete(self, request, course_id):
        try:
            # Ищем курс по id
            course = Course.objects.filter(id=course_id).first()

            # Если курс не найден, возвращаем ошибку
            if not course:
                return Response(
                    {'error': 'Course not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Сериализуем данные курса (опционально, для логгирования или ответа)
            serializer = DelCourseSerializer(course)

            # Удаляем курс (все связанные данные удалятся автоматически)
            course.delete()

            # Возвращаем успешный ответ с данными удаленного курса (опционально)
            return Response(
                {
                    'message': 'Course deleted successfully.',
                    'deleted_course': serializer.data
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
from .serializers import CourseCreateSerializer
class CourseCreateView(APIView):
    def post(self, request):
        try:
            # Получаем параметры из query string
            title = request.query_params.get('title')
            id_creator = request.query_params.get('id_creator')

            # Проверяем, что параметры переданы
            if not title or not id_creator:
                return Response(
                    {'error': 'Both title and id_creator are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Подготавливаем данные для сериализатора
            data = {
                'title': title,
                'id_creator': id_creator
            }

            # Сериализуем данные
            serializer = CourseCreateSerializer(data=data)
            if serializer.is_valid():
                # Сохраняем курс в БД
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            # Если данные невалидны, возвращаем ошибку
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

from .serializers import ModuleCreateSerializer
class ModuleCreateView(APIView):
    def post(self, request):
        try:
            # Получаем параметры из query string
            number_of_days = request.query_params.get('number_of_days')
            id_course = request.query_params.get('id_course')

            # Проверяем, что параметры переданы
            if not number_of_days or not id_course:
                return Response(
                    {'error': 'Both number_of_days and id_course are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Подготавливаем данные для сериализатора
            data = {
                'number_of_days': number_of_days,
                'id_course': id_course
            }

            # Сериализуем данные
            serializer = ModuleCreateSerializer(data=data)
            if serializer.is_valid():
                # Сохраняем модуль в БД
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            # Если данные невалидны, возвращаем ошибку
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


from .serializers import BlockCreateSerializer
class BlockCreateView(APIView):
    def post(self, request):
        try:
            # Получаем параметры из query string
            text_information = request.query_params.get('text_information')
            images = request.query_params.get('images')
            video = request.query_params.get('video')
            id_module = request.query_params.get('id_module')

            # Проверяем, что обязательные параметры переданы
            if not text_information or not id_module:
                return Response(
                    {'error': 'Both text_information and id_module are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Подготавливаем данные для сериализатора
            data = {
                'text_information': text_information,
                'images': images,
                'video': video,
                'id_module': id_module
            }

            # Сериализуем данные
            serializer = BlockCreateSerializer(data=data)
            if serializer.is_valid():
                # Сохраняем блок в БД
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            # Если данные невалидны, возвращаем ошибку
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

from .models import Block, Question, Answer
from .serializers import QuestionSerializer
class BlockTestCreateView(APIView):
    def post(self, request, block_id):
        try:
            # Получаем блок по id
            block = Block.objects.filter(id=block_id).first()

            # Если блок не найден, возвращаем ошибку
            if not block:
                return Response(
                    {'error': 'Block not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Получаем данные из запроса
            questions_data = request.data.get('questions', [])

            # Создаем вопросы и ответы
            for question_data in questions_data:
                # Создаем вопрос
                question = Question.objects.create(
                    text_of_question=question_data['text_of_question'],
                    id_block=block
                )

                # Создаем ответы для вопроса
                answers_data = question_data.get('answers', [])
                for answer_data in answers_data:
                    Answer.objects.create(
                        text_of_answer=answer_data['text_of_answer'],
                        is_true=answer_data['is_true'],
                        id_question=question
                    )

            # Возвращаем успешный ответ
            return Response(
                {'message': 'Test created successfully.'},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
from .models import Module
from .serializers import ModuleSerializer
class CourseModulesView(APIView):
    def get(self, request, course_id):
        try:
            # Получаем все модули курса по id курса
            modules = Module.objects.filter(id_course=course_id)
            
            # Сериализуем данные
            serializer = ModuleSerializer(modules, many=True)
            
            # Возвращаем сериализованные данные
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

from .serializers import BlockSerializer
class ModuleBlocksView(APIView):
    def get(self, request, module_id):
        try:
            # Получаем все блоки модуля по id модуля
            blocks = Block.objects.filter(id_module=module_id)
            
            # Сериализуем данные
            serializer = BlockSerializer(blocks, many=True)
            
            # Возвращаем сериализованные данные
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

from .serializers import QuestionSerializer
class BlockQuestionsView(APIView):
    def get(self, request, block_id):
        try:
            # Получаем блок по id
            block = Block.objects.filter(id=block_id).first()

            # Если блок не найден, возвращаем ошибку
            if not block:
                return Response(
                    {'error': 'Block not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Получаем все вопросы для блока
            questions = Question.objects.filter(id_block=block)
            
            # Сериализуем данные
            serializer = QuestionSerializer(questions, many=True)
            
            # Возвращаем сериализованные данные
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Обработка ошибок
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)