class Category:
    # корректные классовые счётчики
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        # создаём копию списка, чтобы избежать побочных эффектов
        self.products = list(products) if products is not None else []
        # обновляем классовые счётчики
        Category.category_count += 1
        Category.product_count += len(self.products)


    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            Category.product_count -= 1
            return True
        return False
