# chats/permissions.py
from rest_framework import permissions
from .models import Conversation, Message

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access or modify messages/conversations.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # All participants can read
        if request.method in permissions.SAFE_METHODS:
            if isinstance(obj, (Message, Conversation)):
                return request.user in obj.participants.all()
        
        # For PUT, PATCH, DELETE, ensure user is participant
        elif isinstance(obj, (Message, Conversation)):
            return request.user in obj.participants.all()

        return False