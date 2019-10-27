class Category:

    __id = None
    __category_group_id = None
    __name = None
    __hidden = None
    __originial_category_group_id = None
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

    def __init__(
        self,
        id,
        category_group_id,
        name,
        hidden,
        original_category_group_id,
        note,
        budgeted,
        activity,
        balance,
        goal_type,
        goal_creation_month,
        goal_target,
        goal_target_month,
        goal_percentage_complete,
        deleted
    ):
        self.__id = id
        self.__category_group_id = category_group_id
        self.__name = name
        self.__hidden = hidden
        self.__originial_category_group_id = original_category_group_id
        self.__note = note
        self.__budgeted = budgeted
        self.__activity = activity
        self.__balance = balance
        self.__goal_type = goal_type
        self.__goal_creation_month = goal_creation_month
        self.__goal_target = goal_target
        self.__goal_target_month = goal_target_month
        self.__goal_percentage_complete = goal_percentage_complete
        self.__deleted = deleted


    def addChild(self, child):
        self.children.append(child)

    def getName(self):
        return self.name
