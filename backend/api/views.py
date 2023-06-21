from api.models import Balance, Transaction
from api.serializers import (BalanceSerializer, TransactionSerializer,
                             UserSerializer)
from api.utils import update_balance
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def active_users(self, request, pk=None):
        transactions = Transaction.objects.filter(date__month__gte=6).order_by('-value')
        user_ids = list(set([i.user.id for i in transactions]))[:10]
        recent_users = User.objects.filter(id__in=user_ids)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        user = get_object_or_404(User, pk=data['user_id'])
        new_ransaction = Transaction.objects.create(user=user, value=data['value'])
        serializer = TransactionSerializer(new_ransaction)
        update_balance(user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        user = get_object_or_404(User, pk=data['user_id'])
        transaction = self.get_object()
        transaction.value = data['value']
        transaction.user = user
        transaction.save()
        serializer = TransactionSerializer(transaction)
        update_balance(user)
        return Response(serializer.data)


class BalanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]
