class category:

    def __init__(
        self,
        name='',
        parent='',
        catType='',
        children=[],
        budgeted=0
    ):
        self.name = name
        self.type = catType
        if parent and children:
            print('Must only have parent or child')
        elif parent:
            self.parent = parent
            self.budgeted = budgeted
        elif children:
            self.children = children

    def addChild(self, child):
        self.children.append(child)

    def getName(self):
        return self.name
