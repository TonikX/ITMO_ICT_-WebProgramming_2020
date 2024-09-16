from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from newspapersapp.models import *
from django.http import Http404, QueryDict
from django.db.models import Q
from newspapersapp.serializers import (PostOfficeSerializer,
                                       PrintingHouseSerializer,
                                       NewspaperSerializer,
                                       ReportSerializer,
                                       InStockSerializer,
                                       EditorSerializer)


class PostOfficeView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        post_offices = PostOffice.objects.all()
        serializer = PostOfficeSerializer(post_offices, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return PostOffice.objects.get(pk=pk)
        except PostOffice.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        post_office = self.get_object(delete_params['pk'])
        post_office.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        post_office = self.get_object(put_params['id'])
        serializer = PostOfficeSerializer(post_office, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = PostOfficeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditorsView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        editors = Editor.objects.all()
        serializer = EditorSerializer(editors, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Editor.objects.get(pk=pk)
        except Editor.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        editor = self.get_object(delete_params['pk'])
        editor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = EditorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        editor = self.get_object(put_params['id'])
        serializer = EditorSerializer(editor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrintingHouses(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        houses = PrintingHouse.objects.all()
        serializer = PrintingHouseSerializer(houses, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return PrintingHouse.objects.get(pk=pk)
        except PrintingHouse.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        house = self.get_object(delete_params['pk'])
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = PrintingHouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        house = self.get_object(put_params['id'])
        serializer = PrintingHouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Papers(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        papers = Newspaper.objects.all().values_list('id',
                                                     'name',
                                                     'edition_index',
                                                     'editor',
                                                     'price')
        editors = Editor.objects.all().values_list('id',
                                                   'first_name',
                                                   'middle_name',
                                                   'last_name')
        response = {'data' : []}
        for paper in papers:
            for editor in editors:
                if paper[3] == editor[0]:
                    response['data'].append({'id': paper[0],
                                             'name' : paper[1],
                                             'edition_index' : paper[2],
                                             'editor' : editor[1] + ' ' + editor[2] + ' ' + editor[3],
                                             'price' : paper[4]})

        return Response(response)
   
    def get_object(self, pk):
        try:
            return Newspaper.objects.get(pk=pk)
        except Newspaper.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        newspaper = self.get_object(delete_params['pk'])
        newspaper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        full_name = request.data['editor'].split()
        editor = Editor.objects.filter(first_name=full_name[0]) \
                               .filter(middle_name=full_name[1]) \
                               .filter(last_name=full_name[2]) \
                               .values_list('id', flat=True)
        data = request.data.copy()
        data['editor'] = editor[0]
        serializer = NewspaperSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        full_name = put_params['editor'].split()
        editor = Editor.objects.get(Q(first_name=full_name[0]), 
                                    Q(middle_name=full_name[1]),
                                    Q(last_name=full_name[2]))
        data = request.data.copy()
        data['editor'] = editor.id
        newspaper = self.get_object(put_params['id'])
        serializer = NewspaperSerializer(newspaper, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InStockView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        stocks = InStock.objects.all().values_list('id',
                                                   'print_run',
                                                   'newspaper_id',
                                                   'post_office_id',
                                                   'printing_house_id')
        papers = Newspaper.objects.all().values_list('id',
                                                     'name')
        offices = PostOffice.objects.all().values_list('id',
                                                       'number')
        houses = PrintingHouse.objects.all().values_list('id',
                                                         'name')
        response = {'data' : []}
        for stock in stocks:
            for paper in papers:
                if paper[0] == stock[2]:
                    newspaper = paper[1]
            for office in offices:
                if office[0] == stock[3]:
                    post_office = office[1]
            for house in houses:
                if house[0] == stock[4]:
                    printing_house = house[1]
            response['data'].append({'id': stock[0],
                                     'print_run' : stock[1],
                                     'newspaper' : newspaper,
                                     'post_office' : post_office,
                                     'printing_house' : printing_house})
        return Response(response)

    def get_object(self, pk):
        try:
            return InStock.objects.get(pk=pk)
        except InStock.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        stock = self.get_object(delete_params['pk'])
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        newspaper = Newspaper.objects.get(name=request.data['newspaper'])
        office = PostOffice.objects.get(number=request.data['post_office'])
        house = PrintingHouse.objects.get(name=request.data['printing_house'])
        data = request.data.copy()
        data['newspaper'] = newspaper.id
        data['post_office'] = office.id
        data['printing_house'] = house.id
        serializer = InStockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        print(put_params)
        newspaper = Newspaper.objects.get(name=put_params['newspaper'])
        office = PostOffice.objects.get(number=put_params['post_office'])
        house = PrintingHouse.objects.get(name=put_params['printing_house'])
        data = put_params.copy()
        data['newspaper'] = newspaper.id
        data['post_office'] = office.id
        data['printing_house'] = house.id
        stock = self.get_object(put_params['id'])
        serializer = InStockSerializer(stock, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OfficeView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            office_id = request.GET.get("id")
            post_office = PostOffice.objects.get(id=office_id)
            serializer = PostOfficeSerializer(post_office)
            return Response(serializer.data)
        except PostOffice.DoesNotExist:
            raise Http404


class EditorView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            editor_id = request.GET.get("id")
            editor = Editor.objects.get(id=editor_id)
            serializer = EditorSerializer(editor)
            return Response(serializer.data)
        except Editor.DoesNotExist:
            raise Http404


class Paper(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            paper_id = request.GET.get("id")
            paper = Newspaper.objects.get(id=paper_id)
            editor = Editor.objects.get(id=paper.editor_id)
            response = {'data' : {'id': paper.id,
                                  'name' : paper.name,
                                  'edition_index' : paper.edition_index,
                                  'editor' : editor.first_name + ' ' + editor.middle_name + ' ' + editor.last_name,
                                  'price' : paper.price}}
            return Response(response)
        except Newspaper.DoesNotExist:
            raise Http404


class StockView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            stock_id = request.GET.get("id")
            stock = InStock.objects.get(id=stock_id)
            paper = Newspaper.objects.get(id=stock.newspaper_id)
            office = PostOffice.objects.get(id=stock.post_office_id)
            house = PrintingHouse.objects.get(id=stock.printing_house_id)
            response = {'data' : {'id': stock_id,
                                  'print_run' : stock.print_run,
                                  'newspaper' : paper.name,
                                  'post_office' : office.number,
                                  'printing_house' : house.name}}
            return Response(response)
        except InStock.DoesNotExist:
            raise Http404


class PrintingHouseView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            house_id = request.GET.get("id")
            house = PrintingHouse.objects.get(id=house_id)
            serializer = PrintingHouseSerializer(house)
            return Response(serializer.data)
        except PrintingHouse.DoesNotExist:
            raise Http404


class CertificateView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        name = request.GET.get("name")
        index = Newspaper.objects.filter(name=name)
        serializer = NewspaperSerializer(index, many=True)
        if index:
            return Response(serializer.data[0])
        return Http404


class Request1View(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        name = request.GET.get("name")
        newspaper = Newspaper.objects.get(name=name)
        instocks = InStock.objects.filter(newspaper_id=newspaper.id).values_list('printing_house_id', flat=True)
        printhouses = PrintingHouse.objects.filter(id__in=instocks)
        serializer = PrintingHouseSerializer(printhouses, many=True)
        if newspaper:
            return Response(serializer.data)
        return Http404


class Request2View(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        printhouse_name = request.GET.get("name")
        printhouse = PrintingHouse.objects.get(name=printhouse_name)
        max_print_run = max(InStock.objects.filter(printing_house_id=printhouse.id) \
                                           .values_list('print_run', flat=True))
        newspapers = InStock.objects.filter(printing_house_id=printhouse.id) \
                                    .filter(print_run=max_print_run) \
                                    .values_list('newspaper_id', flat=True)
        editors_ids = Newspaper.objects.filter(id__in=newspapers) \
                                   .values_list('editor_id', flat=True)
        editors = Editor.objects.filter(id__in=editors_ids)
        serializer = EditorSerializer(editors, many=True)
        if editors_ids:
            return Response(serializer.data)
        return Http404


class Request3View(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        paper_price = request.GET.get("price")
        newspapers = Newspaper.objects.filter(price__gt=paper_price) \
                                      .values_list('id', flat=True)
        office_ids = set(InStock.objects.filter(newspaper_id__in=newspapers) \
                                        .values_list('post_office_id', flat=True))
        post_offices = PostOffice.objects.filter(id__in=office_ids)
        serializer = PostOfficeSerializer(post_offices, many=True)
        if office_ids:
            return Response(serializer.data)
        raise Http404


class Newspapers(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        newspapers = Newspaper.objects.all()
        serializer = NewspaperSerializer(newspapers, many=True)
        paper_names = [serializer.data[newspaper]['name'] for newspaper in range(len(serializer.data))]
        return Response(paper_names)


class Houses(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        newspapers = PrintingHouse.objects.all()
        serializer = PrintingHouseSerializer(newspapers, many=True)
        house_names = [serializer.data[house]['name'] for house in range(len(serializer.data))]
        return Response(house_names)


class Offices(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        offices = PostOffice.objects.all()
        serializer = PostOfficeSerializer(offices, many=True)
        office_numbers = [serializer.data[office]['number'] for office in range(len(serializer.data))]
        return Response(office_numbers)


class Request4View(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        print_run = request.GET.get("print_run")
        response = {'data' : []}
        paper_ids = InStock.objects.filter(print_run__lt=print_run) \
                                   .values_list('newspaper_id', flat=True)
        office_ids = InStock.objects.filter(print_run__lt=print_run) \
                                    .values_list('post_office_id', flat=True)
        for i in range(len(paper_ids)):
            newspaper = NewspaperSerializer(Newspaper.objects.get(id=paper_ids[i])).data['name']
            post_office = PostOfficeSerializer(PostOffice.objects.get(id=office_ids[i])).data['number']
            response['data'].append({'newspaper' : newspaper,
                                     'post_office' : post_office})
        if office_ids and paper_ids :
            return Response(response)
        raise Http404


class Request5View(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        name = request.GET.get("name")
        address = request.GET.get("address")

        printhouse = PrintingHouse.objects.get(address=address)
        newspaper = Newspaper.objects.get(name=name)
        office_ids = set(InStock.objects.filter(newspaper_id=newspaper.id) \
                                        .filter(printing_house_id=printhouse.id)
                                        .values_list('post_office_id', flat=True))
        post_offices = PostOffice.objects.filter(id__in=office_ids)
        serializer = PostOfficeSerializer(post_offices, many=True)
        if office_ids:
            return Response(serializer.data)
        raise Http404

    
class Addresses(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        houses = PrintingHouse.objects.all()
        serializer = PrintingHouseSerializer(houses, many=True)
        addresses = [serializer.data[house]['address'] for house in range(len(serializer.data))]
        return Response(addresses)


class EditorsListView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        editors = Editor.objects.all()
        serializer = EditorSerializer(editors, many=True)
        editorslist = [serializer.data[editor]['first_name'] + ' ' + \
                       serializer.data[editor]['middle_name'] + ' ' + \
                       serializer.data[editor]['last_name'] \
                       for editor in range(len(serializer.data))]
        return Response(editorslist)


class ReportView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        houses = PrintingHouse.objects.all()
        serializer = PrintingHouseSerializer(houses, many=True)
        response = {'data' : []}
        for i in range(len(houses)):
            name = serializer.data[i]['name']
            house_id = serializer.data[i]['id']
            print_runs = InStock.objects.filter(printing_house_id=house_id) \
                                        .values_list('print_run', flat=True)
            paper_ids = list(set(InStock.objects.filter(printing_house_id=house_id) \
                                                .values_list('newspaper_id', flat=True)))
            papers_run = []
            for paper_id in paper_ids:
                newspaper = Newspaper.objects.get(id=paper_id)
                print_run = sum(InStock.objects.filter(newspaper_id=newspaper.id) \
                                               .filter(printing_house_id=house_id) \
                                               .values_list('print_run', flat=True))
                papers_run.append({'name' : newspaper.name,
                                   'print_run' : print_run})

            paper_ids = list(set(InStock.objects.filter(printing_house_id=house_id) \
                                                .values_list('newspaper_id', flat=True)))
            papers_offices = []
            for paper_id in paper_ids:
                newspaper = Newspaper.objects.get(id=paper_id)
                office_ids = InStock.objects.filter(newspaper_id=newspaper.id) \
                                            .filter(printing_house_id=house_id) \
                                            .values_list('post_office', flat=True)
                for office_id in office_ids:
                    post_office = PostOffice.objects.get(id=office_id)
                    print_run = InStock.objects.filter(newspaper_id=newspaper.id) \
                                               .filter(printing_house_id=house_id) \
                                               .filter(post_office_id=office_id) \
                                               .values_list('print_run', flat=True)[0]
                    papers_offices.append({'name' : newspaper.name,
                                           'print_run' : print_run,
                                           'number' : post_office.number,
                                           'address' : post_office.address})
            response['data'].append({'name' : name,
                                     'print_runs' : sum(print_runs),
                                     'papers_run' : papers_run,
                                     'papers_offices' : papers_offices})
        return Response(response)
