from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.conf import settings
from web3 import Web3

# from web3.middleware import geth_poa_middleware

from app.implementation.instance import Implementation

provider = Web3.HTTPProvider(settings.WEB3_PROVIDER)
contract = settings.CONTRACT_IMPL_ADR


class Name(APIView):
    """
    THIS IS A WIP
    Name.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Build.
        """
        instance = Implementation(provider, contract)
        res = instance.name.call()

        return Response(res)
