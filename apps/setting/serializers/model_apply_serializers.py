# coding=utf-8
"""
    @project: AIsisstant
    @Author：Yue linfeng
    @file： model_apply_serializers.py
    @date：2025/4/13 20:39
    @desc:
"""
from django.db import connection
from django.db.models import QuerySet
from langchain_core.documents import Document
from rest_framework import serializers

from common.config.embedding_config import ModelManage
from common.util.field_message import ErrMessage
from setting.models import Model
from setting.models_provider import get_model
from django.utils.translation import gettext_lazy as _

def get_embedding_model(model_id):
    model = QuerySet(Model).filter(id=model_id).first()
    # 手动关闭数据库连接
    connection.close()
    embedding_model = ModelManage.get_model(model_id,
                                            lambda _id: get_model(model, use_local=True))
    return embedding_model


class EmbedDocuments(serializers.Serializer):
    texts = serializers.ListField(required=True, child=serializers.CharField(required=True,
                                                                             error_messages=ErrMessage.char(
                                                                                 _('vector text'))),
                                  error_messages=ErrMessage.list(_('vector text list')))


class EmbedQuery(serializers.Serializer):
    text = serializers.CharField(required=True, error_messages=ErrMessage.char(_('vector text')))


class CompressDocument(serializers.Serializer):
    page_content = serializers.CharField(required=True, error_messages=ErrMessage.char(_('text')))
    metadata = serializers.DictField(required=False, error_messages=ErrMessage.dict(_('metadata')))


class CompressDocuments(serializers.Serializer):
    documents = CompressDocument(required=True, many=True)
    query = serializers.CharField(required=True, error_messages=ErrMessage.char(_('query')))


class ModelApplySerializers(serializers.Serializer):
    model_id = serializers.UUIDField(required=True, error_messages=ErrMessage.uuid(_('model id')))

    def embed_documents(self, instance, with_valid=True):
        if with_valid:
            self.is_valid(raise_exception=True)
            EmbedDocuments(data=instance).is_valid(raise_exception=True)

        model = get_embedding_model(self.data.get('model_id'))
        return model.embed_documents(instance.getlist('texts'))

    def embed_query(self, instance, with_valid=True):
        if with_valid:
            self.is_valid(raise_exception=True)
            EmbedQuery(data=instance).is_valid(raise_exception=True)

        model = get_embedding_model(self.data.get('model_id'))
        return model.embed_query(instance.get('text'))

    def compress_documents(self, instance, with_valid=True):
        if with_valid:
            self.is_valid(raise_exception=True)
            CompressDocuments(data=instance).is_valid(raise_exception=True)
        model = get_embedding_model(self.data.get('model_id'))
        return [{'page_content': d.page_content, 'metadata': d.metadata} for d in model.compress_documents(
            [Document(page_content=document.get('page_content'), metadata=document.get('metadata')) for document in
             instance.get('documents')], instance.get('query'))]
