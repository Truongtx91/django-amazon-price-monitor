from ..serializers.ProductSerializer import ProductSerializer
from ...models.Product import Product

from rest_framework import generics, permissions


class ProductRetrieveView(generics.RetrieveAPIView):
    """
    Returns single instance of Product, if user is authenticated
    """
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'asin'
    permission_classes = [
        # only return the list if user is authenticated
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        """
        Filters queryset by the authenticated user
        :returns: filtered Product objects
        :rtype:   QuerySet
        """
        return Product.objects.filter(subscription__owner=self.request.user)
