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
    def name(self, invoice_id:str):
         self._service_id = service_id

    @property
    def service_id(self):
         return self._service_id

    @name.setter
    def name(self, service_id:str):
         self._service_id = service_id

    @property
    def service_id(self):
         return self._service_id

    @name.setter
    def name(self, service_id:str):
         self._service_id = service_id