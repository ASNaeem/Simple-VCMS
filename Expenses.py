class Expenses:
    def __init__(self, handler_id:int, expense_date:str, handle_date:str, amount:float, justification:str):
        self.issuer_id = None
        self.expense_id= None
        self.handler_id = handler_id
        self.expense_date = expense_date
        self.handle_date = handle_date
        self.amount = amount
        self.justification = justification

     ##############getter, setter########### 
    @property
    def expense_id(self):
         return self._expense_id
    
    """
    @expense_id.setter
    def expense_id(self, expense_id:int):
         self.expense_id = expense_id
    """
    @property
    def issuer_id(self):
         return self._issuer_id
    '''
    @issuer_id.setter
    def issuer_id(self, issuer_id:int):
         self._issuer_id = issuer_id
     '''
    @property
    def handler_id(self):
         return self._handler_id
    @handler_id.setter
    def handler_id(self, handler_id:int):
         self._handler_id = handler_id

    @property
    def expense_date(self):
         return self._expense_date
    @expense_date.setter
    def expense_date(self, expense_date:str):
         self._expense_date = expense_date

    @property
    def handle_date(self):
         return self._handle_date
    @handle_date.setter
    def handle_date(self, handle_date:str):
         self._handle_date = handle_date

    @property
    def amount(self):
         return self._amount
    @amount.setter
    def amount(self, amount:float):
         self._amount = amount

    @property
    def justification(self):
         return self._justification
    @justification.setter
    def justification(self, justification:str):
         self._justification = justification
