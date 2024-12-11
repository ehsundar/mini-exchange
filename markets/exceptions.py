from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class InsufficientFunds(APIException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_detail = _("Insufficient funds.")
    default_code = "insufficient_funds"
