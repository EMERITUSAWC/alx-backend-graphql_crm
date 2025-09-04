import graphene
from graphene_django import DjangoObjectType
from .models import Product
import logging

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="/tmp/lowstockupdates_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "stock", "price")


class UpdateLowStockProducts(graphene.Mutation):
    """
    Mutation to automatically update low stock products
    """
    updated_count = graphene.Int()

    @classmethod
    def mutate(cls, root, info):
        # Define low stock threshold
        threshold = 5
        # Update stock of products below threshold
        low_stock_products = Product.objects.filter(stock__lt=threshold)
        count = low_stock_products.count()

        for product in low_stock_products:
            product.stock = threshold
            product.save()
            logger.info(f"Updated stock for product {product.name} (ID: {product.id}) to {threshold}")

        return UpdateLowStockProducts(updated_count=count)


class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()
