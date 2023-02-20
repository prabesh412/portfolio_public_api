from rest_framework import serializers
from .models import Skill, Portfolio, Projects, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at','updated_at')
        ordering = ['name']
       
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ('created_at','updated_at')
        ordering = ['name']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'projectParent','project_pics','description')

class PortfolioSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many= True, read_only=True)
    category = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Portfolio
        fields = ('id','full_name','phone_no','portfolioParent','portfolioslug', 'profile_pics','description','skills', 'category')


class PortfolioInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id','full_name','phone_no','portfolioParent', 'profile_pics','description','skills', 'category')