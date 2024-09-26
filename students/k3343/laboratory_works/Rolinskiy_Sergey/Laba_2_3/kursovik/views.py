from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from kursovik.models import *
from django.http import Http404, QueryDict
from kursovik.serializers import *
from datetime import datetime, date, time
from django.db.models import Q
# Create your views here.

class RoomView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self,request,format=None):
        rooms=Room.objects.all()
        serializer=RoomSerialiser(rooms,many=True)
        return Response({"data": serializer.data})

class ClientView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerialiser(clients, many=True)
        return Response({"data": serializer.data})

class WorkerView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        workers = Worker.objects.all()
        serializer = WorkerSerialiser(workers, many=True)
        return Response({"data": serializer.data})
    def get_object(self, pk):
        try:
            return Worker.objects.get(id=pk)
        except Worker.DoesNotExist:
            raise Http404
    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        worker = self.get_object(delete_params['id'])
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = WorkerSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorktableView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        worktable = Worktable.objects.all().values_list('id','worker','floor','weekday')
        workers = Worker.objects.all().values_list('id','fio')
        response = {'data': []}
        for assignment in worktable:
            for theworker in workers:
                if theworker[0] == assignment[1]:
                    worker = theworker[1]
            response['data'].append({'id': assignment[0],
                                     'worker': worker,
                                    'floor':assignment[2],
                                    'weekday':assignment[3]})
        return Response(response)

    def get_object(self, pk):
        try:
            return Worktable.objects.get(pk=pk)
        except Worktable.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        worktable = self.get_object(delete_params['id'])
        worktable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        worker = Worker.objects.get(fio=request.data['worker'])
        data = request.data.copy()
        data['worker'] = worker.id
        serializer = WorktableSerialiser(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        print(put_params)
        worker = Worker.objects.get(fio=put_params['worker'])
        data = put_params.copy()
        data['worker'] = worker.id
        wt = self.get_object(put_params['id'])
        serializer = WorktableSerialiser(wt, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorktableQ(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            wt_id = request.GET.get("id")
            worktable = Worktable.objects.get(id=wt_id)
            worker = Worker.objects.get(fio=worktable.worker)
            response = {'data': {'id': wt_id,
                                 'worker': worker.fio,
                                 'floor': worktable.floor,
                                 'weekday': worktable.weekday}}
            return Response(response)
        except Worktable.DoesNotExist:
            raise Http404

class JournalView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        journal = Journal.objects.all().values_list('id','client','room','checkin','checkout')
        clients = Client.objects.all().values_list('id','fio')
        rooms = Room.objects.all().values_list('id', 'number')
        response = {'data': []}
        for record in journal:
            for theclient in clients:
                if theclient[0] == record[1]:
                    client = theclient[1]
            for theroom in rooms:
                if theroom[0] == record[2]:
                    room = theroom[1]
            response['data'].append({'id': record[0],
                                     'client': client,
                                     'room': room,
                                    'checkin':record[3],
                                    'checkout':record[4]})
        return Response(response)

    def get_object(self, pk):
        try:
            return Journal.objects.get(pk=pk)
        except Journal.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        delete_params = QueryDict(request.body)
        journal = self.get_object(delete_params['id'])
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        client = Client.objects.get(fio=request.data['client'])
        room = Room.objects.get(number=request.data['room'])
        data = request.data.copy()
        data['client'] = client.id
        data['room'] = room.id
        serializer = JournalSerialiser(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        print(put_params)
        client = Client.objects.get(fio=put_params['client'])
        room = Room.objects.get(number=put_params['room'])
        data = put_params.copy()
        data['client'] = client.id
        data['room'] = room.id
        jn = self.get_object(put_params['id'])
        serializer = JournalSerialiser(jn, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalQ(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        try:
            jn_id = request.GET.get("id")
            journal = Journal.objects.get(id=jn_id)
            print(journal.client)
            print(journal.room)
            client = Client.objects.get(fio=journal.client)
            room = Room.objects.get(number=str(journal.room))
            response = {'data': {'id': jn_id,
                                 'client': client.fio,
                                 'room': room.number,
                                 'checkin': journal.checkin,
                                 'checkout':journal.checkout}}
            return Response(response)
        except Journal.DoesNotExist:
            raise Http404

class Request1View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self,request,format=None):
        response = {'data': []}
        roomm = request.GET.get("room")
        firstdate = request.GET.get("firstdate")
        seconddate=request.GET.get("seconddate")
        room_id=Room.objects.get(number=roomm).id
        selection1 = Journal.objects.filter(Q(room=room_id)).filter(
                                            Q(checkout__lt=seconddate)&
                                            Q(checkout__gt=firstdate)|
                                            Q(checkin__lt=seconddate)&
                                            Q(checkin__gt=firstdate)
                                            ).values_list('client')
        clients=Client.objects.filter(id__in=selection1)
        serializer = ClientSerialiser(clients, many=True)
        if selection1:
            return Response(serializer.data,)
        raise Http404

class Request2View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self,request,format=None):
        hometown = request.GET.get("hometown")
        selection1 = Client.objects.filter(hometown=hometown).count()
        print(selection1)
        if selection1:
            return Response({'data':{'thing':selection1}})
        raise Http404

class Request3View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self,request,format=None):
        room = request.GET.get("room")
        weekday = request.GET.get("weekday")
        room_floor = Room.objects.get(number=room).floor
        selection = Worktable.objects.filter(Q(floor=room_floor),Q(weekday=weekday))\
                                            .values_list('worker')
        workers=Worker.objects.filter(id__in=selection)
        serializer = WorkerSerialiser(workers, many=True)
        if selection:
            return Response(serializer.data,)
        raise Http404

class Request5View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self,request,format=None):
        client = request.GET.get("client")
        client_id=Client.objects.get(fio=client)
        firstdate = request.GET.get("firstdate")
        seconddate = request.GET.get("seconddate")
        selection1_in = Journal.objects.filter(Q(client=client_id))\
                                    .filter(Q(checkin__gt=firstdate)&Q(checkin__lt=seconddate)
                                            |Q(checkout__gt=firstdate)&Q(checkout__lt=seconddate))\
                                    .values_list('checkin')
        selection1_out = Journal.objects.filter(Q(client=client_id)) \
                                    .filter(Q(checkin__gt=firstdate) & Q(checkin__lt=seconddate)
                                            | Q(checkout__gt=firstdate) & Q(checkout__lt=seconddate)) \
                                    .values_list('checkout')
        selection2=Journal.objects.filter(Q(checkin__gt=selection1_in)&Q(checkin__lt=selection1_out)
                                            |Q(checkout__gt=selection1_in)&Q(checkout__lt=selection1_out))\
                                    .values_list('client')
        clients=Client.objects.filter(id__in=selection2)
        serializer = ClientSerialiser(clients, many=True)
        if selection2:
            return Response(serializer.data,)
        raise Http404

class Request4View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self,request,format=None):
        now=datetime.today()
        selection1 = Journal.objects.filter(Q(checkin__lt=now)&Q(checkout__gt=now)).values_list('room')
        ans = Room.objects.filter(~Q(id__in=selection1))
        serializer=RoomSerialiser(ans,many=True)
        if selection1:
            return Response(serializer.data,)
        raise Http404

def convert(string):
    dt_fmt = '%Y-%m-%d'
    res = datetime.date((datetime.strptime(string, dt_fmt)))
    return res

class ReportView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request, format=None):
        firstdate = request.GET.get("firstdate")
        seconddate = request.GET.get("seconddate")
        totalcost=0
        totalclients=0
        records=Journal.objects.filter(Q(checkout__lt=seconddate)&
                                            Q(checkout__gt=firstdate)|
                                            Q(checkin__lt=seconddate)&
                                            Q(checkin__gt=firstdate)
                                            )
        rooms = Room.objects.all().values_list('number')
        rooms_tup={str(room[0]):0 for room in rooms}
        print(rooms_tup)
        response = {'clients': [],'totalcost':[],'per_room':rooms_tup,'totalclients':[]}
        for record in records:
            client_fio=Client.objects.get(fio=record.client).fio
            client_home=Client.objects.get(fio=record.client).hometown
            client_room=record.room
            clients_days=(record.checkout-record.checkin).days
            totalclients+=1
            response['clients'].append({'client_fio':client_fio,
                                        'client_home':client_home,
                                        'client_room':str(client_room),
                                        'client_days':clients_days})
            roomcost=Room.objects.get(number=str(record.room)).cost
            if (record.checkin > convert(firstdate)) and (record.checkout < convert(seconddate)):
                diff=record.checkout-record.checkin
                totalcost+=diff.days*roomcost
                thisroom=str(record.room)
                response['per_room'][thisroom]+=diff.days*roomcost
            elif record.checkin > convert(firstdate):
                diff=convert(seconddate)-record.checkin
                totalcost+=diff.days*roomcost
                thisroom = str(record.room)
                response['per_room'][thisroom] += diff.days * roomcost
            elif record.checkout < convert(seconddate):
                diff=record.checkout-convert(firstdate)
                totalcost+=diff.days*roomcost
                thisroom = str(record.room)
                response['per_room'][thisroom] =response['per_room'][thisroom]+diff.days * roomcost
        response['totalclients'].append(totalclients)
        response['per_room']=response['per_room'].items()
        if totalcost>0:
            response['totalcost'].append(totalcost)
            return Response(response)
        raise Http404