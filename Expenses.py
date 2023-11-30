class Expenses:
    def __init__(self, invoice_id:int, issuer_id:int, handler_id:int, handler_name:str, invoice_date:str, handle_date:str, amount:float, justification:str):
        self.invoice_id = invoice_id
        self.issuer_id = issuer_id
        self.handler_id = handler_id
        self.handler_name = handler_name
        self.invoice_date = invoice_date
        self.handle_date = handle_date
        self.amount = amount
        self.justification = justification

    @property
    def invoice_id(self):
         return self._invoice_id
    @invoice_id.setter
    def invoice_id(self, invoice_id:int):
         self.invoice_id = invoice_id
    
    @property
    def issuer_id(self):
         return self._issuer_id
    @issuer_id.setter
    def issuer_id(self, issuer_id:int):
         self._issuer_id = issuer_id

    @property
    def handler_id(self):
         return self._handler_id
    @handler_id.setter
    def handler_id(self, handler_id:int):
         self._handler_id = handler_id

    @property
    def invoice_date(self):
         return self._invoice_date
    @invoice_date.setter
    def invoice_date(self, invoice_date:str):
         self._invoice_date = invoice_date

    @property
    def handle_date(self):
         return self._handle_date
    @handler_id.setter
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
