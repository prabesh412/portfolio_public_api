from .serializers import ProjectSerializer, PortfolioSerializer, PortfolioInputSerializer
from .models import Projects, Portfolio
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from users.permissions import ReadOnly, IsOwner, IsSuperUser
from rest_framework.exceptions import PermissionDenied


class PortfolioViewset(viewsets.ModelViewSet):
    serializer_class= PortfolioSerializer
    queryset = Portfolio.objects.all().select_related("portfolioParent")
    permission_classes = (ReadOnly, )

    def retrieve(self, request, pk=None):
        queryset = Portfolio.objects.filter(portfolioslug = pk).select_related(
            "portfolioParent")
        serializer = PortfolioSerializer(queryset,many=True)
        return Response(serializer.data)


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def retrieve(self, request, pk=None):
        queryset = Projects.objects.filter(projectParent = pk).select_related(
            "projectParent")
        serializer = ProjectSerializer(queryset,many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.projectParent.portfolioParent:
            raise PermissionDenied
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.projectParent.portfolioParent:
            raise PermissionDenied
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user != obj.projectParent.portfolioParent:
            return super().destroy(self, request, *args, **kwargs)
        else:
            return Response("Not Authorized", 404)
    


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    queryset=Portfolio.objects.all().select_related("portfolioParent")
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        query= Portfolio.objects.filter(portfolioParent=self.request.user)
        return query

    def get_serializer_class(self):
        if self.action in ["create","update", "partial_update"]:
            return PortfolioInputSerializer
        return super().get_serializer_class()


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.portfolioParent:
            raise PermissionDenied
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.portfolioParent:
            raise PermissionDenied
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user == obj.portfolioParent:
            return super().destroy(self, request, *args, **kwargs)
        else:
            return Response("Not Authorized", 404)