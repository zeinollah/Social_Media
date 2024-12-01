from rest_framework import serializers
from accounts.serializers import User
from reports.models import PostReport, AccountReport


class PostReportSerializer(serializers.ModelSerializer):
    report_id = serializers.IntegerField(source='id',read_only=True)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    reporter = serializers.SlugRelatedField(
        slug_field='username',
        required=False,
        queryset=User.objects.all())
    post_title = serializers.SerializerMethodField()
    post_author = serializers.SerializerMethodField()

    class Meta:
        model = PostReport
        fields = [
            'report_id',
            'reporter',
            'title',
            'description',
            'image',
            'post',
            'post_author',
            'post_title',
            'created_at',
        ]
        read_only_fields = ['created_at', 'reporter']

    def get_post_title(self, obj):
        return obj.post.title if obj.post else None

    def get_post_author(self, obj):
        return obj.post.author.username if obj.post and obj.post.author else None

    def validate(self, attrs):

        post = attrs.get('post')
        if not post :
            raise serializers.ValidationError('Post is required')

        title = attrs.get('title')
        if not title:
            raise serializers.ValidationError({'title': 'Title can not be empty'})

        if len(title) > 50:
            raise serializers.ValidationError({'title': 'Title must be 50 characters or less'})

        description = attrs.get('description')
        if description and len(description) > 200:
            raise serializers.ValidationError({'description': 'Description can not be longer than 200 characters'})

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        return PostReport.objects.create(
            reporter=user,
            **validated_data
        )



class AccountReportSerializer(serializers.ModelSerializer):
    report_id = serializers.IntegerField(source='id',read_only=True)
    reporter = serializers.SlugRelatedField(
        slug_field='username',
        required=False,
        queryset=User.objects.all()
    )
    account = serializers.PrimaryKeyRelatedField(
        source='account.username',
        queryset = User.objects.all()
    )

    class Meta:
        model = AccountReport
        fields = [
            'report_id',
            'reporter',
            'account',
            'title',
            'description',
            'image',
            'created_at',
        ]
        read_only_fields = ['created_at', 'reporter',]


    def validate(self, attrs):

        account = attrs.get('account')
        if not account:
            raise serializers.ValidationError('Account is required')

        title = attrs.get('title')
        if not title:
            raise serializers.ValidationError({'title': 'title can not be empty'})

        if len(title) > 50:
            raise serializers.ValidationError({'title': 'title must be 50 characters or less'})

        description = attrs.get('description')
        if description and len(description) > 200:
            raise serializers.ValidationError({'description': 'Description can not be longer than 200 characters'})

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['reporter'] = user

        username = validated_data.pop('account')['username']
        validated_data['account'] = User.objects.get(username=username)
        return AccountReport.objects.create(**validated_data)