class Category:

    __id = None
    __category_group_id = None
    __name = None
    __hidden = None
    __original_category_group_id = None
    __note = None
    __budgeted = None
    __activity = None
    __balance = None
    __goal_type = None
    __goal_creation_month = None
    __goal_target = None
    __goal_target_month = None
    __goal_percentage_complete = None
    __deleted = None

    def __init__(self, category):
        self.__create_category(category)

    def __create_category(self, category):
        self.__id = category['id']
        self.__category_group_id = category['category_group_id']
        self.__name = category['name']
        self.__hidden = category['hidden']
        self.__original_category_group_id = category['original_category_group_id']
        self.__note = category['note']
        self.__budgeted = category['budgeted']
        self.__activity = category['activity']
        self.__balance = category['balance']
        self.__goal_type = category['goal_type']
        self.__goal_creation_month = category['goal_creation_month']
        self.__goal_target = category['goal_target']
        self.__goal_target_month = category['goal_target_month']
        self.__goal_percentage_complete = category['goal_percentage_complete']
        self.__deleted = category['deleted']

    def addChild(self, child):
        self.children.append(child)

    def getName(self):
        return self.name

    def get_category(self):
        category = {
            'id': self.__id,
            'category_group_id': self.__category_group_id,
            'name': self.__name,
            'hidden': self.__hidden,
            'original_category_group_id': self.__original_category_group_id,
            'note': self.__note,
            'budgeted': self.__budgeted,
            'activity': self.__activity,
            'balance': self.__balance,
            'goal_type': self.__goal_type,
            'goal_creation_month': self.__goal_creation_month,
            'goal_target': self.__goal_target,
            'goal_target_month': self.__goal_target_month,
            'goal_percentage_complete': self.__goal_percentage_complete,
            'deleted': self.__deleted
        }
        return category
