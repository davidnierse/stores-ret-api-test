from models.item import ItemModel
from models.store import StoreModel

from tests.base_test import BaseTest

class Store_Test(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [],
                             "The store's item length was not 0, but no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'),
                                                      "Found a store with name {} but should not exist in db".format(store.name))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                                         "Did not find the store with name {} in db after saving to db.".format(store.name))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'),
                                                      "Found a store with name {} but should not exist in db.".format(store.name))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected,
                             "Expected JSON not equal to actual exported JSON. Received {}, Expected: {}".format(store.json(), expected))

    def test_store_json_multiple_items(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test',
                'items': [{"name": "test_item",
                          "price": 19.99,}]
            }

            self.assertDictEqual(store.json(), expected,
                                 "Expected JSON not equal to actual exported JSON. Received {}, Expected: {}".format(store.json(), expected))






